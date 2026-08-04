import { listJcodeBuilds, jcodeInstalled } from "@/lib/jcodeAgent";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

export async function GET() {
  return Response.json(
    { installed: jcodeInstalled(), builds: await listJcodeBuilds() },
    { headers: { "cache-control": "no-store" } },
  );
}
