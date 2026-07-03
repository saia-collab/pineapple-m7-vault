/**
 * SHEET TRACKER - Connect Pineapple Media HQ to Master CRM
 * Google Sheet ID: 11n8Bm6fd1dz8EB9_jwGgU9UKlXmoR7Gz9GGiFYtbnpA
 *
 * Usage: Track assets, paste live links, and monitor views
 */

const { google } = require('googleapis');
const { GoogleAuth } = require('google-auth-library');
const fs = require('fs');

const SHEET_ID = '11n8Bm6fd1dz8EB9_jwGgU9UKlXmoR7Gz9GGiFYtbnpA';

async function authorize() {
    const auth = new GoogleAuth({
        keyFile: 'c:\\pineapple-marketing\\service-account.json',
        scopes: ['https://www.googleapis.com/auth/spreadsheets'],
    });
    return auth;
}

// Add asset to tracker
async function trackAsset(assetName, assetPath, category, driveLink) {
    const auth = await authorize();
    const sheets = google.sheets({ version: 'v4', auth });

    const values = [[
        new Date().toISOString(),
        assetName,
        assetPath,
        category,
        driveLink || 'PENDING',
        'INBOX',
        0  // view count
    ]];

    try {
        const result = await sheets.spreadsheets.values.append({
            spreadsheetId: SHEET_ID,
            range: 'Assets!A:G',
            valueInputOption: 'USER_ENTERED',
            resource: { values },
        });
        console.log(`✅ Tracked: ${assetName}`);
        return result.data;
    } catch (err) {
        console.error('❌ Error tracking asset:', err);
    }
}

// Get asset list from tracker
async function getAssets(category) {
    const auth = await authorize();
    const sheets = google.sheets({ version: 'v4', auth });

    try {
        const result = await sheets.spreadsheets.values.get({
            spreadsheetId: SHEET_ID,
            range: `Assets!A:G`,
        });
        const rows = result.data.values || [];
        if (category) {
            return rows.filter(row => row[3] === category);
        }
        return rows;
    } catch (err) {
        console.error('❌ Error fetching assets:', err);
    }
}

// Update asset with drive link
async function updateAssetLink(assetName, driveLink) {
    const auth = await authorize();
    const sheets = google.sheets({ version: 'v4', auth });

    try {
        const assets = await getAssets();
        const rowIndex = assets.findIndex(row => row[1] === assetName);
        if (rowIndex > -1) {
            await sheets.spreadsheets.values.update({
                spreadsheetId: SHEET_ID,
                range: `Assets!E${rowIndex + 1}`,
                valueInputOption: 'USER_ENTERED',
                resource: { values: [[driveLink]] },
            });
            console.log(`✅ Updated link for: ${assetName}`);
        }
    } catch (err) {
        console.error('❌ Error updating asset:', err);
    }
}

module.exports = { trackAsset, getAssets, updateAssetLink };
