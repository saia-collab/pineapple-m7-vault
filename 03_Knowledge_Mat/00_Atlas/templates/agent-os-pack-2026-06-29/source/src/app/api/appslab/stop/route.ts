import { NextResponse } from "next/server";
import { appBySlug, stopApp } from "@/lib/appslab";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function POST(req: Request) {
  const { slug } = await req.json();
  const app = appBySlug(String(slug));
  if (!app) return NextResponse.json({ error: "unknown app" }, { status: 404 });
  return NextResponse.json({ ok: stopApp(app.slug) });
}
