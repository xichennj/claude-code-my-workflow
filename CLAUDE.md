# CLAUDE.MD -- Academic Project Development with Claude Code

<!-- HOW TO USE: Replace [BRACKETED PLACEHOLDERS] with your project info.
     Customize Beamer environments and CSS classes for your theme.
     Keep this file under ~150 lines — Claude loads it every session.
     See the guide at docs/workflow-guide.html for full documentation. -->

**Project:** [YOUR PAPER TITLE] — Reviewer Response Drafting
**Institution:** [YOUR INSTITUTION]
**Branch:** main

---

## Core Principles

- **Plan first** -- enter plan mode before non-trivial tasks; save plans to `quality_reports/plans/`
- **Verify after** -- compile/render and confirm output at the end of every task
- **Single source of truth** -- `reviewer_comments/` + `manuscript/` are immutable inputs; `responses/` is the only output
- **Quality gates** -- nothing ships below 80/100
- **[LEARN] tags** -- when corrected, save `[LEARN:category] wrong → right` to MEMORY.md

---

## Folder Structure

```
[YOUR-PROJECT]/
├── CLAUDE.MD                    # This file
├── .claude/                     # Rules, skills, agents, hooks
├── manuscript/                  # Paper source (*.tex preferred; *.docx, *.pdf accepted)
├── reviewer_comments/           # Reviewer files (reviewer1.txt, ae_comments.txt, etc.)
├── responses/                   # Generated output (responses_v1.tex, .md, .docx)
├── data/                        # Data files for any required new analysis
├── output/                      # Tables, figures from new analysis
├── scripts/                     # R / Python scripts for new analysis
├── quality_reports/             # Plans, session logs, manuscript reviews
├── explorations/                # Research sandbox
├── templates/                   # Session log, quality report, response-letter templates
└── master_supporting_docs/      # Supporting papers and prior versions
```

---

## Commands

```bash
# Draft reviewer responses (produces .tex + .md in responses/)
/draft-responses v1

# Compile response document to PDF
cd responses && pdflatex responses_v1.tex

# Convert Markdown to Word (requires pandoc)
pandoc responses/responses_v1.md -o responses/responses_v1.docx

# Review manuscript before drafting responses
/review-paper manuscript/[filename].tex

# Run R analysis for new empirical checks
Rscript scripts/[analysis_script].R
```

---

## Quality Thresholds

| Score | Gate | Meaning |
|-------|------|---------|
| 80 | Commit | Good enough to save |
| 90 | PR | Ready for deployment |
| 95 | Excellence | Aspirational |

---

## Skills Quick Reference

| Command | What It Does |
|---------|-------------|
| `/draft-responses [vN]` | Draft full reviewer response document (LaTeX + Markdown + docx) |
| `/review-paper [file]` | Manuscript review (5 lenses: identification, econometrics, data, lit, robustness) |
| `/proofread [file]` | Grammar/typo/tone review of response document |
| `/data-analysis [dataset]` | End-to-end R analysis for new empirical checks |
| `/review-r [file]` | R code quality review |
| `/lit-review [topic]` | Literature search + synthesis (for missing citations) |
| `/research-ideation [topic]` | Research questions + strategies |
| `/interview-me [topic]` | Interactive research interview |
| `/validate-bib` | Cross-reference citations in manuscript |
| `/commit [msg]` | Stage, commit, PR, merge |

---

## LaTeX Response Template Elements

| Command / Environment | Effect | Use Case |
|-----------------------|--------|----------|
| `\begin{refereequote}...\end{refereequote}` | Gray italic indented block | Displaying exact referee comment |
| `\analysisneeded{description}` | Bold red placeholder | Flag required new empirical analysis |
| `\msloc{location}` | Italic parenthetical | Cite manuscript location inline |
| `\refereeheader{Referee N}` | Section divider | Heading for each referee's responses |
| `\comment{N}{text}` | Comment block + response prompt | Individual comment + response pair |

## Response Document Conventions

| Convention | Rule |
|------------|------|
| Referee comment | Always quoted verbatim in `refereequote` |
| Manuscript citation | Always explicit: "Section X.Y (p. N)" or "Equation (N)" |
| Non-implemented suggestion | Always explained with substantive reason |
| Analysis gaps | Always flagged with `\analysisneeded{}` before submission |
| Tone | Formal + collegial; never defensive |
| Version | Increment (`v1`, `v2`) — never overwrite |

---

## Current Project State

| Item | File | Status |
|------|------|--------|
| Manuscript | `manuscript/[filename].tex` | [DRAFT / SUBMITTED / UNDER REVIEW] |
| Reviewer Comments — R1 | `reviewer_comments/reviewer1.txt` | [PENDING / LOADED] |
| Reviewer Comments — R2 | `reviewer_comments/reviewer2.txt` | [PENDING / LOADED] |
| AE Letter | `reviewer_comments/ae_comments.txt` | [PENDING / LOADED] |
| Response Document | `responses/responses_v[N].tex` | [NOT STARTED / DRAFT / SUBMITTED] |
| [ANALYSIS NEEDED] items | -- | [N items remaining] |
