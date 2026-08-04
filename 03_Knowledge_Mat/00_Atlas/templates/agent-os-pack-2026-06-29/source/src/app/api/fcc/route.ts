import { NextResponse } from "next/server";
import { getState, setEnabled, setRouter } from "@/lib/fcc";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  const state = await getState();
  return NextResponse.json(state);
}

// Toggle routing on/off — { enabled: true | false }
// Switch the free router  — { router: "omniroute" | "9router" }
export async function POST(req: Request) {
  const body = await req.json().catch(() => ({}));
  let touched = false;
  if (typeof body.enabled === "boolean") { await setEnabled(body.enabled); touched = true; }
  if (body.router === "omniroute" || body.router === "9router") { await setRouter(body.router); touched = true; }
  if (!touched) {
    return NextResponse.json({ error: 'enabled (boolean) or router ("omniroute"|"9router") required' }, { status: 400 });
  }
  return NextResponse.json(await getState());
}
