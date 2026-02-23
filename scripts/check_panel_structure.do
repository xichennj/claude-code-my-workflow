log using "C:\Users\xc77\my-rr-agent\output\check_panel_structure.log", replace text
use "C:\Users\xc77\Dropbox\data_clean\MCBS_PUF_all_years.dta", clear

di "=== Obs and vars ==="
di "N obs: " _N

di "=== Year distribution ==="
tab year, missing

di "=== Obs per year ==="
bysort year: gen n_yr = _N
tab n_yr year, missing

di "=== Is PUF_ID unique within year? ==="
duplicates report PUF_ID year

di "=== Any variable that might serve as cross-year person ID? ==="
* Look for any variable with name containing 'id', 'bene', 'pers', 'link'
describe *id* *bene* *pers* *link* *pid* 2>/dev/null

di "=== Checking if any non-PUF variable repeats across years ==="
* If any variable repeats across years within a person, it could be a person ID
* Check how many unique PUF_ID values vs total obs
di "Total obs: " _N
duplicates report PUF_ID
di "Unique PUF_IDs: checked above"

log close
