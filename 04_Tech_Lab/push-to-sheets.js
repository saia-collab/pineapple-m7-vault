/**
 * push-to-sheets.js
 * Appends all 30 Pineapple posts to the Google Sheet, including the Media Path column.
 * Spreadsheet: https://docs.google.com/spreadsheets/d/11n8Bm6fd1dz8EB9_jwGgU9UKlXmoR7Gz9GGiFYtbnpA
 *
 * ─── ONE-TIME SETUP (5 minutes) ──────────────────────────────────────────────
 * 1. Go to: https://console.cloud.google.com/
 * 2. Select or create a project → Enable "Google Sheets API"
 * 3. IAM & Admin → Service Accounts → Create service account
 *    Name: pineapple-sheets  Role: Editor
 * 4. Click the service account → Keys tab → Add Key → JSON → Download
 * 5. Save the downloaded file as:
 *    C:\Pineapple-Mana-Global\01_Command_Center\service-account.json
 * 6. Open your Google Sheet → Share → paste the service account email → Editor
 * 7. Run: node push-to-sheets.js
 * ──────────────────────────────────────────────────────────────────────────────
 *
 * Run: node push-to-sheets.js
 */

const { google } = require('googleapis');
const path = require('path');

const SPREADSHEET_ID   = '11n8Bm6fd1dz8EB9_jwGgU9UKlXmoR7Gz9GGiFYtbnpA';
const SERVICE_ACCT_KEY = path.join(__dirname, 'service-account.json');

// ─── Asset → local media path mapping ────────────────────────────────────────
const ASSET_MEDIA = {
  'Asset 01': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\CompletedVideos\\Completed Roof\\DJI_20260323101858_0001_D.MP4',
  'Asset 02': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\CompletedVideos\\Completed Roof\\DJI_20260323101953_0006_D.MP4',
  'Asset 03': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\CompletedVideos\\Completed Roof\\DJI_20260323111131_0021_D.MP4',
  'Asset 04': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\CompletedVideos\\Completed Roof\\DJI_20260323111217_0022_D.MP4',
  'Asset 05': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\CompletedVideos\\Completed Roof\\DJI_20260323111300_0023_D.MP4',
  'Asset 06': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\CompletedVideos\\Completed Roof\\DJI_20260323111507_0026_D.MP4',
  'Asset 07': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\Raw\\Photos\\IMG_2179.JPG',
  'Asset 08': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\Raw\\Photos\\IMG_2180.JPG',
  'Asset 09': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\Raw\\Photos\\IMG_1145.JPG',
  'Asset 10': 'C:\\Pineapple-Mana-Global\\02_Media_Vault\\Pineapple-Media-HQ\\01-INBOX\\Raw\\Photos\\IMG_1246.JPG',
};

