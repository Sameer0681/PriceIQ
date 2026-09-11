import os
import pandas as pd
import joblib

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "price_prediction_model.joblib")

_model = None

def _load_model():
    global _model
    if _model is None:
        if not os.path.exists(MODEL_PATH):
            raise FileNotFoundError(
                "Model file not found. Please run: python ml/train_price_model.py"
            )
        _model = joblib.load(MODEL_PATH)
    return _model

def predict_price(brand, model, ram_gb, storage_gb, age_years, battery_health, condition):
    pipeline = _load_model()
    input_df = pd.DataFrame([{
        "brand": brand,
        "model": model,
        "ram_gb": float(ram_gb),
        "storage_gb": float(storage_gb),
        "age_years": float(age_years),
        "battery_health": float(battery_health),
        "condition": condition
    }])
    predicted = pipeline.predict(input_df)[0]
    return round(float(predicted), 2)
