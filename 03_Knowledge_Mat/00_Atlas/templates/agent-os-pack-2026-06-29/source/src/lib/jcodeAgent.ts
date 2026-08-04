// jcode integration — github.com/1jehuang/jcode ("the most RAM-efficient harness").
//
// A Rust coding agent (~28MB PSS, 14ms to first frame) with a semantic memory
// graph, swarm mode, and multi-provider OAuth. It rides the user's existing
// Claude subscription: jcode auto-discovers ~/.claude/.credentials.json (one-time
// consent recorded in ~/.jcode/auth.json) and runs claude-opus-5.
// E2E receipt 2026-08-02: `jcode run -p claude` → "JCODE OK via claude".
//
// Sessions live in ~/.jcode/sessions/session_<animal>_<ts>_<id>.json
// ({id,title,messages[{role,content,timestamp}],provider_key,model,working_dir,
//   short_name,status,last_active_at}) — surfaced in the History tab.

import { readdir, readFile, stat } from "node:fs/promises";
import { existsSync } from "node:fs";
import os from "node:os";
import path from "node:path";

export const JCODE_BIN = path.join(os.homedir(), ".local/bin/jcode");
export const JCODE_BUILDS = path.join(os.homedir(), ".agentic-os", "jcode", "builds");
export const JCODE_SESSIONS = path.join(os.homedir(), ".jcode", "sessions");

export const JCODE_PATH = [
  path.join(os.homedir(), ".local/bin"),
  "/opt/homebrew/bin", "/usr/local/bin",
  process.env.PATH || "",
].filter(Boolean).join(":");

export function jcodeInstalled(): boolean { return existsSync(JCODE_BIN); }

// ── conversation history (the History workspace) ─────────────────────────
export interface JcodeSessionMeta {
  id: string; shortName: string; title: string | null; model: string | null;
  workingDir: string | null; status: string | null; messages: number;
  createdAt: string | null; lastActiveAt: string | null;
}
export interface JcodeMessage { role: string; text: string; timestamp?: string }

function msgText(content: unknown): string {
  if (typeof content === "string") return content;
  if (Array.isArray(content)) {
    return content.map((b) => {
      if (typeof b === "string") return b;
      const o = b as Record<string, unknown>;
      if (typeof o.text === "string") return o.text;
      if (o.type === "tool_use" || o.name) return `[tool: ${String(o.name ?? "?")}]`;
      return "";
    }).filter(Boolean).join("\n");
  }
  if (content && typeof content === "object") {
    const o = content as Record<string, unknown>;
    if (typeof o.text === "string") return o.text;
  }
  return "";
}

export async function listJcodeSessions(limit = 60): Promise<JcodeSessionMeta[]> {
  if (!existsSync(JCODE_SESSIONS)) return [];
  let names: string[] = [];
  try { names = (await readdir(JCODE_SESSIONS)).filter((n) => n.startsWith("session_") && n.endsWith(".json") && !n.endsWith(".journal.jsonl")); }
  catch { return []; }
  const out: JcodeSessionMeta[] = [];
  for (const n of names) {
    try {
      const full = path.join(JCODE_SESSIONS, n);
      const st = await stat(full);
      if (st.size > 25_000_000) continue; // skip pathological files
      const j = JSON.parse(await readFile(full, "utf8")) as Record<string, unknown>;
      const msgs = Array.isArray(j.messages) ? j.messages : [];
      out.push({
        id: String(j.id ?? n.replace(/\.json$/, "")),
        shortName: String(j.short_name ?? "?"),
        title: (j.title as string | null) ?? null,
        model: (j.model as string | null) ?? null,
        workingDir: (j.working_dir as string | null) ?? null,
        status: (j.status as string | null) ?? null,
        messages: msgs.length,
        createdAt: (j.created_at as string | null) ?? null,
        lastActiveAt: (j.last_active_at as string | null) ?? null,
      });
    } catch { /* skip unreadable session */ }
  }
  out.sort((a, b) => String(b.lastActiveAt ?? "").localeCompare(String(a.lastActiveAt ?? "")));
  return out.slice(0, limit);
}

export async function readJcodeTranscript(id: string): Promise<{ meta: JcodeSessionMeta; messages: JcodeMessage[] } | null> {
  if (!/^[A-Za-z0-9_.-]+$/.test(id)) return null;
  const full = path.join(JCODE_SESSIONS, `${id}.json`);
  if (!full.startsWith(JCODE_SESSIONS + path.sep) || !existsSync(full)) return null;
  try {
    const j = JSON.parse(await readFile(full, "utf8")) as Record<string, unknown>;
    const raw = Array.isArray(j.messages) ? j.messages : [];
    const messages: JcodeMessage[] = raw.map((m) => {
      const o = m as Record<string, unknown>;
      return { role: String(o.display_role ?? o.role ?? "?"), text: msgText(o.content).slice(0, 20_000), timestamp: o.timestamp as string | undefined };
    }).filter((m) => m.text.trim());
    const meta: JcodeSessionMeta = {
      id: String(j.id ?? id), shortName: String(j.short_name ?? "?"),
      title: (j.title as string | null) ?? null, model: (j.model as string | null) ?? null,
      workingDir: (j.working_dir as string | null) ?? null, status: (j.status as string | null) ?? null,
      messages: messages.length, createdAt: (j.created_at as string | null) ?? null,
      lastActiveAt: (j.last_active_at as string | null) ?? null,
    };
    return { meta, messages };
  } catch { return null; }
}

// ── builds workspace (visual-first, per the workspace-visual-showcase rule) ──
const SHOWCASE = new Set([".html", ".htm", ".png", ".jpg", ".jpeg", ".webp", ".gif", ".svg", ".mp4", ".webm", ".mp3", ".wav", ".pdf"]);
export interface JcodeBuild { project: string; mtime: number; fileCount: number; html: string[]; files: { rel: string; bytes: number }[] }

export async function listJcodeBuilds(): Promise<JcodeBuild[]> {
  if (!existsSync(JCODE_BUILDS)) return [];
  const out: JcodeBuild[] = [];
  let dirs: string[] = [];
  try { dirs = await readdir(JCODE_BUILDS); } catch { return []; }
  for (const d of dirs) {
    if (d.startsWith(".")) continue;
    const root = path.join(JCODE_BUILDS, d);
    try {
      const st = await stat(root);
      if (!st.isDirectory()) continue;
      const files: { rel: string; bytes: number }[] = [];
      const html: string[] = [];
      async function walk(dir: string, depth: number) {
        if (depth > 4 || files.length > 80) return;
        for (const n of await readdir(dir)) {
          if (n.startsWith(".") || n === "node_modules") continue;
          const full = path.join(dir, n);
          const s = await stat(full);
          if (s.isDirectory()) { await walk(full, depth + 1); continue; }
          if (!SHOWCASE.has(path.extname(n).toLowerCase())) continue;
          const rel = path.relative(root, full);
          files.push({ rel, bytes: s.size });
          if (/\.html?$/i.test(n)) html.push(rel);
        }
      }
      await walk(root, 0);
      html.sort((a, b) => (/(^|\/)index\.html$/i.test(a) ? -1 : 0) - (/(^|\/)index\.html$/i.test(b) ? -1 : 0));
      out.push({ project: d, mtime: st.mtimeMs, fileCount: files.length, html, files });
    } catch { /* skip */ }
  }
  out.sort((a, b) => b.mtime - a.mtime);
  return out;
}
