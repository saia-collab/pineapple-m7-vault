"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Layers, Loader2, ExternalLink, RefreshCw, CornerDownLeft, History as HistoryIcon, ArrowLeft, Feather } from "lucide-react";

// jcode — the most RAM-efficient harness (Rust, ~28MB, 14ms to first frame),
// running on the Claude subscription login. Three tabs:
//   Terminal  — jcode run streamed live
//   Workspace — visual builds gallery (auto-previews, showcase files only)
//   History   — the conversation-history workspace: every jcode session on this
//               Mac (TUI, CLI, Agent OS builds), named like fox/rhino/octopus,
//               readable as full transcripts.

const JC = "#f5a623";       // jcode amber
const CLAUDE = "#d97757";   // Claude terracotta
const TERM_LSK = "agentic-os/jcode/terminal/v1";

type Tab = "terminal" | "workspace" | "history";
interface Line {
  kind: "user" | "text" | "tool" | "tool_result" | "result" | "system" | "error" | "stderr" | "info";
  text?: string; name?: string; input?: Record<string, unknown>;
  ms?: number; model?: string; subtype?: string; session?: string;
}
interface Build { project: string; mtime: number; fileCount: number; html: string[]; files: { rel: string; bytes: number }[] }
interface SessionMeta { id: string; shortName: string; title: string | null; model: string | null; workingDir: string | null; status: string | null; messages: number; lastActiveAt: string | null }
interface Transcript { meta: SessionMeta; messages: { role: string; text: string; timestamp?: string }[] }

const EXAMPLES = [
  "a starfield warp-speed animation I can steer with my mouse",
  "a glowing audio visualizer with fake waveform bars",
  "a retro CRT terminal boot sequence animation",
];

function toolLine(s: Line): string {
  const inp = s.input || {};
  const f = (p: unknown) => String(p ?? "").split("/").pop() ?? "";
  if (s.name === "write" || s.name === "Write") return `Write(${f(inp.path ?? inp.file_path)})`;
  if (s.name === "edit" || s.name === "Edit") return `Edit(${f(inp.path ?? inp.file_path)})`;
  if (s.name === "bash" || s.name === "Bash") return `Bash(${String(inp.command ?? "").slice(0, 48)})`;
  const first = Object.values(inp)[0];
  return `${s.name}(${first !== undefined ? String(first).slice(0, 40) : ""})`;
}

function ago(iso: string | null): string {
  if (!iso) return "";
  const s = (Date.now() - new Date(iso).getTime()) / 1000;
  if (s < 90) return "just now";
  if (s < 3600) return `${Math.round(s / 60)}m ago`;
  if (s < 86400) return `${Math.round(s / 3600)}h ago`;
  return `${Math.round(s / 86400)}d ago`;
}

