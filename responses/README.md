# responses/

Generated output lives here. This folder is **output only** — do not manually edit generated files (edit the source in `manuscript/` or `reviewer_comments/` and re-run).

## File Naming

```
responses_v1.tex       # LaTeX source (primary)
responses_v1.md        # Markdown (for quick reading / pandoc conversion)
responses_v1.docx      # Word document (via pandoc, if installed)
responses_v1.pdf       # Compiled PDF (via pdflatex)
VERSION_LOG.md         # Tracks all versions
```

## Workflow

```bash
# Draft responses (generates responses_v1.tex + responses_v1.md)
/draft-responses v1

# Compile to PDF
pdflatex responses_v1.tex

# Convert to Word
pandoc responses_v1.md -o responses_v1.docx

# Next revision round
/draft-responses v2
```

## Quality Gate

Before submitting:
- [ ] LaTeX compiles without errors
- [ ] No `[ANALYSIS NEEDED]` placeholders remain
- [ ] Every claimed change cites a specific manuscript location
- [ ] Tone is formal, collegial, never defensive
- [ ] Quality score ≥ 90/100
