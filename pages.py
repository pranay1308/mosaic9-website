import os
from build import page, ROOT

def _icon(glyph, accent=""):
    """Wraps a glyph in a consistent duotone 'badge' style: soft backdrop +
    crisp currentColor glyph + a small brand-accent highlight for polish."""
    return (
        '<svg viewBox="0 0 48 48" fill="none">'
        '<rect x="2.5" y="2.5" width="43" height="43" rx="13" fill="currentColor" opacity="0.1"/>'
        '<g stroke="currentColor" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none">'
        f'{glyph}'
        '</g>'
        f'{accent}'
        '</svg>'
    )

ICONS = {
 # Strategy — target + compass arrow (aim, direction, planning)
 "strategy": _icon(
    '<circle cx="21" cy="27" r="12.5"/><circle cx="21" cy="27" r="6.5"/><path d="M36 8 27 17"/><path d="M36 8h-6.5m6.5 0v6.5"/>',
    '<circle cx="21" cy="27" r="2" fill="var(--accent)"/>'
 ),
 # Performance — ascending trend line breaking out of an axis
 "performance": _icon(
    '<path d="M9 9v28h28"/><path d="m13 27 6.5-7 5 5 9.5-11"/>',
    '<path d="M28 12h6v6" stroke="var(--accent)" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
 ),
 # Brand — badge / seal with ribbon tails
 "brand": _icon(
    '<circle cx="24" cy="18" r="10"/><path d="m18 26-3 14 9-5 9 5-3-14"/>',
    '<path d="m24 12.5 1.7 3.5 3.8.5-2.8 2.7.7 3.8-3.4-1.8-3.4 1.8.7-3.8-2.8-2.7 3.8-.5z" fill="var(--accent)"/>'
 ),
 # Social — overlapping chat bubbles
 "social": _icon(
    '<path d="M8 15a7 7 0 0 1 7-7h6a7 7 0 0 1 7 7v3a7 7 0 0 1-7 7h-3.5L12 23v-4.2A7 7 0 0 1 8 13.5z"/>',
    '<circle cx="35" cy="14" r="5.5" fill="var(--accent)" opacity="0.85"/>'
 ),
 # Intelligence (AI) — circuit chip
 "ai": _icon(
    '<rect x="15" y="15" width="18" height="18" rx="4"/>'
    '<path d="M20 15v-5m8 5v-5m-8 28v5m8-5v5M15 20H10m5 8H10m28-8h-5m5 8h-5"/>',
    '<circle cx="20" cy="23" r="1.7" fill="var(--accent)"/><circle cx="28" cy="23" r="1.7" fill="var(--accent)"/><circle cx="24" cy="28" r="1.7" fill="var(--accent)"/>'
 ),
 # SEO — magnifying glass over an upward signal
 "seo": _icon(
    '<circle cx="20" cy="20" r="12"/><path d="m36 36-7-7"/><path d="m14 23 4.5-5.5 4 3.5 6.5-7.5"/>',
    ''
 ),
 # Web / Tech — browser window with a gear
 "web": _icon(
    '<rect x="6" y="9" width="30" height="25" rx="3"/><path d="M6 16h30"/>'
    '<circle cx="27" cy="26" r="4.2"/><path d="M27 19.5v2.3m0 8.4v2.3m7.5-6.5H32m-10 0h-2.5"/>',
    ''
 ),
 # Messaging / WhatsApp — chat bubble with confirmation check
 "whatsapp": _icon(
    '<path d="M9 15.5a9 9 0 0 1 9-9h5a9 9 0 0 1 9 9v2.5a9 9 0 0 1-9 9h-4l-6.5 5v-5.6A9 9 0 0 1 9 18z"/>',
    '<path d="m17.5 19.5 3.8 3.8 7.7-7.8" stroke="var(--accent)" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
 ),
 # Lead generation — funnel with a confirmation tick
 "leadgen": _icon(
    '<path d="M8 10h32l-11.5 14.5v9L19.5 39v-14.5z"/>',
    '<path d="m29 29 3 3 6.5-6.5" stroke="var(--accent)" stroke-width="2.8" stroke-linecap="round" stroke-linejoin="round" fill="none"/>'
 ),
 # Data — layered bar chart on an axis
 "data": _icon(
    '<path d="M9 40V8"/><rect x="14" y="27" width="6" height="13"/><rect x="23" y="19" width="6" height="21"/><rect x="32" y="12" width="6" height="28"/>',
    ''
 ),
 # Always-on performance engine — gear
 "engine": _icon(
    '<circle cx="24" cy="24" r="6.5"/>'
    '<path d="M24 9v4.4m0 21.2V39m15-15h-4.4M13.4 24H9m22.1-10.6-3.1 3.1M19 32.5l-3.1 3.1m18.2-3.1-3.1-3.1M19 15.5l-3.1-3.1"/>',
    ''
 ),
 # Custom dashboard — asymmetric grid
 "dashboard": _icon(
    '<rect x="7" y="7" width="16" height="19" rx="2.5"/><rect x="27" y="7" width="14" height="9" rx="2.5"/>'
    '<rect x="27" y="20" width="14" height="19" rx="2.5"/><rect x="7" y="30" width="16" height="9" rx="2.5"/>',
    ''
 ),
 # Human judgement — person
 "human": _icon(
    '<circle cx="24" cy="16.5" r="8"/><path d="M9 41c0-8.8 6.7-13.5 15-13.5S39 32.2 39 41"/>',
    '<circle cx="24" cy="16.5" r="8" stroke="var(--accent)" stroke-width="0" fill="none"/>'
 ),
}

def _art(shapes, vb="0 0 64 64"):
    """Bigger, multi-layer 'scene' style illustration for the homepage
    mosaic tiles — more detail/depth than the small service-card badges."""
    return f'<svg viewBox="{vb}" fill="none">{shapes}</svg>'

