# E-Governance Service Analytics Dashboard

> **Yuva Intern — Week 1: Strategic Planning and Data Analysis Framework Development**

A portfolio-ready data analytics project that demonstrates how synthetic public-service application data can be cleaned, analysed, and translated into practical service-improvement KPIs.

**Important:** The included CSV is entirely synthetic and created for demonstration. It is not real government data and does not describe actual performance in any district or department.

## Project objectives

- Measure application outcomes and service workload.
- Examine completion rates, pending backlog, rejection reasons, and processing time.
- Compare service types, districts, and submission channels descriptively.
- Propose a Power BI dashboard and an evidence-led improvement workflow.
- Document data quality, privacy, fairness, and interpretation risks.

## Tech stack

- Python 3.10+
- Pandas and NumPy
- Matplotlib
- Jupyter Notebook
- Power BI Desktop (optional dashboard implementation)

## Repository structure

```text
e-governance-data-analysis/
├── data/
│   └── e_governance_applications_synthetic.csv
├── notebooks/
│   └── e_governance_analysis.ipynb
├── dashboard/
│   └── POWER_BI_DASHBOARD_PLAN.md
├── reports/
│   ├── WEEK1_REPORT_INTEGRATION.md
│   └── Week1_Strategic_Plan.docx   # add the submitted Word report here
├── images/
│   └── (add dashboard screenshots here)
├── src/
│   └── analysis.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Dataset overview

The sample contains **5,000 synthetic application records** and 15 columns:

| Column | Meaning |
|---|---|
| `application_id` | Synthetic record key |
| `district` | Example district in Madhya Pradesh |
| `service_type` | Type of public service requested |
| `submission_date` | Application submission date |
| `completion_date` | Completion date; blank when not completed |
| `status` | Completed, Pending, Rejected, or In Review |
| `channel` | Web Portal, Mobile App, or Service Center |
| `applicant_age_group` | Broad age band, not exact age |
| `applicant_gender` | Synthetic demographic category |
| `processing_days` | Processing duration for completed records |
| `rejection_reason` | Reason for rejected applications |
| `complaint_category` | Synthetic complaint category |
| `satisfaction_rating` | Optional rating from 1 to 5 |
| `fee_amount_inr` | Synthetic example fee |
| `is_synthetic` | Always `True` |

## Run the analysis

1. Download or clone this repository.
2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```
3. Start Jupyter:

   ```bash
   jupyter notebook
   ```
4. Open `notebooks/e_governance_analysis.ipynb` and run all cells.

Alternatively, run the script:

```bash
python src/analysis.py
```

The script prints summary tables and saves CSV summaries in `outputs/`. These outputs are reproducible from the synthetic dataset.

## Core KPIs

- **Completion rate:** completed applications / all applications × 100
- **Rejection rate:** rejected applications / all decided applications × 100
- **Pending backlog:** count of Pending and In Review applications
- **Median processing time:** median processing days among completed applications
- **On-time completion:** completed applications within a defined target / completed applications × 100
- **Complaint share:** records with a non-`None` complaint category / all records × 100
- **Average satisfaction:** mean of available satisfaction ratings

For this demo, the on-time target is configurable and is not an official service standard. In a real project, use the published service timeline for each service and document the source.

## Suggested analytical questions

1. Which service types have the largest backlog?
2. Which services have the longest median processing time?
3. How do application outcomes vary by channel?
4. What rejection reasons occur most often?
5. Which complaint categories appear most frequently?
6. What should be investigated before recommending a process change?

## Interpretation guardrails

- Results are descriptive and reflect only this generated sample.
- Group differences do not establish causation.
- A blank satisfaction rating is missing data, not a zero.
- Do not infer that a district or demographic group performs similarly in real life.
- For real data, obtain authorisation, minimise personal data, restrict access, document data quality, and aggregate outputs to reduce disclosure risk.

## Power BI dashboard

See [`dashboard/POWER_BI_DASHBOARD_PLAN.md`](dashboard/POWER_BI_DASHBOARD_PLAN.md) for page layout, data model, KPI definitions, and suggested DAX measures.

## Yuva Intern Week 1 report integration

See [`reports/WEEK1_REPORT_INTEGRATION.md`](reports/WEEK1_REPORT_INTEGRATION.md). Copy the final Word report into `reports/Week1_Strategic_Plan.docx` before committing it. Ensure the report reflects your own review and work.

## Next steps

- Run the notebook and validate all generated outputs.
- Build the Power BI `.pbix` file and export a screenshot to `images/`.
- Add a short **Findings from the synthetic sample** section with actual values produced by your run.
- Replace the demo target with a verified official service standard only if using a real, cited source.

## Author

Lucky Chaurasiya  
GitHub: https://github.com/chaurasiyalucky241-cmd
