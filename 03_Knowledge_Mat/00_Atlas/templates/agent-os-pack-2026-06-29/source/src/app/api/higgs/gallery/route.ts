import { NextResponse } from "next/server";
import { promises as fs, createReadStream } from "fs";
import os from "os";
import path from "path";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// GET /api/higgs/gallery            → everything Higgsfield has made, newest first
// GET /api/higgs/gallery?file=x.png → the asset itself (images + video stream)
const GALLERY = path.join(os.homedir(), ".agentic-os", "higgsfield", "gallery");
const TYPES: Record<string, string> = {
  ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp",
  ".gif": "image/gif", ".mp4": "video/mp4", ".webm": "video/webm", ".mov": "video/quicktime",
};

export async function GET(req: Request) {
  const file = new URL(req.url).searchParams.get("file");
  if (file) {
    const safe = path.basename(file); // never escape the gallery dir
    const fp = path.join(GALLERY, safe);
    try {
      const st = await fs.stat(fp);
      const type = TYPES[path.extname(safe).toLowerCase()] || "application/octet-stream";
      const stream = createReadStream(fp) as unknown as ReadableStream;
      return new Response(stream, {
        headers: { "Content-Type": type, "Content-Length": String(st.size), "Cache-Control": "public, max-age=300" },
      });
    } catch {
      return NextResponse.json({ error: "not found" }, { status: 404 });
    }
  }

  await fs.mkdir(GALLERY, { recursive: true });
  const names = (await fs.readdir(GALLERY).catch(() => [])).filter((f) => !f.startsWith("."));
  const items = await Promise.all(names.map(async (f) => {
    const st = await fs.stat(path.join(GALLERY, f));
    const ext = path.extname(f).toLowerCase();
    return {
      file: f,
      kind: [".mp4", ".webm", ".mov"].includes(ext) ? "video" : "image",
      bytes: st.size,
      at: st.mtimeMs,
      title: f.replace(/\.[^.]+$/, "").replace(/[-_]+/g, " "),
    };
  }));
  items.sort((a, b) => b.at - a.at);
  return NextResponse.json({ root: GALLERY, count: items.length, items });
}
