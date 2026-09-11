# Dataset

## File: `products.csv`

This is a **synthetic/demo dataset** created for the PriceIQ college minor project.

The prices are **not real market prices**. They are realistic estimates used to demonstrate the machine learning model.

## Columns

| Column | Type | Description |
|---|---|---|
| brand | text | Smartphone brand (Apple, Samsung, etc.) |
| model | text | Smartphone model name |
| ram_gb | number | RAM in GB |
| storage_gb | number | Internal storage in GB |
| age_years | number | Age of the phone in years |
| battery_health | number | Battery health percentage (0–100) |
| condition | text | Physical condition (Excellent / Good / Fair / Poor) |
| original_price | number | Original launch price in INR |
| resale_price | number | Estimated resale price in INR (target variable) |

## Brands Covered

- Apple
- Samsung
- OnePlus
- Xiaomi
- Google
- Realme
- Vivo
- OPPO

## Validation

Run the validation script to check the dataset:

```bash
python dataset/validate_dataset.py
```