TILE_ART = {
 # Strategy and Consulting — summit path with a flag: the roadmap metaphor
 "strategy": _art(
    '<path d="M6 50 22 26l8 10 10-16 18 30z" fill="currentColor" opacity="0.14"/>'
    '<path d="M6 50 22 26l8 10 10-16 18 30" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="10" cy="50" r="2.6" fill="currentColor"/>'
    '<path d="M40 20V8" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>'
    '<path d="M40 8h11l-4 4.5 4 4.5H40" fill="var(--accent)" stroke="var(--accent)" stroke-width="1" stroke-linejoin="round"/>'
    '<path d="M14 46q4-3 8 0t8 0t8 0t8 0" stroke="currentColor" stroke-width="2" stroke-dasharray="1 5" stroke-linecap="round"/>'
 ),
 # Paid Media — rocket launch off a rising bar chart
 "performance": _art(
    '<rect x="8" y="46" width="9" height="8" rx="1.5" fill="currentColor" opacity="0.5"/>'
    '<rect x="20" y="38" width="9" height="16" rx="1.5" fill="currentColor" opacity="0.7"/>'
    '<rect x="32" y="28" width="9" height="26" rx="1.5" fill="currentColor" opacity="0.9"/>'
    '<path d="M46 10c6 3 9 9 9 16 0 5-2 9-2 9l-9-2s-1-6 0-11c1-5 2-9 2-12z" fill="currentColor"/>'
    '<path d="M44 33s-6 1-8 6l5 3c2-3 3-9 3-9z" fill="currentColor" opacity="0.75"/>'
    '<circle cx="49" cy="20" r="3" fill="var(--mist)"/>'
    '<path d="M45 37q-2 6-1 11" stroke="var(--accent)" stroke-width="3" stroke-linecap="round"/>'
    '<path d="M50 37q1 6 0 11" stroke="var(--accent)" stroke-width="3" stroke-linecap="round" opacity="0.7"/>'
 ),
 # Brand & Identity — medallion seal with ribbon tails and sparkle accents
 "brand": _art(
    '<circle cx="30" cy="24" r="15" fill="currentColor" opacity="0.14"/>'
    '<circle cx="30" cy="24" r="15" stroke="currentColor" stroke-width="3"/>'
    '<path d="m30 15 3 6.2 6.8.9-5 4.7 1.2 6.7L30 30l-6 3.5 1.2-6.7-5-4.7 6.8-.9z" fill="var(--accent)"/>'
    '<path d="M22 36 17 54l13-6.5L43 54l-5-18" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>'
    '<path d="M48 10l2 4 4 1-4 1-2 4-2-4-4-1 4-1z" fill="var(--accent)" opacity="0.9"/>'
 ),
 # Content & Social — phone feed with a floating like + comment
 "social": _art(
    '<rect x="16" y="6" width="26" height="44" rx="5" fill="currentColor" opacity="0.12"/>'
    '<rect x="16" y="6" width="26" height="44" rx="5" stroke="currentColor" stroke-width="3"/>'
    '<circle cx="29" cy="17" r="3.4" stroke="currentColor" stroke-width="2.4"/>'
    '<path d="M22 27h14M22 33h9" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
    '<path d="M40 34a7 7 0 0 1 7-7h4a7 7 0 0 1 7 7v2a7 7 0 0 1-7 7h-2l-4 3v-3a7 7 0 0 1-5-7z" fill="var(--accent)" opacity="0.92"/>'
    '<path d="m9 42 3.6-1 1-3.6 1 3.6 3.6 1-3.6 1-1 3.6-1-3.6z" fill="var(--accent)"/>'
 ),
 # Human + AI Workflows — human profile handing off to a circuit chip
 "ai": _art(
    '<path d="M10 50c0-8 5-13 11-13s11 5 11 13" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>'
    '<circle cx="21" cy="24" r="8" fill="currentColor" opacity="0.15"/>'
    '<circle cx="21" cy="24" r="8" stroke="currentColor" stroke-width="3"/>'
    '<rect x="36" y="24" width="20" height="20" rx="4" fill="currentColor" opacity="0.14"/>'
    '<rect x="36" y="24" width="20" height="20" rx="4" stroke="currentColor" stroke-width="3"/>'
    '<path d="M42 24v-5m8 5v-5m-8 25v5m8-5v5M36 32h-4m4 8h-4m24-8h4m-4 8h4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'
    '<circle cx="42" cy="34" r="1.8" fill="var(--accent)"/><circle cx="50" cy="34" r="1.8" fill="var(--accent)"/>'
    '<path d="M29 30q4 2 7 3" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="1 4"/>'
 ),
 # SEO / AEO / GEO — search bar + magnifier + generative answer spark
 "seo": _art(
    '<rect x="6" y="14" width="36" height="10" rx="5" fill="currentColor" opacity="0.13"/>'
    '<rect x="6" y="14" width="36" height="10" rx="5" stroke="currentColor" stroke-width="2.6"/>'
    '<circle cx="14" cy="19" r="1.8" fill="currentColor"/>'
    '<circle cx="27" cy="38" r="10" fill="currentColor" opacity="0.12"/>'
    '<circle cx="27" cy="38" r="10" stroke="currentColor" stroke-width="3"/>'
    '<path d="m34.5 45.5 7 7" stroke="currentColor" stroke-width="3.2" stroke-linecap="round"/>'
    '<path d="M50 10l2.2 4.6 4.6 1.4-4.6 1.4L50 22l-2.2-4.6-4.6-1.4 4.6-1.4z" fill="var(--accent)"/>'
    '<path d="m22 39 3-4 3 2.5 5-6" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
 ),
 # Web & Product — laptop mockup with layout blocks + cursor
 "web": _art(
    '<rect x="8" y="12" width="40" height="27" rx="3" fill="currentColor" opacity="0.12"/>'
    '<rect x="8" y="12" width="40" height="27" rx="3" stroke="currentColor" stroke-width="3"/>'
    '<path d="M8 19h40" stroke="currentColor" stroke-width="2.2"/>'
    '<rect x="13" y="24" width="14" height="9" rx="1.5" fill="currentColor" opacity="0.5"/>'
    '<path d="M31 24h13M31 29h9" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'
    '<path d="M2 45q26 8 60 0l-4 6H6z" fill="currentColor" opacity="0.9"/>'
    '<path d="M44 34 54 44l-4 1 2 5-3 1.3-2-5-3.5 2.7z" fill="var(--accent)"/>'
 ),
 # Messaging & CRM — chat bubble with a contact / CRM card
 "whatsapp": _art(
    '<path d="M8 20a12 12 0 0 1 12-12h6a12 12 0 0 1 12 12v3a12 12 0 0 1-12 12h-5l-8.5 6.5v-7A12 12 0 0 1 8 23z" fill="currentColor" opacity="0.13"/>'
    '<path d="M8 20a12 12 0 0 1 12-12h6a12 12 0 0 1 12 12v3a12 12 0 0 1-12 12h-5l-8.5 6.5v-7A12 12 0 0 1 8 23z" stroke="currentColor" stroke-width="3" stroke-linejoin="round"/>'
    '<path d="m17 20 4.2 4.2L30 15.4" stroke="var(--accent)" stroke-width="3.2" stroke-linecap="round" stroke-linejoin="round"/>'
    '<rect x="34" y="36" width="22" height="16" rx="3" fill="currentColor" opacity="0.14"/>'
    '<rect x="34" y="36" width="22" height="16" rx="3" stroke="currentColor" stroke-width="2.6"/>'
    '<circle cx="40" cy="44" r="2.6" fill="currentColor"/>'
    '<path d="M46 41h7m-7 4.5h5" stroke="currentColor" stroke-width="2" stroke-linecap="round"/>'
 ),
 # Data & Martech — dashboard monitor with chart + automation gear
 "data": _art(
    '<rect x="6" y="10" width="38" height="26" rx="3" fill="currentColor" opacity="0.13"/>'
    '<rect x="6" y="10" width="38" height="26" rx="3" stroke="currentColor" stroke-width="3"/>'
    '<path d="M18 42h20m-10 0v-6" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
    '<rect x="11" y="27" width="5" height="6" fill="currentColor" opacity="0.6"/>'
    '<rect x="19" y="21" width="5" height="12" fill="currentColor" opacity="0.8"/>'
    '<rect x="27" y="16" width="5" height="17" fill="currentColor"/>'
    '<path d="M12 20 20 14l6 4 8-6" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/>'
    '<circle cx="50" cy="46" r="7" fill="currentColor" opacity="0.14"/>'
    '<circle cx="50" cy="46" r="3.4" stroke="currentColor" stroke-width="2.2"/>'
    '<path d="M50 39v2.4m0 9.2V53m7-7h-2.4m-9.2 0H43m10.5-5.3-1.7 1.7M47.2 51l-1.7 1.7m9-1.7-1.7-1.7M47.2 41l-1.7-1.7" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/>'
 ),
}

MOSAIC_TILES = [
  ("strategy","Strategy and Consulting"), ("performance","Paid Media"), ("brand","Brand & Identity"),
  ("social","Content & Social"), ("ai","Human + AI Workflows"), ("seo","SEO / AEO / GEO"),
  ("web","Web & Product"), ("whatsapp","Messaging & CRM"), ("data","Data & Martech"),
]

def tiles_svg():
    out = []
    for key, label in MOSAIC_TILES:
        out.append(
            f'<div class="tile" title="{label}">'
            f'<div class="tile-inner">'
            f'<div class="tile-face tile-front">{TILE_ART[key]}</div>'
            f'<div class="tile-face tile-back"><span>{label}</span></div>'
            f'</div>'
            f'</div>'
        )
    return "\n        ".join(out)

# Real client logos (cropped from client-supplied brand sheet), with a plain-text
# fallback for any client we don't have artwork for yet.
CLIENT_LOGOS = [
    ("Yatri Railways", "assets/clients/yatri-railways.png"),
    ("CDP India", "assets/clients/cdp-india.png"),
    ("Inha Wellness", "assets/clients/inha-wellness.png"),
    ("GlobalLinker", "assets/clients/globallinker.png"),
    ("Space AI", "assets/clients/space-ai.png"),
    ("I'm Wholesome", "assets/clients/im-wholesome.png"),
    ("SKM Steels", "assets/clients/skm-steels.png"),
    ("Dials Luggage", "assets/clients/dials-luggage.png"),
]
CLIENTS_TEXT_ONLY = []

def logo_strip(base=""):
    chips = []
    for name, src in CLIENT_LOGOS:
        chips.append(f'<div class="logo-chip logo-chip-img"><img src="{base}{src}" alt="{name} logo" loading="lazy"></div>')
    for c in CLIENTS_TEXT_ONLY:
        chips.append(f'<div class="logo-chip"><span class="dot"></span>{c}</div>')
    return "\n      ".join(chips)

