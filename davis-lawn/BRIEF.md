# Client-Site Brief — Davis Lawn Service & Hauling

This is the **reusable prompt** distilled from the process that built The Oreo Lady site.
Part 1 is filled in for Davis. Part 2 is the blank template — copy it, fill it in for the
next client, and paste it to Claude with the same skills installed
(`impeccable`, `ui-ux-pro-max`, `brandkit` concepts, `scroll-film-studio` if cinematic).

---

## Part 1 — The Davis prompt (as executed)

> Build a **conversion-first one-page website** for **Davis Lawn Service & Hauling**
> (Facebook: https://www.facebook.com/p/Davis-Lawn-Service-Hauling-100078407036199/).
>
> **Business reality:** local lawn care + hauling/junk removal outfit. Holds some city
> contracts (details unknown — leave a marked slot and a note listing the questions to
> ask). Few usable photos online, so build every visual in CSS/SVG — **no AI image
> generation, no stock photos.** We invent the logo.
>
> **Brand (you decide, commit, stay consistent):** working-crew authority. Deep lawn
> greens + charcoal + one safety-orange CTA color that nothing else uses. Condensed
> workwear display type (Anton) + clean body (Inter). Logo = shield badge, D monogram
> with grass blades growing out of it, small truck silhouette.
>
> **Conversion rules (non-negotiable):**
> - Primary action: short quote form (≤4 fields) IN the hero on desktop + tap-to-call
>   everywhere. Sticky header CTA. Mobile sticky bottom bar (Call / Free Quote) that
>   appears after the hero.
> - Every service card ends in a quote link. Final CTA section repeats the ask.
> - Orange is only ever the conversion action. If everything shouts, nothing does.
> - GHL-ready: leave a marked embed slot where the form goes; mailto fallback until then.
> - Trust before features: licensed/insured, response speed, city-contract experience,
>   free estimates — directly under the hero.
> - JSON-LD LocalBusiness schema, semantic HTML, tel: links with real number (TODO).
>
> **Motion rules (learned the hard way on the last build):**
> - **No pinning, no scroll-jacking, anywhere.** All animation is play-once-on-enter
>   (GSAP + ScrollTrigger, `start: "top 78%"`, 150–800 ms), plus ambient loops (cloud
>   drift, marquee). Scroll always moves the page 1:1.
> - Respect `prefers-reduced-motion` with a fully readable static fallback.
> - Implement the dev contract: `?jump=<scrollY>` lands settled, `window.__ready = true`
>   when stable — so the puppeteer harness can screenshot and jank-test it.
>
> **Unknown facts = visible placeholders, never fake specifics.** Phone number stays an
> obvious 555 placeholder, service area says [City], reviews are marked "sample — swap
> with real Facebook reviews." Top-of-file HTML comment lists every TODO.
>
> **Verify before you call it done:** serve locally, screenshot hero/services/form/footer
> at desktop 1440×900 and mobile 375×812 through the harness, run the jank test
> (p95 < 20 ms, no frame > 50 ms), read the screenshots, fix what's ugly, then commit.

### Questions to ask Davis before launch (fills the TODOs)
1. Real phone number, and who answers it (missed-call text-back is the GHL pitch here).
2. Cities/areas actually served, and where most jobs come from.
3. What exactly do the city contracts cover? (right-of-way mowing / code-enforcement
   lots / storm debris / demolition hauling?) Specifics win commercial bids.
4. Licensed & insured — confirm wording is accurate before it stays on the page.
5. Since what year? Crew size? Anything worth bragging about (equipment, response time)?
6. 3–5 real reviews (Facebook recommendations are fine) + permission to use names.
7. Real before/after job photos — the slider is already built to take them.
8. Payment methods; do they invoice commercial accounts?

---

## Part 2 — Blank template for the next client

> Build a **[conversion-first landing / cinematic scroll-film]** site for
> **[BUSINESS NAME]** ([link every profile you have]).
>
> **Business reality:** [what they do, who buys it, service area]. Photos available:
> [yes → use them / no → CSS-SVG everything / budget for N AI images ≤ $X].
> Logo: [existing → replicate faithfully / none → invent one, describe the metaphor].
>
> **Brand:** [2-3 adjectives]. Palette: [base + accent + ONE cta color reserved for
> conversion actions]. Type: [display face with real character] + [clean body face].
>
> **Conversion rules:** primary action = [call / form / booking / DM]; it appears in the
> hero, the sticky header, a mobile sticky bar, after every service block, and in a
> final CTA. Trust strip under the hero: [licenses, years, contracts, guarantees —
> only claims the client confirmed]. Leave a marked [GHL / other CRM] embed slot.
>
> **Motion rules:** no pinning or scroll-jacking; play-once-on-enter reveals + ambient
> loops only; `prefers-reduced-motion` fallback; implement the `?jump` / `__ready`
> dev contract for automated screenshot + jank verification.
>
> **Unknowns:** never invent facts — obvious placeholders + a TODO manifest comment at
> the top of the file + a "questions to ask the client" list in the brief.
>
> **Definition of done:** harness screenshots (desktop + mobile) reviewed, jank test
> passed, placeholders inventoried, committed and pushed.

### Process cheat-sheet (what actually happened, in order)
1. `ui-ux-pro-max` → `--design-system` query for the product type (mine the checklist
   + anti-patterns even when the style match is off).
2. Art-direct yourself: palette, type pairing, logo (inline SVG), one signature visual.
3. Build the page in one self-contained HTML file; vendor GSAP/ScrollTrigger locally.
4. Verify with `scroll-film-studio/scripts/verify.js` (shots + jank) — read the
   screenshots, don't assume.
5. Run `impeccable` critique references over the result; fix; re-shoot.
6. Commit, push, deliver screenshots + the TODO list to the human.
