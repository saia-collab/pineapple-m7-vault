import { NextResponse } from "next/server";
import { promises as fs } from "fs";
import os from "os";
import path from "path";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// The Kanban BOARD state (cards + goal + model) lives on disk, not just in one
// browser's localStorage. Before this, a board assembled in one browser was
// invisible everywhere else — every other browser saw an empty board — because
// the columns were per-browser while the Workspace was server-side.
const FILE = path.join(os.homedir(), ".agentic-os", "agent-kanban", "board.json");

async function read(): Promise<unknown | null> {
  try { return JSON.parse(await fs.readFile(FILE, "utf8")); } catch { return null; }
}

export async function GET() {
  const board = await read();
  return NextResponse.json({ board });
}

export async function POST(req: Request) {
  const body = await req.json().catch(() => null);
  if (!body || !Array.isArray(body.cards)) {
    return NextResponse.json({ error: "cards[] required" }, { status: 400 });
  }
  const board = {
    cards: body.cards.slice(0, 200),
    goal: typeof body.goal === "string" ? body.goal.slice(0, 2000) : "",
    model: typeof body.model === "string" ? body.model.slice(0, 120) : null,
    savedAt: Date.now(),
  };
  await fs.mkdir(path.dirname(FILE), { recursive: true });
  await fs.writeFile(FILE, JSON.stringify(board), "utf8");
  return NextResponse.json({ ok: true, saved: board.cards.length });
}