# ----------------------------------------------------------------------------
# HOMEPAGE
# ----------------------------------------------------------------------------
home_body = f"""
<section class="hero">
  <div class="hero-inner">
    <div>
      <p class="eyebrow on-dark">Full-Service Marketing Ecosystem &middot; Mumbai</p>
      <h1>Nine disciplines.<br>One connected <em>pattern</em>.</h1>
      <p class="lede">Mosaic9 brings strategy, brand, performance, and technology together under one roof &mdash; so every campaign compounds instead of competing with itself.</p>
      <div class="hero-ctas">
        <a class="btn btn-on-dark" href="contact.html">Request a Free Marketing Audit</a>
        <a class="btn btn-outline-on-dark" href="why-mosaic9.html">Why Mosaic9 &rarr;</a>
      </div>
    </div>
    <div class="mosaic-visual" aria-hidden="true">
      <div class="tiles">
        {tiles_svg()}
      </div>
    </div>
  </div>
</section>

<section class="bg-paper" style="padding-top:56px; padding-bottom:56px;">
  <div class="container">
    <p class="eyebrow">Brands we've grown</p>
    <div class="logo-strip">
      {logo_strip()}
    </div>
  </div>
</section>

<section class="bg-mist">
  <div class="container name-story">
    <div>
      <p class="eyebrow">Where the name comes from</p>
      <h2>Why "Mosaic9"?</h2>
      <p>A mosaic is never one material. It's dozens of individually unremarkable tiles &mdash; different colours, different textures, cut at different angles &mdash; set deliberately so that, together, they resolve into a single image with more depth than any one tile could carry alone.</p>
      <p>That's exactly the problem we saw in modern marketing. Brands were hiring a strategy firm here, a performance agency there, a design freelancer somewhere else &mdash; individually competent tiles with no one setting the pattern. The picture never quite resolved.</p>
      <p>We counted the disciplines it actually takes to build a brand properly in 2026: strategy, brand and identity, content and social, SEO, paid performance, web and product, messaging and CRM, data and martech, and the intelligence layer &mdash; human judgement plus AI &mdash; that ties it all together. Nine tiles. One mosaic. One ecosystem, laying them down as a single pattern instead of nine separate invoices.</p>
      <p><strong>Mosaic9</strong> is that pattern, and the name is a daily reminder that no single discipline wins alone.</p>
    </div>
    <div class="tile-legend" aria-hidden="true">
      <div class="cell">{TILE_ART['strategy']}<strong>Strategy and Consulting</strong></div>
      <div class="cell">{TILE_ART['brand']}<strong>Brand &amp; Identity</strong></div>
      <div class="cell">{TILE_ART['social']}<strong>Content &amp; Social</strong></div>
      <div class="cell">{TILE_ART['seo']}<strong>SEO / AEO / GEO</strong></div>
      <div class="cell">{TILE_ART['ai']}<strong>Human + AI Workflows</strong></div>
      <div class="cell">{TILE_ART['performance']}<strong>Paid Media</strong></div>
      <div class="cell">{TILE_ART['web']}<strong>Web &amp; Product</strong></div>
      <div class="cell">{TILE_ART['whatsapp']}<strong>Messaging &amp; CRM</strong></div>
      <div class="cell">{TILE_ART['data']}<strong>Data &amp; Martech</strong></div>
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow" style="justify-content:center;">What we do</p>
      <h2>Every capability a brand needs, under one roof</h2>
      <p class="lede" style="margin:0 auto;">From first strategy session to the dashboard that proves it worked.</p>
    </div>
    <div class="grid grid-4">
      <div class="card">
        <div class="card-icon">{ICONS['performance']}</div>
        <h3>Performance Marketing</h3>
        <p>Google, Meta, LinkedIn, YouTube and programmatic, built to convert and scale.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS['brand']}</div>
        <h3>Brand &amp; Creative</h3>
        <p>Identity systems, content, and campaigns that make a brand recognisable.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS['web']}</div>
        <h3>Web &amp; Martech</h3>
        <p>Conversion-focused websites, CRM, and the tracking stack behind them.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS['ai']}</div>
        <h3>Strategy &amp; Consulting</h3>
        <p>GTM plans, marketing audits, and fractional CMO leadership.</p>
      </div>
    </div>
    <p class="text-center" style="margin-top:32px;"><a class="btn btn-ghost" href="services.html">See the full service list &rarr;</a></p>
  </div>
</section>

<section class="bg-deep">
  <div class="container">
    <div class="stat-strip">
      <div class="stat"><div class="num">80+</div><div class="label">Brands served</div></div>
      <div class="stat"><div class="num">6+</div><div class="label">Industry verticals</div></div>
      <div class="stat"><div class="num">360&deg;</div><div class="label">Marketing coverage</div></div>
      <div class="stat"><div class="num">1</div><div class="label">Unified partner</div></div>
    </div>
  </div>
</section>

<section class="bg-mist">
  <div class="container">
    <div class="grid grid-2" style="align-items:center; gap:56px;">
      <div>
        <p class="eyebrow">Why Mosaic9</p>
        <h2>Human judgement. AI precision. One decision layer.</h2>
        <p class="lede">We don't sell "AI-powered marketing" as a buzzword. Every account runs on a data-backed decision system where AI handles scale and pattern-spotting, and senior strategists handle judgement, taste, and accountability.</p>
        <a class="btn btn-primary" href="why-mosaic9.html">Explore what makes us different</a>
      </div>
      <div class="grid grid-2">
        <div class="card"><div class="card-icon">{ICONS['ai']}</div><h3>AI Workflows</h3><p>Automated research, creative variants, and audience modelling at machine speed.</p></div>
        <div class="card"><div class="card-icon">{ICONS['engine']}</div><h3>Performance Engines</h3><p>Always-on optimisation loops instead of monthly guesswork.</p></div>
        <div class="card"><div class="card-icon">{ICONS['dashboard']}</div><h3>Live Dashboards</h3><p>Custom, data-backed reporting built around your KPIs.</p></div>
        <div class="card"><div class="card-icon">{ICONS['human']}</div><h3>Senior Judgement</h3><p>Every account led by a strategist, never a junior-only team.</p></div>
      </div>
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="cta-band">
      <p class="eyebrow on-dark" style="justify-content:center;">Let's build something great together</p>
      <h2>Ready to scale your brand?</h2>
      <p>Request a free marketing audit or drop us a brief. We'll come back with clarity, ideas, and a plan.</p>
      <div class="cta-actions">
        <a class="btn btn-on-dark" href="contact.html">Request a Free Audit</a>
        <a class="btn btn-outline-on-dark" href="https://wa.me/919930331126" target="_blank" rel="noopener">Message us on WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Mosaic9",
  "url": "https://mosaic9.com",
  "logo": "https://mosaic9.com/assets/logo.png",
  "description": "Full-service digital marketing ecosystem in Mumbai combining strategy, brand, performance and technology into one connected system.",
  "email": "pranay@mosaic9.com",
  "telephone": "+91-9930331126",
  "address": {{
    "@type": "PostalAddress",
    "addressLocality": "Mumbai",
    "addressRegion": "Maharashtra",
    "addressCountry": "IN"
  }},
  "sameAs": [
    "https://www.linkedin.com/company/mosaic9-mediatech"
  ]
}}
</script>
"""

page(
    "index.html", "index.html",
    "Mosaic9 | Full-Service Marketing Ecosystem in Mumbai",
    "Mosaic9 is a full-service marketing ecosystem combining strategy, brand, performance and AI-backed technology into one connected system for brands that mean business.",
    home_body,
)
print("Homepage generated")

# ----------------------------------------------------------------------------
# SERVICES
# ----------------------------------------------------------------------------
def svc_card(icon, tag, title, desc):
    return f"""<div class="card">
        <div class="tile-tag">{tag}</div>
        <div class="card-icon">{ICONS[icon]}</div>
        <h3>{title}</h3>
        <p>{desc}</p>
      </div>"""

