# Power BI Dashboard Plan

## Goal
Create a readable service-performance overview using the synthetic dataset. Label the dashboard **Synthetic Demo Data**.

## Import and preparation
1. Open Power BI Desktop → **Get data → Text/CSV**.
2. Select `data/e_governance_applications_synthetic.csv`.
3. Set `submission_date` and `completion_date` to Date, `processing_days` to Whole Number, `fee_amount_inr` to Decimal Number, and `satisfaction_rating` to Whole Number.
4. Keep blank completion dates and ratings as blank; do not replace them with zero.
5. Create a date table if you want time-intelligence visuals.

## Suggested report pages

### Page 1 — Service Overview
- Cards: Total Applications, Completion Rate, Rejection Rate, Pending Backlog, Median Processing Days.
- Line chart: applications submitted by month.
- Bar chart: applications by service type and status.
- Slicers: submission date, district, service type, channel.

### Page 2 — Processing & Backlog
- Bar chart: pending applications by service type.
- Bar chart: median processing days by service type.
- Matrix: district × status.
- Table: service type, total applications, pending backlog, median processing days.

### Page 3 — Rejections & Citizen Feedback
- Bar chart: rejection count by rejection reason.
- Bar chart: complaint count by complaint category, excluding `None`.
- Column chart: average satisfaction rating by service type.
- Add a note that satisfaction is available only for a subset of completed records and may be affected by response bias.

## Suggested DAX measures

```DAX
Total Applications =
DISTINCTCOUNT(e_governance_applications_synthetic[application_id])

Completed Applications =
CALCULATE(
    [Total Applications],
    e_governance_applications_synthetic[status] = "Completed"
)

Completion Rate =
DIVIDE([Completed Applications], [Total Applications], 0)

Rejected Applications =
CALCULATE(
    [Total Applications],
    e_governance_applications_synthetic[status] = "Rejected"
)

Decided Applications =
CALCULATE(
    [Total Applications],
    e_governance_applications_synthetic[status] IN {"Completed", "Rejected"}
)

Rejection Rate =
DIVIDE([Rejected Applications], [Decided Applications], 0)

Pending Backlog =
CALCULATE(
    [Total Applications],
    e_governance_applications_synthetic[status] IN {"Pending", "In Review"}
)

Median Processing Days =
MEDIAN(e_governance_applications_synthetic[processing_days])

Average Satisfaction =
AVERAGE(e_governance_applications_synthetic[satisfaction_rating])

Applications with Complaints =
CALCULATE(
    [Total Applications],
    e_governance_applications_synthetic[complaint_category] <> "None"
)
```

Format Completion Rate and Rejection Rate as percentages. Depending on locale, Power BI may use semicolons instead of commas in DAX. Check the column/table names after importing.

## Design guidance
- Use a restrained orange, charcoal, and light background palette.
- Keep KPI definitions in tooltips or a definitions panel.
- Use consistent scales and clearly labelled units.
- Include a visible “Synthetic Demo Data — not actual government statistics” disclaimer.
- Do not publish row-level applicant information.
