import { spawn } from "node:child_process";
import { mkdir } from "node:fs/promises";
import path from "node:path";
import { JCODE_BIN, JCODE_BUILDS, JCODE_PATH, jcodeInstalled } from "@/lib/jcodeAgent";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// jcode build stream. `jcode run --ndjson` emits one JSON event per line:
//   {type:"start", model, provider, session_id}
//   {type:"text_delta", text}            — streamed answer text
//   {type:"tool_*" | "tool", ...}        — tool activity (shape varies; passed through)
//   {type:"tokens", input, output, ...}
//   {type:"done", text, session_id}
// We translate those into the same line protocol the other Code tabs speak
// (start/system/text/tool/tool_result/result/done) so the terminal UI is shared.

const STEER =
  "You are a build agent. Build exactly what the user asks as real files in the current working directory. " +
  "If it's a web build, write a complete, working, self-contained index.html (inline CSS/JS, no external assets). " +
  "Create the files now with your tools, then stop. Keep chatter short.";

function slugify(s: string): string {
  return (s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 40) || "build");
}

export async function POST(req: Request) {
  if (!jcodeInstalled()) return new Response(JSON.stringify({ error: "jcode not installed" }), { status: 500 });
  const { prompt, project } = await req.json();
  if (typeof prompt !== "string" || !prompt.trim()) {
    return new Response(JSON.stringify({ error: "missing prompt" }), { status: 400 });
  }
  const name = (typeof project === "string" && /^[a-z0-9-]{1,48}$/.test(project))
    ? project : `${slugify(prompt)}-${Date.now().toString(36).slice(-5)}`;
  const cwd = path.join(JCODE_BUILDS, name);
  await mkdir(cwd, { recursive: true });

  const encoder = new TextEncoder();
  const stream = new ReadableStream({
    start(controller) {
      const emit = (obj: Record<string, unknown>) => {
        try { controller.enqueue(encoder.encode(JSON.stringify(obj) + "\n")); } catch { /* closed */ }
      };
      emit({ type: "start", project: name, cwd });
      const startedAt = Date.now();
      let sessionId: string | undefined;
      let textBuf = "";
      const flushText = () => { if (textBuf.trim()) emit({ type: "text", text: textBuf }); textBuf = ""; };

      const child = spawn(JCODE_BIN, ["run", "-p", "claude", "--ndjson", "--quiet", "--no-update", `${STEER}\n\n${prompt.trim()}`], {
        cwd,
        env: { ...process.env, PATH: JCODE_PATH, NO_COLOR: "1", JCODE_NO_EMOJI: "1" },
      });
      try { child.stdin?.end(); } catch {}

      const killer = setTimeout(() => { try { child.kill("SIGKILL"); } catch {} }, 12 * 60_000);

      const handleLine = (line: string) => {
        if (!line.trim()) return;
        let e: Record<string, unknown>;
        try { e = JSON.parse(line); } catch { return; }
        const t = String(e.type ?? "");
        if (t === "start") {
          sessionId = e.session_id as string | undefined;
          emit({ type: "system", model: e.model, session: e.session_id });
        } else if (t === "text_delta") {
          textBuf += String(e.text ?? "");
          if (textBuf.length > 400) flushText();
        } else if (t === "message_end") {
          flushText();
        } else if (t.startsWith("tool")) {
          // tool events vary by build; surface name + a short input summary
          flushText();
          const name = String(e.name ?? e.tool ?? t);
          const input = (e.input ?? e.args ?? {}) as Record<string, unknown>;
          if (t.includes("result") || e.output !== undefined) {
            emit({ type: "tool_result", text: String(e.output ?? e.text ?? "").slice(0, 400) });
          } else {
            emit({ type: "tool", name, input });
          }
        } else if (t === "tokens") {
          emit({ type: "info", text: `tokens · in ${e.input ?? 0} · out ${e.output ?? 0} · cache ${e.cache_read_input ?? 0}` });
        } else if (t === "error") {
          emit({ type: "error", text: String(e.message ?? e.text ?? "error").slice(0, 240) });
        }
        // connection_* phases are noise — skipped
      };

      let buf = "";
      child.stdout!.on("data", (d: Buffer) => {
        buf += d.toString();
        let nl: number;
        while ((nl = buf.indexOf("\n")) >= 0) { handleLine(buf.slice(0, nl)); buf = buf.slice(nl + 1); }
      });
      child.stderr!.on("data", (d: Buffer) => {
        const s = d.toString().trim();
        if (!s || /^\[Tokens\]/.test(s)) return;
        emit({ type: "stderr", text: s.slice(0, 300) });
      });
      child.on("error", (err) => emit({ type: "error", text: String(err).slice(0, 200) }));
      child.on("close", (code) => {
        clearTimeout(killer);
        if (buf.trim()) handleLine(buf);
        flushText();
        emit({ type: "result", subtype: code === 0 ? "success" : "error", ms: Date.now() - startedAt });
        emit({ type: "done", code: code ?? 0, project: name, session: sessionId });
        try { controller.close(); } catch {}
      });
      req.signal.addEventListener("abort", () => { try { child.kill("SIGKILL"); } catch {} });
    },
  });

  return new Response(stream, {
    headers: {
      "Content-Type": "application/x-ndjson; charset=utf-8",
      "Cache-Control": "no-cache, no-transform",
      "X-Accel-Buffering": "no",
    },
  });
}