services_body = f"""
<section class="page-hero">
  <div class="tile-corner" aria-hidden="true"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
  <div class="container page-hero-grid">
    <div>
      <p class="eyebrow on-dark">What we do</p>
      <h1>One ecosystem. Every capability a growing brand needs.</h1>
      <p class="lede">Most agencies specialise in one tile of the mosaic and call it a full-service offering. We built Mosaic9 the way the larger, category-defining Indian agencies operate &mdash; strategy, creative, performance, and technology reporting into a single account team, so nothing gets lost in translation between vendors.</p>
    </div>
    <div class="mosaic-visual" aria-hidden="true">
      <div class="tiles">
        {tiles_svg()}
      </div>
    </div>
  </div>
</section>

<section class="bg-paper" id="consulting">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Tile 01</p>
      <h2>Strategy and CMO Consulting</h2>
      <p class="lede">Senior marketing leadership without the full-time cost &mdash; the tile that decides what the other eight should actually be doing.</p>
    </div>
    <div class="grid grid-3">
      <div class="card"><div class="card-icon">{ICONS['strategy']}</div><h3>Marketing Audits</h3><p>An honest, structured review of what's working, what isn't, and where budget is leaking.</p></div>
      <div class="card"><div class="card-icon">{ICONS['dashboard']}</div><h3>GTM Planning</h3><p>Go-to-market roadmaps for new products, categories, or geographies.</p></div>
      <div class="card"><div class="card-icon">{ICONS['human']}</div><h3>Fractional CMO</h3><p>Monthly KPI reviews, agency oversight, and full marketing leadership on a flexible retainer.</p></div>
    </div>
  </div>
</section>

<section class="bg-mist" id="performance">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Tile 02&ndash;04</p>
      <h2>Performance and Growth</h2>
      <p class="lede">Drive revenue, reduce CAC, and scale what works with data-driven execution across every paid channel.</p>
    </div>
    <div class="grid grid-3">
      {svc_card('performance','PAID MEDIA','Google, Meta, LinkedIn &amp; YouTube','End-to-end campaign management: strategy, creative direction, A/B testing, audience segmentation, and ongoing optimisation.')}
      {svc_card('data','PROGRAMMATIC','Programmatic &amp; Display','Access to premium ad inventory across OTT, connected TV, high-impact display and exclusive publisher networks via leading DSPs.')}
      {svc_card('leadgen','LEAD GEN','Full-Funnel Lead Generation','Awareness ads, landing pages, form fills and CRM hand-off, with cost-per-lead accountability built in from day one.')}
      {svc_card('seo','ORGANIC','SEO / AEO / GEO','Technical SEO, answer-engine optimisation and generative-engine visibility &mdash; built for search, AI Overviews and answer engines alike.')}
      {svc_card('web','CRO','Conversion Rate Optimisation','Landing page testing, UX analysis and funnel optimisation so every click and every visit works harder.')}
      {svc_card('engine','ALWAYS-ON','Performance Engines',"Continuous, rules-based optimisation loops that reallocate spend toward what's working in near real time.")}
    </div>
  </div>
</section>

<section class="bg-paper" id="brand">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Tile 05&ndash;07</p>
      <h2>Brand and Creative</h2>
      <p class="lede">Great brands are built intentionally. We craft identities, tell stories, and build digital experiences that leave a lasting impression.</p>
    </div>
    <div class="grid grid-3">
      {svc_card('brand','IDENTITY','Brand Strategy &amp; Visual Identity','Logo, visual identity systems, brand guidelines, tone of voice and positioning built for long-term recognition.')}
      {svc_card('social','SOCIAL','Social Media &amp; Content Production','Platform strategy, content calendars, graphic design, reels and video production, and community management.')}
      {svc_card('whatsapp','MESSAGING','WhatsApp &amp; Messaging Automation','Broadcast campaigns, chatbot journeys, and drip automation for acquisition and retention on the channel Indian consumers actually use.')}
      {svc_card('web','WEB','Website &amp; Landing Page Development','Design and development of conversion-focused websites, microsites and campaign landing pages with CRO built in.')}
      {svc_card('data','CONTENT','Content Marketing &amp; Email','Blog content, long-form writing, email sequences and ad copy that carry one consistent brand voice.')}
      {svc_card('ai','CREATIVE AI','AI-Assisted Creative Production','Rapid creative variant generation and testing, reviewed and finished by senior creative talent, never shipped unchecked.')}
    </div>
  </div>
</section>

<section class="bg-deep" id="data-martech">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow on-dark">Tile 08&ndash;09</p>
      <h2>Data and Martech</h2>
      <p class="lede">We combine best-in-class marketing technology with multi-layer audience intelligence, so campaigns reach the right people, at the right time, and you always know exactly why.</p>
    </div>
    <div class="grid grid-3">
      <div class="card card-dark"><div class="card-icon">{ICONS['data']}</div><h3>Martech Stack Implementation</h3><p>CRM setup, marketing automation, tag management, attribution dashboards and CDP implementation, built from scratch.</p></div>
      <div class="card card-dark"><div class="card-icon">{ICONS['dashboard']}</div><h3>Custom Data Dashboards</h3><p>Live, brand-specific dashboards tracking the KPIs that actually matter to your business &mdash; not vanity metrics.</p></div>
      <div class="card card-dark"><div class="card-icon">{ICONS['ai']}</div><h3>Multi-Layer Audience Intelligence</h3><p>First-party CRM activation, second-party partnerships and vetted third-party segments for hyper-targeted campaigns built on real data.</p></div>
    </div>
  </div>
</section>

<section class="bg-mist">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow" style="justify-content:center;">How we engage</p>
      <h2>Flexible models, scalable partnerships</h2>
    </div>
    <div class="grid grid-3">
      <div class="card" style="border-color:var(--royal); border-width:2px;">
        <div class="tile-tag">RECOMMENDED</div>
        <h3>Retainer</h3>
        <p>Dedicated account team, monthly strategy and execution, all services under one roof, live dashboards, continuous optimisation. Best for brands seeking a long-term, fully integrated marketing partner.</p>
      </div>
      <div class="card">
        <h3>Project</h3>
        <p>Brand identity or rebrand, website or campaign build, a marketing audit, or a one-time campaign launch with defined scope and timelines.</p>
      </div>
      <div class="card">
        <h3>Fractional CMO</h3>
        <p>CMO-level strategy and planning, team and agency oversight, monthly KPI reviews and full marketing leadership &mdash; without the full-time cost.</p>
      </div>
    </div>
    <p class="text-center lede" style="margin:32px auto 0;">All engagements are custom scoped. Let's find the right fit for your business.</p>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="cta-band">
      <h2>Not sure which tile you need first?</h2>
      <p>Tell us where growth is stuck and we'll map the right mix of services to fix it.</p>
      <div class="cta-actions">
        <a class="btn btn-on-dark" href="contact.html">Talk to Us</a>
      </div>
    </div>
  </div>
</section>
"""

page(
    "services.html", "services.html",
    "Services | Mosaic9 &mdash; Performance, Brand, Tech & Strategy",
    "Explore Mosaic9's full-service offering: performance marketing, SEO, branding, social, web development, WhatsApp marketing, martech and CMO consulting.",
    services_body,
)
print("Services generated")

