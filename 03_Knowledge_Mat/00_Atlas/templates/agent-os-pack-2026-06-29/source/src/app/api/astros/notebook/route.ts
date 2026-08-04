import { NextResponse } from "next/server";
export const runtime = "nodejs";
export const dynamic = "force-dynamic";
export async function POST(req: Request) {
  try {
    const { topic } = await req.json();
    // NotebookLM side-load needs the notebooklm CLI/MCP connected. Until then, report clearly.
    return NextResponse.json({ ok: false, error: `NotebookLM handoff isn't wired yet — connect the notebooklm CLI, then this button side-loads the competitor transcript. Queued topic: ${String(topic || "")}` });
  } catch (e) { return NextResponse.json({ ok: false, error: String(e) }, { status: 500 }); }
}
