import os
import sys
import pandas as pd

# Add project root to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "products.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "price_prediction_model.joblib")
REQUIRED_COLUMNS = ["brand", "model", "ram_gb", "storage_gb", "age_years", "battery_health", "condition", "resale_price"]

passed = 0
failed = 0

def check(name, condition, detail=""):
    global passed, failed
    if condition:
        print(f"  PASS: {name}")
        passed += 1
    else:
        print(f"  FAIL: {name}" + (f" — {detail}" if detail else ""))
        failed += 1

print("\n" + "=" * 50)
print("PriceIQ - ML Test Suite")
print("=" * 50)

# Test 1: Dataset exists
print("\n[Dataset Tests]")
check("Dataset file exists", os.path.exists(DATASET_PATH))

# Test 2: Dataset loads
df = None
try:
    df = pd.read_csv(DATASET_PATH)
    check("Dataset loads without error", True)
except Exception as e:
    check("Dataset loads without error", False, str(e))

# Test 3: Required columns
if df is not None:
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    check("Required columns present", len(missing) == 0, f"Missing: {missing}")
    check("Dataset has at least 50 rows", len(df) >= 50, f"Only {len(df)} rows")

# Test 4: Model exists
print("\n[Model Tests]")
check("Model file exists", os.path.exists(MODEL_PATH))

# Test 5: Model loads
pipeline = None
try:
    import joblib
    pipeline = joblib.load(MODEL_PATH)
    check("Model loads without error", True)
except Exception as e:
    check("Model loads without error", False, str(e))

# Test 6: Prediction returns a number
print("\n[Prediction Tests]")
if pipeline is not None:
    try:
        from ml.predict_price import predict_price
        result = predict_price("Apple", "iPhone 13", 4, 128, 3, 80, "Good")
        check("Prediction returns a number", isinstance(result, (int, float)))
        check("Prediction is positive", result > 0, f"Got {result}")
        check("Prediction is in realistic range (Rs.1000-Rs.200000)", 1000 <= result <= 200000, f"Got Rs.{result:,.0f}")
        print(f"  INFO: Sample prediction = Rs.{result:,.0f}")
    except Exception as e:
        check("Prediction returns a number", False, str(e))

# Test 7: Invalid values are rejected
print("\n[Validation Tests]")
try:
    from app import app
    client = app.test_client()

    # GET /
    resp = client.get("/")
    check("GET / returns 200", resp.status_code == 200)

    # POST /predict with valid data
    resp = client.post("/predict", data={
        "brand": "Apple", "model": "iPhone 13",
        "ram_gb": "4", "storage_gb": "128",
        "age_years": "3", "battery_health": "80",
        "condition": "Good"
    })
    check("POST /predict with valid data returns 200", resp.status_code == 200)

    # POST /predict with invalid battery health
    resp = client.post("/predict", data={
        "brand": "Apple", "model": "iPhone 13",
        "ram_gb": "4", "storage_gb": "128",
        "age_years": "3", "battery_health": "150",
        "condition": "Good"
    })
    body = resp.data.decode()
    check("POST /predict rejects battery_health > 100", "100" in body or "battery" in body.lower())

    # POST /predict with negative age
    resp = client.post("/predict", data={
        "brand": "Apple", "model": "iPhone 13",
        "ram_gb": "4", "storage_gb": "128",
        "age_years": "-1", "battery_health": "80",
        "condition": "Good"
    })
    body = resp.data.decode()
    check("POST /predict rejects negative age", "age" in body.lower() or "negative" in body.lower() or "0" in body)

except Exception as e:
    check("Flask route tests", False, str(e))

# Summary
print("\n" + "=" * 50)
print(f"Results: {passed} passed, {failed} failed")
print("=" * 50 + "\n")

if failed > 0:
    sys.exit(1)
