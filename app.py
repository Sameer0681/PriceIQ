import os
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

DATASET_PATH = os.path.join(os.path.dirname(__file__), "dataset", "products.csv")
CONDITIONS = ["Excellent", "Good", "Fair", "Poor"]

def get_brands_models():
    try:
        df = pd.read_csv(DATASET_PATH)
        brands = sorted(df["brand"].unique().tolist())
        models_by_brand = (
            df.groupby("brand")["model"]
            .apply(lambda x: sorted(x.unique().tolist()))
            .to_dict()
        )
        return brands, models_by_brand
    except Exception:
        return [], {}

def validate_form(form):
    errors = []
    brand = form.get("brand", "").strip()
    model = form.get("model", "").strip()
    condition = form.get("condition", "").strip()

    if not brand:
        errors.append("Brand is required.")
    if not model:
        errors.append("Model is required.")
    if condition not in CONDITIONS:
        errors.append("Please select a valid condition.")

    try:
        ram_gb = float(form.get("ram_gb", ""))
        if ram_gb <= 0:
            errors.append("RAM must be a positive number.")
    except ValueError:
        errors.append("RAM must be a valid number.")
        ram_gb = None

    try:
        storage_gb = float(form.get("storage_gb", ""))
        if storage_gb <= 0:
            errors.append("Storage must be a positive number.")
    except ValueError:
        errors.append("Storage must be a valid number.")
        storage_gb = None

    try:
        age_years = float(form.get("age_years", ""))
        if age_years < 0:
            errors.append("Age cannot be negative.")
    except ValueError:
        errors.append("Age must be a valid number.")
        age_years = None

    try:
        battery_health = float(form.get("battery_health", ""))
        if not (0 <= battery_health <= 100):
            errors.append("Battery health must be between 0 and 100.")
    except ValueError:
        errors.append("Battery health must be a valid number.")
        battery_health = None

    values = {
        "brand": brand, "model": model, "condition": condition,
        "ram_gb": ram_gb, "storage_gb": storage_gb,
        "age_years": age_years, "battery_health": battery_health
    }
    return errors, values

@app.route("/")
def index():
    brands, models_by_brand = get_brands_models()
    return render_template("index.html",
        brands=brands,
        models_by_brand=models_by_brand,
        conditions=CONDITIONS
    )

@app.route("/predict", methods=["POST"])
def predict():
    brands, models_by_brand = get_brands_models()
    errors, values = validate_form(request.form)

    if errors:
        return render_template("index.html",
            brands=brands,
            models_by_brand=models_by_brand,
            conditions=CONDITIONS,
            errors=errors,
            form_values=request.form
        )

    try:
        from ml.predict_price import predict_price
        price = predict_price(
            values["brand"], values["model"],
            values["ram_gb"], values["storage_gb"],
            values["age_years"], values["battery_health"],
            values["condition"]
        )
        return render_template("index.html",
            brands=brands,
            models_by_brand=models_by_brand,
            conditions=CONDITIONS,
            result=price,
            form_values=request.form
        )
    except FileNotFoundError as e:
        return render_template("index.html",
            brands=brands,
            models_by_brand=models_by_brand,
            conditions=CONDITIONS,
            errors=[str(e)],
            form_values=request.form
        )
    except Exception as e:
        return render_template("index.html",
            brands=brands,
            models_by_brand=models_by_brand,
            conditions=CONDITIONS,
            errors=["Prediction failed. Please check your inputs and try again."],
            form_values=request.form
        )

if __name__ == "__main__":
    app.run(debug=True)