export default function JcodeView() {
  const [tab, setTab] = useState<Tab>("terminal");
  const [input, setInput] = useState("");
  const [lines, setLines] = useState<Line[]>([]);
  const [building, setBuilding] = useState(false);
  const [project, setProject] = useState<string | null>(null);
  const [installed, setInstalled] = useState<boolean | null>(null);
  const ctrlRef = useRef<AbortController | null>(null);
  const termRef = useRef<HTMLDivElement>(null);
  const inputRef = useRef<HTMLInputElement>(null);
  const hydrated = useRef(false);

  const [builds, setBuilds] = useState<Build[]>([]);
  const loadBuilds = useCallback(async () => {
    try { const r = await fetch("/api/jcode/workspace", { cache: "no-store" }); const j = await r.json(); setBuilds(j.builds ?? []); setInstalled(!!j.installed); } catch {}
  }, []);

  const [sessions, setSessions] = useState<SessionMeta[]>([]);
  const [transcript, setTranscript] = useState<Transcript | null>(null);
  const loadSessions = useCallback(async () => {
    try { const r = await fetch("/api/jcode/sessions", { cache: "no-store" }); const j = await r.json(); setSessions(j.sessions ?? []); } catch {}
  }, []);
  async function openSession(id: string) {
    try { const r = await fetch(`/api/jcode/sessions?id=${encodeURIComponent(id)}`, { cache: "no-store" }); const j = await r.json(); if (!j.error) setTranscript(j); } catch {}
  }

  useEffect(() => {
    try { const raw = localStorage.getItem(TERM_LSK); if (raw) setLines(JSON.parse(raw).slice(-400)); } catch {}
    hydrated.current = true;
    loadBuilds(); loadSessions();
  }, [loadBuilds, loadSessions]);
  useEffect(() => { if (hydrated.current) try { localStorage.setItem(TERM_LSK, JSON.stringify(lines.slice(-400))); } catch {} }, [lines]);
  useEffect(() => { if (termRef.current) termRef.current.scrollTop = termRef.current.scrollHeight; }, [lines, building]);

  const build = useCallback(async (text?: string) => {
    const p = (text ?? input).trim();
    if (!p || building) return;
    setInput("");
    setLines((l) => [...l, { kind: "user", text: p }]);
    setBuilding(true); setProject(null);
    const ctrl = new AbortController(); ctrlRef.current = ctrl;
    try {
      const r = await fetch("/api/jcode/build", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ prompt: p }), signal: ctrl.signal,
      });
      const reader = r.body?.getReader(); const dec = new TextDecoder(); let buf = "";
      while (reader) {
        const { value, done } = await reader.read(); if (done) break;
        buf += dec.decode(value, { stream: true });
        let nl: number;
        while ((nl = buf.indexOf("\n")) >= 0) {
          const ln = buf.slice(0, nl); buf = buf.slice(nl + 1);
          if (!ln.trim()) continue;
          let e: Line & { type?: string; project?: string };
          try { e = JSON.parse(ln); } catch { continue; }
          const type = (e as { type?: string }).type;
          if (type === "start") setProject(e.project ?? null);
          else if (type === "system") setLines((l) => [...l, { kind: "system", model: e.model, session: e.session }]);
          else if (type === "text") setLines((l) => [...l, { kind: "text", text: e.text }]);
          else if (type === "tool") setLines((l) => [...l, { kind: "tool", name: e.name, input: e.input }]);
          else if (type === "tool_result") setLines((l) => [...l, { kind: "tool_result", text: e.text }]);
          else if (type === "result") setLines((l) => [...l, { kind: "result", subtype: e.subtype, ms: e.ms }]);
          else if (type === "info") setLines((l) => [...l, { kind: "info", text: e.text }]);
          else if (type === "stderr") setLines((l) => [...l, { kind: "stderr", text: e.text }]);
          else if (type === "error") setLines((l) => [...l, { kind: "error", text: e.text }]);
        }
      }
    } catch (err) {
      if ((err as Error).name !== "AbortError") setLines((l) => [...l, { kind: "error", text: String(err).slice(0, 160) }]);
    }
    setBuilding(false); loadBuilds(); loadSessions();
  }, [input, building, loadBuilds, loadSessions]);

  function stop() { ctrlRef.current?.abort(); setBuilding(false); setLines((l) => [...l, { kind: "info", text: "⎿ Interrupted." }]); }
  const previewUrl = (proj: string, file: string) => `/api/jcode/preview/${proj}/${file.split("/").map(encodeURIComponent).join("/")}`;

  return (
    <div className="flex flex-col h-full min-h-0">
      {/* header */}
      <div className="flex items-center gap-3 mb-3 shrink-0 flex-wrap">
        <div className="w-8 h-8 rounded-lg grid place-items-center font-bold text-[#1a1206]" style={{ background: `linear-gradient(135deg,${JC},${CLAUDE})` }}>⟡</div>
        <div className="min-w-0">
          <div className="text-[15px] font-semibold text-[var(--cream)] leading-none flex items-center gap-2">
            jcode
            <span className="inline-flex items-center gap-1 text-[10px] font-medium px-1.5 py-0.5 rounded-full" style={{ background: `${JC}1e`, color: JC, border: `1px solid ${JC}40` }}>
              {installed == null ? <Loader2 size={9} className="animate-spin" /> : <span className="w-1.5 h-1.5 rounded-full" style={{ background: installed ? JC : "#e8728a" }} />}
              {installed == null ? "checking" : installed ? "Claude login ready" : "not installed"}
            </span>
          </div>
          <div className="text-[10.5px] text-[var(--cream-mute)] mt-1">The most RAM-efficient harness · Rust · ~28MB · 14ms to first frame · runs claude-opus-5 on your subscription</div>
        </div>
        <div className="ml-auto flex gap-1.5">
          {([{ k: "terminal", label: "Terminal", n: 0 }, { k: "workspace", label: "Workspace", n: builds.length }, { k: "history", label: "History", n: sessions.length }] as const).map((t) => (
            <button key={t.k} onClick={() => { setTab(t.k as Tab); if (t.k === "workspace") loadBuilds(); if (t.k === "history") { setTranscript(null); loadSessions(); } }}
              className="inline-flex items-center gap-1.5 px-3 py-1.5 rounded-lg text-[12px] font-medium border transition"
              style={{ borderColor: tab === t.k ? JC : "var(--line-soft)", background: tab === t.k ? `${JC}1e` : "transparent", color: tab === t.k ? JC : "var(--cream-dim)" }}>
              {t.k === "history" && <HistoryIcon size={11} />}{t.label}{t.n ? ` · ${t.n}` : ""}
            </button>
          ))}
        </div>
      </div>

      {/* ── TERMINAL ── */}
      {tab === "terminal" && (
        <div className="flex flex-col min-h-0 flex-1 rounded-xl overflow-hidden border" style={{ borderColor: "var(--line-soft)", background: "#0f0c08" }}>
          <div className="flex items-center gap-2 px-3.5 py-2 border-b shrink-0" style={{ borderColor: "#2a2114", background: "#151009" }}>
            <span className="flex gap-1.5"><i className="w-3 h-3 rounded-full inline-block" style={{ background: "#ff5f57" }} /><i className="w-3 h-3 rounded-full inline-block" style={{ background: "#febc2e" }} /><i className="w-3 h-3 rounded-full inline-block" style={{ background: "#28c840" }} /></span>
            <span className="text-[11px] text-[var(--cream-mute)] mono ml-1">jcode — claude — ~/.agentic-os/jcode</span>
            {lines.length > 0 && <button onClick={() => { setLines([]); try { localStorage.removeItem(TERM_LSK); } catch {} }} className="ml-auto mono text-[10px] text-[var(--cream-mute)] hover:text-[var(--cream)]">clear</button>}
          </div>

          <div ref={termRef} onClick={() => inputRef.current?.focus()} className="flex-1 min-h-0 overflow-y-auto scroll px-4 py-3 mono text-[12.5px] leading-[1.7] cursor-text" style={{ color: "#d4c7b0" }}>
            <div className="rounded-lg border px-4 py-3 mb-3" style={{ borderColor: "#332816", background: "#171106" }}>
              <div style={{ color: JC }}>⟡ jcode — the most RAM-efficient harness</div>
              <div className="mt-2" style={{ color: "#93865f" }}>  engine: <span style={{ color: CLAUDE }}>claude-opus-5</span> · your Claude subscription</div>
              <div style={{ color: "#93865f" }}>  ~28MB per session · 14ms to first frame · semantic memory graph · swarm mode</div>
              <div style={{ color: "#93865f" }}>  sessions get animal names (fox, rhino, octopus…) — all readable in <span style={{ color: JC }}>History</span></div>
            </div>
            {lines.length === 0 && (
              <div className="mb-2" style={{ color: "#93865f" }}>
                <div style={{ color: "var(--cream)" }}>Tips</div>
                <div>1. Type what you want built and press <span style={{ color: JC }}>Enter</span> — jcode writes the files itself.</div>
                <div>2. Builds land in the <span style={{ color: JC }}>Workspace</span> tab with live previews.</div>
                <div>3. Every conversation is saved — the <span style={{ color: JC }}>History</span> tab is the whole archive.</div>
              </div>
            )}
            {lines.map((s, i) => {
              if (s.kind === "user") return <div key={i} className="mt-2"><span style={{ color: JC }}>&gt; </span><span style={{ color: "var(--cream)" }}>{s.text}</span></div>;
              if (s.kind === "system") return <div key={i} style={{ color: "#77693f" }}>⎿ session {s.session ? String(s.session).split("_")[1] : ""} · {s.model}</div>;
              if (s.kind === "text") return <div key={i} className="whitespace-pre-wrap" style={{ color: "#d4c7b0" }}><span style={{ color: JC }}>● </span>{s.text}</div>;
              if (s.kind === "tool") return <div key={i} style={{ color: "var(--cream)" }}><span style={{ color: "#34E5B0" }}>● </span>{toolLine(s)}</div>;
              if (s.kind === "tool_result") return <div key={i} className="truncate" style={{ color: "#77693f" }}>  ⎿ {s.text}</div>;
              if (s.kind === "result") return <div key={i} className="mt-1" style={{ color: s.subtype === "success" ? "#34E5B0" : "#e8728a" }}>⎿ {s.subtype === "success" ? "Done" : s.subtype} · {Math.round((s.ms ?? 0) / 1000)}s</div>;
              if (s.kind === "info") return <div key={i} style={{ color: "#77693f" }}>{s.text}</div>;
              if (s.kind === "stderr") return <div key={i} className="truncate" style={{ color: "#77693f", opacity: .7 }}>{s.text}</div>;
              if (s.kind === "error") return <div key={i} style={{ color: "#e8728a" }}>⎿ {s.text}</div>;
              return null;
            })}
            {building && <div className="inline-flex items-center gap-2 mt-1" style={{ color: JC }}><Loader2 size={12} className="animate-spin" /> <span style={{ color: "#93865f" }}>jcode working…</span></div>}
            {project && !building && builds.find((b) => b.project === project)?.html?.[0] && (
              <div className="mt-1"><a href={previewUrl(project, builds.find((b) => b.project === project)!.html[0])} target="_blank" rel="noopener" style={{ color: "#34E5B0" }}>  ⎿ open {builds.find((b) => b.project === project)!.html[0]} ↗</a></div>
            )}
          </div>

          <div className="border-t px-3.5 py-2.5 shrink-0 flex items-center gap-2" style={{ borderColor: "#2a2114", background: "#151009" }}>
            <span className="mono text-[13px]" style={{ color: building ? "#77693f" : JC }}>&gt;</span>
            <input ref={inputRef} value={input} onChange={(e) => setInput(e.target.value)} disabled={building}
              onKeyDown={(e) => { if (e.key === "Enter" && !e.shiftKey) { e.preventDefault(); build(); } }}
              placeholder={building ? "building… (esc to stop)" : "tell jcode what to build…"}
              className="flex-1 bg-transparent mono text-[13px] focus:outline-none disabled:opacity-60" style={{ color: "var(--cream)" }} />
            {building
              ? <button onClick={stop} className="mono text-[11px] px-2 py-1 rounded border" style={{ borderColor: "#e8728a55", color: "#e8728a" }}>esc</button>
              : <button onClick={() => build()} disabled={!input.trim() || installed === false} className="inline-flex items-center gap-1 mono text-[11px] px-2 py-1 rounded border disabled:opacity-30" style={{ borderColor: `${JC}55`, color: JC }}><CornerDownLeft size={11} /> run</button>}
          </div>
          <div className="px-3.5 pb-2.5 shrink-0 flex items-center gap-2 flex-wrap" style={{ background: "#151009" }}>
            <span className="mono text-[10px]" style={{ color: "#77693f" }}>? try:</span>
            {EXAMPLES.map((ex) => (
              <button key={ex} onClick={() => build(ex)} disabled={building} className="mono text-[10px] px-2 py-0.5 rounded-full border disabled:opacity-40 transition" style={{ borderColor: "var(--line-soft)", color: "var(--cream-dim)" }}>{ex}</button>
            ))}
          </div>
        </div>
      )}

      {/* ── WORKSPACE (visual-first) ── */}
      {tab === "workspace" && (
        <div className="panel p-0 flex flex-col min-h-0 flex-1 overflow-hidden">
          <div className="flex items-center gap-2 px-4 py-2.5 border-b border-[var(--line-soft)] shrink-0">
            <Layers size={14} style={{ color: JC }} />
            <span className="text-[12.5px] text-[var(--cream)] font-medium">jcode builds</span>
            <span className="text-[10.5px] text-[var(--cream-mute)]">{builds.length} project{builds.length === 1 ? "" : "s"} · saved on your Mac</span>
            <button onClick={loadBuilds} className="ml-auto p-1.5 rounded-lg border border-[var(--line-soft)] text-[var(--cream-mute)] hover:text-[var(--cream)]"><RefreshCw size={12} /></button>
          </div>
          <div className="flex-1 min-h-0 overflow-y-auto scroll p-3">
            {builds.length === 0 ? (
              <div className="h-full grid place-items-center text-center"><div className="text-[11.5px] text-[var(--cream-mute)] max-w-[320px]">No builds yet. Type a goal in the Terminal — jcode builds it, and every project lands here with a live preview.</div></div>
            ) : (
              <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-3">
                {builds.map((b) => (
                  <div key={b.project} className="rounded-xl border border-[var(--line-soft)] overflow-hidden bg-[var(--bg-card)] hover:border-[#f5a62355] transition">
                    {b.html[0]
                      ? <iframe src={previewUrl(b.project, b.html[0])} title={b.project} loading="lazy" sandbox="allow-scripts allow-same-origin allow-popups" className="w-full bg-black border-0" style={{ aspectRatio: "16/10" }} />
                      : <div className="w-full grid place-items-center text-[var(--cream-mute)] text-[11px] bg-[#120e06]" style={{ aspectRatio: "16/10" }}>{b.fileCount} file{b.fileCount === 1 ? "" : "s"} · no html</div>}
                    <div className="p-2.5">
                      <div className="text-[12px] font-medium text-[var(--cream)] truncate mono">{b.project}</div>
                      <div className="flex items-center gap-2 mt-1.5">
                        <span className="text-[9.5px] text-[var(--cream-mute)]">{b.fileCount} file{b.fileCount === 1 ? "" : "s"}</span>
                        {b.html[0] && <a href={previewUrl(b.project, b.html[0])} target="_blank" rel="noopener" className="ml-auto text-[9.5px] inline-flex items-center gap-1" style={{ color: JC }}><ExternalLink size={9} /> open</a>}
                      </div>
                    </div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}

      {/* ── HISTORY — the conversation-history workspace ── */}
      {tab === "history" && (
        <div className="panel p-0 flex flex-col min-h-0 flex-1 overflow-hidden">
          <div className="flex items-center gap-2 px-4 py-2.5 border-b border-[var(--line-soft)] shrink-0">
            {transcript
              ? <button onClick={() => setTranscript(null)} className="inline-flex items-center gap-1.5 text-[12px]" style={{ color: JC }}><ArrowLeft size={12} /> all sessions</button>
              : <><HistoryIcon size={14} style={{ color: JC }} /><span className="text-[12.5px] text-[var(--cream)] font-medium">Conversation history</span></>}
            <span className="text-[10.5px] text-[var(--cream-mute)]">
              {transcript ? `${transcript.meta.shortName} · ${transcript.meta.model ?? ""} · ${transcript.messages.length} messages` : `${sessions.length} session${sessions.length === 1 ? "" : "s"} · every jcode conversation on this Mac`}
            </span>
            {!transcript && <button onClick={loadSessions} className="ml-auto p-1.5 rounded-lg border border-[var(--line-soft)] text-[var(--cream-mute)] hover:text-[var(--cream)]"><RefreshCw size={12} /></button>}
          </div>
          <div className="flex-1 min-h-0 overflow-y-auto scroll p-3">
            {!transcript ? (
              sessions.length === 0
                ? <div className="h-full grid place-items-center text-[11.5px] text-[var(--cream-mute)]">No sessions yet — run something in the Terminal.</div>
                : <div className="space-y-1.5">
                    {sessions.map((s) => (
                      <button key={s.id} onClick={() => openSession(s.id)}
                        className="w-full text-left rounded-lg border p-3 transition hover:bg-[rgba(255,255,255,0.02)]"
                        style={{ borderColor: "var(--line-soft)" }}>
                        <div className="flex items-center gap-2 flex-wrap">
                          <Feather size={12} style={{ color: JC }} />
                          <span className="text-[12.5px] mono font-medium" style={{ color: "var(--cream)" }}>{s.shortName}</span>
                          {s.title && <span className="text-[11px] truncate max-w-[40ch]" style={{ color: "var(--cream-dim)" }}>{s.title}</span>}
                          <span className="text-[10px] mono ml-auto shrink-0" style={{ color: "var(--cream-mute)" }}>
                            {s.messages} msg{s.messages === 1 ? "" : "s"} · {s.model ?? "?"} · {ago(s.lastActiveAt)}
                          </span>
                        </div>
                        {s.workingDir && <div className="text-[10px] mono mt-1 truncate" style={{ color: "var(--cream-mute)" }}>{s.workingDir.replace(/^\/Users\/[^/]+/, "~")}</div>}
                      </button>
                    ))}
                  </div>
            ) : (
              <div className="space-y-2 max-w-[860px]">
                {transcript.messages.map((m, i) => (
                  <div key={i} className="rounded-lg border p-3" style={{ borderColor: "var(--line-soft)", background: m.role === "user" ? `${JC}0a` : "transparent" }}>
                    <div className="text-[9.5px] uppercase tracking-widest mb-1" style={{ color: m.role === "user" ? JC : "#34E5B0" }}>{m.role}</div>
                    <div className="text-[12px] whitespace-pre-wrap leading-relaxed" style={{ color: "var(--cream-soft)" }}>{m.text}</div>
                  </div>
                ))}
              </div>
            )}
          </div>
        </div>
      )}
    </div>
  );
}
