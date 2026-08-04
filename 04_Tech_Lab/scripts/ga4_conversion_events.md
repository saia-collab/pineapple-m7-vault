---
type: technical_seo
title: GA4 Conversion Events — phone-click + CPPA button (goes in Site Kit / header plugin)
status: ready — paste into a site-wide header/footer plugin (NOT per page)
last_updated: 2026-07-17
important: Your site ALREADY has Site Kit (GA4 base tag) + PixelYourSite (Meta Pixel). Do NOT add a second base gtag — that double-counts every visit. This snippet only adds the two CONVERSIONS Site Kit doesn't auto-track.
---

# 📊 GA4 conversion tracking — the two events that matter

Site Kit already records pageviews. What it does NOT know is when someone **calls** or **clicks the CPPA button** — the actions that mean money. This snippet reports those to GA4 as events you can then mark as "Key events" (conversions) in the GA4 UI.

**Where it goes:** one site-wide header/footer plugin (you likely have one; if not, "WPCode" or Site Kit's snippet area). Paste once — it covers every page.

```html
<script>
document.addEventListener('click', function (e) {
  var a = e.target.closest('a');
  if (!a) return;
  // Phone-call clicks (any tel: link)
  if (a.href && a.href.indexOf('tel:') === 0 && window.gtag) {
    gtag('event', 'phone_call_click', { event_category: 'lead', event_label: a.href });
  }
  // CPPA button clicks (matches links/buttons whose text mentions CPPA or Audit)
  if (window.gtag && /CPPA|Photo Audit|Complimentary/i.test(a.textContent || '')) {
    gtag('event', 'cppa_request_click', { event_category: 'lead', event_label: a.href || 'cppa' });
  }
});
</script>
```

**Then, one-time in GA4 (analytics.google.com):** Admin → Events → mark `phone_call_click` and `cppa_request_click` as **Key events**. Now they count as conversions and show ROI per page/city.

> Why not push this live for you? It's site-wide JavaScript that belongs in the theme header, not in a single page's body. Injecting it site-wide safely = one paste into your header plugin. 2 minutes, and you avoid the double-tracking bug a second base tag would cause.

<!-- M7-FIREWALL-EXEMPT: technical-seo -->
