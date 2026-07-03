// INTENT: M7 Agentic OS — Express localhost engine.
// Serves the dashboard and exposes live API endpoints:
//   /api/metrics    live vault scan + system status
//   /api/models     AI fleet health (Ollama, Hermes, Antigravity, NotebookLM)
//   /api/telemetry  avatar telemetry (1-3-12 offensive)
//   /api/execute    run a named playbook task / script
//   /api/ollama     proxy a prompt to a local Ollama model
//   /api/trigger    legacy action map (kept)
//   /api/log        recent log lines (kept)
// Ko e hala 'o e fononga ko e faka'apa'apa.

const express = require('express');
const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');

const app = express();
const PORT = 3000;
const ROOT = path.join(__dirname, '..');
const SCRIPTS = fs.existsSync(path.join(ROOT, '04_Tech_Lab', 'Scripts'))
    ? path.join(ROOT, '04_Tech_Lab', 'Scripts')
    : path.join(ROOT, '04_Tech_Lab', 'scripts');

app.use(express.json());
app.use(express.static(path.join(ROOT, '01_Command_Center')));

app.get('/', (req, res) => {
    res.sendFile(path.join(ROOT, '01_Command_Center', 'OS_Dashboard.html'));
});

// ---------------------------------------------------------------
// helpers
// ---------------------------------------------------------------
function loadModelsConfig() {
    try {
        return JSON.parse(fs.readFileSync(
            path.join(ROOT, '04_Tech_Lab', 'config', 'models.json'), 'utf8'));
    } catch (_) {
        return { fleet: [] };
    }
}

async function probe(url, timeoutMs = 1500) {
    if (!url) return { ok: false, status: 'unconfigured' };
    const ctrl = new AbortController();
    const t = setTimeout(() => ctrl.abort(), timeoutMs);
    try {
        const r = await fetch(url, { signal: ctrl.signal });
        clearTimeout(t);
        let body = null;
        try { body = await r.json(); } catch (_) { body = null; }
        return { ok: r.ok, status: r.ok ? 'online' : `http_${r.status}`, body };
    } catch (e) {
        clearTimeout(t);
        return { ok: false, status: 'offline' };
    }
}

// ---------------------------------------------------------------
// /api/metrics  — live directory scan + system status
// ---------------------------------------------------------------
app.get('/api/metrics', (req, res) => {
    try {
        const rooms = [
            { id: '01_Command_Center', label: '01 Command Center' },
            { id: '02_Workspaces',     label: '02 Workspaces'     },
            { id: '02_Media_Vault',    label: '02 Media Vault'    },
            { id: '03_Knowledge_Mat',  label: '03 Knowledge Mat'  },
            { id: '04_Tech_Lab',       label: '04 Tech Lab'       },
            { id: '05_Campaign_Factory', label: '05 Campaign Factory' },
        ];
        function countFiles(dir) {
            let total = 0;
            try {
                for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
                    if (e.name.startsWith('.')) continue;
                    const full = path.join(dir, e.name);
                    total += e.isDirectory() ? countFiles(full) : 1;
                }
            } catch (_) {}
            return total;
        }
        function listClusters(dir) {
            const clusters = [];
            try {
                let rootFiles = 0;
                for (const e of fs.readdirSync(dir, { withFileTypes: true })) {
                    if (e.name.startsWith('.')) continue;
                    if (e.isDirectory()) clusters.push({ name: e.name, files: countFiles(path.join(dir, e.name)) });
                    else rootFiles++;
                }
                if (rootFiles > 0) clusters.unshift({ name: '(room root)', files: rootFiles });
            } catch (_) {}
            return clusters;
        }
        let outboxCount = 0;
        try { outboxCount = fs.readdirSync(path.join(ROOT, '01_Command_Center', 'Outbox_Drafts')).filter(f => !f.startsWith('.')).length; } catch (_) {}

        const roomData = rooms.map(r => {
            const clusters = listClusters(path.join(ROOT, r.id));
            return { ...r, files: clusters.reduce((s, c) => s + c.files, 0), clusters };
        });
        res.json({
            status: 'LIVE',
            generated: new Date().toISOString(),
            totalFiles: roomData.reduce((s, r) => s + r.files, 0),
            rooms: roomData,
            totalClusters: roomData.reduce((s, r) => s + r.clusters.length, 0),
            outboxCount,
            ports: { server: PORT, obsidian_http: 27124, obsidian_https: 27123 },
        });
    } catch (err) {
        res.status(500).json({ error: 'Directory scan failed', detail: err.message });
    }
});

