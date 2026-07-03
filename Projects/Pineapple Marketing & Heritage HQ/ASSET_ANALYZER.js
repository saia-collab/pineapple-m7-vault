#!/usr/bin/env node

/**
 * ASSET ANALYZER + BLOATATO CAPTIONS
 * Analyzes assets from Inbox and generates Bloatato-ready captions
 */

const fs = require('fs');
const path = require('path');
const { exec } = require('child_process');
const { trackAsset } = require('./SHEET_TRACKER');

const INBOX_PATH = 'c:\\pineapple-marketing\\Pineapple-Media-HQ\\01-INBOX';

// Analyze asset and return metadata
function analyzeAsset(filePath) {
    const fileName = path.basename(filePath);
    const ext = path.extname(filePath).toLowerCase();
    const stats = fs.statSync(filePath);
    const category = path.dirname(filePath).split('\\').pop();

    return {
        fileName,
        filePath,
        category,
        extension: ext,
        size: stats.size,
        created: stats.birthtime,
        isVideo: ['.mp4', '.mov', '.avi'].includes(ext),
        isPhoto: ['.jpg', '.jpeg', '.png'].includes(ext),
    };
}

// Generate Bloatato caption based on asset type
function generateBloatataCaption(asset) {
    const { category, isVideo, isPhoto } = asset;

    const captions = {
        'CompletedVideos': {
            template: `🏠 Another roof transformation complete. Our crew doesn't just fix roofs—we protect homes like family. That's the Pineapple promise. | #RoofingPros #FriscoStrong #WarriorContractors`,
            hashtags: ['#roofing', '#beforeandafter', '#frisco', '#homeowners']
        },
        'FounderStory': {
            template: `⚔️ 'Oua e lau kafo kae lau lava—Don't count the wounds, count the victories. This is why we do it. | #FounderStory #SaiaMoe #PolynesiaPride`,
            hashtags: ['#founder', '#entrepreneurship', '#leadership', '#tongan']
        },
        'Diwali': {
            template: `🪔 Celebrating Diwali with the Pineapple family. Light, community, and strength. | #Diwali #Community #FriscoLove`,
            hashtags: ['#diwali', '#celebration', '#community', '#festival']
        },
        'DronePhotos': {
            template: `🚁 Drone view of Frisco protection. Every angle tells a story of quality and care. | #DronePhotography #AerialView #RoofingQuality`,
            hashtags: ['#drone', '#aerial', '#photography', '#roofing']
        },
        'Personal': {
            template: `🌍 Family moments fuel the hustle. The Pineapple Standard protecting your home so you can focus on moments like these. | #FamilyFirst #TonganPride`,
            hashtags: ['#family', '#moments', '#polynesia', '#tongan']
        }
    };

    const cap = captions[category] || captions['Personal'];
    return {
        primaryCaption: cap.template,
        hashtags: cap.hashtags,
        category: category,
        readyForBloutato: true
    };
}

// Generate Bloatato script
function generateBloatatoScript(asset, caption) {
    const script = {
        type: 'BLOATATO_CAPTION',
        timestamp: new Date().toISOString(),
        asset: {
            name: asset.fileName,
            path: asset.filePath,
            category: asset.category,
        },
        caption: caption.primaryCaption,
        hashtags: caption.hashtags.join(' '),
        instructions: `
🤖 BLOATATO SCHEDULE INSTRUCTIONS:
1. Use the caption EXACTLY as provided—don't let Bloatato AI rewrite it
2. Post to Instagram Reels (if video) or Feed (if photo)
3. Schedule for 9 AM Frisco time (optimal engagement)
4. Pin the caption to Stories for 24 hours
5. Tag @pineapplecontractorsfrisco and your personal handle

CAPTION TO POST:
${caption.primaryCaption}

HASHTAGS (add all):
${caption.hashtags.join(' ')}

DO NOT MODIFY: Tone is Polynesian-proud, local, and authentic.
        `,
        readyToSchedule: true
    };

    return script;
}

// Main test run
async function runTest() {
    console.log('🚀 ASSET ANALYZER TEST RUN\n');

    // Find first video in Inbox
    const walkDir = (dir) => {
        let files = [];
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
    };

    const allFiles = walkDir(INBOX_PATH);
    const videoFiles = allFiles.filter(f => ['.mp4', '.mov'].includes(path.extname(f).toLowerCase()));

    if (videoFiles.length === 0) {
        console.log('❌ No videos found in Inbox');
        return;
    }

    const testAsset = videoFiles[0];
    console.log(`📹 Analyzing: ${testAsset}\n`);

    const asset = analyzeAsset(testAsset);
    console.log('📊 ASSET METADATA:');
    console.log(JSON.stringify(asset, null, 2));
    console.log('\n');

    const caption = generateBloatataCaption(asset);
    console.log('✏️ BLOATATO CAPTION:');
    console.log(JSON.stringify(caption, null, 2));
    console.log('\n');

    const script = generateBloatatoScript(asset, caption);
    console.log('🎬 BLOATATO SCRIPT:');
    console.log(JSON.stringify(script, null, 2));
    console.log('\n');

    // Save script to file
    const scriptPath = path.join(INBOX_PATH, `BLOATATO_${path.basename(testAsset, path.extname(testAsset))}.json`);
    fs.writeFileSync(scriptPath, JSON.stringify(script, null, 2));
    console.log(`✅ Script saved: ${scriptPath}`);

    // Track in Sheet
    await trackAsset(
        asset.fileName,
        asset.filePath,
        asset.category,
        'PENDING_BLOATATO'
    );

    console.log('\n✅ TEST RUN COMPLETE\n');
}

// Run test
runTest().catch(console.error);
