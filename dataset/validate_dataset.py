import pandas as pd
import sys
import os

REQUIRED_COLUMNS = [
    "brand", "model", "ram_gb", "storage_gb",
    "age_years", "battery_health", "condition",
    "original_price", "resale_price"
]

def validate():
    csv_path = os.path.join(os.path.dirname(__file__), "products.csv")

    print("=" * 50)
    print("PriceIQ Dataset Validation Report")
    print("=" * 50)

    # File exists
    if not os.path.exists(csv_path):
        print("FAIL: products.csv not found.")
        sys.exit(1)
    print("PASS: products.csv found.")

    df = pd.read_csv(csv_path)
    print(f"INFO: {len(df)} rows, {len(df.columns)} columns.")

    # Required columns
    missing_cols = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing_cols:
        print(f"FAIL: Missing columns: {missing_cols}")
        sys.exit(1)
    print("PASS: All required columns present.")

    # Missing values
    nulls = df[REQUIRED_COLUMNS].isnull().sum()
    if nulls.any():
        print(f"WARN: Missing values found:\n{nulls[nulls > 0]}")
    else:
        print("PASS: No missing values.")

    # Duplicate rows
    dupes = df.duplicated().sum()
    if dupes:
        print(f"WARN: {dupes} duplicate rows found.")
    else:
        print("PASS: No duplicate rows.")

    # Numeric checks
    numeric_cols = ["ram_gb", "storage_gb", "age_years", "battery_health", "original_price", "resale_price"]
    for col in numeric_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            print(f"FAIL: Column '{col}' is not numeric.")
            sys.exit(1)
    print("PASS: All numeric columns are numeric.")

    # Positive prices
    if (df["resale_price"] <= 0).any():
        print("FAIL: Some resale_price values are <= 0.")
        sys.exit(1)
    print("PASS: All resale prices are positive.")

    # Battery health range
    if ((df["battery_health"] < 0) | (df["battery_health"] > 100)).any():
        print("FAIL: battery_health values out of range [0, 100].")
        sys.exit(1)
    print("PASS: Battery health values in range [0, 100].")

    # Age >= 0
    if (df["age_years"] < 0).any():
        print("FAIL: age_years contains negative values.")
        sys.exit(1)
    print("PASS: All age values are >= 0.")

    print("=" * 50)
    print("Validation complete. Dataset is ready.")
    print("=" * 50)

if __name__ == "__main__":
    validate()
