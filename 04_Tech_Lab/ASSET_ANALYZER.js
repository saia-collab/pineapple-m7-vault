#!/usr/bin/env node

/**
 * ASSET ANALYZER — BATCH MODE + MULTIPLIER TRICK
 * Processes 10 most-recent Reels, generates 3 captions each (Sale, Culture, Recruitment).
 * Every caption includes a Tongan Proverb and compliant "Complimentary" language.
 * Outputs a 30-post JSON manifest ready for Blotato scheduling.
 */

const fs = require('fs');
const path = require('path');
const { trackAsset } = require('./SHEET_TRACKER');

const INBOX_PATH = 'c:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX';
const REELS_PATH = path.join(INBOX_PATH, 'Raw', 'VIDEOS', 'REELS');
const MANIFEST_PATH = path.join(INBOX_PATH, 'BATCH_MANIFEST.json');

// ─── TONGAN PROVERBS ─────────────────────────────────────────────────────────
const PROVERBS = [
    { tongan: "'Oua e lau kafo kae lau lava",          english: "Don't count the wounds, count the victories." },
    { tongan: "Ko e tahi 'oku iku ki uta",              english: "The sea always returns to shore. Persistence wins." },
    { tongan: "Tauhi vā",                               english: "Nurture the space between you. Protect every relationship." },
    { tongan: "Ko e ngutu 'o e ika 'oku iku ai",        english: "The fish is caught by its mouth. Let your work speak louder." },
    { tongan: "Faka'apa'apa",                           english: "Respect above all else." },
    { tongan: "'Oku 'ikai ko e langi 'oku 'ikai ha ngāue", english: "Even on a dark day, there is always work to be done." },
    { tongan: "Ko e 'Otua mo Tonga ko hoku tofi'a",    english: "God and Tonga are my inheritance." },
    { tongan: "Fakakoloa 'o e laumālie",                english: "Enrich the spirit first. Everything else follows." },
    { tongan: "Ko e me'a lelei 'oku faingata'a ke ma'u", english: "Good things are hard to come by. Never cut corners." },
    { tongan: "Tō e lelei he 'aho ni",                  english: "Plant good today; don't block tomorrow's harvest." },
];

// ─── MULTIPLIER TRICK CAPTION TEMPLATES ──────────────────────────────────────
// Each function receives (videoName, proverb) and returns Instagram-ready text.

function saleCaptions(videoName, p) {
    return [
        // SALE 1 — Insurance Hook
        `🏠 Your roof took a hit. Insurance should pay for it.\n\nMost ${getCity(videoName)} homeowners don't know their hail damage qualifies for a full insurance-funded roof replacement — until we show them.\n\nWe offer a complimentary on-site inspection. Our GAF-Certified crew documents everything your adjuster needs to see. No commitment. Just answers.\n\n${p.tongan} — ${p.english}\n\n📍 Drop your address below or DM us "INSPECT" to book your complimentary visit.\n\n#PineappleRoofing #FriscoRoofing #HailDamage #InsuranceClaim #ComplimentaryInspection #GAFCertified #StormRestoration`,

        // SALE 2 — Urgency Hook
        `⛈️ ${getCity(videoName)} got hit. Are you on the list?\n\nIf your neighborhood saw hail in the last 12 months, your roof could qualify for a full insurance replacement — paid by your carrier, not your wallet.\n\nWe do the paperwork. We run the inspection. We deliver the job. All you do is say yes.\n\n${p.tongan} — ${p.english}\n\nLimited complimentary inspection slots this week. DM us or drop 📍 below.\n\n#FriscoRoofing #HailStorm #InsuranceFunded #ComplimentaryInspection #PineappleRoofing #StormDamage`,

        // SALE 3 — Neighborhood Hook
        `🏘️ Your neighbor just got a new roof. Yours could be next — and your insurance might cover it.\n\nHail storms don't hit one house at a time. If your block got tagged, every home on the street qualifies for a complimentary inspection.\n\n${p.tongan} — ${p.english}\n\nTag a neighbor and book your complimentary inspection this week. RCAT Licensed. IKO Certified (RCAT License #03-0637). 5-star rated.\n\n#${getCity(videoName).replace(/ /g, '')}Neighborhoods #HailDamage #InsuranceClaim #RoofReplacement #ComplimentaryInspection #PineappleRoofing`,
    ];
}

