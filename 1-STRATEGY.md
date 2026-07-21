# Michelle Lee / Minjung Lee — Personal Website Strategy

Prepared July 2026. Companion files: `2-COPY.md` (all draft copy) and `index.html` (working coded draft).

---

## 1. Reference site analysis

### A. alexjongholee.com

**Structure observed:**
- Single long-scroll page. Nav: Home · About · Projects · Writing · Contact
- Hero: name + identity line ("Seoul National University · Journalist · Social Entrepreneur") + personal quote ("I build bridges between languages, cultures, and communities…")
- Statistics banner: 2,500+ books donated · 3 libraries built · 4 languages · 6+ years of service · 2 research papers
- About: "Student, writer, and builder" framing; language proficiencies listed
- Three featured project cards (Lumen, Angels for the Journey, Jurio), each with role, date range, location, description, bulleted achievements
- Chronological timeline 2019 → 2026
- Community & journalism roles (MediaWatchTV, LeadersTimes, AsianHub, Mission Center for Migrants)
- Writing & research: two papers with journal names and volume numbers
- Skills grouped by category; contact with plain email

**What works (adapt for Michelle):**
1. **One-sentence identity + quote in the hero** — a reader knows who he is in 5 seconds.
2. **Metrics banner** — concrete numbers create instant credibility. Only works because the numbers are specific and plausible.
3. **Project cards with role / dates / location / bulleted outcomes** — reads like evidence, not description.
4. **Timeline** — turns a list of activities into a narrative of development. This is exactly what admissions readers look for.
5. **Specific citations** in Writing & Research (journal, volume, issue) — verifiable = credible.
6. **Photography from the field** integrated into sections, not a separate gallery.

**Weaknesses (avoid):**
1. Identity line leads with a university name — fine for a student, wrong for Michelle, who is post-BA with professional experience.
2. "Social entrepreneur / builder / CEO & Founder" language skews startup-flavored; it would ring false for Michelle's educator-writer-advocate identity.
3. Skills section mixes JavaScript/Pandas with cultural mediation — grab-bag feel.
4. No teaching or pedagogy dimension at all — that's Michelle's differentiator.

**⚠️ The critical strategic issue — shared projects.**
Alex's site claims Lumen ("CEO & Founder"), Angels for the Journey ("Co-founder"), AsianHub, and LeadersTimes — the same organizations in Michelle's history. If both sites present identical org-level achievements ("3 libraries built," "186 students supported"), a reader who encounters both (admissions offices do search) will see duplication and discount both. **Michelle's site must therefore describe her specific, personal contributions** — what *she* wrote, translated, taught, edited, organized — and may cite org-level outcomes only with attribution ("as part of a team…"). This is not just honest; it's what makes her site stronger than a copy.

### B. michellelee337.myportfolio.com (current site)

**Content found:**
- Nav: Welcome · About Michelle · My Journey · Leaders Times · Writing & Research · Contact · YouTube
- Welcome: "student, educator, and storyteller"; core questions "Who gets to learn? Who is remembered? Whose stories are heard?"; theme of law, policy, language, translation, and historical memory
- About: B.A. International Studies (concentration in **International Law and Diplomacy**), Ewha; **pursuing LL.B. at Korea Cyber University**; thematic timeline (2018 languages & exchange → 2021 educational empowerment → 2023 publishing & journalism → 2024 law, policy & memory)
- Journey covers: Angels for the Journey, Lumen, ISC Global, Mission Migrant Center, UN Memorial / Soldiers' Angels, Hiroshima Peace Memorial, AsianHub, Peaceful Unification Advisory Council, MEDIAWATCH
- Writing topic: "The Second Great Game"

**What is genuinely good (keep):**
- The three questions — *"Who gets to learn? Who is remembered? Whose stories are heard?"* — are the single best asset on either site. Distinctive, sincere, and they unify education + memory + justice. They should anchor the new hero.
- The thematic framing of the timeline (era titles like "Law, Policy & Memory") — smarter than Alex's plain years.
- The insight "how laws and policies look from the perspective of the people they are written about" — this is a law-school-essay-grade sentence. Feature it.
- Real, current facts (LL.B., law & diplomacy concentration) that strengthen the law narrative.

