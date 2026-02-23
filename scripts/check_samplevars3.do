log using "C:\Users\xc77\my-rr-agent\output\check_samplevars3.log", replace text
use "C:\Users\xc77\Dropbox\data_clean\MCBS_PUF_all_years.dta", clear

gen stroke_imp = (HLT_OCSTROKE_imp == 1)
gen paral_imp  = (HLT_OCPPARAL_imp == 1)
gen parkin_imp = (HLT_OCPARKIN_imp == 1)
gen neuro_ctrl = (stroke_imp==1 | paral_imp==1 | parkin_imp==1) & hlth_adrd!=1

* Candidate analytical samples with progressively stricter restrictions
di "=== (1) ins_ma2==1, vet!=1, adrd or ctrl ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1)
di r(N)

di "=== (2) + non-missing on care_access ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access)
di r(N)

di "=== (3) + non-missing on payment ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(payment)
di r(N)

di "=== (4) + non-missing on access_sp ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(payment) & !missing(access_sp)
di r(N)

di "=== (5) + non-missing on sat_quality ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(payment) & !missing(access_sp) & !missing(sat_quality)
di r(N)

* Try without payment (payment has 23% missing overall)
di "=== (6) ins_ma2==1, vet!=1, adrd or ctrl, non-missing care_access + access_sp + sat_quality ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(access_sp) & !missing(sat_quality)
di r(N)

* Breakdown of best candidate
di "=== Breakdown at spec (2): ins_ma2==1, vet!=1, non-missing care_access ==="
count if ins_ma2==1 & vet!=1 & hlth_adrd==1 & !missing(care_access)
di "ADRD: " r(N)
count if ins_ma2==1 & vet!=1 & neuro_ctrl==1 & !missing(care_access)
di "Control: " r(N)

log close
