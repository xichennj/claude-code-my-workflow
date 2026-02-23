# Response Letter Template

<!--
  TEMPLATE: Reviewer Response Document

  This file serves two purposes:
  1. A configurable LaTeX preamble for response documents
  2. A guide for structuring the response letter

  Usage: /draft-responses uses this template as the document skeleton.
  Customize PAPER_TITLE, JOURNAL_NAME, and AUTHOR_INFO before first use.

  LaTeX commands defined here:
    \begin{refereequote}...\end{refereequote}  — Displays referee comment in gray italic
    \analysisneeded{description}               — Flags required new analysis in red
    \msloc{location}                           — Cites manuscript location in italic
-->

---

## LaTeX Preamble

```latex
\documentclass[12pt]{article}
\usepackage[margin=1in]{geometry}
\usepackage{amsmath, amssymb}
\usepackage[dvipsnames]{xcolor}
\usepackage{hyperref}
\usepackage{enumitem}
\usepackage{booktabs}
\usepackage{parskip}

% ── Response document custom commands ──────────────────────────────────────

% Referee quote block (gray italic, indented)
\newenvironment{refereequote}{%
  \begin{quote}\itshape\color{gray}%
}{%
  \end{quote}%
}

% Flag items requiring new empirical analysis
\newcommand{\analysisneeded}[1]{%
  \textbf{\color{red}[ANALYSIS NEEDED: #1]}%
}

% Cite manuscript location
\newcommand{\msloc}[1]{\textit{(#1)}}

% Referee section header
\newcommand{\refereeheader}[1]{%
  \bigskip\noindent\rule{\linewidth}{0.4pt}\\[2pt]%
  {\large\bfseries #1}\\[-4pt]%
  \rule{\linewidth}{0.4pt}\bigskip%
}

% Comment subsection
\newcommand{\comment}[2]{%
  \subsection*{Comment #1}%
  \begin{refereequote}#2\end{refereequote}%
  \noindent\textbf{Response:}~%
}

% ── Document metadata ──────────────────────────────────────────────────────

\title{Response to Reviewers\\[6pt]
  \large [PAPER_TITLE]\\[4pt]
  \normalsize Submitted to [JOURNAL_NAME]}
\author{[AUTHOR_NAMES]}
\date{[DATE]}

\begin{document}
\maketitle
```

---

## Opening Letter Structure

```latex
% ── Opening Letter ─────────────────────────────────────────────────────────

Dear [Editor Name / Professor [LASTNAME]] and Referees,

Thank you for the careful reading of ``[PAPER_TITLE]'' and for the
constructive and detailed comments from the referees. We have revised
the manuscript substantially in response to these comments.

The main changes relative to the previous version are:

\begin{itemize}
  \item [CHANGE_1 — one sentence, specific and concrete]
  \item [CHANGE_2 — one sentence]
  \item [CHANGE_3 — one sentence]
  % Add 1-2 more if needed; 3–5 bullets is the right length
\end{itemize}

All page and section references below refer to the \emph{revised} manuscript.
We respond to each comment in detail below.

\bigskip
\noindent Sincerely,\\[6pt]
[AUTHOR_NAMES]
```

---

## Referee Response Block Structure

```latex
% ── Response to Associate Editor ───────────────────────────────────────────

\refereeheader{Response to the Associate Editor}

\comment{1}{[Exact AE comment text pasted here]}
[Response text. \msloc{Section X.Y, p. N}]

% ── Response to Referee 1 ──────────────────────────────────────────────────

\refereeheader{Response to Referee 1}

\noindent We thank Referee 1 for the careful reading and the constructive
suggestions. We address each comment in turn below.

\comment{1}{[Exact referee comment text]}
[Response. \msloc{Section X.Y, p. N}]

\comment{2}{[Exact referee comment text]}
[Response.]

% ── Closing ────────────────────────────────────────────────────────────────

\end{document}
```

---

## Tone Quick Reference

| Do | Don't |
|----|-------|
| "We thank the referee for this observation." | "We disagree with the referee." |
| "We have added a robustness check to Section 4.2." | "As we already showed in the original draft..." |
| "The referee raises an important concern about..." | "The referee misunderstood our approach." |
| "We did not implement this suggestion because [reason]." | "This is beyond the scope of the paper." |
| "See Equation (7) and the surrounding discussion." | "See the paper." |

---

## Configurable Parameters

Before first use, fill in these values in CLAUDE.md or tell the agent:

```
PAPER_TITLE:   [Full title of your paper]
JOURNAL_NAME:  [Journal name, e.g., "the American Economic Review"]
AUTHOR_NAMES:  [Author 1, Author 2, Author 3]
EDITOR_NAME:   [Editor's name and title]
```
