"""
Apply the 8 major recommendations to the HCAP dementia abstract.
Builds on the first-round edited file (_edited.docx) -> saves as _edited_v2.docx.
Placeholders [AUTHOR TO SPECIFY: ...] mark items needing author-supplied numbers.
"""

import shutil
import docx

SRC = r"C:\Users\xc77\Dropbox\Algorithmic Performance and Fairness of Dementia in HCAP_edited.docx"
DST = r"C:\Users\xc77\Dropbox\Algorithmic Performance and Fairness of Dementia in HCAP_edited_v2.docx"

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
# Apply recommendations
# ---------------------------------------------------------------------------

for para in doc.paragraphs:
    ft = full_text(para)

    # ── REC 1: Reframe study type ────────────────────────────────────────────
    edit(para,
         "This cross-sectional study used",
         "This prediction model development and validation study used",
         "Rec 1 (Design): 'cross-sectional study' -> 'prediction model development and validation study'")

    # ── REC 2: Name the reference standard ──────────────────────────────────
    edit(para,
         "clinician-validated dementia classifications",
         "the Langa-Weir clinician-adjudicated dementia classification as the reference standard",
         "Rec 2 (Design): named reference standard (Langa-Weir)")

    # ── REC 3: Train/test methodology ───────────────────────────────────────
    # Insert a placeholder sentence after the Super Learner sentence.
    # The Super Learner sentence ends with "Super Learner." (before Rec 8 adds the parenthetical)
    # We handle Rec 8 in the same pass below, so match the current text here.
    edit(para,
         "We compared performance across six algorithms, including logistic regression, LASSO, random forest (RF), support vector machine (SVM), XGBoost, and Super Learner.",
         "We compared performance across six algorithms, including logistic regression, LASSO, random forest (RF), support vector machine (SVM), XGBoost, and Super Learner (an ensemble of the preceding five base learners). "
         "Models were trained on a randomly partitioned training set and evaluated on a held-out test set "
         "[AUTHOR TO SPECIFY: e.g., 80/20 split with 5-fold cross-validation — please replace with the actual approach used].",
         "Rec 3 + Rec 8 (Main Outcomes): added train/test placeholder sentence; clarified Super Learner as ensemble")

    # ── REC 4: Add 'develop' to the Objective ───────────────────────────────
    edit(para,
         "To evaluate predictive performance and algorithmic fairness of six algorithms",
         "To develop and evaluate the predictive performance and algorithmic fairness of six machine learning algorithms",
         "Rec 4 (Objective): added 'develop and'; added 'machine learning' for precision")

    # ── REC 5: Quantify comparison with existing algorithms ─────────────────
    edit(para,
         "Compared with widely used existing HRS dementia algorithms, these models demonstrated substantially improved case detection.",
         "Compared with widely used existing HRS dementia algorithms "
         "[AUTHOR TO SPECIFY: insert sensitivity of existing algorithm, e.g., 'sensitivity: X%'], "
         "these models demonstrated improved sensitivity across all six algorithms (range: 0.81–0.93).",
         "Rec 5 (Results): inserted placeholder for baseline sensitivity; replaced 'substantially improved case detection' with quantified range")

    # ── REC 6a: Clarify fairness direction in Key Points – Findings ──────────
    edit(para,
         "with Hispanic and male participants showing systematically lower equal opportunity "
         "and predictive equality in several models",
         "with Hispanic and male participants showing lower sensitivity (equal opportunity) "
         "and lower false positive rates (predictive equality) in several models, "
         "indicating a pattern of systematic under-detection in these groups",
         "Rec 6a (KP Findings): specified direction of fairness violations — lower TPR and lower FPR = systematic under-detection")

    # ── REC 6b: Clarify fairness direction in Results ────────────────────────
    edit(para,
         "indicating that Hispanic participants and male participants were more likely "
         "to have dementia cases missed by the algorithms.",
         "indicating that Hispanic participants and male participants had lower sensitivity "
         "(more missed dementia cases) and lower false positive rates across several models, "
         "a pattern consistent with systematic under-detection. "
         "Fairness disparities and overall accuracy varied across algorithms "
         "[AUTHOR TO SPECIFY: if any single model achieved both acceptable fairness and high performance, note it here].",
         "Rec 6b (Results): clarified both directions of fairness violation; added placeholder for fairness-performance frontier note")

    # ── REC 7: Acknowledge absence of external validation ────────────────────
    edit(para,
         "potentially magnifying disparities in dementia detection.",
         "potentially magnifying disparities in dementia detection. "
         "Findings require external validation in independent cohorts before clinical or research deployment.",
         "Rec 7 (Conclusions): added external validation caveat")


# ---------------------------------------------------------------------------
# Save and report
# ---------------------------------------------------------------------------

doc.save(DST)

SEP = "-" * 65
print(SEP)
print("HCAP ABSTRACT v2 EDITS COMPLETE")
print(SEP)
print(f"Source  : {SRC}")
print(f"Saved   : {DST}")
print()

done = [(s, l) for s, l in log if s == "DONE"]
miss = [(s, l) for s, l in log if s == "MISS"]

print(f"Changes applied ({len(done)}):")
for _, label in done:
    print(f"  [DONE] {label}")

if miss:
    filtered = [(s, l) for s, l in miss
                if any(k in l for k in ["Rec 1", "Rec 2", "Rec 3", "Rec 4",
                                        "Rec 5", "Rec 6", "Rec 7", "Rec 8"])]
    if filtered:
        print(f"\n  [WARNING] The following targeted edits did not match:")
        for _, label in filtered:
            print(f"    [MISS] {label}")

print()
print("Placeholders requiring author input:")
print("  [AUTHOR TO SPECIFY] in Main Outcomes: training/test split methodology")
print("  [AUTHOR TO SPECIFY] in Results: baseline sensitivity of existing algorithms")
print("  [AUTHOR TO SPECIFY] in Results: whether any model achieves fairness-performance balance")
print()
print("View track changes: Word > Review > Compare > Compare Documents")
print("  Base (first-round edits) : ...HCAP_edited.docx")
print("  Revised (this version)   : ...HCAP_edited_v2.docx")
