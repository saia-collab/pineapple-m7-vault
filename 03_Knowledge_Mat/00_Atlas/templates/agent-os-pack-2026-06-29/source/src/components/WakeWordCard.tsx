"use client";

// "Hey Hermes" — voice activation living entirely inside the Agent OS.
// Browser-side wake detection; the command is handed to the REAL chat send()
// so the exchange lands in the thread (and is spoken back). Auto-arms on load
// once the mic has been granted, so you never click the ear again.
// Calm UI: still ear, soft glow, one slow-breathing dot. No flashing.
import { useEffect, useRef, useState, useCallback } from "react";
import { motion } from "framer-motion";
import { Ear, EarOff, Loader2 } from "lucide-react";

type SR = {
  continuous: boolean; interimResults: boolean; lang: string;
  onresult: ((e: { resultIndex: number; results: { length: number; [i: number]: { isFinal: boolean; length: number; [j: number]: { transcript: string } } } }) => void) | null;
  onend: (() => void) | null; onerror: ((e: { error?: string }) => void) | null;
  maxAlternatives: number;
  start: () => void; stop: () => void;
};
function getSR(): { new (): SR } | null {
  const w = window as unknown as { SpeechRecognition?: { new (): SR }; webkitSpeechRecognition?: { new (): SR } };
  return w.SpeechRecognition || w.webkitSpeechRecognition || null;
}

// tolerant of what browsers actually hear for "hermes"
const WAKE = /\b(hey|ok|okay|hi)?\s*(hermes|herm\u00e8s|hermez|hermees|hermies|homies|hermas|herms|herbies|hermis|hermits|ermes|kermes|her mes|her miss|air mes)\b/i;

// phonetic fallback: any word within edit-distance 2 of "hermes"
function lev(a: string, b: string): number {
  const m = a.length, n = b.length;
  const d = Array.from({ length: m + 1 }, (_, i) => [i, ...Array(n).fill(0)]);
  for (let j = 1; j <= n; j++) d[0][j] = j;
  for (let i = 1; i <= m; i++) for (let j = 1; j <= n; j++)
    d[i][j] = Math.min(d[i - 1][j] + 1, d[i][j - 1] + 1, d[i - 1][j - 1] + (a[i - 1] === b[j - 1] ? 0 : 1));
  return d[m][n];
}
function exactIndex(text: string): { idx: number; len: number } | null {
  const m = text.match(WAKE);
  return m ? { idx: m.index ?? 0, len: m[0].length } : null;
}
function wakeIndex(text: string): { idx: number; len: number } | null {
  const m = text.match(WAKE);
  if (m) return { idx: m.index ?? 0, len: m[0].length };
  // fuzzy word scan
  let pos = 0;
  for (const w of text.split(/\s+/)) {
    const clean = w.toLowerCase().replace(/[^a-z]/g, "");
    if (clean.length >= 4 && lev(clean, "hermes") <= 2) {
      const idx = text.toLowerCase().indexOf(w.toLowerCase(), pos);
      return { idx: idx < 0 ? pos : idx, len: w.length };
    }
    pos += w.length + 1;
  }
  return null;
}
const LS_KEY = "os_wake_hermes_on";

// Speech APIs re-emit growing interim text and repeat the wake phrase; clean both.
function stripWake(s: string): string {
  return s.replace(new RegExp(WAKE.source, "gi"), " ").replace(/\s+/g, " ").trim();
}
function dedupe(s: string): string {
  const w = s.split(/\s+/).filter(Boolean);
  // drop any immediately-repeated run of 1-6 words ("what time is it what time is it")
  for (let n = 6; n >= 1; n--) {
    for (let i = 0; i + 2 * n <= w.length; i++) {
      while (i + 2 * n <= w.length &&
             w.slice(i, i + n).join(" ").toLowerCase() === w.slice(i + n, i + 2 * n).join(" ").toLowerCase()) {
        w.splice(i + n, n);
      }
    }
  }
  return w.join(" ").trim();
}

type Phase = "off" | "listening" | "capturing" | "working" | "mic-blocked";

