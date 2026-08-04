import { NextResponse } from "next/server";
import { promises as fs } from "fs";
import os from "os";
import path from "path";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// GET /api/higgs/history        → every Higgsfield conversation, newest first
// GET /api/higgs/history?id=... → one full session incl. the Hermes transcript
const SESSIONS = path.join(os.homedir(), ".agentic-os", "higgsfield", "sessions");

export async function GET(req: Request) {
  const id = new URL(req.url).searchParams.get("id");
  await fs.mkdir(SESSIONS, { recursive: true });

  if (id) {
    try {
      const raw = await fs.readFile(path.join(SESSIONS, `${path.basename(id)}.json`), "utf8");
      return NextResponse.json(JSON.parse(raw));
    } catch {
      return NextResponse.json({ error: "not found" }, { status: 404 });
    }
  }

  const files = (await fs.readdir(SESSIONS).catch(() => [])).filter((f) => f.endsWith(".json"));
  const rows = await Promise.all(files.map(async (f) => {
    try {
      const j = JSON.parse(await fs.readFile(path.join(SESSIONS, f), "utf8"));
      return {
        id: j.id ?? f.replace(/\.json$/, ""),
        prompt: j.prompt ?? "",
        kind: j.kind ?? "auto",
        created: Array.isArray(j.created) ? j.created : [],
        note: j.note ?? "",
        ms: j.ms ?? 0,
        at: j.at ?? 0,
      };
    } catch { return null; }
  }));
  const sessions = rows.filter(Boolean).sort((a, b) => (b!.at as number) - (a!.at as number));
  return NextResponse.json({ count: sessions.length, sessions });
}
