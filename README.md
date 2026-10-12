# Public Data Acquisition and Transformation — Week 2

**Prepared by:** Lucky Chaurasiya  
**Project area:** E-Governance and Data Analysis

## Objective
Document a repeatable process for finding, acquiring, cleaning, validating, and preparing public data about digital services and e-governance.

## Candidate official sources
- India Open Government Data Platform: https://data.gov.in/
- OGD Platform help: https://www.data.gov.in/help
- API Setu: https://apisetu.gov.in/aboutus
- National Government Services Portal: https://services.india.gov.in/
- India.gov.in — Governance and Planning: https://www.india.gov.in/category/governance-planning

These are candidate starting points. Before using a particular resource, verify its publisher, dataset metadata, update date, licence/terms, format, and access conditions. This repository does not claim that a dataset has already been acquired from these sources.

## Folder structure
- `data/raw/`: unchanged original source files. Do not commit restricted or personal data.
- `data/processed/`: transformed outputs.
- `src/transform.py`: reusable CSV cleaning and quality-report script.
- `reports/acquisition_log_template.csv`: record the source and retrieval details.
- `reports/data_dictionary_template.csv`: define fields and transformations.
- `reports/Week2_Public_Data_Acquisition_Transformation.docx`: place the finalized report here.

## Run the transformation script
1. Install Python 3.10+.
2. Install dependencies: `pip install -r requirements.txt`
3. Put the selected public CSV file in `data/raw/`.
4. Edit `INPUT_FILE` in `src/transform.py` if needed.
5. Run from the repository root: `python src/transform.py`

The script writes `cleaned_data.csv` and `quality_summary.csv` under `data/processed/`.

## Responsible use
Use official downloads or documented APIs where possible. Scrape only if permitted by site terms and access rules. Do not bypass logins, CAPTCHAs, rate limits, or other controls. Keep API keys out of GitHub. The sample script is a generic template; adapt column-specific validation rules to the chosen dataset.
