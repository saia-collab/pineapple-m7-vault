// M7 fix: Hermes Astros calls /api/astros/* but the pack only shipped /api/radar/*.
// This aliases the working radar logic so Astros stops 404-ing (the "not valid JSON" bug).
export const runtime = "nodejs";
export const dynamic = "force-dynamic";
export { GET, POST } from "../../radar/scan/route";
