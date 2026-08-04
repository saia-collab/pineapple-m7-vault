# -*- coding: utf-8 -*-
"""Generate 7 HyperFrames <template> sub-composition fragments. Portrait 1080x1920."""
import os
W, H = 1080, 1920
NAVY, GOLD, CYAN, PAPER = "#1A365D", "#FBC02D", "#00BFFF", "#F7F5EF"
FONTS = "@import url('https://fonts.googleapis.com/css2?family=Libre+Caslon+Display&family=DM+Sans:wght@400;500;700&display=swap');"
GSAP = '<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>'
OUT = "compositions/frames"
os.makedirs(OUT, exist_ok=True)

def frame(fid, dur, bg, body_html, tl_js, extra_css=""):
    return f'''<template>
<style>
{FONTS}
#root{{position:relative;width:{W}px;height:{H}px;overflow:hidden;font-family:"DM Sans",system-ui,sans-serif;}}
#{fid}-bg{{position:absolute;inset:0;background:{bg};}}
.{fid}-wrap{{position:absolute;inset:0;display:flex;flex-direction:column;justify-content:center;align-items:center;padding:0 96px;text-align:center;box-sizing:border-box;}}
.{fid}-serif{{font-family:"Libre Caslon Display",Georgia,serif;font-weight:400;line-height:.92;letter-spacing:-.02em;}}
.{fid}-eyebrow{{font-family:"DM Sans",sans-serif;font-weight:700;font-size:26px;letter-spacing:.28em;text-transform:uppercase;}}
{extra_css}
</style>
<div id="root" data-composition-id="{fid}" data-start="0" data-width="{W}" data-height="{H}" data-duration="{dur}">
  <div id="{fid}-bg" class="clip" data-start="0" data-duration="{dur}" data-track-index="0"></div>
  <div class="{fid}-wrap clip" data-start="0" data-duration="{dur}" data-track-index="1">
{body_html}
  </div>
</div>
{GSAP}
<script>
window.__timelines = window.__timelines || {{}};
(function(){{
  const tl = gsap.timeline({{paused:true}});
{tl_js}
  window.__timelines["{fid}"] = tl;
}})();
</script>
</template>'''

F = []
F.append(("frame-01-hook", 4, NAVY, f'''
    <div class="frame-01-hook-serif" id="f1-a" style="color:{PAPER};font-size:150px;">YOUR ROOF<br>LOOKS FINE.</div>
    <div class="frame-01-hook-serif" id="f1-b" style="color:{GOLD};font-size:150px;font-style:italic;margin-top:34px;">Prove it.</div>
''', '''  tl.fromTo("#f1-a",{opacity:0,y:60},{opacity:1,y:0,duration:.7,ease:"power4.out"},0.15);
  tl.fromTo("#f1-b",{opacity:0,y:40},{opacity:1,y:0,duration:.6,ease:"power4.out"},2.0);''', ""))

F.append(("frame-02-bruise", 9, NAVY, f'''
    <div class="frame-02-bruise-eyebrow" id="f2-eb" style="color:{CYAN};margin-bottom:40px;">Mat Fracture</div>
    <div class="frame-02-bruise-serif" id="f2-h1" style="color:{PAPER};font-size:120px;">Hail doesn't<br>break a shingle.</div>
    <div class="frame-02-bruise-serif" id="f2-h2" style="color:{GOLD};font-size:132px;font-style:italic;margin-top:28px;">It bruises it.</div>
    <div id="f2-bar" style="width:520px;height:70px;background:rgba(247,245,239,.14);border-radius:8px;margin-top:64px;position:relative;overflow:hidden;">
      <div id="f2-crack" style="position:absolute;top:50%;left:6%;width:88%;height:3px;background:{CYAN};transform-origin:left center;"></div>
    </div>
    <div id="f2-sub" style="color:rgba(247,245,239,.7);font-size:30px;margin-top:34px;max-width:640px;">Fracturing the layer that actually keeps water out.</div>
''', '''  tl.fromTo("#f2-eb",{opacity:0,y:24},{opacity:1,y:0,duration:.5},0.2);
  tl.fromTo("#f2-h1",{opacity:0,y:44},{opacity:1,y:0,duration:.6,ease:"power3.out"},0.9);
  tl.fromTo("#f2-h2",{opacity:0,y:34},{opacity:1,y:0,duration:.6,ease:"power3.out"},2.6);
  tl.fromTo("#f2-bar",{opacity:0,scale:.9},{opacity:1,scale:1,duration:.6,ease:"power2.out"},4.2);
  tl.fromTo("#f2-crack",{scaleX:0},{scaleX:1,duration:1.1,ease:"power2.inOut"},4.9);
  tl.fromTo("#f2-sub",{opacity:0,y:24},{opacity:1,y:0,duration:.6},6.3);''', ""))

