log using "C:\Users\xc77\my-rr-agent\output\check_samplevars.log", replace text
use "C:\Users\xc77\Dropbox\data_clean\MCBS_PUF_all_years.dta", clear

di "=== ins_ma ==="
tab ins_ma, missing

di "=== ins_ma2 ==="
tab ins_ma2, missing

di "=== vet ==="
tab vet, missing

di "=== hlth_adrd ==="
tab hlth_adrd, missing

di "=== HLT_OCSTROKE (stroke indicator) ==="
tab HLT_OCSTROKE, missing

di "=== HLT_OCPPARAL (paralysis indicator) ==="
tab HLT_OCPPARAL, missing

di "=== HLT_OCPARKIN (Parkinson's indicator) ==="
tab HLT_OCPARKIN, missing

di "=== care_access ==="
tab care_access, missing

di "=== payment ==="
tab payment, missing

di "=== access_sp ==="
tab access_sp, missing

di "=== sat_quality ==="
tab sat_quality, missing

* Quick count of analytical sample using likely restrictions
di "=== Analytical sample N (ins_ma==1, vet==0, adrd or control) ==="
gen control_cand = (HLT_OCSTROKE==1 | HLT_OCPPARAL==1 | HLT_OCPARKIN==1) & hlth_adrd==0
count if ins_ma==1 & vet==0 & (hlth_adrd==1 | control_cand==1)
di "  ins_ma==1, vet==0, (adrd or neurological control): N = " r(N)

log close
