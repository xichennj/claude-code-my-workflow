# manuscript/

Drop your paper source file here. Preferred format: `.tex` (LaTeX).
Also accepted: `.docx`, `.pdf` (read-only).

**This folder is INPUT ONLY.** The workflow never modifies files here.

## Naming Convention

```
[PaperShortname].tex          # e.g., myPaper.tex, jpe_submission.tex
```

## Usage

Place your paper source here before running `/draft-responses`. The skill will:
1. Detect the file automatically (prefers `.tex`, falls back to `.docx`, `.pdf`)
2. Build a manuscript index (sections, equations, tables, figures)
3. Use the index to cite specific locations in each response

## Notes

- For `.tex` files, all included files (`\input{}`, `\include{}`) should also be present here
- For `.pdf`, the skill reads text but cannot resolve internal cross-references
- Do NOT place reviewer comment files here — those go in `reviewer_comments/`