photos = "".join(f'<div id="f3-p{i}" class="f3-photo" style="background:rgba(247,245,239,.10);border:1px solid rgba(0,191,255,.4);"></div>' for i in range(1,5))
F.append(("frame-03-goup", 12, NAVY, f'''
    <div class="frame-03-goup-serif" id="f3-h" style="color:{PAPER};font-size:150px;">So we<br>go up.</div>
    <div class="frame-03-goup-eyebrow" id="f3-sub" style="color:{CYAN};margin-top:44px;">Drone &amp; Ground &middot; Slope by Slope</div>
    <div id="f3-grid" style="display:grid;grid-template-columns:1fr 1fr;gap:26px;margin-top:70px;width:560px;">{photos}</div>
    <div id="f3-cap" style="color:rgba(247,245,239,.7);font-size:30px;margin-top:44px;">Every impact photographed.</div>
''', '''  tl.fromTo("#f3-h",{opacity:0,y:60},{opacity:1,y:0,duration:.7,ease:"power4.out"},0.2);
  tl.fromTo("#f3-sub",{opacity:0,y:24},{opacity:1,y:0,duration:.5},1.8);
  tl.fromTo(".f3-photo",{opacity:0,scale:.88},{opacity:1,scale:1,duration:.5,stagger:.35,ease:"power2.out"},3.2);
  tl.fromTo("#f3-cap",{opacity:0,y:24},{opacity:1,y:0,duration:.6},7.8);''',
    ".f3-photo{aspect-ratio:16/10;border-radius:6px;}"))

rows = [("Hail","impact map"),("Wind","lifted seals"),("Flashing","penetration points"),("Gutters","storm-date proof")]
rows_html = "".join(f'''<div id="f4-r{i}" class="f4-row" style="border-bottom:1px solid rgba(247,245,239,.18);">
  <span style="color:{GOLD};font-size:34px;">&#10003;</span>
  <span class="frame-04-file-serif" style="color:{PAPER};font-size:56px;">{a}</span>
  <span style="color:rgba(247,245,239,.55);font-size:28px;">{b}</span></div>''' for i,(a,b) in enumerate(rows,1))
F.append(("frame-04-file", 12, NAVY, f'''
    <div class="frame-04-file-eyebrow" id="f4-eb" style="color:{CYAN};margin-bottom:36px;">The Evidence File</div>
    <div class="frame-04-file-serif" id="f4-h" style="color:{PAPER};font-size:104px;">Then we build<br>the file.</div>
    <div id="f4-list" style="margin-top:56px;width:640px;display:flex;flex-direction:column;">{rows_html}</div>
''', '''  tl.fromTo("#f4-eb",{opacity:0,y:24},{opacity:1,y:0,duration:.5},0.2);
  tl.fromTo("#f4-h",{opacity:0,y:44},{opacity:1,y:0,duration:.6,ease:"power3.out"},0.9);
  tl.fromTo(".f4-row",{opacity:0,x:-40},{opacity:1,x:0,duration:.55,stagger:.9,ease:"power2.out"},2.8);''',
    ".f4-row{display:flex;align-items:center;gap:22px;padding:20px 0;}"))

