# Pineapple Roofing M7 Migration Build

This package contains 33 premium editorial pages:

- 7 core pages
- 13 roofing service pages
- 13 city pages
- 33 matching Elementor HTML-widget blocks
- a migrated-page redirect master and a Redirection-plugin import CSV
- the click-by-click WordPress cleanup guide

## Brand system

- Libre Caslon Display + DM Sans
- Navy `#1A365D`, gold `#FBC02D`, cyan `#00BFFF`, paper `#F7F5EF`
- RCAT `#03-0637`
- IKO Certified
- `972-928-0788`
- Meta Pixel `2545389655696737`
- exact CTA: “Reserve Your Complimentary Professional Photo Audit.”

## Before publishing

1. Replace `PASTE_YOUR_APPS_SCRIPT_OR_FORMSPREE_URL_HERE` with the approved Apps Script `/exec` endpoint in every page or in the global Elementor implementation.
2. Replace `G-XXXXXXX` only after the correct GA4 Measurement ID is confirmed.
3. Replace all marked review and video placeholders with verified Pineapple sources.
4. For Elementor, create a page, set **Page Layout → Elementor Canvas**, drag in one **HTML** widget, and paste the matching file from `elementor-blocks/`. Canvas prevents the theme from adding a second header and footer.
5. If Meta Pixel `2545389655696737` is already installed globally, the block’s guard prevents a second page-level loader. Verify a single PageView with Meta Pixel Helper.
6. Publish the destination page before importing its redirect.
7. Validate FAQ and LocalBusiness schema after WordPress or optimization plugins process the page.

## Redirect deployment

`redirection-plugin-import.csv` uses the Redirection plugin’s supported format: `source,target,regex,http code,type`. Import it at **Tools → Redirection → Import/Export → Import** only after every BUILD destination is published.

The plugin must run on the server that receives requests for `pineapplecontractors.com`. If the old domain remains on a separate Scorpion/host environment, a plugin installed only on `pineappleroofingllc.com` cannot intercept old-domain traffic. In that case, give the same mapping to the old host for server-level 301s, or route the old domain to the WordPress environment before importing.

After import, test representative old URLs with an HTTP checker and confirm one direct `301` hop to the matching new page—never a 302, 404, homepage catch-all, or redirect chain.

The insurance language is intentionally conservative: Pineapple documents conditions and construction scope; the carrier determines coverage; claim approval is not guaranteed; the homeowner is responsible for the deductible.
