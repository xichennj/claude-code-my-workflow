# Reviewer Response Protocol

**Activated when working in:** `responses/**`, `reviewer_comments/**`, `manuscript/**`

---

## Source-of-Truth Chain

```
reviewer_comments/  (INPUT — immutable, never modify)
      +
manuscript/         (INPUT — immutable, never modify)
      ↓
responses/          (OUTPUT — generated, versioned)
```

**Golden rule:** Never modify files in `reviewer_comments/` or `manuscript/`. If you discover an error in reviewer comment parsing, correct the interpretation in `responses/`, not the source file.

---

## Mandatory Tone Rules

Every response block must satisfy all 7 rules before being written:

1. **Acknowledge first** — open each response by recognizing the comment's validity (1 sentence)
2. **State actions, not beliefs** — "We have revised Section 3" not "We believe Section 3 already addresses this"
3. **Cite every claimed change** — format: "See Section X.Y (p. N)" or "See Equation (N)" or "See Table N"
4. **Never use these phrases:**
   - "We disagree with the referee"
   - "The referee misunderstood"
   - "As we already stated" / "As we already showed"
   - "This is standard in the literature" (without a citation)
   - "We are happy to..." (too informal)
5. **Explain non-changes** — if a suggestion was not implemented, give a substantive reason (not "it's beyond scope")
6. **Flag analysis gaps honestly** — use `\analysisneeded{[description]}` for items needing new empirical work
7. **Match journal register** — assume top-field journal formality unless told otherwise

---

## Required Document Structure

Assemble the response document in this order:

1. **Opening letter** to Editor
   - Thank editors and referees (1 sentence each)
   - 3–5 bullet summary of main changes
   - Statement that all page/section references use the revised manuscript
2. **Response to Associate Editor** (if `ae_comments.*` exists)
3. **Response to Referee 1** (if `reviewer1.*` or `referee1.*` exists)
4. **Response to Referee 2** (if `reviewer2.*` or `referee2.*` exists)
5. **Response to Referee 3+** (if present)
6. **Required Robustness Checks** section (if any `[ANALYSIS NEEDED]` items remain)

---

## Version Naming

```
responses_v1.tex    # First submission response
responses_v2.tex    # Second round (major revision)
responses_v3.tex    # Third round (if needed)
```

Never overwrite a previous version. Increment the version number.

---

## Quality Gate Checklist (required before any submission)

Run through all items before declaring a response document ready:

- [ ] **LaTeX compiles** — `pdflatex responses_v[N].tex` with zero errors
- [ ] **No `[ANALYSIS NEEDED]` remaining** — all placeholders resolved
- [ ] **All citations have location** — every "we added X" is followed by "(Section Y, p. Z)"
- [ ] **Tone check** — none of the 4 forbidden phrases appear
- [ ] **Structure check** — opening letter present, referees in correct order
- [ ] **Version log updated** — `responses/VERSION_LOG.md` has entry for this version
- [ ] **Quality score ≥ 90/100** — run `/proofread responses_v[N].md` if uncertain

---

## LaTeX Preamble Requirements

The `responses_v[N].tex` file must define (or import from template):

```latex
\newenvironment{refereequote}{%
  \begin{quote}\itshape\color{gray}%
}{%
  \end{quote}%
}

\newcommand{\analysisneeded}[1]{%
  \textbf{\color{red}[ANALYSIS NEEDED: #1]}%
}

\newcommand{\msloc}[1]{\textit{(#1)}}
```

---

## Comment Classification Rules

When parsing `reviewer_comments/` files:

| Label | Criteria |
|-------|----------|
| MAJOR | Requests new empirical analysis, challenges identification, questions main results, asks for new tables/figures |
| MINOR | Requests clarification, additional discussion, notation change, minor rewriting |
| EDITORIAL | Typos, citation format, reference list, punctuation |

When in doubt, classify UPWARD (treat as MAJOR rather than MINOR).

---

## Pandoc Conversion (optional)

If pandoc is available, convert Markdown to Word:

```bash
pandoc responses/responses_v[N].md -o responses/responses_v[N].docx
```

The Word document is for co-author review only. The `.tex` file is the authoritative source.
