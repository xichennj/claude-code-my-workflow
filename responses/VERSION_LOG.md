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
- **Status:** NEAR-FINAL — ready for author review and manuscript edits
