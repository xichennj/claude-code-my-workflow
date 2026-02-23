log using "C:\Users\xc77\my-rr-agent\output\check_uniqueN.log", replace text
use "C:\Users\xc77\Dropbox\data_clean\MCBS_PUF_all_years.dta", clear

gen stroke_imp = (HLT_OCSTROKE_imp == 1)
gen paral_imp  = (HLT_OCPPARAL_imp == 1)
gen parkin_imp = (HLT_OCPARKIN_imp == 1)
gen neuro_ctrl = (stroke_imp==1 | paral_imp==1 | parkin_imp==1) & hlth_adrd!=1

* Count unique beneficiaries (PUF_ID) per restriction
* vet: 1=ever served, 2=never served

di "=== (A) ins_ma2==1, vet!=1, adrd or ctrl — unique PUF_IDs ==="
preserve
keep if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1)
duplicates drop PUF_ID, force
count
di "Unique beneficiaries: " r(N)
count if hlth_adrd==1
di "  ADRD: " r(N)
count if neuro_ctrl==1
di "  Control: " r(N)
restore

di "=== (B) ins_ma==1, vet!=1, adrd or ctrl — unique PUF_IDs ==="
preserve
keep if ins_ma==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1)
duplicates drop PUF_ID, force
count
di "Unique beneficiaries: " r(N)
count if hlth_adrd==1
di "  ADRD: " r(N)
count if neuro_ctrl==1
di "  Control: " r(N)
restore

di "=== (C) ins_ma2==1, vet!=1, adrd or ctrl, care_access nonmissing — unique PUF_IDs ==="
preserve
* keep only obs where care_access is non-missing, then count unique IDs
* (i.e., ID had at least one valid observation)
keep if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access)
duplicates drop PUF_ID, force
count
di "Unique beneficiaries: " r(N)
restore

log close
