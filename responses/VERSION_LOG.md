# Response Version Log

Tracks each round of reviewer responses.

---

## Template Entry

```
### v[N] — [YYYY-MM-DD]
- **Input:** [manuscript filename] + [reviewer files]
- **Referee files:** [list]
- **Comments:** [N total — M major, K minor, J editorial]
- **Analysis needed:** [N items flagged]
- **Quality score:** [N/100]
- **Status:** [DRAFT / SUBMITTED / ACCEPTED]
- **Notes:** [Any round-specific context]
```

---

<!-- Entries will be appended here by /draft-responses -->

### v1 — 2026-02-22
- **Input:** `ADRD Risk model-manucript.docx` + `reviewer_comments.docx`
- **Referee files:** `reviewer_comments.docx` (contains Editor + Reviewers 1, 2, 3)
- **Comments:** 30 total — 9 major, 8 minor, 13 editorial
- **[ANALYSIS NEEDED] items:** 8 (see Summary table in responses_v1.md)
- **Quality score:** 72/100 (DRAFT — analysis items unresolved)
- **Status:** SUPERSEDED by v2

### v2 — 2026-02-23
- **Input:** Same manuscript + reviewer comments as v1
- **Changes from v1:** All 8 [ANALYSIS NEEDED] items resolved
  - AN1, AN3, AN6, AN8: existing supplement analyses cited (eMethods 5, eFigs 12-13, 6, 7; eTables 1-2)
  - AN2: control group N stated in Methods (PD=47, paralysis=1,039, stroke=3,071)
  - AN4: addressed in writing + `scripts/AN4_balanced_panel.do` to fill in balanced-panel N
  - AN5: addressed in writing (PUF has no MedPAR linkage key; RIF requires DUA)
  - AN7: year FE confirmed in equation S.2; eMethods 2 clarified
- **Supplement copied to repo:** `manuscript/Supplementary_Material.docx`
- **New script:** `scripts/AN4_balanced_panel.do`
- **Remaining author action:** Run AN4_balanced_panel.do to fill in balanced-panel N in Methods
- **Quality score:** 90/100
- **Status:** SUPERSEDED by v2.1 (proofreading pass)

### v2.1 — 2026-02-23
- **Input:** Same as v2; no new analysis
- **Changes from v2:** 26 proofreading fixes (see `quality_reports/responses_v2_report.md`)
  - CRITICAL: Removed 4 internal author-action/script notes from submission text
  - MAJOR: Fixed opening letter tense (present perfect throughout); added missing article
  - MAJOR: Removed dismissive "already implemented prior to this review round" framing
  - MAJOR: Replaced "differently-raced subgroups" with standard phrasing
  - MAJOR: Fixed subject-verb agreement ("version that does not contain")
  - MAJOR: Added [CITE] markers for unsupported "standard practice" claims (R2.2)
  - MAJOR: Updated eTable 5–20 title to "Negative Control Analyses" (was "Placebo Tests")
  - MINOR: DiD capitalization, N spacing, "data set" spelling, eTable qualifier, JAMA NO clarified
- **Remaining author actions:**
  1. Fill in `[N]` (run `scripts/AN4_balanced_panel.do`)
  2. Fill in `[DATE OF SUBMISSION]`
  3. Replace two `[CITE]` markers in R2.2 with actual references
- **Quality score:** 93/100
- **Status:** NEAR-FINAL — pending 3 author actions above
