<<<<<<< HEAD
# PriceIQ — AI-Based Used Smartphone Price Prediction

> **"From Data to Price."**

A college minor project that uses Machine Learning to estimate the resale price of a used smartphone based on its specifications and condition.

---

## 1. Problem Statement

When selling or buying a used smartphone, it is difficult to know the fair resale price. The price depends on many factors — brand, model, RAM, storage, age, battery health, and physical condition. There is no simple formula. People either overprice or underprice their devices.

---

## 2. Objective

PriceIQ uses a Machine Learning model (Random Forest Regressor) trained on smartphone data to predict the estimated resale price from a user's input. The user fills a simple web form and gets an instant price estimate.

---

## 3. Features

- Web-based form to enter smartphone details
- Instant AI-generated resale price estimate
- Smart dropdowns populated from the dataset
- Input validation with friendly error messages
- Clean, responsive single-page design
- Fully Python-based backend (Flask + scikit-learn)

---

## 4. Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Flask | Web framework — serves pages, handles form submission |
| Pandas | Data loading and manipulation |
| scikit-learn | Machine Learning (Random Forest, Pipeline, OneHotEncoder) |
| Joblib | Saving and loading the trained model |
| HTML / CSS | Frontend — form and result display |
| Jinja2 | HTML templating (built into Flask) |

---

## 5. How It Works

```
User fills the form
        ↓
Flask receives the POST request
        ↓
Input is validated
        ↓
predict_price() is called
        ↓
Saved Pipeline loads the model
        ↓
OneHotEncoder encodes brand/model/condition
        ↓
Random Forest predicts the resale price
        ↓
Flask renders the result back to the page
```

---

## 6. Dataset

**File:** `dataset/products.csv`

**Note: This is a synthetic/demo dataset created for this college project. The prices are NOT real market prices. They are realistic estimates used to demonstrate the machine learning model.**

The dataset contains 122 records covering:
- 8 brands: Apple, Samsung, OnePlus, Xiaomi, Google, Realme, Vivo, OPPO
- Multiple models per brand
- RAM: 4 GB to 16 GB
- Storage: 64 GB to 512 GB
- Age: 1 to 5 years
- Battery health: 50% to 96%
- Conditions: Excellent, Good, Fair, Poor

---

## 7. Project Structure

```
PriceIQ/
├── app.py                        # Flask application
├── requirements.txt              # Python dependencies
├── README.md                     # This file
├── .gitignore
├── dataset/
│   ├── products.csv              # Smartphone dataset
│   ├── validate_dataset.py       # Dataset validation script
│   └── README.md
├── ml/
│   ├── train_price_model.py      # Train and save the model
│   ├── predict_price.py          # Prediction function
│   ├── test_price_model.py       # Test suite
│   └── README.md
├── models/
│   └── price_prediction_model.joblib   # Saved trained model
├── templates/
│   └── index.html                # Main web page
└── static/
    └── style.css                 # Stylesheet
```

---

## 8. Installation

```bash
# 1. Clone or download the project
cd PriceIQ

# 2. (Optional) Create a virtual environment
python -m venv venv
venv\Scripts\activate        # Windows
# source venv/bin/activate   # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt
```

---

## 9. Validate Dataset

```bash
python dataset/validate_dataset.py
```

---

## 10. Train the Model

```bash
python ml/train_price_model.py
```

This will:
- Load the dataset
- Train the Random Forest model
- Print MAE, RMSE, and R² metrics
- Save the model to `models/price_prediction_model.joblib`

**You must run this before starting the application.**

---

## 11. Run the Application

```bash
python app.py
```

---

## 12. Open in Browser

Flask will print a local address like:

```
* Running on http://127.0.0.1:5000
```

Open that address in your browser.

---

## 13. Run Tests

```bash
python ml/test_price_model.py
```

Tests cover: dataset, model loading, prediction output, and Flask routes.

---

## 14. Example Usage

```
Brand:          Apple
Model:          iPhone 13
RAM:            4 GB
Storage:        128 GB
Age:            3 years
Battery Health: 80%
Condition:      Good

→ Estimated Resale Price: ₹27,230
```

---

## 15. Limitations

- The dataset is **synthetic/demo data**, not real market prices
- Only 122 training records — a larger dataset would improve accuracy
- Market prices change over time; the model does not update automatically
- Predictions are estimates, not guarantees
- The model is not production-grade
- Only covers 8 brands and selected models

---

## 16. Future Improvements

- Collect a larger real-world dataset from resale platforms
- Integrate live market price data
- Add more smartphone brands and models
- Try other ML algorithms (Gradient Boosting, XGBoost)
- Add price trend charts
- Deploy to a cloud platform (AWS, Heroku)

---


# PriceIQ

