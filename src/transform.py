"""Generic CSV cleaning template for public e-governance data.

Run from repository root:
    python src/transform.py

Before running, place a CSV in data/raw/ or change INPUT_FILE below.
This script does not assume a particular portal schema.
"""
from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
OUT_DIR = ROOT / "data" / "processed"
INPUT_FILE = RAW_DIR / "source_file.csv"


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Input not found: {INPUT_FILE}. Put your selected public CSV in data/raw/ "
            "and name it source_file.csv, or update INPUT_FILE in src/transform.py."
        )

    df = pd.read_csv(INPUT_FILE, encoding="utf-8", low_memory=False)
    rows_before = len(df)
    original_columns = list(df.columns)

    # Standardize column names.
    df.columns = (
        df.columns.astype(str).str.strip().str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )

    # Trim text and normalize common missing-value markers.
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = df[col].astype("string").str.strip()
        df[col] = df[col].replace({
            "": pd.NA, "NA": pd.NA, "N/A": pd.NA,
            "null": pd.NA, "NULL": pd.NA, "None": pd.NA
        })

    duplicate_count = int(df.duplicated().sum())
    df = df.drop_duplicates()

    # Report quality after basic cleaning. Do not automatically impute values.
    quality = pd.DataFrame({
        "column": df.columns,
        "dtype": [str(df[c].dtype) for c in df.columns],
        "missing_count": [int(df[c].isna().sum()) for c in df.columns],
        "missing_percent": [
            round(float(df[c].isna().mean() * 100), 2) for c in df.columns
        ],
        "unique_values": [int(df[c].nunique(dropna=True)) for c in df.columns],
    })

    df.to_csv(OUT_DIR / "cleaned_data.csv", index=False, encoding="utf-8")
    quality.to_csv(OUT_DIR / "quality_summary.csv", index=False, encoding="utf-8")

    print(f"Input rows: {rows_before}")
    print(f"Exact duplicate rows removed: {duplicate_count}")
    print(f"Output rows: {len(df)}")
    print(f"Original columns: {original_columns}")
    print(f"Cleaned columns: {list(df.columns)}")
    print(f"Saved: {OUT_DIR / 'cleaned_data.csv'}")
    print(f"Saved: {OUT_DIR / 'quality_summary.csv'}")


if __name__ == "__main__":
    main()
