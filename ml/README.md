# ML — Machine Learning Module

## What is Machine Learning?

Machine Learning (ML) is a way to teach computers to learn from data and make predictions without being explicitly programmed for every case.

## Supervised Learning

In supervised learning, we give the computer a set of examples with known answers (input → output). The computer learns the pattern and can then predict the output for new inputs.

## Regression

Regression is a type of supervised learning where the output is a **continuous number** (like a price), not a category.

PriceIQ predicts a price (₹32,500), so it is a **regression** problem.

## Random Forest

Random Forest is a machine learning algorithm that builds many decision trees and combines their predictions. It is:

- Accurate
- Resistant to overfitting
- Works well with mixed data (numbers + categories)
- Easy to use

## Features and Target

- **Features (inputs):** brand, model, RAM, storage, age, battery health, condition
- **Target (output):** resale_price

## Train-Test Split

We split the dataset into two parts:
- **Training set (80%):** used to teach the model
- **Test set (20%):** used to evaluate how well the model learned

This prevents the model from just memorising the data.

## OneHotEncoder

Computers cannot directly understand text like "Apple" or "Good". OneHotEncoder converts each category into a series of 0s and 1s.

Example:
```
condition = "Good"  →  [0, 1, 0, 0]  (Excellent=0, Good=1, Fair=0, Poor=0)
```

## Pipeline

A Pipeline chains preprocessing and the model together into one object. This ensures:
- The same transformations are applied during training and prediction
- No data leakage
- Easy to save and load

## Evaluation Metrics

### MAE (Mean Absolute Error)
Average of absolute differences between predicted and actual prices.
Lower is better. Easy to interpret: "On average, predictions are off by ₹X."

### RMSE (Root Mean Squared Error)
Similar to MAE but penalises large errors more. Lower is better.

### R² (R-squared)
Measures how well the model explains the variation in prices.
- R² = 1.0 → perfect predictions
- R² = 0.0 → model is no better than guessing the average
- Higher is better

## Files

| File | Purpose |
|---|---|
| `train_price_model.py` | Loads data, trains model, saves it |
| `predict_price.py` | Loads saved model, makes predictions |
| `test_price_model.py` | Tests dataset, model, and Flask routes |