**What feels outdated / weak (fix):**
- Adobe Portfolio template look: text-heavy, placeholder graphics, no photos, no visual hierarchy. It reads as a *document*, not a professional presence.
- No proof layer: no metrics, no article links, no PDFs, no images of the work.
- "Student" self-description undersells a working educator with a completed B.A.
- Project pages are organization descriptions, not "here is what I did" cards with roles and dates.
- A YouTube nav link with unclear purpose; "Leaders Times" as a top-level nav item gives one activity outsized weight.
- No teaching section at all, despite teaching being her deepest experience.
- No clear contact call-to-action; no downloadable CV.
- It feels like a scrapbook of affiliations rather than one person's coherent story.

---

## 2. Brand positioning recommendation

**Position Michelle as:** *an educator, writer, and translator whose decade of work in classrooms, migrant communities, and multilingual publishing is now leading her into public-interest law.*

Three pillars, one thread:
1. **Education** — teaching (English, social studies, writing, debate, AP), curriculum, Lumen's books and libraries, Angels for the Journey.
2. **Language access** — AsianHub translation for multicultural families, MEDIAWATCH translation, bilingual publishing, cross-cultural coordination (ISC Global).
3. **Justice & memory** — LeadersTimes journalism on historical memory, labor/migrant-rights interests, LL.B. study, U.S. JD direction.

**The thread:** access — to learning, to language, to the law, to being remembered. Every project is her removing a barrier between a person and something they're entitled to.

**Identity line (recommended):**
> **Educator · Writer · Translator — working toward public-interest law**

Runner-up (warmer, for the hero sub-line rather than the title):
> *Working at the intersection of education, language access, and justice — across borders.*

Avoid "future legal advocate" as a headline — it frames her by what she isn't yet. The LL.B. and JD direction belong in the story, not the title.

**Mission line for hero (keep hers):**
> *Who gets to learn? Who is remembered? Whose stories are heard?*

**Differentiation from Alex's site:** Michelle = the educator/writer/interpreter of the shared work (pedagogy, editorial, translation, care), moving toward law. Not "founder/builder/CEO." Different verbs: *taught, translated, edited, wrote, organized, coordinated* — not *built, launched, founded* (except where "co-founded" is literally true).

---

## 3. Sitemap

