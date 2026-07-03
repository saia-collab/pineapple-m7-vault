/**
 * delete-facebook-posts.js
 *
 * Deletes Facebook posts identified in facebook-post-ids-to-delete.json
 * using the Meta Graph API. Posts list is printed for manual review BEFORE
 * any deletions occur. Requires META_ACCESS_TOKEN in .env.
 *
 * ⚠ REVIEW the post list printed on startup before confirming.
 *
 * Run: node 01_Command_Center/delete-facebook-posts.js
 * Add --confirm flag to actually delete: node ... --confirm
 */

const fs    = require('fs');
const path  = require('path');
const https = require('https');

const POSTS_FILE   = path.join(__dirname, 'facebook-post-ids-to-delete.json');
const REPORT_FILE  = path.join(__dirname, 'fb-delete-report.json');
const DRY_RUN      = !process.argv.includes('--confirm');

// Load access token from .env
function loadEnv() {
  const envPath = path.join(__dirname, '.env');
  if (!fs.existsSync(envPath)) return;
  for (const raw of fs.readFileSync(envPath, 'utf8').split('\n')) {
    const line = raw.replace(/\r$/, '').trim();
    if (!line || line.startsWith('#')) continue;
    const eq = line.indexOf('=');
    if (eq < 0) continue;
    const key = line.slice(0, eq).trim();
    const val = line.slice(eq + 1).trim();
    if (key && val) process.env[key] = val;
  }
}
loadEnv();

const ACCESS_TOKEN = process.env.META_ACCESS_TOKEN;
const PAGE_ID      = process.env.META_PAGE_ID;
if (!ACCESS_TOKEN) {
  console.error('Missing META_ACCESS_TOKEN in .env');
  process.exit(1);
}
if (!PAGE_ID) {
  console.error('Missing META_PAGE_ID in .env');
  process.exit(1);
}

function fbDelete(objectId) {
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: 'graph.facebook.com',
      path: `/v19.0/${objectId}?access_token=${encodeURIComponent(PAGE_ACCESS_TOKEN)}`,
      method: 'DELETE',
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        let body;
        try { body = JSON.parse(d); } catch { body = d; }
        resolve({ status: res.statusCode, body });
      });
    });
    req.on('error', reject);
    req.setTimeout(15000, () => { req.destroy(); reject(new Error('timeout')); });
    req.end();
  });
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

let PAGE_ACCESS_TOKEN = '';

function fetchPageAccessToken() {
  return new Promise((resolve, reject) => {
    const req = https.request({
      hostname: 'graph.facebook.com',
      path: `/v19.0/${PAGE_ID}?fields=access_token&access_token=${encodeURIComponent(ACCESS_TOKEN)}`,
      method: 'GET',
    }, res => {
      let d = '';
      res.on('data', c => d += c);
      res.on('end', () => {
        try {
          const body = JSON.parse(d);
          if (body?.access_token) {
            resolve(body.access_token);
            return;
          }
          const msg = body?.error?.message || 'Unable to fetch page access token';
          reject(new Error(msg));
        } catch {
          reject(new Error('Unable to parse page token response'));
        }
      });
    });
    req.on('error', reject);
    req.setTimeout(15000, () => { req.destroy(); reject(new Error('timeout')); });
    req.end();
  });
}

(async () => {
  if (!fs.existsSync(POSTS_FILE)) {
    console.error(`Missing: ${POSTS_FILE}`);
    process.exit(1);
  }

  const posts = JSON.parse(fs.readFileSync(POSTS_FILE, 'utf8'));
  if (!Array.isArray(posts) || posts.length === 0) {
    console.log('No posts to delete.');
    process.exit(0);
  }

  console.log('='.repeat(68));
  console.log('  FACEBOOK POST DELETION — DEC-005 Clean Slate');
  console.log('='.repeat(68));
  console.log(`  Target count : ${posts.length} posts`);
  console.log(`  Mode         : ${DRY_RUN ? 'DRY-RUN (no changes) — add --confirm to delete' : '⚠ LIVE DELETE'}`);
  console.log('');
  console.log('  Posts targeted:');
  posts.forEach((p, i) => {
    const objectId = p.objectId || `${PAGE_ID}_${p.fbPostId}`;
    console.log(`  ${String(i + 1).padStart(3, '0')}. obj:${objectId} | ${(p.text || '').slice(0, 60)}`);
  });
  console.log('');

  if (DRY_RUN) {
    console.log('  DRY-RUN complete. Re-run with --confirm to execute deletions.');
    console.log('='.repeat(68));
    process.exit(0);
  }

  try {
    PAGE_ACCESS_TOKEN = await fetchPageAccessToken();
  } catch (err) {
    console.error(`Failed to acquire page token: ${err.message}`);
    process.exit(1);
  }

  console.log('  Starting deletions...');
  console.log('-'.repeat(68));

  const results = [];
  let deleted = 0, failed = 0;

  for (let i = 0; i < posts.length; i++) {
    const { fbPostId, blotatoId } = posts[i];
    const objectId = posts[i].objectId || `${PAGE_ID}_${fbPostId}`;
    try {
      const { status, body } = await fbDelete(objectId);
      if (body?.success === true || status === 200) {
        deleted++;
        results.push({ objectId, fbPostId, blotatoId, status: 'deleted' });
        console.log(`  OK  [${String(i + 1).padStart(3)}/${posts.length}] obj:${objectId}`);
      } else {
        failed++;
        const msg = body?.error?.message || JSON.stringify(body);
        results.push({ objectId, fbPostId, blotatoId, status: 'error', error: msg });
        console.log(`  ERR [${String(i + 1).padStart(3)}/${posts.length}] obj:${objectId} -> ${msg}`);
      }
    } catch (err) {
      failed++;
      results.push({ objectId, fbPostId, blotatoId, status: 'error', error: err.message });
      console.log(`  ERR [${String(i + 1).padStart(3)}/${posts.length}] obj:${objectId} -> ${err.message}`);
    }
    await sleep(500);
  }

  fs.writeFileSync(REPORT_FILE, JSON.stringify({
    deletedAt: new Date().toISOString(),
    totalTargeted: posts.length,
    deleted,
    failed,
    results,
  }, null, 2));

  console.log('');
  console.log(`  Deleted  : ${deleted}`);
  console.log(`  Failed   : ${failed}`);
  console.log(`  Report   : ${REPORT_FILE}`);
  console.log('='.repeat(68));

  if (failed > 0) process.exit(1);
})().catch(err => { console.error(`Fatal: ${err.message}`); process.exit(1); });
