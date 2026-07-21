# Update Strategy — Legal Studies, Labor Research, Jurio, Civic Service

July 2026. Integrates Michelle's newer law/labor/technology direction into the existing site without scattering it. Source material: her revised research proposal (`3 수정·보완된 연구계획안.docx`), interview questions (`인터뷰 질문.docx`), the live Jurio app (jurio-gamma.vercel.app), and the user's brief.

---

## 1. The one-story arc (how it stays coherent)

Three acts, one theme (access):

1. **Education & language** (2018–) — teaching, translation, AFJ, Lumen: helping people reach learning and stories in their own language.
2. **The turn to law** (2023–) — Int'l Law & Diplomacy concentration, LL.B. at Korea Cyber University, migrant-community engagement: realizing the barriers she kept meeting were legal ones.
3. **Law + technology in practice** (2025–) — labor-rights & automation research (interviews with certified labor attorneys), Jurio legal-information app: applying research, writing, and technology to make labor law legible to the people it governs.

Connective sentence used across the site:
> *Michelle works at the intersection of education, language, community, and law — using writing, translation, teaching, research, and technology to support people whose voices are often overlooked.*

The bridge (used verbatim in About + research page — improved from the brief):
> Michelle's interest in labor protection grew out of her engagement with migrant communities — including concern for Sri Lankan migrant workers whose employment prospects can be narrowed by industrial robots, automation, and shifting labor demand. Watching technological change arrive faster than the protections around it shaped the question that now drives her research: when machines change the terms of work, what does the law actually do for the workers affected?

*(Wording rules respected: "engagement," "concern," "shaped" — no claims of legal advice or representation.)*

## 2. Key facts established from the uploaded documents

**Research project (from the revised proposal):**
- Final Korean title: 산업로봇 도입과 한국 제조업 노동자 보호: 안전·참여·전환 보호에 대한 노무사 인식을 중심으로
- English rendering used on site: *Industrial Robots and the Protection of Korean Manufacturing Workers: How Certified Labor Attorneys Assess Safety, Participation, and Transition Protection*
- Research question: how far Korean labor law protects manufacturing workers' **safety, procedural participation, and job transition** during robot adoption — and how 노무사 perceive the current system's limits.
- Stance: not "should robots be stopped," but "what protection do workers actually get when adoption is already under way." Korea has among the world's highest manufacturing robot densities — a present-tense issue, not futurism.
- Legal analysis spans five areas: Occupational Safety and Health Act; Act on the Promotion of Workers' Participation and Cooperation (labor-management councils); Trade Union Act (bargaining over adoption vs. its effects); Labor Standards Act (redeployment, restructuring, dismissal); vocational training / transition-support institutions.
- Analytical frame: Lina Khan's Amazon critique + OSHA ergonomics cases — efficiency's hidden costs borne by workers (pace, monitoring, musculoskeletal risk, bargaining power).
- Method: literature review → statutory analysis → U.S. comparison → short semi-structured interviews with certified labor attorneys (proposal planned 20–30; **user reports 39 completed — flagged for confirmation**), 5 core questions, anonymized, thematic coding, frequency analysis, employer-side vs. worker-side comparison.
- Terminology: 노무사 = **certified labor attorney (공인노무사)** — a licensed Korean professional specializing in labor law, workplace compliance, and labor-management relations. Site always explains this once; never plain "lawyers."

**Jurio (verified from the deployed app bundle):**
- Bilingual KR/EN app ("Jurio 주리오"), Expo/React Native web, early stage.
- Real features: plain-language issue guides ("임금을 못 받았어요" / "일하다 다쳤어요(산재)" / 계약만료); statute cards citing article numbers (LSA arts. 15, 23, 26, 27, 49; Minimum Wage Act art. 6; Foreign Workers Employment Act art. 25) linked to law.go.kr; six-statute reference set incl. Industrial Accident Insurance Act, Retirement Benefits Act; a regional directory of certified labor attorneys and labor-law firms; resource navigation with hotlines incl. multilingual migrant-worker lines (다누리 1577-1366 — 13 languages; 외국인력상담 1644-0644 — 18 languages; 1345); wage-arrears documentation guidance (체불 확인서); a disclaimer field exists in the data model.
- Positioning language: **legal information / legal-literacy tool / early-stage prototype** — never "legal advice." Disclaimer shown on the project page.
- Roles: Michelle = co-planner, legal-content strategist, UX feedback (per user brief); Alex Lee = developer/builder. (His site claims "Builder" — consistent, no conflict if her card is content/planning-side.)

## 3. Positioning statements (5 versions)

**A. Law-school / formal:**
"Michelle Lee is an educator, writer, and translator completing a Bachelor of Laws at Korea Cyber University. Her work connects language access, children's literacy, migrant communities, and labor rights: she has co-founded a multilingual children's publisher in Cambodia and a youth education network in Southeast Asia, and now conducts interview-based research on how Korean labor law protects manufacturing workers in the age of industrial robots, while helping build Jurio, a legal-information app for labor-rights issues."

