/**
 * Pineapple M7 — CPPA capture form → Google_LSA_Leads sheet
 * Paste this into: your CRM Google Sheet → Extensions → Apps Script → Code.gs
 * Then set SHEET_ID below, Deploy as Web App (Anyone), and paste the /exec URL
 * into index.html's FORM_ENDPOINT.
 */
var SHEET_ID = 'PASTE_YOUR_GOOGLE_SHEET_ID_HERE';   // from the Sheet URL: docs.google.com/spreadsheets/d/<THIS_PART>/edit
var TAB_NAME = 'Google_LSA_Leads';

function doPost(e) {
  try {
    var d = JSON.parse(e.postData.contents);
    var ss = SpreadsheetApp.openById(SHEET_ID);
    var sh = ss.getSheetByName(TAB_NAME) || ss.insertSheet(TAB_NAME);
    // header row if empty
    if (sh.getLastRow() === 0) {
      sh.appendRow(['Timestamp','Name','Phone','Address','Roof Age','Storm','Carrier','Owner','Source','Campaign','Content','fbclid','Status']);
    }
    sh.appendRow([
      new Date(), d.name||'', d.phone||'', d.address||'', d.roof_age||'', d.storm||'',
      d.carrier||'', d.owner||'', d.utm_source||'', d.utm_campaign||'', d.utm_content||'',
      d.fbclid||'', 'NEW — call in 5 min'
    ]);
    return ContentService.createTextOutput(JSON.stringify({ok:true})).setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService.createTextOutput(JSON.stringify({ok:false,error:String(err)})).setMimeType(ContentService.MimeType.JSON);
  }
}

// optional: lets you open the /exec URL in a browser to confirm it's live
function doGet() {
  return ContentService.createTextOutput('Pineapple CPPA endpoint is live.');
}
