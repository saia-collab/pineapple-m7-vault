"use client";

import { useCallback, useEffect, useRef, useState } from "react";
import { Sparkles, Send, Loader2, Image as ImageIcon, Film, History, FolderOpen, ExternalLink, Check, Copy, AlertTriangle, RefreshCw, Wand2, Download } from "lucide-react";

const ACCENT = "#c084fc";   // Higgsfield violet
const ACCENT2 = "#f0abfc";
const SITE = "https://higgsfield.ai/mcp";
const LS_KIND = "higgs.kind";

interface Status { registered: boolean; authed: boolean; tools: number; url: string; profile: string; detail: string; loginCommand: string }
interface Item { file: string; kind: "image" | "video"; bytes: number; at: number; title: string }
interface Session { id: string; prompt: string; kind: string; created: string[]; note: string; ms: number; at: number }

type Tab = "create" | "gallery" | "history";

const IDEAS = [
  "A cinematic 4K product shot of a glowing bronze pocket-watch on black velvet, dramatic rim light",
  "A 6-second video: neon city street at night, camera pushes slowly through falling rain",
  "A moody portrait of a woman in a red coat on a foggy Victorian street, film grain",
  "A 5-second video: golden liquid pouring into a crystal glass in extreme slow motion",
];

function ago(ms: number) {
  const s = Math.round((Date.now() - ms) / 1000);
  if (s < 60) return `${s}s ago`;
  if (s < 3600) return `${Math.round(s / 60)}m ago`;
  if (s < 86400) return `${Math.round(s / 3600)}h ago`;
  return `${Math.round(s / 86400)}d ago`;
}
function kb(n: number) { return n > 1e6 ? `${(n / 1e6).toFixed(1)}MB` : `${Math.round(n / 1000)}KB`; }

