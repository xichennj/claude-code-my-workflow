"""
Edit the HCAP dementia abstract for JAMA submission.
Saves edited copy; use Word Review > Compare Documents for tracked changes.
"""

import shutil
import docx

SRC = r"C:\Users\xc77\Dropbox\Algorithmic Performance and Fairness of Dementia in HCAP.docx"
DST = r"C:\Users\xc77\Dropbox\Algorithmic Performance and Fairness of Dementia in HCAP_edited.docx"

shutil.copy(SRC, DST)
doc = docx.Document(DST)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def full_text(para):
    return "".join(r.text for r in para.runs)


def replace_in_para(para, old, new):
    ft = full_text(para)
    if old not in ft:
        return False
    new_ft = ft.replace(old, new, 1)
    if para.runs:
        para.runs[0].text = new_ft
        for r in para.runs[1:]:
            r.text = ""
    return True


log = []

def edit(para, old, new, label):
    if replace_in_para(para, old, new):
        log.append(("DONE", label))
        return True
    log.append(("MISS", label))
    return False


# ---------------------------------------------------------------------------
# Apply edits paragraph by paragraph
# ---------------------------------------------------------------------------

for para in doc.paragraphs:
    ft = full_text(para)

    # ── TITLE ───────────────────────────────────────────────────────────────
    # "for Dementia in the Harmonized" is grammatically misleading;
    # adding "Classification Using" clarifies what the models do and the data source
    edit(para,
         "Machine Learning Models for Dementia in the Harmonized Cognitive Assessment Protocol (HCAP)",
         "Machine Learning Models for Dementia Classification Using the Harmonized Cognitive Assessment Protocol (HCAP)",
         "Title: 'for Dementia in the HCAP' -> 'for Dementia Classification Using the HCAP'")

    # ── KEY POINTS – QUESTION ───────────────────────────────────────────────
    # "perform accurate" is an adjective used where an adverb is needed
    edit(para,
         "perform accurate and equitably",
         "perform accurately and equitably",
         "KP Question: adverb fix 'accurate' -> 'accurately'")

    # ── KEY POINTS – FINDINGS ───────────────────────────────────────────────
    # "minority" is vague; Results specifically name Hispanic participants
    # "in select models" is imprecise
    edit(para,
         "with minority and male subgroups showing systematically lower equal opportunity and predictive equality in select models",
         "with Hispanic and male participants showing systematically lower equal opportunity and predictive equality in several models",
         "KP Findings: 'minority' -> 'Hispanic' (consistent with Results); 'select' -> 'several'")

    # ── IMPORTANCE ──────────────────────────────────────────────────────────
    # Subject-verb agreement: "algorithms…has" -> "have"
    # Tense consistency: present "are developed" -> past "were developed"
    edit(para,
         "most existing algorithms are developed on earlier cohorts and has rarely been evaluated for fairness",
         "most existing algorithms were developed using earlier cohorts and have rarely been evaluated for fairness",
         "Importance: subject-verb agreement ('has' -> 'have'); tense fix ('are developed' -> 'were developed')")

    # ── DESIGN, SETTING, AND PARTICIPANTS ───────────────────────────────────
    # "utilized" -> "used" (JAMA style preference)
    edit(para,
         "This cross-sectional study utilized",
         "This cross-sectional study used",
         "Design: 'utilized' -> 'used' (JAMA style)")

    # "aged 65 and older" -> "aged 65 years or older" (JAMA standard)
    edit(para,
         "Americans aged 65 and older",
         "Americans aged 65 years or older",
         "Design: 'aged 65 and older' -> 'aged 65 years or older' (JAMA style)")

    # Verbose promotional relative clause -> concise factual description
    # Note: contains \xa0 (non-breaking space) before "by employing"
    edit(para,
         "which advances prior dementia ascertainment\xa0by employing a comprehensive in-person neuropsychological battery and clinically validated dementia classification in a more recent, diverse older adult cohort",
         "a nationally representative study that used a comprehensive in-person neuropsychological battery and clinician-validated dementia classifications",
         "Design: replaced promotional relative clause with concise factual description of HCAP")

    # "Data analyses were performed" -> "Data were analyzed" (JAMA standard phrasing)
    edit(para,
         "Data analyses were performed from",
         "Data were analyzed from",
         "Design: 'Data analyses were performed' -> 'Data were analyzed' (JAMA style)")

    # ── MAIN OUTCOMES AND MEASURES ──────────────────────────────────────────
    # Specify "absolute" gaps for precision
    edit(para,
         "with gaps exceeding 0.10 considered meaningful disparities",
         "with absolute gaps exceeding 0.10 considered meaningful disparities",
         "Main Outcomes: added 'absolute' before 'gaps exceeding 0.10'")

    # ── RESULTS ─────────────────────────────────────────────────────────────
    # JAMA sex-language guidance: use "women/men" not "female/male" as nouns
    edit(para,
         "60.0% female",
         "60.0% women",
         "Results: 'female' -> 'women' (JAMA sex/gender language guidance)")

    # Remove "range:" label and fix inconsistent hyphen -> en dash in specificity range
    # En dash is U+2013 (–)
    edit(para,
         "accuracy (range: 0.83–0.91), sensitivity (range: 0.81–0.93), and specificity (range: 0.82-0.93)",
         "accuracy (0.83–0.91), sensitivity (0.81–0.93), and specificity (0.82–0.93)",
         "Results: removed 'range:' labels; fixed hyphen -> en dash in specificity range")

    # "Compared to" -> "Compared with" (JAMA style: 'with' for contrasts)
    # "our models" -> "these models" (avoid first-person possessive in results)
    edit(para,
         "Compared to widely used existing HRS dementia algorithms, our models demonstrated",
         "Compared with widely used existing HRS dementia algorithms, these models demonstrated",
         "Results: 'Compared to' -> 'Compared with' (JAMA style); 'our models' -> 'these models'")

    # "Hispanic groups" -> "Hispanic participants" (consistent terminology)
    edit(para,
         "indicating that Hispanic groups and male participants",
         "indicating that Hispanic participants and male participants",
         "Results: 'Hispanic groups' -> 'Hispanic participants'")

    # ── CONCLUSIONS AND RELEVANCE ────────────────────────────────────────────
    # Missing comma after appositive phrase "especially machine learning models"
    edit(para,
         "especially machine learning models demonstrated strong overall predictive performance",
         "especially machine learning models, demonstrated strong overall predictive performance",
         "Conclusions: added missing comma after 'especially machine learning models'")

    # "racial/ethnic and sex" reads as two items; should be three: racial, ethnic, and sex
    edit(para,
         "racial/ethnic and sex subgroups",
         "racial, ethnic, and sex subgroups",
         "Conclusions: 'racial/ethnic and sex' -> 'racial, ethnic, and sex' (three distinct categories)")


# ---------------------------------------------------------------------------
# Save and report
# ---------------------------------------------------------------------------

doc.save(DST)

SEP = "-" * 65
print(SEP)
print("HCAP ABSTRACT EDITS COMPLETE")
print(SEP)
print(f"Original : {SRC}")
print(f"Edited   : {DST}")
print()

done = [(s, l) for s, l in log if s == "DONE"]
miss = [(s, l) for s, l in log if s == "MISS"]

print(f"Changes applied ({len(done)}):")
for _, label in done:
    print(f"  [DONE] {label}")

if miss:
    print(f"\nMissed ({len(miss)}) -- text not found as expected:")
    for _, label in miss:
        print(f"  [MISS] {label}")

print()
print("View track changes: Word > Review > Compare > Compare Documents")
print(f"  Original : {SRC.split(chr(92))[-1]}")
print(f"  Revised  : {DST.split(chr(92))[-1]}")