One long-scrolling homepage (like Alex's — right call for this stage), plus two optional subpages later.

```
/                      Home (long scroll)
 ├─ #home              Hero
 ├─ #impact            Impact at a glance (stats)
 ├─ #about             About Michelle
 ├─ #projects          Featured Projects (6 cards + 2 conditional)
 ├─ #writing           Writing & Research
 ├─ #teaching          Teaching & Education
 ├─ #law               Toward Public-Interest Law
 ├─ #journey           Journey (timeline)
 ├─ #skills            Skills & Languages
 └─ #contact           Contact
/writing/<slug>        (Phase 2, optional) individual article/translation pages
/cv                    (Phase 2, optional) printable CV page or PDF link
```

**Navigation labels (keep to 6):** About · Projects · Writing · Teaching · Journey · Contact
(Stats, Law direction, and Skills are passed through by scrolling; they don't need nav slots.)

---

## 4. Homepage wireframe (section by section)

1. **Sticky nav** — "Michelle Lee" wordmark left; 6 links right; hamburger on mobile.
2. **Hero** — full-width, warm ivory background. Left: eyebrow ("Michelle Lee · 이민정 Minjung Lee"), H1 identity line, the three questions as an italic mission line, one-sentence intro, three buttons (View Projects / Read Writing / Contact Michelle). Right: professional or warm fieldwork photo, soft-radius mask. Mobile: photo above text, buttons full-width.
3. **Impact strip** — 5 stats on one band, big serif numerals. All numbers verified or visibly placeholdered.
4. **About** — two columns: 4-paragraph bio left; facts card right (education, languages, based in, focus areas, CV download).
5. **Featured Projects** — responsive card grid (3 → 2 → 1 columns). Each card: image, category tag, title, role · dates · location, 2–4 sentence description, "My contributions" bullets, impact line, optional link.
6. **Writing & Research** — list rows (not cards): title, publication/venue, date, one-line description, link/PDF chip.
7. **Teaching & Education** — split: philosophy paragraph + subjects/age-groups/formats grid; one testimonial slot.
8. **Toward Public-Interest Law** — narrow prose section, visually quieter (darker band), 3 short paragraphs. No bullets — this is the essay moment.
9. **Journey** — vertical timeline, thematic era headers + year markers, alternating on desktop, single rail on mobile.
10. **Skills & Languages** — 6 category cards with short tag lists; languages with honest proficiency levels.
11. **Contact** — centered invitation, email button, optional LinkedIn, note on languages ("English / 한국어 welcome").
12. **Footer** — name, one-line identity, nav repeat, © year.

---

## 5. Visual design direction

- **Feel:** academic warmth — personal academic site × nonprofit portfolio × writer's page. Serious, but human.
- **Palette:** warm ivory background `#FAF6EF`; ink `#26221C`; muted `#6E6459`; primary accent deep pine `#1E5C4B` (credible, calm, not corporate blue); secondary accent terracotta `#C1683C` used sparingly (tags, timeline dots).
- **Type:** Fraunces (serif) for display/headings — literary and warm; Inter for body/UI. Generous line-height (1.7 body).
- **Imagery:** real photographs only — classrooms, libraries, book pages, fieldwork. No stock. Consistent warm grade. If a project has no photo, use a typographic tile in palette colors rather than a random image.
- **Layout:** max content width ~1100px; large section spacing (96–128px); cards with 1px warm borders + soft shadow on hover; no parallax, no animation heavier than a fade-up.
- **Accessibility:** all text ≥ 4.5:1 contrast; visible focus rings; semantic headings; alt text on every image.

**Mobile:** single column throughout; hero photo above name; stats 2×2 grid + 1; timeline collapses to left rail; nav collapses to hamburger; buttons full-width with 48px tap targets; base font 17px.

---

## 6. Platform recommendation

**Recommended: Framer** — best balance for this site: modern templates, real typography control, fast hosting, easy CMS for adding articles later, ~$10/mo, and you can paste structure from the coded draft. Squarespace is the fallback if you want the least maintenance. Webflow is overkill; Wix skews decorative; WordPress adds upkeep burden.

**Also viable: the custom-coded site in this folder** (`index.html`) — zero cost on GitHub Pages/Netlify, total control, already built. Downside: edits require editing HTML. Honest recommendation: use `index.html` now (it's ready once content is filled in), migrate to Framer only if Michelle wants to self-edit frequently.

**Domain:** buy `michelleminjunglee.com` or `minjunglee.com` (check availability) — a real domain matters for the audiences listed. Keep "michellelee.com"-style consistency with how she signs her writing.

---

## 7. SEO

- **Title:** `Michelle Lee (Minjung Lee) — Educator, Writer & Translator | Education, Language Access & Public-Interest Law`
- **Meta description:** `Michelle Lee (Minjung Lee) is an educator, writer, and translator working across Korea and Southeast Asia — multilingual children's books, migrant-community translation, journalism on historical memory, and a path toward public-interest law.`
- H1 = the identity line; her full names (English + Korean) appear in visible text; Open Graph image = hero photo; `og:` and `twitter:` tags included in the draft.

---

## 8. What to remove or rewrite from the old site

| Old | Action |
|---|---|
| "Student, educator, and storyteller" | Rewrite → "Educator, writer, and translator" (post-BA professional) |
| The three questions | **Keep verbatim** — promote to hero |
| "…perspective of the people they are written about" line | **Keep** — anchor of the Law section |
| Thematic timeline eras | Keep concept; add specifics, dates, verbs |
| Organization-description project pages | Rewrite as role-first cards with personal contributions |
| "Leaders Times" as top-level nav | Remove; fold into Writing section |
| YouTube nav link | Remove unless it hosts specific project videos — then link from those cards |
| Placeholder graphics / no photos | Remove; replace with real photography or typographic tiles |
| "The Second Great Game" | Keep only with full citation + link/PDF; otherwise hold for Phase 2 |
| Peaceful Unification Advisory Council, Hiroshima, UN Memorial items | Consolidate — these become timeline entries and one "Community & Memory" card, not separate pages |

---

## 9. Implementation plan

**Phase 1 — Content (Michelle, ~1 week):** answer the checklist in `2-COPY.md` §Checklist; gather 8–12 photos; collect article links/PDFs; confirm which numbers are real.
**Phase 2 — Fill (1–2 days):** replace every `[bracketed placeholder]` in `index.html` / copy doc; drop in images; delete conditional sections that don't apply (e.g., Jurio card if not involved).
**Phase 3 — Publish (half day):** buy domain; deploy `index.html` to Netlify or GitHub Pages (or rebuild in Framer from this structure); connect domain; test on phone.
**Phase 4 — Verify:** contrast check, mobile check, every link clicked, someone who doesn't know Michelle reads it and answers "who is she?" in one sentence.
**Phase 5 — Ongoing:** add each new article/translation to Writing within a week of publication; update stats twice a year; add testimonials as they arrive.