export default function HiggsfieldView() {
  const [st, setSt] = useState<Status | null>(null);
  const [tab, setTab] = useState<Tab>("create");
  const [prompt, setPrompt] = useState("");
  const [kind, setKind] = useState<string>(() => { try { return localStorage.getItem(LS_KIND) || "auto"; } catch { return "auto"; } });
  const [busy, setBusy] = useState(false);
  const [elapsed, setElapsed] = useState(0);
  const [err, setErr] = useState<string | null>(null);
  const [items, setItems] = useState<Item[]>([]);
  const [sessions, setSessions] = useState<Session[]>([]);
  const [open, setOpen] = useState<Item | null>(null);
  const [copied, setCopied] = useState(false);
  const timer = useRef<ReturnType<typeof setInterval> | null>(null);

  useEffect(() => { try { localStorage.setItem(LS_KIND, kind); } catch { /* ignore */ } }, [kind]);

  const ping = useCallback(() => {
    fetch("/api/higgs/status", { cache: "no-store" }).then((r) => r.json()).then(setSt).catch(() => setSt(null));
  }, []);
  const loadGallery = useCallback(() => {
    fetch("/api/higgs/gallery", { cache: "no-store" }).then((r) => r.json()).then((j) => setItems(j.items ?? [])).catch(() => {});
  }, []);
  const loadHistory = useCallback(() => {
    fetch("/api/higgs/history", { cache: "no-store" }).then((r) => r.json()).then((j) => setSessions(j.sessions ?? [])).catch(() => {});
  }, []);

  useEffect(() => { ping(); loadGallery(); loadHistory(); }, [ping, loadGallery, loadHistory]);

  async function send(text?: string) {
    const p = (text ?? prompt).trim();
    if (!p || busy) return;
    setErr(null); setBusy(true); setElapsed(0);
    timer.current = setInterval(() => setElapsed((e) => e + 1), 1000);
    try {
      const j = await fetch("/api/higgs/run", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ prompt: p, kind }),
      }).then((r) => r.json());
      if (!j.ok) setErr(j.error || "Higgsfield returned nothing — check the connection above.");
      else { setPrompt(""); setTab("gallery"); }
      loadGallery(); loadHistory();
    } catch (e) {
      setErr(String((e as Error).message || e));
    } finally {
      if (timer.current) clearInterval(timer.current);
      setBusy(false);
    }
  }

  const live = !!st?.registered && !!st?.authed;

  return (
    <div className="flex flex-col gap-4">
      {/* HERO */}
      <div className="relative overflow-hidden rounded-2xl border p-5" style={{ borderColor: "var(--panel-border)", background: "rgba(255,255,255,0.02)" }}>
        <div className="pointer-events-none absolute -inset-24 opacity-60" style={{ background: `radial-gradient(closest-side, ${ACCENT}22, transparent 70%)`, animation: "hgAurora 14s ease-in-out infinite" }} />
        <div className="relative">
          <div className="flex items-center gap-3">
            <div className="grid place-items-center w-11 h-11 rounded-xl" style={{ background: `linear-gradient(135deg, ${ACCENT}, ${ACCENT2})`, color: "#160a1f", boxShadow: `0 8px 26px ${ACCENT}44` }}><Wand2 size={22} /></div>
            <div>
              <div className="text-[10px] uppercase tracking-[0.2em] flex items-center gap-1.5" style={{ color: ACCENT }}><Sparkles size={11} /> Higgsfield · MCP · Studio</div>
              <div className="text-[19px] font-semibold text-[var(--cream)] leading-tight">Higgsfield</div>
            </div>
            <div className="ml-auto flex items-center gap-2 text-[11px] px-3 py-1.5 rounded-full" style={{ background: live ? "rgba(192,132,252,0.12)" : "rgba(255,255,255,0.05)", color: live ? ACCENT : "var(--cream-mute)", border: `1px solid ${live ? ACCENT + "55" : "var(--line-soft)"}` }}>
              <span className="w-2 h-2 rounded-full" style={{ background: live ? ACCENT : "#6b7280" }} />
              {live ? `connected${st?.tools ? ` · ${st.tools} tools` : ""}` : st?.registered ? "needs sign-in" : "not connected"}
              <button onClick={ping} className="ml-1 opacity-70 hover:opacity-100" title="re-check"><RefreshCw size={11} /></button>
            </div>
          </div>
          <p className="text-[13px] text-[var(--cream-soft)] mt-3 leading-relaxed max-w-[700px]">
            Generate images and video with <b className="text-[var(--cream)]">Higgsfield</b> from inside the OS. Your agent drives it through
            the MCP, every asset lands in the gallery below, and every conversation is kept.
          </p>
          <div className="flex flex-wrap gap-2 mt-3">
            {[{ t: "images up to 4K" }, { t: "video up to 15s" }, { t: "30+ models" }, { t: "driven by Hermes" }].map((c) => (
              <span key={c.t} className="px-2.5 py-1 rounded-full text-[11px]" style={{ border: "1px solid var(--line-soft)", color: "var(--cream-mute)" }}>{c.t}</span>
            ))}
          </div>
        </div>
      </div>

      {/* CONNECT — only when it actually needs doing */}
      {!live && (
        <div className="rounded-xl border p-4" style={{ borderColor: "rgba(240,171,252,0.35)", background: "rgba(192,132,252,0.06)" }}>
          <div className="flex items-center gap-2 text-[13px] font-semibold" style={{ color: ACCENT2 }}>
            <AlertTriangle size={14} /> {st?.registered ? "One sign-in left" : "Not connected yet"}
          </div>
          <p className="text-[12.5px] text-[var(--cream-soft)] mt-2 leading-relaxed">
            {st?.registered
              ? "The Higgsfield MCP is registered with Hermes. It signs in through your Higgsfield account in a browser, which has to be done once from your terminal:"
              : "Add the Higgsfield MCP to Hermes, then sign in through your Higgsfield account:"}
          </p>
          <div className="mt-2 flex items-center gap-2">
            <code className="flex-1 px-3 py-2 rounded-lg text-[12px] mono" style={{ background: "rgba(0,0,0,0.35)", border: "1px solid var(--line-soft)", color: "var(--cream)" }}>
              {st?.loginCommand || "hermes -p julian mcp login higgsfield"}
            </code>
            <button
              onClick={() => { navigator.clipboard.writeText(st?.loginCommand || "hermes -p julian mcp login higgsfield"); setCopied(true); setTimeout(() => setCopied(false), 1500); }}
              className="px-3 py-2 rounded-lg text-[12px] flex items-center gap-1.5"
              style={{ border: "1px solid var(--line-soft)", color: "var(--cream)" }}>
              {copied ? <Check size={12} /> : <Copy size={12} />}{copied ? "copied" : "copy"}
            </button>
          </div>
          <p className="text-[11.5px] text-[var(--cream-mute)] mt-2">
            A browser opens, you approve Higgsfield, and this panel goes live. Hit the refresh icon above afterwards.
            {st?.detail ? <> <span className="mono opacity-70">· {st.detail}</span></> : null}
          </p>
        </div>
      )}

      {/* TABS */}
      <div className="flex items-center gap-2">
        {([["create", "Create", Wand2], ["gallery", "Gallery", FolderOpen], ["history", "History", History]] as const).map(([k, label, Icon]) => (
          <button key={k} onClick={() => { setTab(k); if (k === "gallery") loadGallery(); if (k === "history") loadHistory(); }}
            className="px-3 py-1.5 rounded-lg text-[12.5px] flex items-center gap-1.5"
            style={{ border: `1px solid ${tab === k ? ACCENT + "77" : "var(--line-soft)"}`, background: tab === k ? "rgba(192,132,252,0.12)" : "transparent", color: tab === k ? ACCENT : "var(--cream-mute)" }}>
            <Icon size={12} /> {label}
            {k === "gallery" && items.length ? <span className="opacity-60">{items.length}</span> : null}
            {k === "history" && sessions.length ? <span className="opacity-60">{sessions.length}</span> : null}
          </button>
        ))}
      </div>

      {/* CREATE */}
      {tab === "create" && (
        <div className="rounded-xl border p-4" style={{ borderColor: "var(--panel-border)", background: "rgba(255,255,255,0.02)" }}>
          <div className="flex gap-2 mb-3">
            {(["auto", "image", "video"] as const).map((k) => (
              <button key={k} onClick={() => setKind(k)}
                className="px-3 py-1.5 rounded-lg text-[12px] flex items-center gap-1.5"
                style={{ border: `1px solid ${kind === k ? ACCENT + "77" : "var(--line-soft)"}`, background: kind === k ? "rgba(192,132,252,0.12)" : "transparent", color: kind === k ? ACCENT : "var(--cream-mute)" }}>
                {k === "image" ? <ImageIcon size={12} /> : k === "video" ? <Film size={12} /> : <Sparkles size={12} />} {k}
              </button>
            ))}
          </div>
          <textarea value={prompt} onChange={(e) => setPrompt(e.target.value)} rows={3}
            onKeyDown={(e) => { if (e.key === "Enter" && (e.metaKey || e.ctrlKey)) { e.preventDefault(); send(); } }}
            placeholder={live ? "Describe the shot — lighting, mood, camera move…" : "Sign in above to start generating"}
            disabled={!live || busy}
            className="w-full resize-none p-3 rounded-lg text-[13px]"
            style={{ background: "rgba(255,255,255,0.03)", border: "1px solid var(--panel-border)", color: "var(--cream)", opacity: live ? 1 : 0.6 }} />
          <div className="flex items-center gap-2 mt-2">
            <button onClick={() => send()} disabled={!live || busy || !prompt.trim()}
              className="px-4 py-2 rounded-lg text-[12.5px] font-semibold flex items-center gap-1.5"
              style={{ background: live && prompt.trim() && !busy ? `linear-gradient(135deg, ${ACCENT}, ${ACCENT2})` : "rgba(255,255,255,0.06)", color: live && prompt.trim() && !busy ? "#160a1f" : "var(--cream-mute)" }}>
              {busy ? <Loader2 size={13} className="animate-spin" /> : <Send size={13} />}{busy ? `generating… ${elapsed}s` : "Generate"}
            </button>
            <span className="text-[11.5px] text-[var(--cream-mute)]">⌘↵ to send · video can take a couple of minutes</span>
          </div>
          {err && <div className="mt-3 p-3 rounded-lg text-[12px] mono" style={{ background: "rgba(248,113,113,0.08)", border: "1px solid rgba(248,113,113,0.3)", color: "#fca5a5", whiteSpace: "pre-wrap" }}>{err}</div>}

          <div className="mt-4">
            <div className="text-[11px] uppercase tracking-[0.18em] text-[var(--cream-mute)] mb-2">Try one</div>
            <div className="flex flex-col gap-1.5">
              {IDEAS.map((i) => (
                <button key={i} onClick={() => setPrompt(i)} disabled={busy}
                  className="text-left px-3 py-2 rounded-lg text-[12.5px]"
                  style={{ border: "1px solid var(--line-soft)", background: "rgba(255,255,255,0.02)", color: "var(--cream-soft)" }}>{i}</button>
              ))}
            </div>
          </div>
        </div>
      )}

      {/* GALLERY */}
      {tab === "gallery" && (
        items.length === 0 ? (
          <div className="rounded-xl border p-8 text-center text-[13px] text-[var(--cream-mute)]" style={{ borderColor: "var(--panel-border)" }}>
            Nothing generated yet — everything you make lands here.
          </div>
        ) : (
          <div className="grid gap-3" style={{ gridTemplateColumns: "repeat(auto-fill, minmax(220px, 1fr))" }}>
            {items.map((it) => (
              <button key={it.file} onClick={() => setOpen(it)} className="rounded-xl overflow-hidden text-left" style={{ border: "1px solid var(--panel-border)", background: "rgba(255,255,255,0.02)" }}>
                {it.kind === "video"
                  ? <video src={`/api/higgs/gallery?file=${encodeURIComponent(it.file)}`} muted loop playsInline
                      onMouseEnter={(e) => (e.currentTarget as HTMLVideoElement).play().catch(() => {})}
                      onMouseLeave={(e) => (e.currentTarget as HTMLVideoElement).pause()}
                      style={{ display: "block", width: "100%", aspectRatio: "16/10", objectFit: "cover", background: "#120d18" }} />
                  : <img src={`/api/higgs/gallery?file=${encodeURIComponent(it.file)}`} alt={it.title} loading="lazy"
                      style={{ display: "block", width: "100%", aspectRatio: "16/10", objectFit: "cover", background: "#120d18" }} />}
                <div className="px-3 py-2">
                  <div className="text-[12.5px] text-[var(--cream)] truncate">{it.title}</div>
                  <div className="text-[11px] text-[var(--cream-mute)] flex items-center gap-1.5">
                    {it.kind === "video" ? <Film size={10} /> : <ImageIcon size={10} />} {kb(it.bytes)} · {ago(it.at)}
                  </div>
                </div>
              </button>
            ))}
          </div>
        )
      )}

      {/* HISTORY */}
      {tab === "history" && (
        sessions.length === 0 ? (
          <div className="rounded-xl border p-8 text-center text-[13px] text-[var(--cream-mute)]" style={{ borderColor: "var(--panel-border)" }}>
            No conversations yet — every generation you run is kept here with its prompt and result.
          </div>
        ) : (
          <div className="flex flex-col gap-2">
            {sessions.map((s) => (
              <div key={s.id} className="rounded-xl border p-3" style={{ borderColor: "var(--panel-border)", background: "rgba(255,255,255,0.02)" }}>
                <div className="flex items-center gap-2 text-[11px] text-[var(--cream-mute)]">
                  <span className="mono">{s.kind}</span> · {ago(s.at)} · {Math.round(s.ms / 1000)}s
                  {s.created?.length ? <span style={{ color: ACCENT }}>· {s.created.length} asset{s.created.length > 1 ? "s" : ""}</span> : <span style={{ color: "#fca5a5" }}>· nothing produced</span>}
                </div>
                <div className="text-[13px] text-[var(--cream)] mt-1">{s.prompt}</div>
                {s.note && <div className="text-[12px] text-[var(--cream-soft)] mt-1 italic">{s.note}</div>}
                {!!s.created?.length && (
                  <div className="flex gap-2 mt-2 flex-wrap">
                    {s.created.map((f) => (
                      <a key={f} href={`/api/higgs/gallery?file=${encodeURIComponent(f)}`} target="_blank" rel="noopener"
                        className="text-[11.5px] px-2 py-1 rounded-lg flex items-center gap-1"
                        style={{ border: "1px solid var(--line-soft)", color: ACCENT }}><Download size={10} /> {f}</a>
                    ))}
                  </div>
                )}
              </div>
            ))}
          </div>
        )
      )}

      {/* LIGHTBOX */}
      {open && (
        <div onClick={() => setOpen(null)} className="fixed inset-0 z-50 grid place-items-center p-6" style={{ background: "rgba(8,5,12,0.82)", backdropFilter: "blur(6px)" }}>
          <div onClick={(e) => e.stopPropagation()} className="max-w-[92vw] max-h-[88vh] rounded-2xl overflow-hidden" style={{ border: `1px solid ${ACCENT}55` }}>
            {open.kind === "video"
              ? <video src={`/api/higgs/gallery?file=${encodeURIComponent(open.file)}`} controls autoPlay loop style={{ display: "block", maxWidth: "92vw", maxHeight: "80vh" }} />
              : <img src={`/api/higgs/gallery?file=${encodeURIComponent(open.file)}`} alt={open.title} style={{ display: "block", maxWidth: "92vw", maxHeight: "80vh" }} />}
            <div className="px-4 py-2 flex items-center gap-3" style={{ background: "rgba(0,0,0,0.5)" }}>
              <span className="text-[12.5px] text-[var(--cream)]">{open.title}</span>
              <a href={`/api/higgs/gallery?file=${encodeURIComponent(open.file)}`} download className="ml-auto text-[12px] flex items-center gap-1" style={{ color: ACCENT }}><Download size={12} /> download</a>
            </div>
          </div>
        </div>
      )}

      <div className="text-[11px] text-[var(--cream-mute)] px-1 flex items-center gap-1.5">
        <FolderOpen size={11} /> Saved to <span className="mono">~/.agentic-os/higgsfield/</span> — assets in <span className="mono">gallery/</span>, conversations in <span className="mono">sessions/</span>.
        <a href={SITE} target="_blank" rel="noopener" className="ml-auto flex items-center gap-1" style={{ color: ACCENT }}><ExternalLink size={11} /> higgsfield.ai/mcp</a>
      </div>

      <style jsx global>{`
        @keyframes hgAurora { 0%,100% { transform: translate3d(-4%, -2%, 0) scale(1); } 50% { transform: translate3d(4%, 3%, 0) scale(1.06); } }
      `}</style>
    </div>
  );
}
