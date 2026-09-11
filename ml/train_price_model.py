import os
import sys
import pandas as pd
import numpy as np
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

DATASET_PATH = os.path.join(os.path.dirname(__file__), "..", "dataset", "products.csv")
MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "price_prediction_model.joblib")

FEATURES = ["brand", "model", "ram_gb", "storage_gb", "age_years", "battery_health", "condition"]
TARGET = "resale_price"
CATEGORICAL = ["brand", "model", "condition"]
NUMERICAL = ["ram_gb", "storage_gb", "age_years", "battery_health"]

def train():
    # 1. Load dataset
    if not os.path.exists(DATASET_PATH):
        print(f"ERROR: Dataset not found at {DATASET_PATH}")
        sys.exit(1)

    df = pd.read_csv(DATASET_PATH)
    print(f"Loaded {len(df)} rows from dataset.")

    # 2. Validate required columns
    required = FEATURES + [TARGET]
    missing = [c for c in required if c not in df.columns]
    if missing:
        print(f"ERROR: Missing columns: {missing}")
        sys.exit(1)

    # 3. Check for missing values
    if df[required].isnull().any().any():
        print("ERROR: Dataset contains missing values. Please clean the data first.")
        sys.exit(1)

    # 4. Prepare X and y
    X = df[FEATURES]
    y = df[TARGET]

    # 5. Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    print(f"Training samples: {len(X_train)}, Test samples: {len(X_test)}")

    # 6. Build preprocessing + model pipeline
    preprocessor = ColumnTransformer(transformers=[
        ("cat", OneHotEncoder(handle_unknown="ignore"), CATEGORICAL),
        ("num", "passthrough", NUMERICAL)
    ])

    pipeline = Pipeline(steps=[
        ("preprocessor", preprocessor),
        ("model", RandomForestRegressor(n_estimators=100, random_state=42))
    ])

    # 7. Train
    pipeline.fit(X_train, y_train)
    print("Model trained successfully.")

    # 8. Evaluate
    y_pred = pipeline.predict(X_test)
    mae = mean_absolute_error(y_test, y_pred)
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    r2 = r2_score(y_test, y_pred)

    # 9. Print metrics
    print("\n--- Model Evaluation ---")
    print(f"MAE  : Rs.{mae:,.0f}")
    print(f"RMSE : Rs.{rmse:,.0f}")
    print(f"R2   : {r2:.4f}")
    print("------------------------\n")

    # 10. Save model
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to: {MODEL_PATH}")

if __name__ == "__main__":
    train()