function cultureCaptions(videoName, p) {
    return [
        // CULTURE 1 — Brotherhood
        `🍍 The Pineapple Standard. One promise. Protect every home like it's our own.\n\nThis is what happens when a Polynesian family brings their values to work — we don't just install shingles, we protect the people inside.\n\n${p.tongan} — ${p.english}\n\nThis is the Pineapple promise. And we mean every word.\n\n#TonganPride #PolynesianPride #FamilyBusiness #FriscoStrong #PineappleContractors #SixBrothers`,

        // CULTURE 2 — Island Heritage
        `🌊 We come from islands where the sea taught us patience and the land taught us strength.\n\nThat upbringing shows in every job we finish. Every shingle set with care. Every client treated like 'ohana — family.\n\n${p.tongan} — ${p.english}\n\nThis is Pineapple. And we're proud of where we're from.\n\n#PolynesianPride #IslandStrong #TonganHeritage #FamilyBusiness #PineappleContractors #FriscoRoofing`,

        // CULTURE 3 — Values
        `🤝 In our culture, we protect the people around us. That's not a company slogan — it's how we were raised.\n\nSix Polynesian brothers brought that value from home to every jobsite in DFW.\n\n${p.tongan} — ${p.english}\n\nThank you, ${getCity(videoName)}. You've trusted us with your most important asset. We don't take that lightly.\n\n#TonganValues #PolynesianCulture #FriscoRoofing #PineappleContractors #Grateful #HomeProtection`,
    ];
}

function recruitmentCaptions(videoName, p) {
    return [
        // RECRUITMENT 1 — Career Builder
        `🔨 We're not just hiring. We're growing a legacy.\n\nPineapple Contractors is RCAT Licensed, IKO Certified (RCAT License #03-0637), and built on Polynesian family values. If you hustle hard, treat every client like family, and want to build a career — not just a paycheck — we want to meet you.\n\n${p.tongan} — ${p.english}\n\nDM us "JOIN" to learn about open positions. No experience required — only drive.\n\n#NowHiring #RoofingJobs #FriscoJobs #JoinTheCrew #PineappleContractors #PolynesianPride`,

        // RECRUITMENT 2 — Sales Rep Income
        `📈 Our top reps earned 6 figures last year in roofing sales. Real numbers. Real neighborhoods. Real commissions.\n\nIf you can build rapport and are willing to learn our system, we'll put you in front of homeowners who need you NOW.\n\n${p.tongan} — ${p.english}\n\nDM "EARN" and let's talk numbers.\n\n#RoofingSales #SixFigures #DFWSales #NowHiring #PineappleContractors #UncappedCommission`,

        // RECRUITMENT 3 — Culture Fit
        `💪 If you've been grinding for a company that doesn't respect your time, your hustle, or your potential — we see you.\n\nPineapple Contractors leads with respect, rewards performance, and promotes from within.\n\n${p.tongan} — ${p.english}\n\nReady for a crew that values you? DM "RESPECT" and let's talk.\n\n#RoofingCareers #JoinTheCrew #DFWJobs #PineappleContractors #GoodCulture #NowHiring`,
    ];
}

// ─── HELPERS ─────────────────────────────────────────────────────────────────

function getCity(videoName) {
    const lower = videoName.toLowerCase();
    if (lower.includes('frisco'))        return 'Frisco';
    if (lower.includes('allen'))         return 'Allen';
    if (lower.includes('mckinney'))      return 'McKinney';
    if (lower.includes('colony'))        return 'The Colony';
    if (lower.includes('arlington'))     return 'Arlington';
    if (lower.includes('grapevine'))     return 'Grapevine';
    if (lower.includes('carrolton') || lower.includes('carrollton')) return 'Carrollton';
    if (lower.includes('rockwall'))      return 'Rockwall';
    if (lower.includes('plano'))         return 'Plano';
    if (lower.includes('irving'))        return 'Irving';
    return 'DFW';
}

function walkDir(dir) {
    let files = [];
    if (!fs.existsSync(dir)) return files;
    const items = fs.readdirSync(dir, { withFileTypes: true });
    for (const item of items) {
        const fullPath = path.join(dir, item.name);
        if (item.isDirectory()) {
            files = files.concat(walkDir(fullPath));
        } else {
            files.push(fullPath);
        }
    }
    return files;
}

