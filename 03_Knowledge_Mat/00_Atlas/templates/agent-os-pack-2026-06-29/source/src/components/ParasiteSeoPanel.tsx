"use client";

import { useEffect, useState } from "react";
import Link from "next/link";
import { Crosshair, RefreshCw, Copy, Check, ExternalLink, Video, MessageCircle, Clapperboard, KanbanSquare } from "lucide-react";

// Parasite SEO — GSC platform properties → cross-platform keyword arbitrage.
// Find what already ranks (on your sites today; on X/IG/TikTok/YT the moment
// Google's API exposes platform properties), then remake it platform-native
// with the Agent OS: Claude writes it all — threads in the Claude tab, video
// scripts inside the Video Director pipeline.

type PlatformId = "x" | "instagram" | "tiktok" | "youtube";
interface Platform { id: PlatformId; name: string; connected: boolean; apiVisible: boolean; status: string; }
interface Play { platform: PlatformId; format: string; tool: string; href: string; prompt: string; }
interface Opp { keyword: string; impressions: number; clicks: number; position: number; site?: string; badges: string[]; plays: Play[]; }

const ACCENT = "#00BFFF";
const P_META: Record<PlatformId, { icon: string; color: string }> = {
  x: { icon: "𝕏", color: "#e7e9ea" },
  instagram: { icon: "📸", color: "#e1618d" },
  tiktok: { icon: "🎵", color: "#69f0d2" },
  youtube: { icon: "▶", color: "#ff6b6b" },
};

type Filter = "all" | "video" | "thread" | "vertical" | "noclick";
const FILTERS: { key: Filter; label: string }[] = [
  { key: "all", label: "All plays" },
  { key: "video", label: "▶ YouTube videos" },
  { key: "vertical", label: "📱 Reels · Shorts" },
  { key: "thread", label: "𝕏 Threads · posts" },
  { key: "noclick", label: "💰 No-click gold" },
];