# ----------------------------------------------------------------------------
# ABOUT US
# ----------------------------------------------------------------------------
about_body = f"""
<section class="page-hero">
  <div class="tile-corner" aria-hidden="true"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
  <div class="container">
    <p class="eyebrow on-dark">About Us</p>
    <h1>Built by someone who's already scaled and sold one of these.</h1>
    <p class="lede">Mosaic9 exists because most brands don't need another vendor. They need one accountable partner who has actually built a company before, not just pitched for one.</p>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="grid grid-2" style="gap:56px;">
      <div class="card">
        <div class="tile-tag">MISSION</div>
        <h3>Why we exist</h3>
        <p>To give ambitious brands a single, senior-led marketing partner &mdash; one that combines strategy, creative, performance and technology into one connected system instead of nine disconnected vendors, and that is judged on revenue and growth, not impressions.</p>
      </div>
      <div class="card">
        <div class="tile-tag">VISION</div>
        <h3>Where we're headed</h3>
        <p>To become India's benchmark for full-service, data-and-AI-backed marketing &mdash; the ecosystem growing companies point to when they explain what "accountable partner" is supposed to mean.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-mist">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow" style="justify-content:center;">What we believe</p>
      <h2>The principles behind every brief</h2>
    </div>
    <div>
      <div class="value-row">
        <div class="mark">01</div>
        <div>
          <h3 style="margin-bottom:6px;">One partner, zero gaps</h3>
          <p style="color:var(--muted); margin:0;">Strategy, creative, performance and tech report into a single account team. No misaligned agencies, no briefing gaps, one partner who owns outcomes end-to-end.</p>
        </div>
      </div>
      <div class="value-row">
        <div class="mark">02</div>
        <div>
          <h3 style="margin-bottom:6px;">Every brief starts with a business goal</h3>
          <p style="color:var(--muted); margin:0;">Not a deliverable. We measure success in revenue, leads and growth &mdash; not just reach and impressions.</p>
        </div>
      </div>
      <div class="value-row">
        <div class="mark">03</div>
        <div>
          <h3 style="margin-bottom:6px;">Senior-led, always</h3>
          <p style="color:var(--muted); margin:0;">Senior strategists are engaged from day one through execution. You never get handed to a junior-only team after the pitch is won.</p>
        </div>
      </div>
      <div class="value-row">
        <div class="mark">04</div>
        <div>
          <h3 style="margin-bottom:6px;">Transparent, on principle</h3>
          <p style="color:var(--muted); margin:0;">Live dashboards, monthly reviews and proactive communication. You always know what we're doing, what it's delivering, and what's next.</p>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">The founder</p>
      <h2>Pranay Chowdhary</h2>
    </div>
    <div class="founder">
      <div class="founder-photo">
        <img src="assets/founder-pranay.jpg" alt="Pranay Chowdhary, Founder of Mosaic9">
      </div>
      <div>
        <p class="lede" style="max-width:60ch;">Pranay is the founder of Mosaic9 and brings 15+ years of experience across marketing, media and technology. Earlier in his career, he built and led a marketing-technology company that he successfully sold to a US-based entity &mdash; an exit that taught him firsthand what actually moves revenue for a business, versus what merely looks good in a slide deck.</p>
        <p style="max-width:60ch; color:var(--muted);">That operator's lens shapes how Mosaic9 works: every engagement is scoped against a business outcome first, technology and creative second. Pranay is personally involved in strategy for every retainer client &mdash; not as a figurehead, but as the senior strategist in the room.</p>
        <div class="founder-cred">
          <span>15+ Years in Marketing</span>
          <span>Founder, Mosaic9</span>
          <span>Prior Exit to a US Entity</span>
        </div>
        <p style="margin-top:24px;">
          <a class="btn btn-ghost" href="https://www.linkedin.com/in/pranaychowdhary" target="_blank" rel="noopener">Connect on LinkedIn &rarr;</a>
        </p>
      </div>
    </div>
  </div>
</section>

<section class="bg-deep">
  <div class="container">
    <div class="grid grid-4">
      <div class="stat"><div class="num">15+</div><div class="label">Years in marketing</div></div>
      <div class="stat"><div class="num">1</div><div class="label">Prior company, successfully exited</div></div>
      <div class="stat"><div class="num">80+</div><div class="label">Brands scaled at Mosaic9</div></div>
      <div class="stat"><div class="num">6+</div><div class="label">Industries served</div></div>
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="cta-band">
      <h2>Want to work directly with the founder?</h2>
      <p>Every retainer relationship at Mosaic9 starts with Pranay in the room.</p>
      <div class="cta-actions">
        <a class="btn btn-on-dark" href="contact.html">Get in Touch</a>
      </div>
    </div>
  </div>
</section>
"""

page(
    "about.html", "about.html",
    "About Us | Mosaic9 &mdash; Founder-Led Marketing Ecosystem",
    "Meet Mosaic9: a founder-led, full-service marketing ecosystem in Mumbai. Learn our mission, vision, and the story of founder Pranay Chowdhary, 15+ years in marketing.",
    about_body,
)
print("About generated")

# ----------------------------------------------------------------------------
# WHY MOSAIC9
# ----------------------------------------------------------------------------
why_body = f"""
<section class="page-hero">
  <div class="tile-corner" aria-hidden="true"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
  <div class="container">
    <p class="eyebrow on-dark">Why Mosaic9</p>
    <h1>Human judgement, running on machine-speed intelligence.</h1>
    <p class="lede">Most agencies now say "we use AI." Very few can show you the decision system behind that claim. Here's ours &mdash; and why every recommendation we make is backed by data, not opinion.</p>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="grid grid-2" style="gap:56px; align-items:center;">
      <div>
        <p class="eyebrow">The core idea</p>
        <h2>AI does the scale. Humans do the judgement.</h2>
        <p class="lede">AI is extraordinary at pattern-spotting across thousands of data points, generating creative variants, and testing at a speed no human team can match. It is not good at knowing your brand's taste, reading a market shift before the data catches up, or taking accountability for a client relationship. Mosaic9 is built so each side does only what it's actually good at.</p>
        <p>Every campaign runs through both layers: machine intelligence surfaces the options and the evidence; a senior strategist decides, contextualises, and owns the outcome. Neither layer ships alone.</p>
      </div>
      <div class="card" style="text-align:center; padding:48px 28px; background:linear-gradient(160deg, var(--mist) 0%, var(--mist-2) 100%);">
        <div style="width:130px; height:130px; margin:0 auto 20px; color:var(--royal);">{TILE_ART['ai']}</div>
        <p class="eyebrow" style="justify-content:center; margin-bottom:6px;">Human + AI Workflow</p>
        <p style="margin:0; color:var(--muted); font-size:0.92rem;">Every account runs on this exact decision system &mdash; not a slide, an actual workflow.</p>
      </div>
    </div>
    <div class="grid grid-2" style="margin-top:32px;">
      <div class="card"><div class="card-icon">{ICONS['ai']}</div><h3>What AI Handles</h3><p>Audience modelling, creative variant generation, anomaly detection, bid and budget signals, content drafts at scale.</p></div>
      <div class="card"><div class="card-icon">{ICONS['human']}</div><h3>What Humans Handle</h3><p>Brand judgement, final creative sign-off, strategic trade-offs, client context, and accountability for results.</p></div>
    </div>
  </div>
</section>

<section class="bg-mist">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow" style="justify-content:center;">The differentiators</p>
      <h2>What's actually running under the hood</h2>
      <p class="lede" style="margin:0 auto;">Four systems most agencies talk about, that we've actually built.</p>
    </div>
    <div class="grid grid-2">
      <div class="card">
        <div class="card-icon">{ICONS['ai']}</div>
        <h3>AI Workflows</h3>
        <p>Research, briefing, audience segmentation, and first-draft creative are assembled by AI workflows before a human ever opens a blank page. This compresses weeks of manual groundwork into hours, so strategists spend their time deciding and refining, not gathering.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS['engine']}</div>
        <h3>Performance Engines</h3>
        <p>Instead of a monthly optimisation cycle, budgets, bids and creative rotation are governed by always-on performance engines that react to signal changes daily &mdash; reallocating spend toward what's converting before a human would have noticed the shift.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS['web']}</div>
        <h3>Self-Working, Autonomous Tech Stacks</h3>
        <p>Tagging, attribution, CRM syncs and reporting pipelines are built to run themselves &mdash; auto-validating data quality, flagging tracking breaks, and feeding clean data into your dashboard without a person manually stitching spreadsheets every week.</p>
      </div>
      <div class="card">
        <div class="card-icon">{ICONS['dashboard']}</div>
        <h3>Customised Intelligent Dashboards</h3>
        <p>Every retainer client gets a dashboard built around their own KPIs &mdash; not a generic template. It's data-backed, updated continuously, and designed so you can see exactly what's working, what isn't, and where to double down, at any hour.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-deep">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow on-dark" style="justify-content:center;">Data-backed, not opinion-backed</p>
      <h2>Every decision traces back to evidence</h2>
    </div>
    <div class="grid grid-3">
      <div class="card card-dark"><h3>1st-Party Data</h3><p>Your CRM, website visitors and purchase history, activated for retention and lookalike expansion.</p></div>
      <div class="card card-dark"><h3>2nd-Party Data</h3><p>Trusted partner data through direct relationships &mdash; extending targeting precision without relying on third-party ecosystems.</p></div>
      <div class="card card-dark"><h3>3rd-Party Data</h3><p>Premium segments from verified providers: demographic, behavioural, purchase-intent and contextual targeting at scale.</p></div>
    </div>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="section-head center">
      <p class="eyebrow" style="justify-content:center;">The comparison</p>
      <h2>Mosaic9 vs. the traditional agency model</h2>
    </div>
    <div class="grid grid-2">
      <div class="card" style="border-color:var(--line);">
        <h3>Traditional multi-agency setup</h3>
        <p>Strategy, creative and media split across separate vendors &middot; monthly reporting stitched together manually &middot; optimisation happens in weekly or monthly cycles &middot; "AI" bolted on as a buzzword, not a workflow &middot; junior teams after the pitch is won.</p>
      </div>
      <div class="card" style="border-color:var(--royal); border-width:2px;">
        <h3>Mosaic9</h3>
        <p>One accountable team across every discipline &middot; a live, custom dashboard instead of a monthly PDF &middot; performance engines optimising continuously &middot; AI workflows built into how work actually gets done &middot; senior strategists on the account from day one.</p>
      </div>
    </div>
  </div>
</section>

<section class="bg-mist">
  <div class="container">
    <div class="cta-band" style="background:linear-gradient(135deg, var(--deep), var(--royal));">
      <h2>See the system in action</h2>
      <p>We'll walk you through a live dashboard example and show you exactly how the AI and human layers work together on a real account.</p>
      <div class="cta-actions">
        <a class="btn btn-on-dark" href="contact.html">Book a Walkthrough</a>
      </div>
    </div>
  </div>
</section>
"""

