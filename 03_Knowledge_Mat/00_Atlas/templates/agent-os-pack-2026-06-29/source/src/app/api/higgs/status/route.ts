import { NextResponse } from "next/server";
import fs from "fs";
import path from "path";
import yaml from "js-yaml";
import { hermesHome } from "@/lib/config";
import { run } from "@/lib/runner";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// GET /api/higgs/status — is the Higgsfield MCP registered, and is its OAuth live?
// Registration is just a config entry; AUTH is a one-time browser sign-in the user
// performs (`hermes mcp login higgsfield`). We report the two separately so the UI can
// say exactly which half is missing instead of a vague "not connected".
// Profile: HIGGS_PROFILE env → the member's active Hermes profile (never a hardcoded name).
function higgsProfile(): string {
  if (process.env.HIGGS_PROFILE) return process.env.HIGGS_PROFILE;
  try { return fs.readFileSync(path.join(hermesHome(), "active_profile"), "utf8").trim() || "main"; } catch { return "main"; }
}
const PROFILE = higgsProfile();
const MCP_URL = "https://mcp.higgsfield.ai/mcp";

function registered(): boolean {
  for (const p of [
    path.join(hermesHome(), "profiles", PROFILE, "config.yaml"),
    path.join(hermesHome(), "config.yaml"),
  ]) {
    try {
      const d = yaml.load(fs.readFileSync(p, "utf8")) as { mcp_servers?: Record<string, unknown> };
      if (d?.mcp_servers?.higgsfield) return true;
    } catch { /* ignore */ }
  }
  return false;
}

export async function GET() {
  const reg = registered();
  let authed = false;
  let tools = 0;
  let detail = "";
  if (reg) {
    const r = await run("hermes", ["-p", PROFILE, "mcp", "test", "higgsfield"], { timeoutMs: 90_000 }).catch(() => null);
    const out = `${r?.stdout ?? ""}${r?.stderr ?? ""}`.replace(/\[[0-9;]*m/g, "");
    const unauthorized = /401|unauthor|not authenticated|no cached tokens|login/i.test(out);
    // `mcp test` prints one indented "tool_name   description" line per tool — count those
    const names = (out.match(/^\s{2,}[a-z][a-z0-9_]{2,}\s{2,}\S/gm) || [])
      .map((l) => l.trim().split(/\s+/)[0])
      .filter((n) => !["Testing", "Transport", "Auth"].includes(n));
    tools = new Set(names).size;
    authed = !unauthorized && tools > 0;
    detail = tools ? `${tools} tools · ${[...new Set(names)].slice(0, 6).join(", ")}` : out.split("\n").map((s) => s.trim()).filter(Boolean).slice(-2).join(" · ").slice(0, 240);
  }
  return NextResponse.json({
    registered: reg,
    authed,
    tools,
    url: MCP_URL,
    profile: PROFILE,
    detail,
    loginCommand: `hermes -p ${PROFILE} mcp login higgsfield`,
  });
}