export default function WakeWordCard({ onCommand, busy }: { onCommand: (cmd: string) => void; busy?: boolean }) {
  const [phase, setPhase] = useState<Phase>("off");
  const [heard, setHeard] = useState<string | null>(null);
  const [echo, setEcho] = useState<string | null>(null);
  const srRef = useRef<SR | null>(null);
  const onRef = useRef(false);
  const phaseRef = useRef<Phase>("off");
  const bufRef = useRef("");
  const liveRef = useRef("");
  const holdRef = useRef<ReturnType<typeof setTimeout> | null>(null);
  const coolRef = useRef(0);
  const lastCmdRef = useRef<{ cmd: string; at: number }>({ cmd: "", at: 0 });
  const setPh = (p: Phase) => { phaseRef.current = p; setPhase(p); };

  const fire = useCallback((cmd: string) => {
    const clean = cmd.trim();
    const words = clean.split(/\s+/).filter(Boolean);
    // guards: empty, ambient rambles (>20 words), or a repeat of the last command within 30s
    if (!clean || words.length > 20) { setPh("listening"); return; }
    const lc = lastCmdRef.current;
    if (Date.now() - lc.at < 30000 && (clean === lc.cmd || clean.includes(lc.cmd) || lc.cmd.includes(clean)) && lc.cmd) {
      setPh("listening"); return;
    }
    lastCmdRef.current = { cmd: clean, at: Date.now() };
    coolRef.current = Date.now() + 5000;   // 5s wake cooldown after firing
    setHeard(clean);
    setPh("working");
    onCommand(clean);
    setTimeout(() => { if (onRef.current) setPh("listening"); }, 1200);
  }, [onCommand]);

  const startRecognizer = useCallback(() => {
    const Ctor = getSR();
    if (!Ctor) { setPh("mic-blocked"); return; }
    try { srRef.current?.stop(); } catch { /* previous */ }
    const sr = new Ctor();
    sr.continuous = true; sr.interimResults = true; sr.lang = "en-US"; sr.maxAlternatives = 5;

    sr.onresult = (e) => {
      let finals = "", interim = "";
      const altSet: string[] = [];
      for (let i = e.resultIndex; i < e.results.length; i++) {
        const res = e.results[i];
        const tx = res[0].transcript;
        for (let j = 0; j < Math.min(res.length ?? 1, 5); j++) {
          if (res[j]?.transcript) altSet.push(res[j].transcript);
        }
        if (res.isFinal) finals += tx + " "; else interim += tx;
      }
      // debug line: always show the latest primary transcription
      const latest = (finals || interim).trim();
      if (latest) setEcho(latest.length > 60 ? "…" + latest.slice(-60) : latest);
      const p = phaseRef.current;
      if (p === "working") return;

      if (p === "listening") {
        if (Date.now() < coolRef.current) return;          // post-fire cooldown
        const all = finals + " " + interim;
        // exact phrase can fire from interim; FUZZY requires a FINAL transcript
        let hit = exactIndex(all);
        let src = all;
        if (!hit && finals.trim()) {
          hit = wakeIndex(finals); src = finals;
          if (!hit) {
            for (const alt of altSet) {
              const h = wakeIndex(alt);
              if (h) { hit = h; src = alt; break; }
            }
          }
        }
        if (!hit) return;
        const after = dedupe(stripWake(src.slice(hit.idx + hit.len)));
        if (wakeIndex(finals) && after.split(/\s+/).filter(Boolean).length >= 2) {
          fire(after);                      // wake + command in one breath
        } else {
          bufRef.current = after;
          setPh("capturing");               // wake alone → wait for the command
          if (holdRef.current) clearTimeout(holdRef.current);
          holdRef.current = setTimeout(() => {
            if (phaseRef.current === "capturing") {
              const b = dedupe(stripWake(`${bufRef.current} ${liveRef.current}`));
              bufRef.current = ""; liveRef.current = "";
              if (b) fire(b); else setPh("listening");
            }
          }, 4000);
        }
      } else if (p === "capturing") {
        // interim text is a GROWING re-emission of the same phrase — replace, never append
        if (interim) liveRef.current = interim.trim();
        if (finals.trim()) {
          if (holdRef.current) clearTimeout(holdRef.current);
          const cmd = dedupe(stripWake(`${bufRef.current} ${finals}`));
          bufRef.current = ""; liveRef.current = "";
          fire(cmd);
        }
      }
    };

    sr.onerror = (e) => {
      if (e.error === "not-allowed" || e.error === "service-not-allowed") {
        onRef.current = false; setPh("mic-blocked");
      }
    };
    // Chrome cuts continuous sessions every ~60s — restart so it stays always-on
    sr.onend = () => {
      if (onRef.current && phaseRef.current !== "mic-blocked") {
        setTimeout(() => { try { srRef.current?.start(); } catch { /* racing */ } }, 300);
      }
    };

    srRef.current = sr;
    try { sr.start(); setPh("listening"); } catch { setPh("mic-blocked"); }
  }, [fire]);

  const arm = useCallback(() => {
    onRef.current = true;
    try { localStorage.setItem(LS_KEY, "1"); } catch { /* private mode */ }
    startRecognizer();
  }, [startRecognizer]);

  const disarm = () => {
    onRef.current = false;
    try { srRef.current?.stop(); } catch { /* off */ }
    try { localStorage.setItem(LS_KEY, "0"); } catch { /* private mode */ }
    setPh("off");
  };

  // AUTO-ARM: if the mic is already granted for this site, start listening on load —
  // no click needed, ever again. Only a first-time (or revoked) permission needs the tap.
  useEffect(() => {
    let cancelled = false;
    (async () => {
      const wanted = (() => { try { return localStorage.getItem(LS_KEY) !== "0"; } catch { return true; } })();
      if (!wanted) return;
      try {
        const perms = (navigator as unknown as { permissions?: { query: (d: { name: string }) => Promise<{ state: string }> } }).permissions;
        const st = perms ? await perms.query({ name: "microphone" }) : null;
        if (!cancelled && (!st || st.state === "granted")) arm();
        else if (!cancelled) setPh("off");
      } catch { if (!cancelled) arm(); }
    })();
    return () => {
      cancelled = true;
      onRef.current = false;
      try { srRef.current?.stop(); } catch { /* unmount */ }
      if (holdRef.current) clearTimeout(holdRef.current);
    };
  }, [arm]);

  const live = phase === "listening" || phase === "capturing" || phase === "working";
  const teal = "#3fd6c0";
  const label =
    phase === "capturing" ? "GO AHEAD" :
    phase === "working" || busy ? "ON IT" :
    phase === "listening" ? "LISTENING" :
    phase === "mic-blocked" ? "ALLOW MIC" : "OFF";

  return (
    <div
      className="mx-5 mt-3 rounded-2xl px-5 py-4"
      style={{
        border: `1px solid ${live ? "rgba(63,214,192,.35)" : "var(--panel-border)"}`,
        background: "linear-gradient(135deg, rgba(255,255,255,.025), rgba(255,255,255,.008))",
        boxShadow: live ? "inset 0 0 60px -30px rgba(63,214,192,.22)" : "none",
        transition: "border-color .6s ease, box-shadow .6s ease",
      }}
    >
      <div className="flex items-center gap-5">
        <button
          onClick={() => (live ? disarm() : arm())}
          aria-label={live ? "Turn wake word off" : "Turn wake word on"}
          className="grid place-items-center rounded-full flex-none"
          style={{
            width: 58, height: 58, cursor: "pointer", border: 0,
            background: live
              ? "radial-gradient(circle at 35% 30%, #49e0c9, #17705f)"
              : "radial-gradient(circle at 35% 30%, #38323f, #221d2b)",
            boxShadow: live
              ? "0 6px 26px -8px rgba(63,214,192,.55), inset 0 1px 0 rgba(255,255,255,.25)"
              : "0 4px 16px -8px rgba(0,0,0,.6), inset 0 1px 0 rgba(255,255,255,.06)",
            transition: "background .6s ease, box-shadow .6s ease",
          }}
        >
          {phase === "working" || busy
            ? <Loader2 size={24} className="animate-spin" color="#eafffb" />
            : live
              ? <Ear size={24} color="#062a24" strokeWidth={2.4} />
              : <EarOff size={22} color="#8d8499" strokeWidth={2} />}
        </button>

        <div className="min-w-0 flex-1">
          <div className="flex items-baseline justify-between gap-3 flex-wrap">
            <span className="font-semibold truncate"
                  style={{ fontFamily: "'Bricolage Grotesque',sans-serif", fontSize: 20, letterSpacing: "-0.01em", color: "var(--ink, #f0ead9)" }}>
              &ldquo;hey hermes&rdquo;
            </span>
            <span className="flex items-center gap-1.5 text-[11px] font-semibold tracking-[0.14em]"
                  style={{ color: live ? teal : phase === "mic-blocked" ? "#c4607e" : "#8d8499" }}>
              {phase === "listening" && (
                <motion.span className="inline-block rounded-full" style={{ width: 6, height: 6, background: teal }}
                  animate={{ opacity: [1, 0.35, 1] }} transition={{ duration: 3.2, repeat: Infinity, ease: "easeInOut" }} />
              )}
              {label}
            </span>
          </div>
          <div className="text-[12.5px] mt-1" style={{ color: "#a89e8f" }}>
            {phase === "mic-blocked"
              ? "Allow the microphone for this site, then tap the ear once — it stays on after that."
              : phase === "capturing"
                ? "Listening for your command…"
                : live
                  ? "Always on. Say it — the answer lands in the chat in seconds, spoken too."
                  : "Tap once to arm. It re-arms itself every time you open the OS."}
          </div>
          <div className="text-[10.5px] mt-1.5" style={{ color: "#6d6478", letterSpacing: "0.04em" }}>
            {heard ? `last command · "${heard.length > 48 ? heard.slice(0, 48) + "…" : heard}"` : echo ? `hearing · "${echo}"` : "in-browser wake · GPT-5.6 Terra · ~4s replies"}
          </div>
        </div>
      </div>
    </div>
  );
}