page(
    "why-mosaic9.html", "why-mosaic9.html",
    "Why Mosaic9 | Human + AI Marketing Intelligence",
    "Discover how Mosaic9 combines human strategic judgement with AI workflows, performance engines, autonomous tech stacks and custom data dashboards.",
    why_body,
)
print("Why Mosaic9 generated")

# ----------------------------------------------------------------------------
# CONTACT
# ----------------------------------------------------------------------------
contact_body = f"""
<section class="page-hero" style="padding-bottom:64px;">
  <div class="tile-corner" aria-hidden="true"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
  <div class="container">
    <p class="eyebrow on-dark">Let's talk</p>
    <h1>Ready to scale your brand?</h1>
    <p class="lede">Request a free marketing audit or drop us a brief. We'll come back with clarity, ideas, and a plan &mdash; usually within one business day.</p>
  </div>
</section>

<section class="bg-paper">
  <div class="container contact-wrap">
    <div>
      <h2 style="margin-bottom:24px;">Send us a brief</h2>
      <form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ENDPOINT" method="POST">
        <div class="grid grid-2">
          <div class="form-field">
            <label for="name">Full name</label>
            <input type="text" id="name" name="name" placeholder="Your name" required>
          </div>
          <div class="form-field">
            <label for="company">Company</label>
            <input type="text" id="company" name="company" placeholder="Your brand">
          </div>
        </div>
        <div class="grid grid-2">
          <div class="form-field">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" placeholder="you@company.com" required>
          </div>
          <div class="form-field">
            <label for="phone">Phone / WhatsApp</label>
            <input type="tel" id="phone" name="phone" placeholder="+91 ...">
          </div>
        </div>
        <div class="form-field">
          <label for="service">What do you need help with?</label>
          <select id="service" name="service">
            <option>Performance Marketing</option>
            <option>Branding &amp; Creative</option>
            <option>Website / Web Development</option>
            <option>SEO &amp; Organic Growth</option>
            <option>WhatsApp Marketing</option>
            <option>Full-Service Retainer</option>
            <option>Fractional CMO / Consulting</option>
            <option>Something else</option>
          </select>
        </div>
        <div class="form-field">
          <label for="message">Tell us about your brand and goals</label>
          <textarea id="message" name="message" placeholder="A few lines about your business, current challenges and what success looks like." required></textarea>
        </div>
        <button class="btn btn-primary" type="submit">Send Brief</button>
        <p id="form-status" class="form-note" role="status"></p>
        <p class="form-note">Note: this form is wired to send via <a href="https://formspree.io" target="_blank" rel="noopener" style="color:var(--royal); font-weight:700;">Formspree</a> (or any similar static-form service) &mdash; replace <code>YOUR_FORM_ENDPOINT</code> in the page source with your own endpoint before going live, since GitHub Pages cannot run server-side code directly.</p>
      </form>
    </div>
    <div>
      <div class="info-card">
        <h4>Email</h4>
        <p><a href="mailto:pranay@mosaic9.com">pranay@mosaic9.com</a></p>
      </div>
      <div class="info-card">
        <h4>Phone</h4>
        <p><a href="tel:+919930331126">+91 99303 31126</a></p>
      </div>
      <div class="info-card">
        <h4>WhatsApp</h4>
        <p><a href="https://wa.me/919930331126" target="_blank" rel="noopener">wa.me/919930331126 &mdash; message us directly</a></p>
      </div>
      <div class="info-card">
        <h4>Office</h4>
        <p>Mumbai, Maharashtra, India<br><span style="font-size:0.85rem;">(Full office address to be added here.)</span></p>
      </div>
      <div class="info-card" style="background:var(--deep); color:#fff;">
        <h4 style="color:#fff;">Office hours</h4>
        <p style="color:rgba(255,255,255,0.75);">Monday &ndash; Saturday, 10:00 AM &ndash; 7:00 PM IST</p>
      </div>
    </div>
  </div>
</section>
"""

page(
    "contact.html", "contact.html",
    "Contact Us | Mosaic9 &mdash; Mumbai Marketing Ecosystem",
    "Get in touch with Mosaic9 for a free marketing audit. Based in Mumbai, India. Email, call or WhatsApp us to start your brief.",
    contact_body,
)
print("Contact generated")

# ----------------------------------------------------------------------------
# BLOG LISTING
# ----------------------------------------------------------------------------
# Note: no AI image-generation tool is available in this environment, so these
# are original hand-built illustrations (distinct from the service tile art)
# rather than reused icons or sourced photography.
COVER_ART = {
 # Data-driven advertising — a "data detective" dashboard scene
 "data-detective": _art(
    '<rect x="6" y="10" width="40" height="30" rx="4" fill="currentColor" opacity="0.12"/>'
    '<rect x="6" y="10" width="40" height="30" rx="4" stroke="currentColor" stroke-width="2.6"/>'
    '<rect x="11" y="28" width="5" height="8" fill="currentColor" opacity="0.55"/>'
    '<rect x="19" y="21" width="5" height="15" fill="currentColor" opacity="0.8"/>'
    '<rect x="27" y="15" width="5" height="21" fill="currentColor"/>'
    '<circle cx="38" cy="22" r="6.5" fill="none" stroke="var(--accent)" stroke-width="2.2"/>'
    '<path d="M38 15.5A6.5 6.5 0 0 1 44.5 22" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round"/>'
    '<circle cx="46" cy="44" r="10" fill="currentColor" opacity="0.14"/>'
    '<circle cx="46" cy="44" r="10" stroke="currentColor" stroke-width="2.8"/>'
    '<path d="m53.5 51.5 5 5" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>',
    vb="0 0 64 64"
 ),
 # Walled gardens — a fenced enclosure with separated data-silos and a padlock
 "walled-garden": _art(
    '<path d="M6 26v22M18 22v26M30 26v22M42 22v26M54 26v22" stroke="currentColor" stroke-width="2.6" stroke-linecap="round"/>'
    '<path d="M2 30h56M2 40h56" stroke="currentColor" stroke-width="2.2"/>'
    '<rect x="10" y="42" width="10" height="10" rx="1.5" fill="currentColor" opacity="0.5"/>'
    '<rect x="24" y="42" width="10" height="10" rx="1.5" fill="currentColor" opacity="0.7"/>'
    '<rect x="38" y="42" width="10" height="10" rx="1.5" fill="currentColor" opacity="0.9"/>'
    '<rect x="24" y="8" width="16" height="12" rx="3" fill="var(--accent)"/>'
    '<path d="M28 8v-2a4 4 0 0 1 8 0v2" stroke="var(--accent)" stroke-width="2.4" fill="none" stroke-linecap="round"/>'
    '<circle cx="32" cy="13.5" r="1.8" fill="#fff"/>',
    vb="0 0 64 64"
 ),
 # AI in marketing — human profile collaborating with a circuit "mind", plus an insight spark
 "human-ai-collab": _art(
    '<path d="M6 52c0-9 5.5-14.5 12-14.5S30 43 30 52" stroke="currentColor" stroke-width="3" stroke-linecap="round"/>'
    '<circle cx="18" cy="24" r="9" fill="currentColor" opacity="0.15"/>'
    '<circle cx="18" cy="24" r="9" stroke="currentColor" stroke-width="3"/>'
    '<rect x="34" y="26" width="22" height="22" rx="5" fill="currentColor" opacity="0.14"/>'
    '<rect x="34" y="26" width="22" height="22" rx="5" stroke="currentColor" stroke-width="3"/>'
    '<path d="M41 26v-5m8 5v-5m-8 27v5m8-5v5M34 34h-4m4 9h-4m26-9h4m-4 9h4" stroke="currentColor" stroke-width="2.2" stroke-linecap="round"/>'
    '<circle cx="41" cy="37" r="1.8" fill="var(--accent)"/><circle cx="49" cy="37" r="1.8" fill="var(--accent)"/><circle cx="45" cy="43" r="1.8" fill="var(--accent)"/>'
    '<path d="M28 30q4 2 6 4" stroke="var(--accent)" stroke-width="2.4" stroke-linecap="round" stroke-dasharray="1 4"/>'
    '<path d="M45 8l2.4 5 5 .7-3.6 3.5.9 5-4.7-2.5-4.7 2.5.9-5-3.6-3.5 5-.7z" fill="var(--accent)"/>',
    vb="0 0 64 64"
 ),
 # Programmatic in India — skyline + connected-TV screen with signal waves
 "ctv-skyline": _art(
    '<path d="M4 52V34h6v-8h7v14h5V28h7v24h5V22h7v30h5V32h6v20z" fill="currentColor" opacity="0.16"/>'
    '<path d="M4 52h56" stroke="currentColor" stroke-width="2.4" stroke-linecap="round"/>'
    '<rect x="20" y="12" width="30" height="20" rx="3" fill="currentColor" opacity="0.14"/>'
    '<rect x="20" y="12" width="30" height="20" rx="3" stroke="currentColor" stroke-width="2.8"/>'
    '<path d="m31 18 9 4.5-9 4.5z" fill="var(--accent)"/>'
    '<path d="M53 14a11 11 0 0 1 0 16M57 10a17 17 0 0 1 0 24" stroke="var(--accent)" stroke-width="2.2" stroke-linecap="round" fill="none"/>',
    vb="0 0 64 64"
 ),
}

