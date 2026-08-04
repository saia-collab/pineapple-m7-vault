import { NextResponse } from "next/server";
import { promises as fs } from "fs";
import os from "os";
import path from "path";
import { run } from "@/lib/runner";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// POST /api/higgs/run  { prompt, kind?: "image" | "video" | "auto" }
// Drives Higgsfield THROUGH Hermes, so the MCP tool calls, the model's reasoning and
// the resulting asset URLs all land in one place. Hermes is told to save every asset
// it produces into the gallery dir, so the OS gallery is a byproduct of the run rather
// than a separate sync step that can drift.
// Profile: HIGGS_PROFILE env → the member's active Hermes profile (never a hardcoded name).
import { readFileSync } from "fs";
import { hermesHome } from "@/lib/config";
function higgsProfile(): string {
  if (process.env.HIGGS_PROFILE) return process.env.HIGGS_PROFILE;
  try { return readFileSync(path.join(hermesHome(), "active_profile"), "utf8").trim() || "main"; } catch { return "main"; }
}
const PROFILE = higgsProfile();
const ROOT = path.join(os.homedir(), ".agentic-os", "higgsfield");
const GALLERY = path.join(ROOT, "gallery");
const SESSIONS = path.join(ROOT, "sessions");
const ANSI = /\[[0-9;]*m/g;

const GUIDE = (kind: string) =>
  [
    "You have the `higgsfield` MCP server connected — it generates images and video.",
    kind === "image" ? "Use an IMAGE generation tool." : kind === "video" ? "Use a VIDEO generation tool." : "Pick the most appropriate Higgsfield tool for the request.",
    `Save every finished asset into ${GALLERY} using a short kebab-case filename that describes it`,
    "(download it with your file/shell tools — do not just print the URL).",
    "When you are done, print a final line of STRICT JSON and nothing after it:",
    '{"assets":[{"file":"<filename in the gallery dir>","url":"<source url>","kind":"image|video","prompt":"<the prompt you used>","model":"<higgsfield model if known>"}],"note":"<one sentence>"}',
  ].join(" ");

export async function POST(req: Request) {
  const body = await req.json().catch(() => ({}));
  const prompt = String(body.prompt ?? "").trim();
  const kind = ["image", "video", "auto"].includes(String(body.kind)) ? String(body.kind) : "auto";
  if (!prompt) return NextResponse.json({ error: "prompt required" }, { status: 400 });

  await fs.mkdir(GALLERY, { recursive: true });
  await fs.mkdir(SESSIONS, { recursive: true });
  const before = new Set(await fs.readdir(GALLERY).catch(() => []));

  const started = Date.now();
  const full = `${GUIDE(kind)}\n\nREQUEST:\n${prompt}`;
  const r = await run("hermes", ["-p", PROFILE, "-z", full, "--yolo", "--accept-hooks"], { timeoutMs: 900_000, cwd: GALLERY });
  const out = (r.stdout || "").replace(ANSI, "").trim();

  // whatever actually appeared on disk is the truth — the JSON line is only a hint
  const after = await fs.readdir(GALLERY).catch(() => []);
  const created = after.filter((f) => !before.has(f) && !f.startsWith("."));

  let parsed: { assets?: unknown[]; note?: string } = {};
  const m = out.match(/\{[\s\S]*"assets"[\s\S]*\}\s*$/);
  if (m) { try { parsed = JSON.parse(m[0]); } catch { /* keep the disk truth */ } }

  const id = `${new Date().toISOString().replace(/[:.]/g, "-").slice(0, 19)}`;
  const session = {
    id, prompt, kind, created, note: parsed.note ?? "",
    assets: Array.isArray(parsed.assets) ? parsed.assets : [],
    transcript: out.slice(-8000),
    ms: Date.now() - started,
    at: Date.now(),
  };
  await fs.writeFile(path.join(SESSIONS, `${id}.json`), JSON.stringify(session, null, 1), "utf8");

  const failed = !created.length;
  return NextResponse.json({
    ok: !failed,
    id,
    created,
    note: parsed.note ?? "",
    ms: session.ms,
    // when nothing landed, hand back the tail so the cause is visible instead of a silent empty gallery
    error: failed ? (out.slice(-600) || `hermes exited ${r.code} with no output`) : undefined,
  });
}
