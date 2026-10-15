"""Generic data cleaning and quality summary template.
Run from repository root: python week3/src/clean_data.py
Place the selected CSV at week3/data/raw/source_file.csv.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
INPUT_FILE = ROOT / "week3" / "data" / "raw" / "source_file.csv"
OUTPUT_DIR = ROOT / "week3" / "data" / "processed"

def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Missing {INPUT_FILE}. Place your chosen public CSV there first."
        )
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT_FILE, encoding="utf-8", low_memory=False)
    rows_before = len(df)

    df.columns = (
        df.columns.astype(str).str.strip().str.lower()
          .str.replace(r"[^a-z0-9]+", "_", regex=True)
          .str.strip("_")
    )
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].astype("string").str.strip()
        df[col] = df[col].replace({
            "": pd.NA, "NA": pd.NA, "N/A": pd.NA,
            "null": pd.NA, "NULL": pd.NA
        })

    exact_duplicates = int(df.duplicated().sum())
    df = df.drop_duplicates()  # only exact duplicates; inspect key duplicates separately

    quality = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns],
        "missing_count": [int(df[c].isna().sum()) for c in df.columns],
        "missing_percent": [round(float(df[c].isna().mean() * 100), 2) for c in df.columns],
        "unique_values": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })
    df.to_csv(OUTPUT_DIR / "cleaned_data.csv", index=False, encoding="utf-8")
    quality.to_csv(OUTPUT_DIR / "quality_summary.csv", index=False, encoding="utf-8")
    print(f"Rows before: {rows_before}")
    print(f"Exact duplicates removed: {exact_duplicates}")
    print(f"Rows after: {len(df)}")
    print(f"Saved outputs to: {OUTPUT_DIR}")

if __name__ == "__main__":
    main()
