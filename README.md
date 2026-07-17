# Mosaic9 — Website Source

A multi-page, static marketing site for **mosaic9.com** — purple/white, mosaic-tile visual system, built with plain HTML/CSS/JS (no build tools needed) so it deploys straight to **GitHub Pages for free**.

## Pages
- `index.html` — Homepage (mosaic hero animation, naming story, clients, services teaser, why-us teaser)
- `services.html` — Full service catalogue, grouped like a full-service Indian agency (Performance, Brand & Creative, Technology & Data, Strategy & Consulting)
- `about.html` — Mission, vision, values, founder bio (Pranay Chowdhary)
- `why-mosaic9.html` — Differentiators: human + AI, AI workflows, performance engines, autonomous tech stacks, custom dashboards
- `contact.html` — Contact form + office details
- `blog.html` + `blog/*.html` — 4 original articles on data-driven advertising, walled gardens, AI in marketing, and programmatic in India
- `404.html` — Custom not-found page

## SEO hygiene already in place
- Unique `<title>` and meta description per page
- Canonical tags, Open Graph + Twitter card tags
- Semantic HTML (`header`, `nav`, `main` sections, `footer`), single `<h1>` per page
- `sitemap.xml` and `robots.txt`
- Organization JSON-LD structured data on the homepage
- Descriptive `alt` text on images, favicon set for all devices

---

## 1. Deploy to GitHub Pages (free)

1. Create a new GitHub repository, e.g. `mosaic9-website` (public repo — required for free GitHub Pages on a personal account).
2. Upload **all files in this folder** (keeping the folder structure — `css/`, `js/`, `assets/`, `blog/`, plus the root `.html` files, `CNAME`, `robots.txt`, `sitemap.xml`) to the repo. Easiest ways:
   - Drag-and-drop upload via the GitHub web UI ("Add file → Upload files"), or
   - Using git locally:
     ```bash
     cd mosaic9
     git init
     git add .
     git commit -m "Initial Mosaic9 website"
     git branch -M main
     git remote add origin https://github.com/<your-username>/mosaic9-website.git
     git push -u origin main
     ```
3. In the repo, go to **Settings → Pages**.
4. Under **Build and deployment → Source**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`. Save.
5. GitHub will publish the site at `https://<your-username>.github.io/mosaic9-website/` within a minute or two.

## 2. Connect your Squarespace domain (mosaic9.com)

The repo already includes a `CNAME` file containing `mosaic9.com`, which tells GitHub Pages to serve the site on your custom domain instead of the default `github.io` address.

**In GitHub:**
1. Settings → Pages → under "Custom domain", enter `mosaic9.com` and save (this should auto-detect from the `CNAME` file already in the repo).
2. Tick **Enforce HTTPS** once it becomes available (can take a few minutes to an hour after DNS is set up).

**In Squarespace Domains (DNS settings for mosaic9.com):**
Add these DNS records (Squarespace → Domains → mosaic9.com → DNS Settings):

| Type  | Host / Name | Value                  |
|-------|-------------|------------------------|
| A     | @           | 185.199.108.153        |
| A     | @           | 185.199.109.153        |
| A     | @           | 185.199.110.153        |
| A     | @           | 185.199.111.153        |
| CNAME | www         | `<your-username>.github.io` |

(These four A-records are GitHub Pages' fixed IP addresses; add all four.)

DNS changes can take anywhere from a few minutes to 24-48 hours to propagate fully.

## 3. Make the contact form actually send email

GitHub Pages is static hosting — it can't run a server-side script to send form emails. The form in `contact.html` is pre-wired for a drop-in service:

1. Create a free account at [formspree.io](https://formspree.io) (or Web3Forms, Getform, etc.)
2. Create a new form and copy your unique endpoint URL.
3. Open `contact.html`, find this line:
   ```html
   <form id="contact-form" action="https://formspree.io/f/YOUR_FORM_ENDPOINT" method="POST">
   ```
4. Replace `YOUR_FORM_ENDPOINT` with your real Formspree form ID and commit the change. Submissions will then arrive at `pranay@mosaic9.com` (or whichever inbox you register).

## 4. Things to personalise before launch
- Swap the placeholder social links in the footer (Instagram, X/Twitter, YouTube handles) for your real profiles, or remove any you don't have yet.
- Add the exact street address in `contact.html` (currently shows "Mumbai, Maharashtra, India" only).
- The client logos on the homepage are shown as clean text wordmarks since no individual client logo files were supplied — swap in real logo images under `assets/clients/` and update the `.logo-chip` markup in `index.html` whenever you have them.
- Add a real founder photo in place of the "PC" initials placeholder in `about.html`.
- `pages.py` / `build.py` are the Python scripts used to generate the HTML — edit copy there and re-run `python3 pages.py` if you prefer editing content in one place rather than each HTML file directly. Editing the `.html` files directly also works fine going forward.
