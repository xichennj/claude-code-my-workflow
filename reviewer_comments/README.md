# reviewer_comments/

Drop reviewer files here. This folder is **immutable input** — the workflow never modifies these files.

## Naming Convention

```
reviewer1.txt          # Referee 1 comments
reviewer2.txt          # Referee 2 comments
ae_comments.txt        # Associate Editor letter
editor_letter.txt      # Editor decision letter (if separate)
```

Also accepted: `.md`, `.docx`, `.pdf`

## File Format

The `/draft-responses` skill auto-detects numbered or lettered comment structures:

```
# Numbered (most common)
1. [Comment text]
2. [Comment text]

# Lettered
a) [Comment text]
b) [Comment text]

# Explicit labels
Major Comment 1: [Comment text]
Minor Comment 1: [Comment text]
```

Plain prose (no numbering) is also handled — the skill segments by paragraph.

## After Revision

Keep old reviewer comment files across revision rounds. Version your responses instead:
- Round 1: `responses/responses_v1.tex`
- Round 2: `responses/responses_v2.tex`