export default function ParasiteSeoPanel() {
  const [platforms, setPlatforms] = useState<Platform[]>([]);
  const [connected, setConnected] = useState<boolean | null>(null);
  const [opps, setOpps] = useState<Opp[] | null>(null);
  const [days, setDays] = useState(28);
  const [scanning, setScanning] = useState(false);
  const [err, setErr] = useState<string | null>(null);
  const [filter, setFilter] = useState<Filter>("all");
  const [copied, setCopied] = useState<string | null>(null);

  useEffect(() => {
    fetch("/api/seo/parasite", { cache: "no-store" })
      .then((r) => r.json())
      .then((j) => { setPlatforms(j.platforms ?? []); setConnected(!!j.connected); })
      .catch(() => setConnected(false));
  }, []);

  async function scan() {
    setScanning(true); setErr(null);
    try {
      const r = await fetch("/api/seo/parasite", {
        method: "POST", headers: { "content-type": "application/json" },
        body: JSON.stringify({ days }),
      });
      const j = await r.json();
      if (j.error) setErr(j.error);
      else setOpps(j.opportunities ?? []);
    } catch { setErr("scan failed"); }
    setScanning(false);
  }

  function copyPrompt(key: string, text: string) {
    navigator.clipboard?.writeText(text);
    setCopied(key);
    setTimeout(() => setCopied((c) => (c === key ? null : c)), 1500);
  }

  const shown = (opps ?? []).filter((o) => {
    if (filter === "all") return true;
    if (filter === "noclick") return o.clicks === 0 && o.impressions >= 50;
    if (filter === "video") return o.plays.some((p) => p.platform === "youtube");
    if (filter === "vertical") return o.plays.some((p) => p.format === "reel" || p.format === "short");
    if (filter === "thread") return o.plays.some((p) => p.platform === "x");
    return true;
  });

  return (
    <div className="space-y-4">
      {/* the loop, in one strip */}
      <div className="rounded-md border p-4" style={{ borderColor: "var(--line-soft)", background: "rgba(0,191,255,0.04)" }}>
        <div className="flex items-center gap-2 mb-1.5">
          <Crosshair size={14} style={{ color: ACCENT }} />
          <span className="text-[13px] font-medium" style={{ color: "var(--cream)" }}>Parasite SEO — rank once, harvest everywhere</span>
        </div>
        <div className="text-[11.5px] leading-relaxed" style={{ color: "var(--cream-dim)" }}>
          Search Console now tracks how <b>Instagram, TikTok, X and YouTube posts</b> perform on Google.
          The loop: find a query you already rank for on one platform → remake it <i>platform-native</i> on the others
          (thread on X, Reel on IG, Short on TikTok, video on YouTube) → every platform becomes a door to the same search demand.
          Below: your live search queries, auto-matched to the right play and the Agent OS surface that makes it.
        </div>
      </div>

      {/* platform property status — honest about what Google exposes */}
      <div className="grid grid-cols-2 lg:grid-cols-4 gap-2">
        {platforms.map((p) => (
          <div key={p.id} className="rounded-md border p-3" style={{ borderColor: "var(--line-soft)" }}>
            <div className="flex items-center gap-2">
              <span className="text-[15px]" style={{ color: P_META[p.id].color }}>{P_META[p.id].icon}</span>
              <span className="text-[12px]" style={{ color: "var(--cream)" }}>{p.name}</span>
              <span className="ml-auto w-2 h-2 rounded-full"
                style={{ background: p.apiVisible ? "#00BFFF" : p.connected ? "#fbbf24" : "#4a4456" }} />
            </div>
            <div className="text-[10px] mt-1.5 leading-snug" style={{ color: "var(--cream-mute)" }}>{p.status}</div>
            {!p.connected && (
              <a href="https://search.google.com/search-console/welcome" target="_blank" rel="noopener noreferrer"
                className="inline-flex items-center gap-1 text-[10px] mt-1.5 hover:underline" style={{ color: ACCENT }}>
                <ExternalLink size={9} /> Add in Search Console
              </a>
            )}
          </div>
        ))}
      </div>

      {/* scan controls */}
      <div className="flex items-center gap-2 flex-wrap">
        <button onClick={scan} disabled={scanning || connected === false}
          className="px-4 py-2 rounded-md text-[12px] font-medium transition disabled:opacity-40"
          style={{ background: `${ACCENT}22`, border: `1px solid ${ACCENT}66`, color: ACCENT }}>
          {scanning ? <RefreshCw size={12} className="inline mr-1.5 animate-spin" /> : <Crosshair size={12} className="inline mr-1.5" />}
          {scanning ? "Scanning your search demand…" : "Scan queries → plays"}
        </button>
        {[7, 28, 90].map((d) => (
          <button key={d} onClick={() => setDays(d)}
            className="px-2.5 py-1.5 rounded-md text-[11px] mono transition"
            style={{
              border: `1px solid ${days === d ? `${ACCENT}66` : "var(--line-soft)"}`,
              color: days === d ? ACCENT : "var(--cream-mute)",
              background: days === d ? `${ACCENT}11` : "transparent",
            }}>{d}d</button>
        ))}
        {connected === false && (
          <span className="text-[11px]" style={{ color: "#fbbf24" }}>
            Search Console not connected — open the Research tab first.
          </span>
        )}
        {opps && (
          <span className="text-[11px] mono ml-auto" style={{ color: "var(--cream-mute)" }}>
            {shown.length} opportunities
          </span>
        )}
      </div>

      {err && <div className="text-[11.5px] rounded-md border p-3" style={{ borderColor: "rgba(248,113,113,.4)", color: "#f8a3a3" }}>{err}</div>}

      {/* results */}
      {opps && (
        <>
          <div className="flex items-center gap-1.5 flex-wrap">
            {FILTERS.map((f) => (
              <button key={f.key} onClick={() => setFilter(f.key)}
                className="px-2.5 py-1 rounded-full text-[10.5px] transition"
                style={{
                  border: `1px solid ${filter === f.key ? `${ACCENT}66` : "var(--line-soft)"}`,
                  color: filter === f.key ? ACCENT : "var(--cream-dim)",
                  background: filter === f.key ? `${ACCENT}11` : "transparent",
                }}>{f.label}</button>
            ))}
          </div>

          <div className="space-y-1.5">
            {shown.slice(0, 60).map((o, i) => (
              <div key={`${o.keyword}-${i}`} className="rounded-md border p-3" style={{ borderColor: "var(--line-soft)" }}>
                <div className="flex items-center gap-2 flex-wrap">
                  <span className="text-[12.5px]" style={{ color: "var(--cream)" }}>{o.keyword}</span>
                  {o.clicks === 0 && o.impressions >= 50 && (
                    <span className="text-[9px] px-1.5 py-0.5 rounded-full uppercase tracking-wider"
                      style={{ background: "rgba(251,191,36,.12)", border: "1px solid rgba(251,191,36,.4)", color: "#fbbf24" }}>
                      shown {o.impressions}× · zero clicks
                    </span>
                  )}
                  <span className="text-[10px] mono ml-auto shrink-0" style={{ color: "var(--cream-mute)" }}>
                    {o.impressions.toLocaleString()} impr · {o.clicks} clicks · pos {o.position.toFixed(1)}{o.site ? ` · ${o.site.replace(/^(sc-domain:|https?:\/\/)/, "").replace(/\/$/, "")}` : ""}
                  </span>
                </div>
                <div className="flex items-center gap-1.5 mt-2 flex-wrap">
                  {o.plays.map((p) => {
                    const key = `${o.keyword}:${p.platform}`;
                    const Icon = p.platform === "youtube" ? Video : p.platform === "x" ? MessageCircle : Clapperboard;
                    return (
                      <span key={key} className="inline-flex items-center rounded-md overflow-hidden border" style={{ borderColor: "var(--line-soft)" }}>
                        <Link href={p.href}
                          className="inline-flex items-center gap-1.5 px-2 py-1 text-[10.5px] transition hover:bg-[rgba(255,255,255,0.04)]"
                          style={{ color: P_META[p.platform].color }}>
                          <Icon size={10} />
                          {P_META[p.platform].icon} {p.format} · {p.tool}
                        </Link>
                        <button onClick={() => copyPrompt(key, p.prompt)} title="Copy the ready-to-paste prompt"
                          className="px-1.5 py-1 border-l transition hover:bg-[rgba(255,255,255,0.04)]"
                          style={{ borderColor: "var(--line-soft)", color: copied === key ? "#00BFFF" : "var(--cream-mute)" }}>
                          {copied === key ? <Check size={10} /> : <Copy size={10} />}
                        </button>
                      </span>
                    );
                  })}
                  <Link href="/kanban" className="inline-flex items-center gap-1 px-2 py-1 rounded-md border text-[10.5px] transition hover:bg-[rgba(255,255,255,0.04)]"
                    style={{ borderColor: "var(--line-soft)", color: "var(--cream-dim)" }}>
                    <KanbanSquare size={10} /> Kanban
                  </Link>
                </div>
              </div>
            ))}
          </div>
        </>
      )}

      {!opps && !scanning && (
        <div className="text-[11.5px] italic p-2" style={{ color: "var(--cream-mute)" }}>
          Hit <b>Scan queries → plays</b> — every query Google already shows you for becomes a platform play:
          𝕏 thread written by Claude, ▶ video / 📱 Reel / Short scripted by Claude in the Video Director, one copy-paste prompt each.
        </div>
      )}
    </div>
  );
}