// ─── All 30 posts ─────────────────────────────────────────────────────────────
const POSTS = [
  { id: 17, asset: 'Asset 01', type: 'Sale',    caption: 'Frisco just got hit. Again. 🌩️',                         copy: 'Frisco just got hit. Again. 🌩️\n\nHail season doesn\'t ask permission — and most homeowners don\'t find the damage until water is dripping through their ceiling.\n\nPineapple Contractors | IKO Certified (RCAT License #03-0637) | RCAT Licensed #03-0637\nFREE insurance-ready inspection. 50-year warranty roofs. Zero out-of-pocket on approved claims.\n\n📍 Serving Frisco, Plano, McKinney & all of Collin County.\n\nDM us \'ROOF\' or tap the link in bio. We\'ll be there before your insurance deadline closes.' },
  { id: 18, asset: 'Asset 01', type: 'Culture', caption: 'Before we swing a hammer, we talk story. 🤙',            copy: 'Before we swing a hammer, we talk story. 🤙\n\nOur dad taught us: when you do work for someone\'s family, you do it like it\'s your own family\'s house. No shortcuts. No low-balling. No disappearing after the check clears.\n\nThe Pineapple Standard. One standard. Every single job.\n\nThat\'s the Polynesian way. That\'s the Pineapple way.\n\n#PineappleContractors #FriscoRoofing #FamilyFirst #PolynesianPride' },
  { id: 19, asset: 'Asset 01', type: 'Recruit', caption: 'We\'re looking for 2 crew leads...',                      copy: 'We\'re looking for 2 crew leads who are done working for companies that don\'t pay what you\'re worth.\n\nHere\'s what we offer:\n→ $28–$38/hr based on skill\n→ Steady work (not just storm season)\n→ Family-run culture — you\'re not a number\n→ Room to grow into project management\n\nIf you show up, do the work, and take pride in it — we want to talk.\n\nDM us \'CREW\' to start the conversation. Frisco TX.' },
  { id: 20, asset: 'Asset 02', type: 'Sale',    caption: 'Your neighbor just got a new roof. For Full Restoration Coverage.', copy: 'Your neighbor just got a new roof. For Full Restoration Coverage.\n\nInsurance covered it after last month\'s storm. All it took was a professional photo audit.\n\nMost homeowners don\'t file. They don\'t know how.\nWe do. We\'ve done it 350+ times across DFW.\n\nIKO Certified (RCAT License #03-0637) | 50-year product warranty | RCAT #03-0637\n\n🍍 Complimentary Professional Photo Audit (CPPA). No pressure. Just answers.\n\nDM \'Complimentary\' to book yours before the claims window closes.' },
  { id: 21, asset: 'Asset 02', type: 'Culture', caption: 'In Tonga, when a storm damages someone\'s home...',      copy: 'In Tonga, when a storm damages someone\'s home — the whole village shows up. Nobody waits to be asked.\n\nWe built this company on that same value.\n\nWhen Frisco gets hammered with hail, we don\'t sit back and wait for leads. We show up. We check on neighbors. We help families navigate something stressful.\n\nThat\'s not a marketing strategy. That\'s who we are.\n\n#SixBrothers #PineappleRoofing #PolynesianValues #FriscoTX' },
  { id: 22, asset: 'Asset 02', type: 'Recruit', caption: 'Most roofing companies talk about \'opportunity\'...',    copy: 'Most roofing companies talk about \'opportunity\' then leave you out in the heat with no support.\n\nWe do it different.\n\nEvery crew member at Pineapple gets:\n✅ A real schedule (not day-by-day guessing)\n✅ A project manager who has your back on every job\n✅ Paid on time. Every time.\n✅ A team that actually cares if you grow\n\nWe\'re hiring in Frisco/Collin County. Experience preferred, character required.\n\nDM \'JOIN\' — let\'s talk.' },
  { id: 23, asset: 'Asset 03', type: 'Sale',    caption: 'Storm damage doesn\'t always look like damage. 🔍',      copy: 'Storm damage doesn\'t always look like damage. 🔍\n\nGranule loss. Soft spots. Lifted edges. Things you can\'t see from the ground — but your insurance adjuster can, and will use them against you if you don\'t document first.\n\nWe photograph everything. We write the report. We submit it properly.\n\n50-year GAF warranty. RCAT Licensed. 5-star rated across Frisco & DFW.\n\nBook your Complimentary roof audit before your 30-day claims window closes.\n📲 DM \'AUDIT\' now.' },
  { id: 24, asset: 'Asset 03', type: 'Culture', caption: 'We didn\'t set out to build a roofing company.',         copy: 'We didn\'t set out to build a roofing company. We set out to take care of people.\n\nRoofing just happened to be the thing we were good at. 🍍\n\nEvery completed job you see on this page represents a family who trusted six Polynesian brothers with the roof over their heads. That\'s not something we take lightly.\n\nHumility. Hard work. Hospitality. Three words our parents drilled into us before we ever knew what a shingle was.\n\n#PineappleContractors #FriscoRoofing #Polynesian #BuiltOnValues' },
  { id: 25, asset: 'Asset 03', type: 'Recruit', caption: 'Real talk: if you\'re tired of working for a boss...',   copy: 'Real talk: if you\'re tired of working for a boss who can\'t spell your name right — apply here.\n\nPineapple Contractors is family-owned and we run it that way. Small enough that you matter. Established enough that your paycheck never bounces.\n\nRight now we need:\n→ Experienced shingle installers\n→ Gutter crews\n→ Reliable laborers willing to learn\n\nFrisco, TX. Full-time. Steady.\n\nDM \'WORK\' and let\'s get on a 5-minute call this week.' },
  { id: 26, asset: 'Asset 04', type: 'Sale',    caption: 'This roof was TRASHED after the last Frisco storm.',      copy: 'This roof was TRASHED after the last Frisco storm.\n\nThe homeowner had no idea. She thought it was fine — a few missing shingles. Our inspector found 47 hail impact points, granule loss on 80% of the surface, and three soft spots the insurance adjuster missed entirely.\n\nWe documented it. The claim was approved. She paid $0.\n\n50-year GAF warranty. Full Restoration Coverage. Done in 2 days.\n\nThat\'s the Pineapple process. 📲 Book your Complimentary audit — DM \'CLAIM\'.' },
  { id: 27, asset: 'Asset 04', type: 'Culture', caption: 'There\'s a Tongan concept called \'fefeka\'...',          copy: 'There\'s a Tongan concept called \'fefeka\' — it roughly means toughness with heart. You do hard things, but you do them with love.\n\nThat\'s how we run every job. 🏡\n\nThe work is physical. The weather doesn\'t care. The deadlines are real. But every brother on this crew knows we\'re not just laying shingles — we\'re protecting someone\'s family.\n\nFefeka. Every. Single. Day.\n\n#SixBrothers #PineappleRoofing #TonganPride #FriscoTX' },
  { id: 28, asset: 'Asset 04', type: 'Recruit', caption: 'We\'re not hiring for a \'position.\'',                   copy: 'We\'re not hiring for a \'position.\' We\'re building a crew.\n\nIf you\'re the kind of person who:\n→ Shows up on time without being chased\n→ Takes pride in a clean, well-done installation\n→ Wants to actually understand the business, not just the task\n\n...then we\'re probably a good fit.\n\nPineapple Contractors | Frisco TX | Family-owned since day one\n\nDrop \'CREW\' in our DMs. No resume needed. Just show up ready.' },
  { id: 29, asset: 'Asset 05', type: 'Sale',    caption: 'You have 30 days after a hail event to file...',          copy: 'You have 30 days after a hail event to file an insurance claim in Texas.\n\nMost homeowners don\'t know that. And most contractors don\'t tell them until the window is almost closed.\n\nWe tell you on day one. 📅\n\nFree professional inspection. Insurance-ready photo report. IKO Certified (RCAT License #03-0637) crew. 50-year warranties on materials.\n\nPineapple Contractors — RCAT Licensed #03-0637, serving Frisco, McKinney, Plano & all of Collin County.\n\n📲 DM \'DEADLINE\' to book before yours passes.' },
  { id: 30, asset: 'Asset 05', type: 'Culture', caption: 'Growing up in a Polynesian home...',                      copy: 'Growing up in a Polynesian home meant you never left the table until everyone was fed.\n\nWe run our job sites the same way. 🍽️\n\nNobody goes home until the work is right. Nobody cuts corners so they can get to the next job faster. Nobody leaves a homeowner confused or unsure about what just happened to their roof.\n\nEvery family on our job list gets the same care.\n\nThat\'s not a slogan. That\'s what our mom would do.\n\n#PineappleContractors #FamilyValues #FriscoRoofing #PolynesianPride' },
  { id: 31, asset: 'Asset 05', type: 'Recruit', caption: 'We grew this company by hiring people who outwork...',    copy: 'We grew this company by hiring people who outwork the competition — not the ones who just talk about it.\n\nRight now Pineapple is growing fast across Collin County. We need people who want to grow with us.\n\nWhat you need:\n✅ 1+ year roofing or construction experience\n✅ Reliable transportation\n✅ A phone you actually answer\n✅ Pride in doing things right\n\nWhat you\'ll get: Good pay. Consistent work. A team worth showing up for.\n\nDM \'GROW\' — hiring now.' },
  { id: 32, asset: 'Asset 06', type: 'Sale',    caption: 'The roof on this Frisco home was 14 years old...',        copy: 'The roof on this Frisco home was 14 years old when the storm hit. The owners figured it had a few more years left.\n\nIt didn\'t. 🌧️\n\nThe hail cracked the underlayment in three places. Water was already tracking before they called us.\n\nWe caught it before it became a $30,000 interior problem. Insurance covered the full replacement.\n\nIKO Certified (RCAT License #03-0637) | 50-year warranty | RCAT Licensed | Frisco TX\n\nIf your roof is 10+ years old and you\'ve had any storms this season — DM \'CHECK\' for your Complimentary audit.' },
  { id: 33, asset: 'Asset 06', type: 'Culture', caption: 'Our brother Jr. always says...',                          copy: 'Our brother Jr. always says: \'A roof you\'re proud of is a roof you\'d put over your own parents\' house.\'\n\nThat stuck with all of us. 🏠\n\nEvery shingle we lay, every gutter we hang, every restoration we complete — we ask ourselves that question. Would we do this job for Mom and Dad?\n\nIf the answer is yes, it\'s done right. If it\'s not, we go back.\n\nThe Pineapple Standard. One standard.\n\n#Pineapple #FriscoRoofing #PolynesianValues #FamilyOwned' },
  { id: 34, asset: 'Asset 06', type: 'Recruit', caption: 'The roofing industry is full of companies...',            copy: 'The roofing industry is full of companies that will hire you fast and burn you out faster.\n\nWe\'ve heard the stories. A lot of our guys came from those companies.\n\nAt Pineapple, we run jobs with a dedicated project manager on every site. You always know who to call. You always know what\'s next. You\'re never left guessing.\n\nWe\'re hiring installers and crew in Frisco/Collin County.\n\nStable schedule. Real pay. People who care.\n\nDM \'APPLY\' to start a conversation this week.' },
  { id: 35, asset: 'Asset 07', type: 'Sale',    caption: 'Here\'s what a $0 roof looks like. 🍍',                   copy: 'Here\'s what a $0 roof looks like. 🍍\n\nStorm hits. Homeowner calls us. We inspect within 48 hours, document every impact point with photos, write a claim-ready report, and coordinate with their insurance adjuster.\n\nResult: full replacement approved. GAF 50-year shingles installed. Done.\n\nThis is the Pineapple process — built for DFW storms, backed by 20+ years of experience and a GAF Certification that puts us in the top tier of contractors nationwide.\n\nComplimentary Professional Photo Audit (CPPA) for Frisco homeowners. DM \'STORM\' to get started.' },
  { id: 36, asset: 'Asset 07', type: 'Culture', caption: 'We started this company with a truck...',                 copy: 'We started this company with a truck, a few tools, and a lot of Polynesian stubbornness. 💪\n\nIn our culture, giving up isn\'t really an option. When things get hard, you lean on family. You show up. You do the work.\n\nOver 350 completed projects later — that\'s still exactly how we operate.\n\nSmall enough to care. Experienced enough to deliver. Family-owned from the first nail to the final inspection.\n\n#SixBrothers #PineappleContractors #Polynesian #FriscoTX #RoofingFamily' },
  { id: 37, asset: 'Asset 07', type: 'Recruit', caption: 'I\'m going to be direct: we pay more than most...',       copy: 'I\'m going to be direct: we pay more than most, we\'re more organized than most, and we have a better culture than most.\n\nThe catch? We have high standards.\n\nWe\'re not looking for someone to fill a spot. We\'re looking for someone who takes the trade seriously — who wants to do excellent work and get paid well for it.\n\nIf that\'s you, Pineapple Contractors wants to meet you.\n\nFrisco TX | Full-time | Hiring now\n\nDM \'STANDARDS\' — let\'s talk this week.' },
  { id: 38, asset: 'Asset 08', type: 'Sale',    caption: 'Hail the size of a pea doesn\'t look dangerous.',         copy: 'Hail the size of a pea doesn\'t look dangerous. But it destroys shingle granules — the layer that protects your home from UV damage and water intrusion. ☀️🌧️\n\nMost homeowners don\'t notice it for months. By then, the insurance window has closed.\n\nWe catch it early. We document it properly. We make sure your claim gets paid.\n\nIKO Certified (RCAT License #03-0637) Contractor | RCAT Licensed #03-0637 | 50-year product warranty\n\nFree roof audit for Frisco homeowners. DM \'GRANULES\' or tap the link in bio.' },
  { id: 39, asset: 'Asset 08', type: 'Culture', caption: 'In the islands, your home is your family\'s legacy.',    copy: 'In the islands, your home is your family\'s legacy. You protect it like you protect your name.\n\nThat belief followed our family from the Pacific to Texas. 🌴\n\nWhen a Frisco homeowner hands us the keys and trusts us with their property — we treat it like it belongs to our own family. That means honest work, clean job sites, and we don\'t leave until they\'re satisfied.\n\nNot because we have to. Because that\'s who we are.\n\n#PineappleRoofing #PolynesianPride #FriscoTX #HomeIsFamily' },
  { id: 40, asset: 'Asset 08', type: 'Recruit', caption: 'Tired of roofing companies that treat you like a number?', copy: 'Tired of roofing companies that treat you like a number?\n\nAt Pineapple, the owners are on the job sites. You\'ll know your project manager\'s name. Your questions get answered same day.\n\nWe\'re a growing family-owned company in Frisco and we\'re adding to our crew:\n→ Experienced shingle installers\n→ Laborers ready to learn the trade\n→ People who want to be part of something real\n\nPay: Competitive. Schedule: Consistent. Culture: Earned.\n\nDM \'TEAM\' to apply.' },
  { id: 41, asset: 'Asset 09', type: 'Sale',    caption: 'The storm two weeks ago damaged more Frisco roofs...',    copy: 'The storm two weeks ago damaged more Frisco roofs than most homeowners realize. 🌩️\n\nWe\'ve already completed 11 inspections in Frisco this week alone. Roughly 70% had significant damage their owners didn\'t know about.\n\nHere\'s what we do:\n→ Complimentary 20-minute photo inspection\n→ Full damage report (insurance-ready)\n→ We coordinate with your adjuster\n→ Replacement with 50-year GAF warranty\n\nOut of pocket: $0 on approved claims.\n\nIKO Certified (RCAT License #03-0637) | RCAT Licensed | 5-star rated\n\nDM \'FRISCO\' to book your Complimentary audit.' },
  { id: 42, asset: 'Asset 09', type: 'Culture', caption: 'Hard work was never optional in our family.',             copy: 'Hard work was never optional in our family. It was just what you did. 🤙\n\nGrowing up Polynesian, the concept of \'doing less\' didn\'t really exist. You showed up. You helped. You did it right. You didn\'t make excuses.\n\nAll six of us carry that into every job — from the first inspection to the final walkthrough.\n\nOur clients feel it. Our reviews show it. And the roofs we build last decades.\n\nThat\'s the inheritance our parents gave us. We just turned it into a business.\n\n#SixBrothers #PineappleContractors #PolynesianWork #FriscoRoofing' },
  { id: 43, asset: 'Asset 09', type: 'Recruit', caption: 'Most people in roofing are either underpaid or undervalued.', copy: 'Most people in roofing are either underpaid or undervalued. Sometimes both.\n\nWe started Pineapple because we knew it could be done better.\n\nNow we\'re at a point where we need talented people who want:\n💰 Competitive pay with room to grow\n📋 Organized jobs with a project manager on every site\n🤝 A team that treats you like a person\n🔨 Consistent work — not just when it storms\n\nFrisco TX | Collin County | Hiring now\n\nDM \'BETTER\' and let\'s have a real conversation.' },
  { id: 44, asset: 'Asset 10', type: 'Sale',    caption: 'This is what a properly installed... GAF-certified roof looks like. 🏡', copy: 'This is what a properly installed, insurance-backed, GAF-certified roof looks like. 🏡\n\n50-year warranty. Installed by a family crew that treats your home like their own.\n\nIf you\'ve had any hail or wind this season across Frisco, Plano, McKinney or the surrounding areas — there\'s a real chance your current roof has hidden damage.\n\nOne Complimentary Professional Photo Audit (CPPA). 48-hour report. Zero pressure.\n\nPineapple Contractors | RCAT #03-0637 | IKO Certified (RCAT License #03-0637) | 5 Stars\n\n📲 DM \'WARRANTY\' to book yours today.' },
  { id: 45, asset: 'Asset 10', type: 'Culture', caption: 'The job isn\'t done when the materials are installed.',   copy: 'The job isn\'t done when the materials are installed. The job is done when the homeowner smiles. 😊\n\nThat\'s something Saia says before every project walkthrough. And every brother on this crew lives by it.\n\nIn Polynesian culture, the measure of your work isn\'t what YOU think of it — it\'s what the people you served think of it. That keeps us humble. And it keeps our standards high.\n\n350+ families protected across DFW. Every single one got our best.\n\n#PineappleRoofing #FriscoTX #PolynesianPride #BuiltWithHeart' },
  { id: 46, asset: 'Asset 10', type: 'Recruit', caption: 'We\'re not the biggest roofing company in DFW.',         copy: 'We\'re not the biggest roofing company in DFW. We never tried to be.\n\nWe\'re the most family-oriented. The most hands-on. The most honest about what we do and what we pay.\n\nRight now we\'re growing our crew for the season and we want people who:\n✅ Take the trade seriously\n✅ Show up and communicate\n✅ Want to grow within a real company — not just float job to job\n\nPineapple Contractors | Frisco TX | Minority-owned | 5-star rated\n\nDM \'SEASON\' to apply. We\'ll respond within 24 hours.' },
];