F.append(("frame-05-keep", 10, NAVY, f'''
    <div id="f5-seal" style="width:200px;height:200px;border:2px solid {GOLD};border-radius:50%;display:flex;align-items:center;justify-content:center;color:{GOLD};font-family:'DM Sans';font-weight:700;font-size:26px;letter-spacing:.14em;text-transform:uppercase;line-height:1.3;margin-bottom:56px;">Keep the<br>Report</div>
    <div class="frame-05-keep-serif" id="f5-h" style="color:{PAPER};font-size:118px;">You keep<br>the file.</div>
    <div id="f5-sub" style="color:rgba(247,245,239,.72);font-size:34px;margin-top:40px;">Even if you never hire us.</div>
    <div class="frame-05-keep-serif" id="f5-q" style="color:{GOLD};font-size:76px;font-style:italic;margin-top:56px;">Evidence beats opinions.</div>
''', '''  tl.fromTo("#f5-seal",{opacity:0,scale:.7},{opacity:1,scale:1,duration:.7,ease:"back.out(1.6)"},0.3);
  tl.fromTo("#f5-h",{opacity:0,y:44},{opacity:1,y:0,duration:.6,ease:"power3.out"},1.4);
  tl.fromTo("#f5-sub",{opacity:0,y:24},{opacity:1,y:0,duration:.6},3.2);
  tl.fromTo("#f5-q",{opacity:0,y:34},{opacity:1,y:0,duration:.7,ease:"power3.out"},5.4);''', ""))

creds = [("IKO Certified","Expert Shingle Installer"),("RCAT #03-0637","Texas licensed &amp; verified"),("Since 2005","Family-owned, North Texas")]
creds_html = "".join(f'''<div id="f6-c{i}" class="f6-cred">
  <div class="frame-06-cred-serif" style="color:{PAPER};font-size:78px;">{a}</div>
  <div style="color:{CYAN};font-size:28px;letter-spacing:.06em;margin-top:8px;">{b}</div></div>''' for i,(a,b) in enumerate(creds,1))
F.append(("frame-06-cred", 8, NAVY, f'''
    <div class="frame-06-cred-eyebrow" id="f6-eb" style="color:{GOLD};margin-bottom:56px;">The Pineapple Standard</div>
    <div id="f6-stack" style="display:flex;flex-direction:column;gap:52px;">{creds_html}</div>
''', '''  tl.fromTo("#f6-eb",{opacity:0,y:24},{opacity:1,y:0,duration:.5},0.2);
  tl.fromTo(".f6-cred",{opacity:0,y:40},{opacity:1,y:0,duration:.6,stagger:1.2,ease:"power3.out"},1.0);''', ""))

F.append(("frame-07-cta", 5, GOLD, f'''
    <div class="frame-07-cta-serif" id="f7-h" style="color:{NAVY};font-size:118px;">Proof before<br>opinions.</div>
    <div id="f7-phone" style="color:{NAVY};font-family:'DM Sans';font-weight:700;font-size:88px;letter-spacing:.02em;margin-top:48px;">(972) 928-0788</div>
    <div id="f7-sub" class="frame-07-cta-eyebrow" style="color:{NAVY};opacity:.72;margin-top:26px;">Complimentary Professional Photo Audit</div>
''', '''  tl.fromTo("#f7-h",{opacity:0,y:50},{opacity:1,y:0,duration:.7,ease:"power4.out"},0.2);
  tl.fromTo("#f7-phone",{opacity:0,y:34},{opacity:1,y:0,duration:.6,ease:"power3.out"},1.4);
  tl.fromTo("#f7-sub",{opacity:0},{opacity:.72,duration:.5},2.3);
  tl.fromTo("#f7-phone",{scale:1},{scale:1.06,duration:.28,ease:"power1.inOut"},3.1);
  tl.fromTo("#f7-phone",{scale:1.06},{scale:1,duration:.28,ease:"power1.inOut"},3.4);''', ""))

for fid, dur, bg, body, tl_js, css in F:
    open(f"{OUT}/{fid}.html","w",encoding="utf-8").write(frame(fid,dur,bg,body,tl_js,css))
    print("wrote", fid)
print("done", len(F), "frames")
