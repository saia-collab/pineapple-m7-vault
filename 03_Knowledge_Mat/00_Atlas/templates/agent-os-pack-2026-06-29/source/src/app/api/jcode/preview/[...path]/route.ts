import { readFile } from "node:fs/promises";
import path from "node:path";
import { JCODE_BUILDS } from "@/lib/jcodeAgent";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

const TYPES: Record<string, string> = {
  ".html": "text/html; charset=utf-8", ".htm": "text/html; charset=utf-8",
  ".css": "text/css; charset=utf-8", ".js": "text/javascript; charset=utf-8",
  ".json": "application/json; charset=utf-8", ".svg": "image/svg+xml",
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif",
  ".webp": "image/webp", ".mp4": "video/mp4", ".webm": "video/webm",
  ".mp3": "audio/mpeg", ".wav": "audio/wav", ".pdf": "application/pdf",
  ".txt": "text/plain; charset=utf-8",
};

export async function GET(_req: Request, { params }: { params: Promise<{ path: string[] }> }) {
  const { path: parts } = await params;
  const rel = (parts || []).map(decodeURIComponent).join("/");
  const full = path.resolve(JCODE_BUILDS, rel);
  if (!full.startsWith(JCODE_BUILDS + path.sep)) return new Response("forbidden", { status: 403 });
  try {
    const buf = await readFile(full);
    const ext = path.extname(full).toLowerCase();
    return new Response(new Uint8Array(buf), {
      headers: { "Content-Type": TYPES[ext] || "application/octet-stream", "Cache-Control": "no-store" },
    });
  } catch {
    return new Response("not found", { status: 404 });
  }
}
