log using "C:\Users\xc77\my-rr-agent\output\check_samplevars2.log", replace text
use "C:\Users\xc77\Dropbox\data_clean\MCBS_PUF_all_years.dta", clear

* Use imputed neurological condition variables (avoids missing-value issues)
* Use HLT_OCSTROKE_imp, HLT_OCPPARAL_imp, HLT_OCPARKIN_imp (float, _imp suffix)
* vet: 1=ever served, 2=never served, 100=DK/RF — non-veterans are vet!=1

di "=== vet coding ==="
tab vet, missing

di "=== Try ins_ma==1, vet!=1, (adrd or neurological control) ==="
gen stroke_imp  = (HLT_OCSTROKE_imp == 1)
gen paral_imp   = (HLT_OCPPARAL_imp == 1)
gen parkin_imp  = (HLT_OCPARKIN_imp == 1)
gen neuro_ctrl  = (stroke_imp==1 | paral_imp==1 | parkin_imp==1) & hlth_adrd!=1

count if ins_ma==1  & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1)
di "  ins_ma==1, vet!=1, (adrd or neuro_ctrl): N = " r(N)

count if ins_ma2==1 & vet!=1 & (hlth_adrd==1 | neuro_ctrl==1)
di "  ins_ma2==1, vet!=1, (adrd or neuro_ctrl): N = " r(N)

di "=== Breakdown by ins_ma, ins_ma2, adrd vs control ==="
count if ins_ma==1  & vet!=1 & hlth_adrd==1
di "  ADRD (ins_ma): " r(N)
count if ins_ma==1  & vet!=1 & neuro_ctrl==1
di "  Control (ins_ma): " r(N)

count if ins_ma2==1 & vet!=1 & hlth_adrd==1
di "  ADRD (ins_ma2): " r(N)
count if ins_ma2==1 & vet!=1 & neuro_ctrl==1
di "  Control (ins_ma2): " r(N)

log close