// ---------------------------------------------------------------
// /api/models  — AI fleet health probes
// ---------------------------------------------------------------
app.get('/api/models', async (req, res) => {
    const cfg = loadModelsConfig();
    const results = await Promise.all((cfg.fleet || []).map(async m => {
        const p = await probe(m.health_url);
        let detail = m.notes || '';
        let loaded = [];
        if (m.kind === 'ollama' && p.ok && p.body && Array.isArray(p.body.models)) {
            loaded = p.body.models.map(x => x.name || x.model).filter(Boolean);
            detail = loaded.length ? `${loaded.length} model(s) loaded` : 'runtime up, no models pulled';
        }
        return {
            id: m.id, label: m.label, role: m.role, kind: m.kind,
            status: p.status, online: p.ok,
            loaded, detail, health_url: m.health_url,
            default_model: m.default_model || null,
        };
    }));
    res.json({ generated: new Date().toISOString(), fleet: results });
});

// ---------------------------------------------------------------
// /api/telemetry  — avatar telemetry feed
// ---------------------------------------------------------------
app.get('/api/telemetry', (req, res) => {
    try {
        res.json(JSON.parse(fs.readFileSync(
            path.join(ROOT, '01_Command_Center', 'avatar_telemetry.json'), 'utf8')));
    } catch (_) {
        res.json({});
    }
});

// ---------------------------------------------------------------
// /api/execute  — run a named playbook task / script
// ---------------------------------------------------------------
const TASKS = {
    firewall_scan:   { cmd: `python "${path.join(SCRIPTS, 'brand_firewall.py')}" --report`, label: 'Brand Firewall — scan + report' },
    firewall_fix:    { cmd: `python "${path.join(SCRIPTS, 'brand_firewall.py')}" --fix`,    label: 'Brand Firewall — auto-mutate banned terms' },
    score_demo:      { cmd: `python "${path.join(SCRIPTS, 'm7_scoring.py')}" --demo`,        label: 'Scoring — 1-3-12 demo run' },
    refresh_telemetry: { cmd: `python "${path.join(SCRIPTS, 'm7_scoring.py')}" --demo`,      label: 'Refresh avatar telemetry', post: 'telemetry' },
    scaffold:        { cmd: `powershell -ExecutionPolicy Bypass -File "${path.join(SCRIPTS, 'setup_m7.ps1')}"`, label: 'Scaffold / verify 4-Fala topography' },
};

app.post('/api/execute', (req, res) => {
    const { task } = req.body || {};
    const def = TASKS[task];
    if (!def) return res.status(400).json({ ok: false, output: `Unknown task: ${task}`, available: Object.keys(TASKS) });
    exec(def.cmd, { cwd: ROOT, timeout: 120000, maxBuffer: 1024 * 1024 * 8 }, (err, stdout, stderr) => {
        // refresh_telemetry: persist the parsed avatar feed for the dashboard
        if (!err && def.post === 'telemetry') {
            try {
                const data = JSON.parse(stdout);
                const map = { PAUSE: 'PAUSE (1% Kill)', SCALE: 'SCALE (+15%)', HOLD: 'HOLD' };
                const tele = {};
                for (const r of data.campaign.results) {
                    tele[r.avatar] = { ctr: r.ctr, cpl: Math.round(r.cpl), status: map[r.action] || r.action };
                }
                fs.writeFileSync(path.join(ROOT, '01_Command_Center', 'avatar_telemetry.json'),
                    JSON.stringify(tele, null, 2));
                appendHistory(tele);
            } catch (_) {}
        }
        res.json({
            ok: !err, task, label: def.label,
            output: (stdout || '').trim() || (stderr || '').trim() || (err ? err.message : 'done'),
            exit: err ? (err.code ?? 1) : 0,
        });
    });
});

// ---------------------------------------------------------------
// /api/ollama  — proxy a prompt to a local Ollama model
// ---------------------------------------------------------------
app.post('/api/ollama', async (req, res) => {
    const cfg = loadModelsConfig();
    const ol = (cfg.fleet || []).find(m => m.id === 'ollama') || {};
    const url = ol.generate_url || 'http://localhost:11434/api/generate';
    const model = (req.body && req.body.model) || ol.default_model || 'gemma4-pineapple';
    const prompt = (req.body && req.body.prompt) || '';
    if (!prompt) return res.status(400).json({ ok: false, error: 'Missing prompt' });
    try {
        const r = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ model, prompt, stream: false }),
        });
        const body = await r.json();
        res.json({ ok: true, model, response: body.response || '' });
    } catch (e) {
        res.status(502).json({ ok: false, error: 'Ollama unreachable', detail: e.message,
            hint: 'Start Ollama (ollama serve) and pull the model.' });
    }
});

