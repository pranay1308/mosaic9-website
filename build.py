import os

ROOT = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://mosaic9.com"

NAV = [
    ("index.html", "Home"),
    ("services.html", "Services"),
    ("why-mosaic9.html", "Why Mosaic9"),
    ("about.html", "About Us"),
    ("blog.html", "Blog"),
    ("contact.html", "Contact"),
]

SOCIAL_SVGS = {
    "linkedin": '<svg viewBox="0 0 24 24"><path d="M20.45 20.45h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.86 0-2.14 1.45-2.14 2.94v5.67H9.34V9h3.42v1.56h.05c.48-.9 1.64-1.85 3.38-1.85 3.6 0 4.27 2.37 4.27 5.46v6.28zM5.34 7.43a2.07 2.07 0 1 1 0-4.13 2.07 2.07 0 0 1 0 4.13zM7.12 20.45H3.56V9h3.56v11.45z"/></svg>',
    "whatsapp": '<svg viewBox="0 0 24 24"><path d="M17.47 14.38c-.29-.15-1.73-.85-2-.95-.27-.1-.46-.15-.66.15-.2.29-.75.94-.92 1.14-.17.19-.34.22-.63.07-.29-.15-1.22-.45-2.32-1.43-.86-.76-1.44-1.71-1.6-2-.17-.29-.02-.45.13-.6.13-.13.29-.34.44-.51.15-.17.19-.29.29-.48.1-.2.05-.36-.02-.51-.07-.15-.66-1.59-.9-2.18-.24-.57-.48-.5-.66-.51h-.56c-.2 0-.51.07-.78.36-.27.29-1.02 1-1.02 2.44s1.05 2.83 1.19 3.03c.15.19 2.06 3.15 5 4.42.7.3 1.24.48 1.67.61.7.22 1.34.19 1.84.12.56-.08 1.73-.71 1.97-1.39.24-.68.24-1.27.17-1.39-.07-.12-.27-.19-.56-.34z"/><path d="M12.02 2C6.5 2 2 6.48 2 12c0 1.85.5 3.58 1.36 5.07L2 22l5.06-1.33A9.94 9.94 0 0 0 12.02 22C17.52 22 22 17.52 22 12S17.52 2 12.02 2zm0 18.11c-1.7 0-3.29-.47-4.65-1.28l-.33-.2-3 .79.8-2.92-.22-.34a8.11 8.11 0 0 1-1.25-4.36c0-4.48 3.65-8.11 8.13-8.11 4.48 0 8.13 3.63 8.13 8.11 0 4.48-3.65 8.11-8.13 8.11z"/></svg>',
    "instagram": '<svg viewBox="0 0 24 24"><path d="M12 2.16c3.2 0 3.58.01 4.85.07 1.17.05 1.8.25 2.23.41.56.22.96.48 1.38.9.42.42.68.82.9 1.38.16.42.36 1.06.41 2.23.06 1.27.07 1.65.07 4.85s-.01 3.58-.07 4.85c-.05 1.17-.25 1.8-.41 2.23-.22.56-.48.96-.9 1.38-.42.42-.82.68-1.38.9-.42.16-1.06.36-2.23.41-1.27.06-1.65.07-4.85.07s-3.58-.01-4.85-.07c-1.17-.05-1.8-.25-2.23-.41-.56-.22-.96-.48-1.38-.9a3.75 3.75 0 0 1-.9-1.38c-.16-.42-.36-1.06-.41-2.23-.06-1.27-.07-1.65-.07-4.85s.01-3.58.07-4.85c.05-1.17.25-1.8.41-2.23.22-.56.48-.96.9-1.38.42-.42.82-.68 1.38-.9.42-.16 1.06-.36 2.23-.41 1.27-.06 1.65-.07 4.85-.07M12 0C8.74 0 8.33.01 7.05.07c-1.28.06-2.15.26-2.91.56-.79.31-1.46.72-2.13 1.38A5.94 5.94 0 0 0 .63 3.14c-.3.76-.5 1.63-.56 2.91C0 7.33 0 7.74 0 11s.01 3.67.07 4.95c.06 1.28.26 2.15.56 2.91.31.79.72 1.46 1.38 2.13.66.66 1.34 1.07 2.13 1.38.76.3 1.63.5 2.91.56C8.33 22.99 8.74 23 12 23s3.67-.01 4.95-.07c1.28-.06 2.15-.26 2.91-.56a5.9 5.9 0 0 0 2.13-1.38 5.94 5.94 0 0 0 1.38-2.13c.3-.76.5-1.63.56-2.91.06-1.28.07-1.69.07-4.95s-.01-3.67-.07-4.95c-.06-1.28-.26-2.15-.56-2.91a5.9 5.9 0 0 0-1.38-2.13A5.94 5.94 0 0 0 19.86.63c-.76-.3-1.63-.5-2.91-.56C15.67.01 15.26 0 12 0z"/><path d="M12 5.84A6.16 6.16 0 1 0 12 18.16 6.16 6.16 0 0 0 12 5.84zm0 10.16a4 4 0 1 1 0-8 4 4 0 0 1 0 8z"/><circle cx="18.41" cy="5.59" r="1.44"/></svg>',
    "twitter": '<svg viewBox="0 0 24 24"><path d="M18.9 2H22l-7.5 8.57L23.3 22h-6.9l-5.4-7.06L4.7 22H1.6l8.03-9.17L.8 2h7.07l4.88 6.45L18.9 2zm-1.2 18h1.9L7.4 3.9H5.36L17.7 20z"/></svg>',
    "youtube": '<svg viewBox="0 0 24 24"><path d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.4 3.6 12 3.6 12 3.6s-7.4 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c2 .5 9.4.5 9.4.5s7.4 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.6 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><path d="M2 5.5A1.5 1.5 0 0 1 3.5 4h17A1.5 1.5 0 0 1 22 5.5v13a1.5 1.5 0 0 1-1.5 1.5h-17A1.5 1.5 0 0 1 2 18.5v-13zm2.2.5 7.8 6.1L19.8 6H4.2zM20 8.3l-7.5 5.9a1 1 0 0 1-1 0L4 8.3v10.2h16V8.3z"/></svg>',
}

