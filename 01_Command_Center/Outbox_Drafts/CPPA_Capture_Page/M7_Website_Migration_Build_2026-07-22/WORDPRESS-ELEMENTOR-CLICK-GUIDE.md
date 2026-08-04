# Pineapple Roofing — WordPress + Elementor “Complimentary” Cleanup

Use this on `pineappleroofingllc.com`. Do not change the phone number `972-928-0788`, RCAT license `#03-0637`, fonts, or brand colors. The final button language is:

> Reserve Your Complimentary Professional Photo Audit.

## 0. Make a restore point first

1. Sign in at `https://pineappleroofingllc.com/wp-admin/`.
2. In the left sidebar, open the backup plugin your host/site uses.
3. Create a database backup and confirm it finished before running a database replacement.
4. Leave the backup browser tab open until the live-page check is complete.

## 1. Install Better Search Replace

1. In WP Admin, click **Plugins** in the left sidebar.
2. Click **Add New Plugin**.
3. In the search box at the upper right, type **Better Search Replace**.
4. Find **Better Search Replace** by WP Engine.
5. Click **Install Now**.
6. When the button changes, click **Activate**.
7. In the left sidebar, click **Tools**.
8. Click **Better Search Replace**.

## 2. Run the first replacement as a dry run

1. Stay on **Tools → Better Search Replace → Search/Replace**.
2. In **Search for**, enter exactly: `FREE Quote`
3. In **Replace with**, enter exactly: `Complimentary Quote`
4. In **Select tables**, click the first table, then press `Ctrl+A` on Windows or `Command+A` on Mac while the table list has focus. Confirm every table is highlighted. This includes `wp_posts` and `wp_postmeta`, where Elementor content is normally stored. Your prefix may not be `wp_`.
5. Leave **Replace GUIDs** unchecked.
6. Check **Run as dry run**.
7. Click **Run Search/Replace**.
8. Read the result banner. Record the number of cells that would change. A dry run writes nothing.

## 3. Dry-run the other two replacements

Repeat the same clicks one pair at a time. Keep **Run as dry run** checked.

| Search for | Replace with |
|---|---|
| `Free Estimate` | `Complimentary Estimate` |
| `Get a Free` | `Get a Complimentary` |

Do not run a blanket replacement of the four letters `free`; it can alter unrelated text and URLs. The plugin supports serialized WordPress/Elementor data and lets you preview changes with a dry run, which is why it is safer than editing a raw database export.

## 4. Commit the three replacements

For each pair above:

1. Enter the exact **Search for** and **Replace with** values.
2. Confirm all tables are still selected.
3. Confirm **Replace GUIDs** is unchecked.
4. Uncheck **Run as dry run**.
5. Click **Run Search/Replace**.
6. Wait for the success message before starting the next pair.

## 5. Fix the hero form in Elementor

1. In the left sidebar, click **Pages → All Pages**.
2. Find the page marked **Front Page** or titled **Home**.
3. Hover over it and click **Edit with Elementor**.
4. Wait for the Elementor editor to finish loading.
5. On the canvas, click the heading that currently reads **Get your FREE Quote Today**.
6. In the left panel, stay on the **Content** tab.
7. In the **Title** or **Heading** field, replace the entire heading with: `Reserve Your Complimentary Professional Photo Audit.`
8. On the canvas, click the yellow form submit button that currently reads **Get A FREE Quote**.
9. In the left panel, open the form’s **Content** settings, then open **Buttons** or **Submit Button**. Elementor versions label this field **Button Text**, **Submit Button Text**, or **Text**.
10. Replace the entire button label with: `Reserve Your Complimentary Professional Photo Audit.`
11. Click the arrow beside **Update** only if you want to save a draft first; otherwise click **Update** in the top bar.
12. Click the preview icon, open the live preview in a new tab, and confirm the hero heading and yellow button are correct.

## 6. Fix the global top-navigation button

1. Return to WP Admin.
2. Click **Elementor → Theme Builder**.
3. Click the **Header** card.
4. Find the header assigned to **Entire Site** and click **Edit**.
5. In the Elementor canvas, click the top-navigation quote button.
6. In the left panel under **Content**, replace its **Text** with: `Reserve Your Complimentary Professional Photo Audit.`
7. In the **Link** field, keep the existing destination if it already opens the quote form. If it is blank, set it to `#form`.
8. Click **Update**.
9. If your site does not show **Elementor → Theme Builder**, try **Templates → Theme Builder → Header**. Do not edit the logo, phone, license, or colors.

## 7. Clear generated files and caches

1. In WP Admin, open **Elementor → Tools**.
2. On the **General** tab, click **Clear Files & Data** or **Regenerate CSS & Data**—the label varies by Elementor version.
3. Confirm the action.
4. Clear the cache in the active performance/cache plugin.
5. If Cloudflare is connected, purge the page cache there too.
6. Open the homepage in an incognito window and hard-refresh with `Ctrl+Shift+R` on Windows or `Command+Shift+R` on Mac.

## 8. Final live-site brand check

1. View the homepage on desktop and a phone.
2. Use the browser’s Find command and search for `free` case-insensitively.
3. Confirm the hero heading, yellow button, and top-nav button all use the exact CPPA CTA.
4. Confirm the phone is `972-928-0788` and the license is `#03-0637`.
5. Confirm no element changed to green. Keep navy `#1A365D`, gold `#FBC02D`, cyan `#00BFFF`, and paper `#F7F5EF`.
6. Submit one test lead and verify it reaches the CRM before announcing completion.

References: [Better Search Replace](https://wordpress.org/plugins/better-search-replace/), [Elementor header editing](https://elementor.com/help/header-site-part/).