POSTS = [
    ("data-driven-advertising.html","Data & Strategy","What 'Data-Driven Advertising' Actually Means in 2026","Every agency claims to be data-driven. Here's the honest version: what it takes, what it doesn't fix, and how to tell the real thing from a dashboard.","data-detective"),
    ("walled-gardens-explained.html","Ad Tech","Walled Gardens, Explained: Google, Meta & Amazon","Why the biggest platforms keep their data to themselves, what it costs advertisers, and how brands can still build real audience intelligence.","walled-garden"),
    ("ai-in-marketing.html","AI & Marketing","Where AI Actually Helps in Marketing (And Where It Doesn't)","A practical, unhyped look at which parts of a marketing workflow benefit from AI today, and which still need a human in the room.","human-ai-collab"),
    ("future-of-programmatic-india.html","Programmatic","The Future of Programmatic Advertising in India","CTV, retail media and first-party data are reshaping programmatic buying in India. Here's what brands should be preparing for.","ctv-skyline"),
]

def blog_card(href, tag, title, desc, art_key):
    return f"""<a class="card blog-card" href="blog/{href}" style="text-decoration:none;">
        <div class="blog-cover" aria-hidden="true">{COVER_ART[art_key]}</div>
        <span class="tag">{tag}</span>
        <h3>{title}</h3>
        <p>{desc}</p>
        <div class="blog-meta">Mosaic9 Insights</div>
      </a>"""

blog_cards = "\n      ".join(blog_card(h,t,ti,d,a) for h,t,ti,d,a in POSTS)

blog_body = f"""
<section class="page-hero">
  <div class="tile-corner" aria-hidden="true"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div>
  <div class="container">
    <p class="eyebrow on-dark">Mosaic9 Insights</p>
    <h1>Marketing, advertising & AI &mdash; without the hype.</h1>
    <p class="lede">Notes from the strategists and analysts running your campaigns, on the trends actually worth paying attention to.</p>
  </div>
</section>

<section class="bg-paper">
  <div class="container">
    <div class="grid grid-2">
      {blog_cards}
    </div>
  </div>
</section>
"""

page(
    "blog.html", "blog.html",
    "Blog | Mosaic9 Insights on Marketing, Data & AI",
    "Mosaic9 Insights: practical, unhyped articles on data-driven advertising, walled gardens, AI in marketing, and the future of programmatic in India.",
    blog_body,
)
print("Blog listing generated")

# ----------------------------------------------------------------------------
# BLOG POSTS
# ----------------------------------------------------------------------------
def post_wrap(title, tag, read_time, content_html):
    return f"""
<section class="bg-paper" style="padding-top:56px;">
  <div class="container">
    <p style="margin-bottom:24px;"><a href="../blog.html" style="color:var(--royal); font-weight:700; font-family:var(--font-mono); font-size:0.85rem;">&larr; Back to Insights</a></p>
    <article class="post">
      <span class="pill">{tag}</span>
      <h1>{title}</h1>
      <div class="post-meta"><span>Mosaic9 Insights</span><span>{read_time} read</span></div>
      {content_html}
      <div class="divider-sm"></div>
      <p><strong>Want a second opinion on your own marketing stack?</strong> <a href="../contact.html" style="color:var(--royal); font-weight:700;">Request a free audit &rarr;</a></p>
    </article>
  </div>
</section>
"""

# ---- Post 1: Data-driven advertising ----
p1 = post_wrap("What 'Data-Driven Advertising' Actually Means in 2026", "Data & Strategy", "6 min", """
<p>"Data-driven" has become one of those phrases that shows up in almost every agency pitch deck, right next to a stock photo of a dashboard. Ask five agencies what it actually means and you'll usually get five different, mostly vague, answers. So it's worth being precise about what the phrase should mean, and what it definitely doesn't.</p>

<h2>What it isn't</h2>
<p>Data-driven advertising is not simply looking at last month's numbers before writing next month's plan. That's reporting, not strategy. It's also not the same as running everything through an algorithm and hoping the platform's black box figures it out &mdash; that's outsourcing judgement, not applying data.</p>

<h2>What it actually requires</h2>
<p>Real data-driven advertising rests on three layers working together, not one dashboard sitting on top of business as usual.</p>
<h3>1. Clean, connected data</h3>
<p>Before any optimisation is meaningful, the tracking has to be trustworthy: correctly implemented tags, a CRM that talks to your ad accounts, and attribution that reflects how customers actually move through your funnel, not just the last click before a purchase.</p>
<h3>2. A decision framework, not just a report</h3>
<p>A dashboard tells you what happened. A decision framework tells you what to do about it &mdash; predefined thresholds for when to pause a campaign, reallocate budget, or test a new audience. Without this, "data-driven" quietly turns into "data-informed, sometimes, when someone remembers to check."</p>
<h3>3. Continuous testing</h3>
<p>Data-driven teams treat almost every creative, audience and landing page as a hypothesis to be tested, not a final answer. The compounding value comes from dozens of small, structured tests over a quarter, not one big campaign launch.</p>

<h2>The honest limitation</h2>
<p>Data can tell you what happened and, with good modelling, what's likely to happen next. It can't tell you whether a brand's tone of voice is right, or whether a creative idea will resonate emotionally before it's tested in market. That's why the strongest teams pair data with senior human judgement, rather than treating data as a replacement for it.</p>

<blockquote>The goal isn't to remove human decisions from marketing. It's to make sure every human decision has real evidence behind it.</blockquote>

<h2>A simple way to audit your own setup</h2>
<ul>
<li>Can you trace a single sale back to the specific campaign, ad and audience that generated it?</li>
<li>Do you have a written rule for when a campaign gets paused, not just a gut feeling?</li>
<li>Are you testing at least one new variable &mdash; audience, creative, or offer &mdash; every two weeks?</li>
</ul>
<p>If the answer to any of these is no, the marketing may be data-informed, but it isn't yet data-driven.</p>
""")

page("blog/data-driven-advertising.html", "data-driven-advertising.html",
     "What 'Data-Driven Advertising' Actually Means in 2026 | Mosaic9",
     "A practical, no-hype breakdown of what data-driven advertising really requires: clean data, a decision framework, and continuous testing.",
     p1, base="../", og_type="article")