function getTop10RecentReels() {
    const all = walkDir(REELS_PATH);
    const videos = all.filter(f => ['.mp4', '.mov', '.MP4', '.MOV'].includes(path.extname(f)));
    return videos
        .map(f => ({ path: f, mtime: fs.statSync(f).mtimeMs }))
        .sort((a, b) => b.mtime - a.mtime)
        .slice(0, 10)
        .map(f => f.path);
}

// Schedule slots: 3 per month (1st, 11th, 21st) at 9 AM CDT (14:00 UTC)
// Starting June 2026 for 10 months → June 2026 – March 2027
function buildScheduleDates() {
    const slots = [];
    const startYear = 2026;
    const startMonth = 5; // 0-indexed: 5 = June
    for (let m = 0; m < 10; m++) {
        const d = new Date(Date.UTC(startYear, startMonth + m, 1, 14, 0, 0));
        slots.push(new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 1,  14, 0, 0)).toISOString());
        slots.push(new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 11, 14, 0, 0)).toISOString());
        slots.push(new Date(Date.UTC(d.getUTCFullYear(), d.getUTCMonth(), 21, 14, 0, 0)).toISOString());
    }
    return slots; // 30 slots
}

// ─── BATCH RUNNER ─────────────────────────────────────────────────────────────

async function runBatch() {
    console.log('🚀 ASSET ANALYZER — BATCH MODE\n');
    console.log('📋 Multiplier Trick: 1 Sale + 1 Culture + 1 Recruitment per asset\n');

    const videos = getTop10RecentReels();
    if (videos.length < 10) {
        console.warn(`⚠️  Only found ${videos.length} reels (expected 10). Continuing with available assets.`);
    }

    const scheduleDates = buildScheduleDates();
    const posts = [];

    for (let i = 0; i < videos.length; i++) {
        const videoPath = videos[i];
        const videoName = path.basename(videoPath);
        const p = PROVERBS[i];

        const sale        = saleCaptions(videoName, p)[0];        // one per video (slot 0)
        const culture     = cultureCaptions(videoName, p)[0];
        const recruitment = recruitmentCaptions(videoName, p)[0];

        const month = new Date(scheduleDates[i * 3]).toLocaleString('en-US', { month: 'long', year: 'numeric', timeZone: 'UTC' });
        console.log(`📹 Video ${i + 1}: ${videoName}`);
        console.log(`   📅 Month: ${month}`);
        console.log(`   ✍️  Proverb: ${p.tongan}`);
        console.log(`   ✅ 3 captions generated (Sale · Culture · Recruitment)\n`);

        posts.push({
            postNumber: i * 3 + 1,
            type: 'SALE',
            video: videoName,
            scheduledTime: scheduleDates[i * 3],
            platform: 'instagram',
            accountId: '43127',
            text: sale,
            mediaUrls: [],
            proverb: p.tongan,
        });
        posts.push({
            postNumber: i * 3 + 2,
            type: 'CULTURE',
            video: videoName,
            scheduledTime: scheduleDates[i * 3 + 1],
            platform: 'instagram',
            accountId: '43127',
            text: culture,
            mediaUrls: [],
            proverb: p.tongan,
        });
        posts.push({
            postNumber: i * 3 + 3,
            type: 'RECRUITMENT',
            video: videoName,
            scheduledTime: scheduleDates[i * 3 + 2],
            platform: 'instagram',
            accountId: '43127',
            text: recruitment,
            mediaUrls: [],
            proverb: p.tongan,
        });

        await trackAsset(videoName, videoPath, 'Complimentary', 'PENDING_BLOTATO');
    }

    fs.writeFileSync(MANIFEST_PATH, JSON.stringify({ generatedAt: new Date().toISOString(), totalPosts: posts.length, posts }, null, 2));
    console.log(`\n✅ BATCH COMPLETE — ${posts.length} posts written to:\n   ${MANIFEST_PATH}`);
    console.log('\n📤 Next step: Push manifest to Blotato scheduler.\n');

    return posts;
}

runBatch().catch(console.error);
