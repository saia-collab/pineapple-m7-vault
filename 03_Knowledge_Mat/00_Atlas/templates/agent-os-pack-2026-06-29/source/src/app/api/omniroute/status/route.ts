import { NextResponse } from "next/server";

export const runtime = "nodejs";
export const dynamic = "force-dynamic";

// GET /api/omniroute/status?backend=omniroute|ninerouter — is the selected
// Free-AI-Coder backend running locally? Both serve a dashboard on their port
// and an OpenAI-compatible API at /v1.

const BASES: Record<string, string> = {
  omniroute: "http://localhost:20128",
  ninerouter: "http://127.0.0.1:20129",
};

async function ping(BASE: string, path: string, ms = 1500): Promise<number | null> {
  const ctrl = new AbortController();
  const t = setTimeout(() => ctrl.abort(), ms);
  try {
    const r = await fetch(BASE + path, { signal: ctrl.signal, cache: "no-store" });
    return r.status;
  } catch {
    return null;
  } finally {
    clearTimeout(t);
  }
}

export async function GET(req: Request) {
  const backend = new URL(req.url).searchParams.get("backend") === "ninerouter" ? "ninerouter" : "omniroute";
  const BASE = BASES[backend];
  // Try the API first, then the dashboard.
  const api = await ping(BASE, "/v1/models");
  const dash = api == null ? await ping(BASE, "/") : 200;
  const running = api != null || dash != null;

  let models: number | null = null;
  if (api === 200) {
    try {
      const r = await fetch(BASE + "/v1/models", { cache: "no-store" });
      const j = await r.json().catch(() => null);
      const arr = j?.data ?? j?.models ?? [];
      if (Array.isArray(arr)) models = arr.length;
    } catch {
      /* ignore */
    }
  }

  return NextResponse.json({
    backend,
    running,
    base: BASE,
    api: `${BASE}/v1`,
    dashboard: BASE,
    apiStatus: api,
    models,
  });
}
