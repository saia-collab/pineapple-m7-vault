import { NextResponse } from "next/server";
import { readFile, writeFile, mkdir } from "node:fs/promises";
import { existsSync } from "node:fs";
import path from "node:path";
import os from "node:os";
export const runtime = "nodejs";
export const dynamic = "force-dynamic";
const DIR = path.join(os.homedir(), ".agentic-os");
const CFG = path.join(DIR, "astros-config.json");
// M7 default watchlist — roofing/restoration + local-AI niches, keyless RSS engine ($0).
const DEFAULTS = { channels: [] as string[], keywords: ["roofing marketing","storm restoration","home services ai","construction tech","local ai agents"], engine: "rss" };
async function load() { try { return { ...DEFAULTS, ...JSON.parse(await readFile(CFG, "utf8")) }; } catch { return DEFAULTS; } }
export async function GET() { const c = await load(); return NextResponse.json({ ok: true, ...c }); }
export async function POST(req: Request) {
  try {
    const b = await req.json(); const cur = await load();
    const next = { channels: Array.isArray(b.channels) ? b.channels : cur.channels, keywords: Array.isArray(b.keywords) ? b.keywords : cur.keywords, engine: typeof b.engine === "string" ? b.engine : cur.engine };
    if (!existsSync(DIR)) await mkdir(DIR, { recursive: true });
    await writeFile(CFG, JSON.stringify(next, null, 2), "utf8");
    return NextResponse.json({ ok: true, ...next });
  } catch (e) { return NextResponse.json({ ok: false, error: String(e) }, { status: 500 }); }
}
