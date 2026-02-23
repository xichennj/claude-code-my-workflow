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
- **Status:** SUPERSEDED by v2.2 (citations filled)

### v2.2 — 2026-02-23
- **Input:** Same as v2.1; no new analysis
- **Changes from v2.1:** Filled in [CITE] markers in R2.2 with verified references
  - "PUF standard practice" → (Lu and Liao, 2022; Wang et al., 2024)
  - "self-reported ADRD consistent with prior work" → (Schüssler-Fiorenza Rose et al., 2016; Wang et al., 2024)
  - Full references appended after R2.2 response block
- **Note:** Authors should confirm citations or substitute higher-impact alternatives
- **Remaining author actions:**
  1. Fill in `[N]` (run `scripts/AN4_balanced_panel.do`)
  2. Fill in `[DATE OF SUBMISSION]`
  3. Confirm or swap R2.2 citations
- **Quality score:** 95/100
- **Status:** SUPERSEDED by v2.3 (balanced-panel revision)

### v2.3 — 2026-02-23
- **Input:** Same as v2.2; no new analysis
- **Changes from v2.2:** Resolved `[N]` placeholder — revised R2.1 to accurately reflect PUF data structure
  - Diagnosis: MCBS PUF assigns new anonymized ID per beneficiary per year; cross-year linkage impossible from PUF
  - Removed: `[N]` placeholder and balanced-panel N claim (cannot be computed from PUF)
  - Removed: eFigure 5 balanced-panel robustness check claim (same reason)
  - Added: explanation that PUF is a repeated cross-section; pooled DiD valid under this structure
  - Added: Limitations note that within-person subset cannot be enumerated from PUF
  - Updated: AN4 row in summary table to reflect actual resolution
- **Remaining author actions:**
  1. ~~Fill in `[DATE OF SUBMISSION]`~~ → filled: February 23, 2026
  2. Confirm or swap R2.2 citations (Lu & Liao 2022; Wang et al. 2024; Schüssler-Fiorenza Rose et al. 2016)
- **Quality score:** 97/100
- **Status:** NEAR-FINAL — pending citation confirmation only
