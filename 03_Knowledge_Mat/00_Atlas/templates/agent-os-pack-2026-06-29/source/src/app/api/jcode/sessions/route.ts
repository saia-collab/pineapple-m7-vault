import { listJcodeSessions, readJcodeTranscript } from "@/lib/jcodeAgent";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// The conversation-history workspace: every jcode session (TUI, `jcode run`,
// Agent OS builds — they all share ~/.jcode/sessions) listed and readable.
export async function GET(req: Request) {
  const id = new URL(req.url).searchParams.get("id");
  if (id) {
    const t = await readJcodeTranscript(id);
    if (!t) return Response.json({ error: "session not found" }, { status: 404 });
    return Response.json(t, { headers: { "cache-control": "no-store" } });
  }
  return Response.json({ sessions: await listJcodeSessions() }, { headers: { "cache-control": "no-store" } });
}
