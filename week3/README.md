# Week 3 — Data Preparation, Cleaning, and Preprocessing

**Prepared by:** Lucky Chaurasiya  
**Project:** E-Governance and Data Analysis

## Objective
Provide a reproducible workflow for profiling, cleaning, validating, and preparing public digital-service datasets for analysis.

## Workflow
1. Preserve raw data and record source details.
2. Profile columns, data types, missing values, and duplicates.
3. Standardize column names and trim text.
4. Investigate missing values and duplicates before changing records.
5. Screen possible outliers with domain rules or IQR; do not automatically delete them.
6. Apply numeric scaling and categorical encoding only when appropriate.
7. Validate the cleaned output and record changes.

## Tools
- Python, Pandas, NumPy
- scikit-learn for modelling pipelines
- Excel/Power Query or Power BI Power Query for visual workflows

## Run
1. Install Python 3.10+.
2. Run `pip install -r requirements.txt` from the repository root.
3. Put the chosen CSV file at `week3/data/raw/source_file.csv`.
4. Run `python week3/src/clean_data.py`.

The script writes `cleaned_data.csv` and `quality_summary.csv` to `week3/data/processed/`.

## Notes
This is a generic template and does not claim that a real government dataset has been processed. Adapt column-specific checks to the selected dataset. Keep original data unchanged and do not commit restricted data, personal information, or API credentials.