// ---------------------------------------------------------------
// legacy endpoints (kept)
// ---------------------------------------------------------------
app.post('/api/trigger', (req, res) => {
    const { action } = req.body || {};
    if (!action) return res.status(400).json({ error: 'Missing action' });
    const actionMap = {
        graphify_sync:     `python "${path.join(SCRIPTS, 'ingest_router.py')}"`,
        storm_ingest:      `python "${path.join(SCRIPTS, 'm7_fetch.py')}"`,
        generate_matrix:   `python "${path.join(SCRIPTS, 'm7_scoring.py')}" --demo`,
        verify_compliance: `python "${path.join(SCRIPTS, 'brand_firewall.py')}" --report`,
    };
    const cmd = actionMap[action];
    if (!cmd) return res.json({ success: false, output: `Unknown action: ${action}` });
    exec(cmd, { cwd: ROOT, timeout: 120000 }, (err, stdout, stderr) => {
        if (err) return res.json({ success: false, output: stderr || err.message });
        res.json({ success: true, output: stdout.trim() || `${action} completed.` });
    });
});

app.get('/api/log', (req, res) => {
    const logPath = path.join(ROOT, 'knowledge-base', 'wiki', 'log.md');
    try {
        const lines = fs.readFileSync(logPath, 'utf8').split('\n').filter(Boolean).slice(-50);
        res.json({ lines });
    } catch (_) { res.json({ lines: [] }); }
});

// ---------------------------------------------------------------
// telemetry history  — rolling snapshots for trend sparklines
// ---------------------------------------------------------------
const HISTORY_PATH = path.join(ROOT, '04_Tech_Lab', 'logs', 'telemetry_history.json');
const HISTORY_CAP = 60;

function appendHistory(tele) {
    let hist = [];
    try { hist = JSON.parse(fs.readFileSync(HISTORY_PATH, 'utf8')); } catch (_) {}
    if (!Array.isArray(hist)) hist = [];
    hist.push({ ts: new Date().toISOString(), avatars: tele });
    if (hist.length > HISTORY_CAP) hist = hist.slice(-HISTORY_CAP);
    try {
        fs.mkdirSync(path.dirname(HISTORY_PATH), { recursive: true });
        fs.writeFileSync(HISTORY_PATH, JSON.stringify(hist, null, 2));
    } catch (_) {}
    return hist;
}

app.get('/api/history', (req, res) => {
    try { res.json(JSON.parse(fs.readFileSync(HISTORY_PATH, 'utf8'))); }
    catch (_) { res.json([]); }
});

// ---------------------------------------------------------------
// /api/hermes  — dispatch an autonomous goal loop to the Hermes daemon
// ---------------------------------------------------------------
app.post('/api/hermes', async (req, res) => {
    const cfg = loadModelsConfig();
    const h = (cfg.fleet || []).find(m => m.id === 'hermes') || {};
    const url = h.command_url || 'http://localhost:8080/goal';
    const goal = (req.body && req.body.goal) || '';
    if (!goal) return res.status(400).json({ ok: false, error: 'Missing goal' });
    // Outbox Shield: agents may draft/loop but live publishing stays manual.
    const payload = { goal, mode: 'autonomous', outbox_shield: 'PAUSED', source: 'OS_Dashboard' };
    try {
        const r = await fetch(url, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(payload),
        });
        let body = null; try { body = await r.json(); } catch (_) { body = await r.text(); }
        res.json({ ok: r.ok, dispatched: r.ok, goal, response: body });
    } catch (e) {
        res.status(502).json({ ok: false, error: 'Hermes daemon unreachable', detail: e.message,
            hint: 'Start Hermes and set fleet.hermes.command_url in config/models.json.' });
    }
});

app.listen(PORT, () => {
    console.log('\x1b[33m%s\x1b[0m', '='.repeat(52));
    console.log('   M7 AGENTIC OS  —  LOCALHOST ENGINE ACTIVE');
    console.log(`   http://localhost:${PORT}`);
    console.log('   fleet: Ollama · Hermes · Antigravity · NotebookLM');
    console.log('\x1b[33m%s\x1b[0m', '='.repeat(52));
});
