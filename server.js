/* ============================================================
 * Pineapple Contractors M7 — Agent OS local server (server.js)
 * Zero-dependency: uses only Node built-ins. No npm install needed.
 * Run:  node server.js     then open  http://localhost:3939
 * Port note: 3939, not 3737 — the Agentic OS pack claims 3737 for itself
 * (its start script hardcodes PORT=3737), so the two collided.
 * Serves the Command Center dashboard + vault APIs (Kanban, Memory,
 * Outbox, Firewall). Everything stays PAUSED — never publishes or spends.
 * ============================================================ */
const http = require("http");
const fs = require("fs");
const path = require("path");
const { spawnSync } = require("child_process");

const PORT = process.env.PORT || 3939;
const VAULT = __dirname;                                   // server.js lives at vault root
const CMD = path.join(VAULT, "01_Command_Center");
const OUTBOX = path.join(CMD, "Outbox_Drafts");
const KANBAN = path.join(CMD, "M7_Agent_Kanban.md");
const DASHBOARD = path.join(CMD, "M7_COMMAND_CENTER.html");
const SHARED_MEM = path.join(VAULT, "03_Knowledge_Mat", "SHARED_MEMORY.md");
const RESEARCH = path.join(VAULT, "05_Campaign_Factory", "10_Research_Stage");
function firewallPath() {
  for (const p of [path.join(VAULT,"04_Tech_Lab","scripts","brand_firewall.py"),
                   path.join(VAULT,"04_Tech_Lab","Scripts","brand_firewall.py")])
    if (fs.existsSync(p)) return p;
  return null;
}
try { fs.mkdirSync(OUTBOX, { recursive: true }); fs.mkdirSync(RESEARCH, { recursive: true }); } catch (e) {}

/* ---------- helpers ---------- */
function send(res, code, body, type) {
  res.writeHead(code, {
    "Content-Type": type || "application/json",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
  });
  res.end(typeof body === "string" || Buffer.isBuffer(body) ? body : JSON.stringify(body));
}
function readBody(req) {
  return new Promise((resolve) => {
    let d = ""; req.on("data", (c) => (d += c)); req.on("end", () => { try { resolve(JSON.parse(d || "{}")); } catch { resolve({}); } });
  });
}
function safeInVault(p) { const r = path.resolve(p); return r === VAULT || r.startsWith(VAULT + path.sep); }

function parseKanban() {
  if (!fs.existsSync(KANBAN)) return { columns: [] };
  const cols = []; let cur = null;
  for (const line of fs.readFileSync(KANBAN, "utf8").split("\n")) {
    if (line.startsWith("## ")) { cur = { name: line.slice(3).trim(), cards: [] }; cols.push(cur); }
    else if (cur && line.trim().startsWith("- [")) {
      const txt = line.trim().replace(/^- \[.?\]\s*/, "");
      const tag = (txt.match(/#(\w+)/) || [])[1] || "";
      cur.cards.push({ text: txt, agent: tag });
    }
  }
  return { columns: cols };
}
function firewallCheck(text) {
  const fw = firewallPath();
  if (!fw) return { pass: null, output: "brand_firewall.py not found" };
  const py = process.platform === "win32" ? "python" : "python3";
  const r = spawnSync(py, [fw, "--check", text], { encoding: "utf8", timeout: 30000 });
  const out = ((r.stdout || "") + (r.stderr || "")).trim();
  const pass = out.includes("STATUS: OK") && !out.includes("mutated") && !out.includes("FAIL");
  return { pass, output: out.slice(0, 1200) };
}
function writeOutbox(filename, text) {
  let safe = String(filename || "draft.md").replace(/[^A-Za-z0-9_.\-]/g, "_");
  if (!safe.endsWith(".md")) safe += ".md";
  const p = path.join(OUTBOX, safe);
  const header = "---\nstatus: PAUSED\ndelivery_state: PAUSED\nhuman_authorization_required: true\n---\n\n> PAUSED — Saia is the only publisher. Review before sending/posting.\n\n";
  fs.writeFileSync(p, header + (text || ""), "utf8");
  return { ok: true, path: p };
}

/* ---------- server ---------- */
const server = http.createServer(async (req, res) => {
  try {
    const u = new URL(req.url, "http://localhost");
    if (req.method === "OPTIONS") return send(res, 204, "");
    // dashboard
    if (req.method === "GET" && (u.pathname === "/" || u.pathname === "/index.html" || u.pathname === "/M7_COMMAND_CENTER.html")) {
      if (fs.existsSync(DASHBOARD)) return send(res, 200, fs.readFileSync(DASHBOARD), "text/html; charset=utf-8");
      return send(res, 404, { error: "dashboard not found" });
    }
    if (req.method === "GET" && u.pathname === "/api/health") return send(res, 200, { ok: true, vault: VAULT, port: PORT });
    if (req.method === "GET" && u.pathname === "/api/kanban") return send(res, 200, parseKanban());
    if (req.method === "GET" && u.pathname === "/api/memory") {
      const md = fs.existsSync(SHARED_MEM) ? fs.readFileSync(SHARED_MEM, "utf8") : "";
      return send(res, 200, { ok: true, markdown: md, size: md.length });
    }
    if (req.method === "GET" && u.pathname === "/api/filecontent") {
      const rel = u.searchParams.get("path") || ""; const p = path.join(VAULT, rel);
      if (safeInVault(p) && fs.existsSync(p) && fs.statSync(p).isFile())
        return send(res, 200, { ok: true, content: fs.readFileSync(p, "utf8") });
      return send(res, 200, { ok: false, content: null, error: "not found" });
    }
    if (req.method === "GET" && u.pathname === "/api/outbox") {
      const items = fs.existsSync(OUTBOX) ? fs.readdirSync(OUTBOX).filter((f) => f.endsWith(".md")) : [];
      return send(res, 200, { ok: true, items });
    }
    if (req.method === "POST") {
      const body = await readBody(req);
      if (u.pathname === "/api/firewall") return send(res, 200, firewallCheck(body.text || ""));
      if (u.pathname === "/api/approve") return send(res, 200, writeOutbox(body.filename, body.text));
      if (u.pathname === "/api/memory/log") {
        try { fs.appendFileSync(SHARED_MEM, `\n- ${new Date().toISOString().slice(0,16).replace("T"," ")} · **${body.agent||"Saia"}**: ${body.note||""}`); return send(res, 200, { ok: true }); }
        catch (e) { return send(res, 200, { ok: false, error: String(e) }); }
      }
    }
    return send(res, 404, { error: "unknown endpoint" });
  } catch (e) { return send(res, 500, { error: String(e) }); }
});

server.listen(PORT, "127.0.0.1", () => {
  console.log("=".repeat(54));
  console.log(" PINEAPPLE M7 — Agent OS server");
  console.log(" Vault : " + VAULT);
  console.log(" Open  : http://localhost:" + PORT);
  console.log(" Outbox Shield ON — nothing publishes or spends.");
  console.log(" Ctrl+C to stop.");
  console.log("=".repeat(54));
});