// ─── Main ─────────────────────────────────────────────────────────────────────
(async () => {
  const fs = require('fs');
  if (!fs.existsSync(SERVICE_ACCT_KEY)) {
    console.error(`
❌ SERVICE ACCOUNT FILE NOT FOUND.

Expected at: ${SERVICE_ACCT_KEY}

Complete the 5-minute setup:
  1. https://console.cloud.google.com/ → Enable "Google Sheets API"
  2. IAM & Admin → Service Accounts → Create → download JSON key
  3. Save it as: ${SERVICE_ACCT_KEY}
  4. Open your Google Sheet → Share → paste the service account email → Editor
  5. Re-run: node push-to-sheets.js
`);
    process.exit(1);
  }

  const auth = new google.auth.GoogleAuth({
    keyFile: SERVICE_ACCT_KEY,
    scopes: ['https://www.googleapis.com/auth/spreadsheets'],
  });

  const sheets = google.sheets({ version: 'v4', auth });

  // Get existing headers
  const headerRes = await sheets.spreadsheets.values.get({
    spreadsheetId: SPREADSHEET_ID,
    range: 'Sheet1!1:1',
  });

  let headers = headerRes.data.values?.[0] || ['#', 'Asset', 'Type', 'Caption', 'Copy'];

  // Ensure Media Path column exists
  if (!headers.includes('Media Path')) {
    headers = [...headers, 'Media Path'];
    await sheets.spreadsheets.values.update({
      spreadsheetId: SPREADSHEET_ID,
      range: 'Sheet1!A1',
      valueInputOption: 'RAW',
      requestBody: { values: [headers] },
    });
    console.log('✅ Added "Media Path" column to header row');
  }

  const mediaPathCol = headers.indexOf('Media Path');
  const colCount = headers.length;

  // Build rows aligned to header columns
  const rows = POSTS.map(p => {
    const row = new Array(colCount).fill('');
    const set = (name, val) => { const i = headers.indexOf(name); if (i >= 0) row[i] = val; };
    set('#', p.id);
    set('Asset', p.asset);
    set('Type', p.type);
    set('Caption', p.caption);
    set('Copy', p.copy);
    set('Media Path', ASSET_MEDIA[p.asset] || '');
    return row;
  });

  // Append rows
  const appendRes = await sheets.spreadsheets.values.append({
    spreadsheetId: SPREADSHEET_ID,
    range: 'Sheet1!A:A',
    valueInputOption: 'RAW',
    insertDataOption: 'INSERT_ROWS',
    requestBody: { values: rows },
  });

  console.log(`✅ Appended ${POSTS.length} posts to Google Sheets`);
  console.log(`   Updated range: ${appendRes.data.updates?.updatedRange}`);
  console.log(`   Total rows added: ${appendRes.data.updates?.updatedRows}`);
  console.log(`\n🔗 Sheet: https://docs.google.com/spreadsheets/d/${SPREADSHEET_ID}`);
})();
