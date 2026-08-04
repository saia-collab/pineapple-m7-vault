import { execFile } from "node:child_process";
import { promisify } from "node:util";
import { existsSync, readFileSync } from "node:fs";
import path from "node:path";
import os from "node:os";
import { config } from "@/lib/config";

const pexec = promisify(execFile);
export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// Parasite SEO — cross-platform keyword arbitrage on top of Google Search Console.
//
// GSC's July-2026 "platform properties" track how Instagram / TikTok / X / YouTube
// posts perform on Google Search. The play: find a query one platform (or one of
// your sites) already ranks for, then recreate that content platform-native
// everywhere else — thread on X, Reel on Instagram, Short on TikTok/YouTube.
//
// HONEST DATA NOTE: as of 2026-07-31 platform properties exist in the GSC UI but
// are NOT exposed through the Search Console API (sites.list returns website
// properties only — verified live). So this route (a) auto-detects platform
// properties the moment Google ships API support (any siteUrl that isn't a
// website counts), and (b) runs the working arbitrage engine off the member's
// website queries today.

const AOS = path.join(os.homedir(), ".agentic-os");
const BUNDLED = path.join(process.cwd(), "scripts", "gsc-research.py");
const SCRIPT = existsSync(BUNDLED) ? BUNDLED : path.join(AOS, "gsc-research.py");
const TOKEN = path.join(AOS, "gsc-token.json");
const LATEST = path.join(AOS, "gsc-latest.json");
const PARASITE_CFG = path.join(AOS, "parasite.json");
const PY = "/usr/bin/python3";

type PlatformId = "x" | "instagram" | "tiktok" | "youtube";
interface Platform {
  id: PlatformId; name: string;
  connected: boolean;   // member added it as a GSC platform property (UI-side)
  apiVisible: boolean;  // Google exposes its data via the API (auto-detected)
  status: string;
}

function connectedFlags(): Record<PlatformId, boolean> {
  try {
    const j = JSON.parse(readFileSync(PARASITE_CFG, "utf8")) as { connected?: Record<string, boolean> };
    return { x: !!j.connected?.x, instagram: !!j.connected?.instagram, tiktok: !!j.connected?.tiktok, youtube: !!j.connected?.youtube };
  } catch {
    return { x: false, instagram: false, tiktok: false, youtube: false };
  }
}

// Any GSC property that is NOT a website (sc-domain: / http) is a platform property.
async function detectPlatformProps(): Promise<string[]> {
  if (!existsSync(TOKEN)) return [];
  const code = `
import json,sys
from pathlib import Path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
t=Path.home()/'.agentic-os'/'gsc-token.json'
c=Credentials.from_authorized_user_info(json.loads(t.read_text()))
if not c.valid and c.refresh_token:
    c.refresh(Request()); t.write_text(c.to_json())
svc=build('searchconsole','v1',credentials=c,cache_discovery=False)
urls=[s['siteUrl'] for s in svc.sites().list().execute().get('siteEntry',[])]
print(json.dumps([u for u in urls if not (u.startswith('sc-domain:') or u.startswith('http'))]))
`;
  try {
    const { stdout } = await pexec(PY, ["-c", code], { timeout: 30_000, env: { ...process.env, PYTHONWARNINGS: "ignore" } });
    return JSON.parse(stdout.trim().split("\n").filter(Boolean).pop() || "[]");
  } catch { return []; }
}

function platformList(apiProps: string[]): Platform[] {
  const flags = connectedFlags();
  const defs: { id: PlatformId; name: string; match: RegExp }[] = [
    { id: "x", name: "X (Twitter)", match: /x|twitter/i },
    { id: "instagram", name: "Instagram", match: /instagram/i },
    { id: "tiktok", name: "TikTok", match: /tiktok/i },
    { id: "youtube", name: "YouTube", match: /youtube/i },
  ];
  return defs.map((d) => {
    const apiVisible = apiProps.some((u) => d.match.test(u));
    const connected = flags[d.id] || apiVisible;
    return {
      ...{ id: d.id, name: d.name }, connected, apiVisible,
      status: apiVisible ? "data live via API"
        : connected ? "connected · Google is propagating data (~48h) · API not exposed yet"
        : "not connected — add it as a property in Search Console",
    };
  });
}

// ── The arbitrage classifier ─────────────────────────────────────────────
// Deterministic intent → platform-play mapping. Each play names the format,
// the Agent OS surface that makes it, and a ready-to-paste prompt.
export interface Play { platform: PlatformId; format: string; tool: string; href: string; prompt: string; }

