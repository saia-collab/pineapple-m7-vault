import { NextResponse } from "next/server";
import fs from "fs";
import os from "os";
import path from "path";
import { hermesHome } from "@/lib/config";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// GET /api/dscoder/status — DeepSeek is cloud (official API), so "running" means
// we have a DeepSeek key on disk.

function haveKey(): boolean {
  if (process.env.DEEPSEEK_API_KEY) return true;
  for (const file of [path.join(os.homedir(), ".fcc", ".env"), path.join(hermesHome(), ".env")]) {
    try {
      const m = fs.readFileSync(file, "utf8").match(/^DEEPSEEK_API_KEY=(.+)$/m);
      if (m && m[1].trim().length > 10) return true;
    } catch { /* ignore */ }
  }
  return false;
}

export async function GET() {
  return NextResponse.json({
    running: haveKey(),
    model: "deepseek-v4-flash",
    label: "DeepSeek V4 Flash 0731",
    provider: "DeepSeek (official API)",
    models: [
      { id: "deepseek-v4-flash", label: "V4 Flash 0731", sub: "agent-tuned · 1M ctx" },
      { id: "deepseek-v4-pro", label: "V4 Pro", sub: "strong tier · 1M ctx" },
    ],
  });
}
