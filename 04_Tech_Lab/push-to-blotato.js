/**
 * push-to-blotato.js
 *
 * Reads compliant copy from Playbooks/MAY_PRODUCTION_COPY.md,
 * maps each row to Ad_Variation_H001..H030 in the local output vault,
 * and queues all posts 12 months out under DEC-005 safety behavior.
 *
 * Run: node 01_Command_Center/push-to-blotato.js
 */

const fs = require('fs');
const path = require('path');
const https = require('https');

const BLOTATO_API_KEY = process.env.BLOTATO_API_KEY || 'blt_q776zanllf253cwcEE/jXTAHwugySWF4V0afVEqwPXY=';
const ACCOUNT_ID = '28510';
const PAGE_ID = '101578888591535';
const PLAYBOOK_PATH = path.join(__dirname, 'Playbooks', 'MAY_PRODUCTION_COPY.md');
const RENDER_DIR = path.join(__dirname, '..', '02_Media_Vault', '2026_05_GENERAL_READY-TO-BLAST');
const RESULT_LOG_PATH = path.join(__dirname, 'blotato-results.json');

function computeScheduleTime() {
  const d = new Date();
  d.setMonth(d.getMonth() + 12);
  return d.toISOString();
}

function mapType(label) {
  if (label === 'Sale') return 'Sale';
  if (label === 'Culture') return 'Culture';
  return 'Recruitment';
}

function parsePlaybookTable(raw) {
  const posts = [];
  const lines = raw.split(/\r?\n/);
  for (const line of lines) {
    const m = line.match(/^\|\s*(\d+)\s*\|\s*(Sale|Culture|Recruitment)\s*\|\s*(.*?)\s*\|\s*(.*?)\s*\|\s*.*\|\s*$/);
    if (!m) continue;

    const id = Number(m[1]);
    const type = mapType(m[2]);
    const caption = m[3].trim();
    const cta = m[4].trim();

    posts.push({
      id,
      type,
      caption,
      cta,
      text: `${caption}\n\nCTA: ${cta}`,
      mediaPath: path.join(RENDER_DIR, `Ad_Variation_H${String(id).padStart(3, '0')}.mp4`),
    });
  }

  posts.sort((a, b) => a.id - b.id);
  return posts;
}

function validatePosts(posts) {
  if (posts.length !== 30) {
    throw new Error(`Expected 30 posts from playbook, found ${posts.length}`);
  }

  for (let i = 1; i <= 30; i += 1) {
    if (!posts.find(p => p.id === i)) {
      throw new Error(`Missing playbook row #${i}`);
    }
  }

  const banned = /(\bFREE\b|\$0\s*out\s*of\s*pocket)/i;
  const bad = posts.find(p => banned.test(p.text));
  if (bad) {
    throw new Error(`Compliance block: banned term found in post #${bad.id}`);
  }
}

function apiPost(routePath, body) {
  return new Promise((resolve, reject) => {
    const data = JSON.stringify(body);
    const opts = {
      hostname: 'backend.blotato.com',
      path: routePath,
      method: 'POST',
      headers: {
        'blotato-api-key': BLOTATO_API_KEY,
        'Content-Type': 'application/json',
        'Content-Length': Buffer.byteLength(data),
      },
    };

    const req = https.request(opts, res => {
      let out = '';
      res.on('data', chunk => { out += chunk; });
      res.on('end', () => {
        try {
          resolve({ status: res.statusCode, body: JSON.parse(out) });
        } catch {
          resolve({ status: res.statusCode, body: out });
        }
      });
    });

    req.on('error', reject);
    req.setTimeout(15000, () => {
      req.destroy();
      reject(new Error('timeout'));
    });
    req.write(data);
    req.end();
  });
}

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

(async () => {
  if (!fs.existsSync(PLAYBOOK_PATH)) {
    throw new Error(`Missing playbook: ${PLAYBOOK_PATH}`);
  }

  const scheduleTime = computeScheduleTime();
  const playbookRaw = fs.readFileSync(PLAYBOOK_PATH, 'utf8');
  const posts = parsePlaybookTable(playbookRaw);
  validatePosts(posts);

  console.log('Pineapple Blotato Publisher');
  console.log(`Account   : ${ACCOUNT_ID}`);
  console.log(`Page      : ${PAGE_ID}`);
  console.log(`Posts     : ${posts.length}`);
  console.log(`Scheduled : ${scheduleTime} (12-month DEC-005 safety window)`);

  const results = [];
  let ok = 0;
  let fail = 0;

  for (const post of posts) {
    const mediaExists = fs.existsSync(post.mediaPath);

    const payload = {
      post: {
        accountId: ACCOUNT_ID,
        scheduledTime: scheduleTime,
        content: {
          text: post.text,
          mediaUrls: [],
          platform: 'facebook',
        },
        target: {
          targetType: 'facebook',
          pageId: PAGE_ID,
        },
      },
    };

    try {
      const { status, body } = await apiPost('/v2/posts', payload);
      if (status === 201 && body.postSubmissionId) {
        ok += 1;
        results.push({
          id: post.id,
          type: post.type,
          status: 'queued',
          submissionId: body.postSubmissionId,
          mediaPath: post.mediaPath,
          mediaExists,
        });
        console.log(`  OK  #${String(post.id).padStart(2, '0')} ${post.type.padEnd(11)} -> ${body.postSubmissionId}${mediaExists ? '' : ' (missing local media)'}`);
      } else {
        fail += 1;
        results.push({
          id: post.id,
          type: post.type,
          status: 'error',
          error: body.message || JSON.stringify(body),
          mediaPath: post.mediaPath,
          mediaExists,
        });
        console.log(`  ERR #${String(post.id).padStart(2, '0')} ${post.type.padEnd(11)} -> ${body.message || status}`);
      }
    } catch (err) {
      fail += 1;
      results.push({
        id: post.id,
        type: post.type,
        status: 'error',
        error: err.message,
        mediaPath: post.mediaPath,
        mediaExists,
      });
      console.log(`  ERR #${String(post.id).padStart(2, '0')} ${post.type.padEnd(11)} -> ${err.message}`);
    }

    await sleep(400);
  }

  fs.writeFileSync(RESULT_LOG_PATH, JSON.stringify(results, null, 2));

  console.log('');
  console.log(`Done. ${ok} queued | ${fail} failed`);
  console.log(`Results saved: ${RESULT_LOG_PATH}`);
  console.log('Next: attach local media files in Blotato using mediaPath values, then manually review before publish.');
})().catch(err => {
  console.error(`Fatal: ${err.message}`);
  process.exit(1);
});