function plays(q: string): Play[] {
  const out: Play[] = [];
  const add = (platform: PlatformId, format: string, tool: string, href: string, prompt: string) => {
    if (!out.some((p) => p.platform === platform)) out.push({ platform, format, tool, href, prompt });
  };
  // Claude writes everything — threads/posts go to the Claude tab, video formats
  // to the Video Director, whose scripts Claude authors in-pipeline.
  const yt = (why: string) => add("youtube", "video", "Video Director · Claude script", "/video",
    `Write the full YouTube video script targeting the search query "${q}". ${why} Hook in the first 5 seconds, show the real system on screen, end with one clear next step.`);
  const short = (p: PlatformId) => add(p, p === "tiktok" ? "short" : "reel", "Video Director · Claude script", "/video",
    `Write a 30-45s vertical ${p === "tiktok" ? "TikTok" : "Instagram Reel"} script answering "${q}" — one hook line on screen in the first second, fast cuts, big captions, one takeaway.`);
  const thread = () => add("x", "thread", "Claude", "/claude",
    `Write an X thread targeting the search query "${q}". Hook tweet states the payoff plainly, 5-8 tweets, each one concrete step or receipt, last tweet = soft CTA.`);
  const post = () => add("x", "post", "Claude", "/claude",
    `Write one high-signal X post answering "${q}" in under 260 chars — claim, proof, takeaway.`);

  if (/(how to|how do|tutorial|guide|setup|set up|install|build|create|make|step by step|course|learn)/i.test(q)) {
    yt("It's a how-to query — searchers want to watch it done."); short("tiktok"); thread();
  } else if (/( vs |versus|best |top ?\d|review|alternatives?|compare|cheaper|pricing|price)/i.test(q)) {
    thread(); yt("Comparison queries convert — show both sides on screen with receipts.");
  } else if (/(what is|what's|why |explained|meaning|examples?)/i.test(q)) {
    thread(); short("instagram");
  } else if (/(free|template|prompts?|checklist|tools?|download|generator)/i.test(q)) {
    short("instagram"); post();
  } else {
    post(); short("tiktok");
  }
  return out;
}

interface Topic { keyword: string; score: number; impressions: number; clicks: number; ctr: number; position: number; site?: string; badges: string[]; }

async function researchSite(site: string, d: string): Promise<{ topics?: Topic[]; error?: string }> {
  try {
    const { stdout } = await pexec(PY, [SCRIPT, site, d], {
      timeout: 90_000, maxBuffer: 12 * 1024 * 1024,
      env: { ...process.env, PYTHONWARNINGS: "ignore" },
    });
    return JSON.parse(stdout.trim().split("\n").filter(Boolean).pop() || "{}");
  } catch { return { error: "gsc failed" }; }
}

function sites(): string[] {
  try {
    if (existsSync(LATEST)) {
      const keys = Object.keys(JSON.parse(readFileSync(LATEST, "utf8")));
      if (keys.length) return keys;
    }
  } catch { /* fall through */ }
  return Array.isArray(config.seoSites) ? config.seoSites : [];
}

export async function GET() {
  const apiProps = await detectPlatformProps();
  return Response.json({
    connected: existsSync(TOKEN),
    platforms: platformList(apiProps),
    apiProps,
    sites: sites(),
  }, { headers: { "cache-control": "no-store" } });
}

// POST {days} → every site's queries, classified into cross-platform plays.
export async function POST(req: Request) {
  if (!existsSync(SCRIPT) || !existsSync(TOKEN)) {
    return Response.json({ error: "Connect Search Console first (Research tab)." }, { status: 400 });
  }
  const { days } = await req.json().catch(() => ({}));
  const d = String(Math.min(Math.max(parseInt(String(days), 10) || 28, 7), 180));
  const all = await Promise.all(sites().map((s) => researchSite(s, d).then((r) => ({ s, r }))));
  const ok = all.filter(({ r }) => !r.error && Array.isArray(r.topics));
  if (!ok.length) return Response.json({ error: "No GSC data returned." }, { status: 502 });
  const merged = ok.flatMap(({ s, r }) => (r.topics as Topic[]).map((t) => ({ ...t, site: t.site ?? s })));
  merged.sort((a, b) => (b.impressions || 0) - (a.impressions || 0));
  const opportunities = merged.slice(0, 150).map((t) => ({
    keyword: t.keyword, impressions: t.impressions, clicks: t.clicks,
    position: t.position, site: t.site, badges: t.badges ?? [],
    plays: plays(t.keyword),
  }));
  return Response.json({
    days: Number(d), sitesScanned: ok.length, opportunities,
  }, { headers: { "cache-control": "no-store" } });
}