def nav_html(current, base=""):
    items = []
    for href, label in NAV:
        cls_attr = ' class="active"' if href == current else ""
        items.append(f'<li><a{cls_attr} href="{base}{href}">{label}</a></li>')
    return "\n        ".join(items)

def head(title, description, canonical, base="", og_type="website"):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{SITE_URL}/{canonical}">
<meta name="robots" content="index, follow">
<meta name="theme-color" content="#2A1B4D">

<meta property="og:type" content="{og_type}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{SITE_URL}/{canonical}">
<meta property="og:image" content="{SITE_URL}/assets/favicon-512.png">
<meta property="og:site_name" content="Mosaic9">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{SITE_URL}/assets/favicon-512.png">

<link rel="icon" type="image/png" sizes="32x32" href="{base}assets/favicon-32.png">
<link rel="icon" type="image/png" sizes="16x16" href="{base}assets/favicon-16.png">
<link rel="apple-touch-icon" href="{base}assets/favicon-180.png">
<link rel="stylesheet" href="{base}css/style.css">
</head>
"""

def header_html(current, base=""):
    return f"""<header class="site-header">
  <nav class="nav">
    <a class="brand" href="{base}index.html">
      <img src="{base}assets/logo.png" alt="Mosaic9 logo">
      Mosaic9
    </a>
    <ul class="nav-links">
        {nav_html(current, base)}
    </ul>
    <div class="nav-cta">
      <a class="btn btn-primary" href="{base}contact.html">Start a Project</a>
      <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false"><span></span></button>
    </div>
  </nav>
</header>
"""

def footer_html(base=""):
    return f"""<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div>
        <div class="footer-brand">
          <img src="{base}assets/logo.png" alt="Mosaic9 logo">
          <span>Mosaic9</span>
        </div>
        <p style="max-width:32ch; font-size:0.92rem;">A full-service marketing ecosystem where strategy, creative, performance and technology are laid down as one connected pattern &mdash; not nine separate vendors.</p>
        <div class="social-row" style="margin-top:20px;">
          <a href="https://www.linkedin.com/company/mosaic9-mediatech" target="_blank" rel="noopener" aria-label="LinkedIn">{SOCIAL_SVGS['linkedin']}</a>
          <a href="https://wa.me/919930331126" target="_blank" rel="noopener" aria-label="WhatsApp">{SOCIAL_SVGS['whatsapp']}</a>
          <a href="mailto:pranay@mosaic9.com" aria-label="Email">{SOCIAL_SVGS['mail']}</a>
        </div>
      </div>
      <div class="footer-col">
        <h5>Company</h5>
        <ul>
          <li><a href="{base}about.html">About Us</a></li>
          <li><a href="{base}why-mosaic9.html">Why Mosaic9</a></li>
          <li><a href="{base}blog.html">Blog</a></li>
          <li><a href="{base}contact.html">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Services</h5>
        <ul>
          <li><a href="{base}services.html#consulting">Strategy &amp; CMO Consulting</a></li>
          <li><a href="{base}services.html#performance">Performance Marketing</a></li>
          <li><a href="{base}services.html#brand">Branding &amp; Creative</a></li>
          <li><a href="{base}services.html#data-martech">Data &amp; Martech</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h5>Contact</h5>
        <ul>
          <li><a href="mailto:pranay@mosaic9.com">pranay@mosaic9.com</a></li>
          <li><a href="tel:+919930331126">+91 99303 31126</a></li>
          <li><a href="https://wa.me/919930331126" target="_blank" rel="noopener">WhatsApp Us</a></li>
          <li>Mumbai, India</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>&copy; <span id="year"></span> Mosaic9. All rights reserved.</p>
      <p>Built on Performance &middot; Scale &middot; Creativity</p>
    </div>
  </div>
</footer>

<a class="wa-float" href="https://wa.me/919930331126" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{SOCIAL_SVGS['whatsapp']}</a>

<script>document.getElementById('year').textContent = new Date().getFullYear();</script>
<script src="{base}js/main.js"></script>
</body>
</html>
"""

def page(filename, current, title, description, body, base="", og_type="website"):
    canonical = current if base == "" else f"blog/{current}"
    html = head(title, description, canonical, base, og_type) + "<body>\n" + header_html(current, base) + body + footer_html(base)
    path = os.path.join(ROOT, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("wrote", filename)