**B. Warm personal-website version (used in hero/About):**
"I teach, write, and translate across Korea and Southeast Asia — and study law to understand the barriers I kept meeting. From children's books in Khmer to labor-law questions raised by industrial robots, my work asks one question: how do we make systems legible to the people inside them?"

**C. Short homepage line:**
"Educator · Writer · Translator — working toward public-interest law through research, publishing, and legal technology."

**D. LinkedIn bio:**
"Educator, writer & translator | LL.B. candidate (Korea Cyber Univ.) | Co-founder, Lumen Education (multilingual children's books, Cambodia) & Angels for the Journey | Researching labor rights & automation (interviews with certified labor attorneys) | Building Jurio, a labor-law legal-literacy app | Bechtel Prize honorable mention, Teachers & Writers Magazine | EN·KR"

**E. Fellowship version:**
"Michelle Lee works at the intersection of education, language, and law. After co-founding literacy and education projects for children in Cambodia, the Philippines, and Laos, she turned to legal studies to address the barriers her communities faced — completing an LL.B. while researching how automation reshapes worker protection in Korean manufacturing and co-developing a plain-language legal-information app used to navigate labor-rights issues. Her essay on teaching writing in a Cambodian classroom received a Bechtel Prize honorable mention from Teachers & Writers Magazine."

## 4. Navigation (recommended)

`About · Projects · Research · Legal Studies · Teaching · Contact`
- "Research" anchors to Research & Writing (merged section — research rows sit above writing rows).
- Journey/Gallery remain on-page, reached by scrolling; keeping nav ≤6 preserves the clean top bar.
- Project pages: `lumen.html`, `angels.html`, `research.html`, `jurio.html`.

## 5. Homepage structure (updated)

1. Hero (unchanged identity + updated intro sentence)
2. Stats strip (unchanged — 39-interview stat joins **after** confirmation)
3. **NEW: "Current focus" band** — one sentence + three chips (LL.B. · labor-rights & automation research · Jurio legal-information app)
4. About (bio gains act-three paragraph)
5. Featured Projects — **4 major cards** (Lumen, Angels, Research, Jurio) in a 2×2 grid, then 4 smaller cards (Teaching, AsianHub, LeadersTimes, MEDIAWATCH)
6. Research & Writing (research row added on top, "in progress" label)
7. Legal Studies (NEW): LL.B. presentation + coursework placeholders + research interests
8. Teaching & Workshops (unchanged)
9. **Civic Service & Remembrance** (NEW, compact): UN Memorial Cemetery + Soldiers' Angels letter writing — deliberately modest, below major projects
10. Toward Public-Interest Law (updated to land on research/Jurio as the direction already in motion)
11. Journey (timeline gains: LL.B. start [year], migrant-center engagement, Soldiers' Angels, 2026 research + Jurio)
12. Skills (gains Legal Research & Technology category)
13. Gallery · Contact · Footer

## 6. Civic service wording (final)

> After reporting on and volunteering around the UN Memorial Cemetery in Busan — the only United Nations cemetery in the world — Michelle wanted a way to continue that gesture of cross-border gratitude in the present tense. Through Soldiers' Angels' virtual letter-writing program, she writes letters of appreciation to deployed service members: a small, regular practice of remembrance that connects her interest in how nations honor those who serve with the individuals doing so now.

*(Kept modest: an extension of an interest, not a leadership project. Placed in a compact band, not a featured card.)*

## 7. Tone guardrails applied

- Research: "ongoing," "in progress," "working research project" — never "published/proved."
- Jurio: "early-stage," "legal information," "legal-literacy," + explicit disclaimer.
- 39 interviews: shown with a confirm-flag until the user verifies final count and interviewee identity.
- Migrant communities: "engagement," "concern," "shaped her research interest" — no representation claims.
- LL.B.: "completing a Bachelor of Laws… growing academic foundation" — no bar/qualification implications.

## 8. Missing-information checklist (new items)

**Legal studies:** exact English degree/major name; expected completion date (or omit); 5 key courses; honors only if wanted.
**Research:** confirm 39 completed (proposal said 20–30 planned); interviewees all 공인노무사 or mixed; anonymity (proposal says anonymized — confirm); venue (independent / class / journal / supports Jurio?); shareable interim findings?; current stage (interviews done → coding? writing?).
**Jurio:** Michelle's exact role wording; Alex's role wording; which features are live vs. planned; target users (migrant workers confirmed as audience?); multilingual roadmap; is the in-app disclaimer text finalized?; 2–3 screenshots for the project page.
**Soldiers' Angels:** participation period; letters count (only if she wants it); her UN Memorial Cemetery activity precisely (visit? volunteering? journalism?) and date.
**Migrant center:** center name public? role + dates; Sri Lankan workers example publishable? photos/anonymization needs.