# ---- Post 2: Walled gardens ----
p2 = post_wrap("Walled Gardens, Explained: Google, Meta & Amazon", "Ad Tech", "7 min", """
<p>If you've ever felt like you have less visibility into your ad performance than you did a few years ago, you're not imagining it. Google, Meta and Amazon have steadily reduced the amount of raw data advertisers can see, while asking you to trust their automated systems more. This is the "walled garden" model, and it's worth understanding exactly how it works.</p>

<h2>What a walled garden is</h2>
<p>A walled garden is a platform that controls the entire advertising experience &mdash; inventory, targeting, measurement and reporting &mdash; inside its own ecosystem, without letting that data flow out to independent, third-party measurement. Google Search and Display, Meta's Facebook and Instagram inventory, and Amazon's retail media network are the three largest examples advertisers deal with daily.</p>

<h2>Why platforms build them</h2>
<p>Three reasons, mostly rational from the platform's point of view:</p>
<ul>
<li><strong>Privacy regulation.</strong> Rules like GDPR and evolving Indian data protection law make it riskier to share granular user-level data externally, so platforms keep more of it in-house.</li>
<li><strong>Competitive advantage.</strong> Data is the platform's core asset. Sharing it freely with advertisers or third-party tools would erode the reason advertisers need the platform at all.</li>
<li><strong>Automation push.</strong> Broad-match and automated bidding products perform better when the platform, not the advertiser, controls targeting decisions &mdash; which also happens to keep spend inside the platform's own tools.</li>
</ul>

<h2>What it costs advertisers</h2>
<p>Reduced visibility makes it harder to know which specific audience, placement or creative actually drove a result. It also makes cross-platform comparison difficult, since each garden reports success using its own definitions and attribution windows &mdash; which are rarely consistent with each other, and rarely conservative.</p>

<h2>What brands can still do about it</h2>
<h3>Invest in first-party data</h3>
<p>Your own CRM, website behaviour and purchase history are the one dataset no platform controls. The stronger this asset is, the less dependent you are on any single garden's targeting.</p>
<h3>Use server-side, brand-owned tracking</h3>
<p>Server-side tagging and a well-configured CRM give you a version of the truth that isn't filtered entirely through the platform's own attribution model.</p>
<h3>Treat platform-reported numbers as directional</h3>
<p>Compare platform-reported results against your own CRM and revenue data regularly, rather than assuming the two will always match.</p>
<h3>Diversify inventory deliberately</h3>
<p>Programmatic, connected TV and retail media outside the big three gardens are growing precisely because they offer advertisers more transparency and control.</p>

<p>Walled gardens aren't going away &mdash; if anything, the trend is toward more automation and less granular reporting, not less. The brands that come out ahead are the ones building a strong owned-data foundation now, rather than waiting for platforms to hand back visibility they have no incentive to give up.</p>
""")

page("blog/walled-gardens-explained.html", "walled-gardens-explained.html",
     "Walled Gardens Explained: Google, Meta & Amazon | Mosaic9",
     "Why Google, Meta and Amazon limit the ad data advertisers can see, what it costs brands, and how to build first-party data resilience against it.",
     p2, base="../", og_type="article")

# ---- Post 3: AI in marketing ----
p3 = post_wrap("Where AI Actually Helps in Marketing (And Where It Doesn't)", "AI & Marketing", "6 min", """
<p>Every marketing pitch in 2026 mentions AI somewhere. Very few explain, specifically, what task it's doing and why that task is better suited to a machine than a person. Here's a grounded breakdown, split by where AI genuinely earns its place in a workflow, and where it still falls short.</p>

<h2>Where AI clearly helps</h2>
<h3>Pattern-spotting at scale</h3>
<p>Across thousands of keywords, audiences or creative combinations, AI can surface which segments are underperforming or over-indexing far faster than a person manually cross-referencing spreadsheets. This is the single strongest use case in performance marketing today.</p>
<h3>First-draft generation</h3>
<p>Ad copy variants, content outlines, and research summaries are all tasks where AI can produce a reasonable starting point in seconds, freeing a strategist's time for judgement and refinement rather than blank-page staring.</p>
<h3>Anomaly detection</h3>
<p>AI systems can flag a sudden spend spike, a tracking break, or an unusual drop in conversion rate far faster than a human checking dashboards once a day, which matters when every hour of an unnoticed issue costs budget.</p>
<h3>Audience modelling</h3>
<p>Lookalike modelling and predictive scoring &mdash; estimating which users are likely to convert or churn &mdash; are fundamentally statistical problems that AI handles well, provided the underlying first-party data is clean.</p>

<h2>Where AI still falls short</h2>
<h3>Brand judgement</h3>
<p>Whether a joke lands, whether a tone feels right for a specific audience, whether a campaign risks embarrassing the brand &mdash; these are taste calls. AI can generate options; it can't reliably tell you which one is actually right for your brand without a person deciding.</p>
<h3>Reading context outside the data</h3>
<p>A competitor's product recall, a cultural moment, a shift in the news cycle &mdash; AI models trained on historical data are structurally slower to recognise these than a person paying attention to the world right now.</p>
<h3>Accountability</h3>
<p>When a campaign underperforms or a creative choice backfires, "the algorithm decided" isn't an acceptable answer to a client or a board. Someone has to own the decision, which means a human has to be in the loop before anything ships.</p>

<h2>The practical takeaway</h2>
<p>The most effective setup isn't "AI vs. humans," it's a clear division of labour: AI handles the scale and the pattern recognition, humans handle the judgement and the accountability. Agencies that can show you exactly where that line sits &mdash; not just say "we use AI" &mdash; are the ones worth trusting with real budget.</p>
""")

page("blog/ai-in-marketing.html", "ai-in-marketing.html",
     "Where AI Actually Helps in Marketing (And Where It Doesn't) | Mosaic9",
     "A grounded, unhyped look at which marketing tasks genuinely benefit from AI today, and which still require human judgement and accountability.",
     p3, base="../", og_type="article")

# ---- Post 4: Future of programmatic in India ----
p4 = post_wrap("The Future of Programmatic Advertising in India", "Programmatic", "6 min", """
<p>Programmatic advertising in India has matured quickly over the last few years, moving well past simple display retargeting. Three shifts, in particular, are changing how brands should think about programmatic budgets going into the next few years.</p>

<h2>1. Connected TV is becoming a real channel, not a novelty</h2>
<p>As streaming subscriptions and smart TV penetration grow across Indian households, connected TV (CTV) inventory is opening up as a genuinely targetable, measurable alternative to traditional television buying. Unlike linear TV, CTV campaigns can be targeted by audience segment and measured with the same rigour as digital display &mdash; a meaningful shift for brands that previously treated TV and digital as separate budgets with separate logic.</p>

<h2>2. Retail media is emerging as its own walled garden</h2>
<p>E-commerce platforms are increasingly selling advertising placements directly on their own marketplaces, using their first-party purchase data for targeting. This gives brands access to genuinely high-intent audiences, but it also means yet another closed ecosystem with its own reporting standards to reconcile against everything else in the media plan.</p>

<h2>3. First-party data is becoming the deciding factor in campaign quality</h2>
<p>As third-party cookies and cross-app tracking keep getting restricted, the advertisers who win in programmatic are increasingly the ones with strong first-party data &mdash; CRM records, app behaviour, purchase history &mdash; that can be safely activated through server-to-server integrations with demand-side platforms, rather than relying on third-party audience segments alone.</p>

<h2>What this means for Indian brands</h2>
<ul>
<li><strong>Start treating CRM data as a media asset</strong>, not just a sales tool. It will increasingly determine targeting quality across every programmatic channel.</li>
<li><strong>Budget for CTV as a test line item</strong>, not a future consideration &mdash; inventory and measurement are already usable today.</li>
<li><strong>Expect retail media to require its own strategy</strong>, with its own creative formats and its own reporting layer to reconcile against the rest of the media plan.</li>
<li><strong>Build attribution that spans channels</strong>, since no single platform's dashboard will give you the full picture across CTV, retail media and traditional programmatic display.</li>
</ul>

<p>Programmatic in India isn't just growing in spend &mdash; it's diversifying in format and getting more demanding on the data side. The brands that invest in their own first-party data foundation now will have a real targeting advantage as the ecosystem keeps fragmenting across new inventory types.</p>
""")

page("blog/future-of-programmatic-india.html", "future-of-programmatic-india.html",
     "The Future of Programmatic Advertising in India | Mosaic9",
     "How CTV, retail media and first-party data are reshaping programmatic advertising in India, and what brands should prepare for next.",
     p4, base="../", og_type="article")

print("Blog posts generated")

# ----------------------------------------------------------------------------
# 404
# ----------------------------------------------------------------------------
notfound_body = f"""
<section class="bg-deep" style="min-height:60vh; display:flex; align-items:center;">
  <div class="container text-center">
    <div class="tile-legend" style="max-width:220px; margin:0 auto 32px;">
      <div class="cell">{ICONS['strategy']}</div><div class="cell">{ICONS['brand']}</div><div class="cell">{ICONS['social']}</div>
      <div class="cell">{ICONS['seo']}</div><div class="cell">?</div><div class="cell">{ICONS['performance']}</div>
      <div class="cell">{ICONS['web']}</div><div class="cell">{ICONS['whatsapp']}</div><div class="cell">{ICONS['data']}</div>
    </div>
    <h1>This tile is missing.</h1>
    <p class="lede" style="margin:0 auto 28px;">The page you're looking for doesn't exist &mdash; but the rest of the mosaic does.</p>
    <a class="btn btn-on-dark" href="index.html">Back to Homepage</a>
  </div>
</section>
"""

page("404.html", "", "Page Not Found | Mosaic9", "This page doesn't exist. Head back to the Mosaic9 homepage.", notfound_body)
print("404 generated")
