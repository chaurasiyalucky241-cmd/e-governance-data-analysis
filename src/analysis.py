from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "e_governance_applications_synthetic.csv"
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)

df = pd.read_csv(DATA, parse_dates=["submission_date", "completion_date"])
df["processing_days"] = pd.to_numeric(df["processing_days"], errors="coerce")
df["satisfaction_rating"] = pd.to_numeric(df["satisfaction_rating"], errors="coerce")

print("Dataset shape:", df.shape)
print("\nMissing values:\n", df.isna().sum().sort_values(ascending=False))
print("\nDuplicate application IDs:", df["application_id"].duplicated().sum())
print("\nStatus distribution:\n", df["status"].value_counts())

total = df["application_id"].nunique()
completed = (df["status"] == "Completed").sum()
rejected = (df["status"] == "Rejected").sum()
decided = df["status"].isin(["Completed", "Rejected"]).sum()
backlog = df["status"].isin(["Pending", "In Review"]).sum()
kpis = pd.DataFrame([{
    "total_applications": total,
    "completion_rate_pct": round(completed / total * 100, 2) if total else 0,
    "rejection_rate_pct": round(rejected / decided * 100, 2) if decided else 0,
    "pending_backlog": int(backlog),
    "median_processing_days": df.loc[df["status"] == "Completed", "processing_days"].median(),
    "average_satisfaction": df["satisfaction_rating"].mean()
}])
print("\nKPI summary:\n", kpis.to_string(index=False))
kpis.to_csv(OUT / "kpi_summary.csv", index=False)

service_summary = df.groupby("service_type").agg(
    applications=("application_id", "nunique"),
    completed=("status", lambda s: (s == "Completed").sum()),
    rejected=("status", lambda s: (s == "Rejected").sum()),
    pending_or_review=("status", lambda s: s.isin(["Pending", "In Review"]).sum()),
    median_processing_days=("processing_days", "median")
).reset_index()
service_summary.to_csv(OUT / "service_summary.csv", index=False)
print("\nService summary:\n", service_summary.to_string(index=False))

rejections = (df.loc[df["status"] == "Rejected", "rejection_reason"]
              .value_counts().rename_axis("rejection_reason").reset_index(name="count"))
rejections.to_csv(OUT / "rejection_reasons.csv", index=False)

monthly = df.assign(submission_month=df["submission_date"].dt.to_period("M").astype(str))
monthly_counts = monthly.groupby("submission_month").size().reset_index(name="applications")
monthly_counts.to_csv(OUT / "monthly_applications.csv", index=False)

ax = service_summary.sort_values("applications").plot(
    kind="barh", x="service_type", y="applications", legend=False, figsize=(9, 5)
)
ax.set_title("Applications by Service Type (Synthetic Demo)")
ax.set_xlabel("Number of applications")
ax.set_ylabel("")
plt.tight_layout()
plt.savefig(OUT / "applications_by_service.png", dpi=160)
plt.close()
print(f"\nOutputs saved to: {OUT}")
