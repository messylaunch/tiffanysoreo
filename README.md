# The Oreo Lady — Website + GHL Sales Kit

Cinematic one-page scroll site for **The Oreo Lady** (Tiffany Ponds — fresh-fried
Oreos, Lakeland / the 863), plus the internal GoHighLevel sales playbook.

## What's in here

| File | What it is |
|---|---|
| `index.html` | The customer-facing site — a scroll-film: galaxy hero → 3 menu chapters → horizontal schedule route → text-alert + booking CTAs |
| `ghl-sales-worksheet.html` | **Internal** — discovery worksheet + pitch script for selling Tiffany on GoHighLevel (printable) |
| `vendor/` | GSAP, ScrollTrigger, Lenis (vendored locally, no CDN dependency) |

## Menu (from the flyer)

1. Regular Powdered Sugar Oreos — **6 for $10**
2. Dubai Chocolate Pistachio Oreos — **4 for $10**
3. Half / Half (3 + 3) — **6 for $10**

## Running locally

Any static server works:

```bash
python3 -m http.server 8000
# open http://localhost:8000
```

## GoHighLevel hookup points

Search `index.html` for `GHL` — there are two marked slots:

- **Text alerts** (`#alerts`): drop the GHL form/2-step embed where the comment
  indicates; repoint "Get on the list" at the funnel URL.
- **Booking** (`#book`): swap the Facebook links for the GHL booking-calendar link.

Until GHL is live, both CTAs point at the real Facebook page / TikTok.

## Dev contract (for automated screenshots)

`index.html?jump=<scrollY>` lands pre-scrolled with all scroll animations settled,
and `window.__ready === true` fires when the page is stable. Respects
`prefers-reduced-motion` (all scenes readable with animations off).

## Socials

- TikTok: [@theoreolady863](https://www.tiktok.com/@theoreolady863)
- Facebook: [The Oreo Lady / Tiffany Ponds](https://www.facebook.com/theoreolady863)
