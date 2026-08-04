import { NextResponse } from "next/server";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// POST /api/hermes/realtime/sdp?model=gpt-realtime
//   header: x-oai-ephemeral = <ephemeral client secret from /session>
//   body:   the browser's WebRTC SDP offer (Content-Type: application/sdp)
//   → returns OpenAI's SDP answer (application/sdp)
//
// M7 fix: the browser POSTs its SDP offer to THIS local route instead of calling
// api.openai.com directly. The dashboard server (which CAN reach OpenAI) relays the
// exchange and returns the answer. This bypasses browser/AV/proxy blocks that stop
// Chrome from opening the realtime audio link directly.
export async function POST(req: Request) {
  const url = new URL(req.url);
  const model = url.searchParams.get("model") || "gpt-realtime";
  const ephemeral = req.headers.get("x-oai-ephemeral") || "";
  if (!ephemeral) return NextResponse.json({ error: "missing ephemeral token" }, { status: 400 });

  const offer = await req.text();
  if (!offer || offer.length < 10) return NextResponse.json({ error: "missing SDP offer" }, { status: 400 });

  const attempts: [string, Record<string, string>][] = [
    [`https://api.openai.com/v1/realtime/calls?model=${encodeURIComponent(model)}`,
      { Authorization: `Bearer ${ephemeral}`, "Content-Type": "application/sdp" }],
    [`https://api.openai.com/v1/realtime?model=${encodeURIComponent(model)}`,
      { Authorization: `Bearer ${ephemeral}`, "Content-Type": "application/sdp", "OpenAI-Beta": "realtime=v1" }],
  ];

  let lastErr = "";
  for (const [u, headers] of attempts) {
    try {
      const r = await fetch(u, { method: "POST", body: offer, headers });
      const text = await r.text();
      if (r.ok) return new Response(text, { status: 200, headers: { "Content-Type": "application/sdp" } });
      lastErr = `HTTP ${r.status}: ${text.slice(0, 300)}`;
    } catch (e) {
      lastErr = String(e);
    }
  }
  return NextResponse.json({ error: "SDP exchange failed", detail: lastErr }, { status: 502 });
}
