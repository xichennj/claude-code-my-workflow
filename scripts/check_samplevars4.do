log using "C:\Users\xc77\my-rr-agent\output\check_samplevars4.log", replace text
use "C:\Users\xc77\Dropbox\data_clean\MCBS_PUF_all_years.dta", clear

gen stroke_imp = (HLT_OCSTROKE_imp == 1)
gen paral_imp  = (HLT_OCPPARAL_imp == 1)
gen parkin_imp = (HLT_OCPARKIN_imp == 1)
gen neuro_ctrl = (stroke_imp==1 | paral_imp==1 | parkin_imp==1) & hlth_adrd!=1

di "=== payment2 distribution ==="
tab payment2, missing

di "=== ls_prob_paybill distribution ==="
tab ls_prob_paybill, missing

di "=== ins_ma==1, vet!=1, adrd or ctrl + non-missing care_access ==="
count if ins_ma==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access)
di r(N)

di "=== ins_ma==1, vet!=1, adrd or ctrl + non-missing care_access + payment2 ==="
count if ins_ma==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(payment2)
di r(N)

di "=== ins_ma==1, vet!=1, adrd or ctrl + non-missing care_access + ls_prob_paybill ==="
count if ins_ma==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(ls_prob_paybill)
di r(N)

* Try the exact target: see what restriction gives 5353
di "=== ins_ma2, vet!=1, adrd or ctrl, non-missing care_access + payment2 + access_sp + sat_quality ==="
count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1) & !missing(care_access) & !missing(payment2) & !missing(access_sp) & !missing(sat_quality)
di r(N)

di "=== ADRD/Control breakdown for best approximation ==="
* Best so far: ins_ma2, non-missing care_access (N=5511)
count if ins_ma2==1 & vet!=1 & hlth_adrd==1 & !missing(care_access)
di "ADRD (ins_ma2 + care_access nonmissing): " r(N)
count if ins_ma2==1 & vet!=1 & neuro_ctrl==1 & !missing(care_access)
di "Control (ins_ma2 + care_access nonmissing): " r(N)

log close
