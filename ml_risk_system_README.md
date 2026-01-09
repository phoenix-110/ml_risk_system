# ML Risk Monitoring System

## Overview
This project implements an end-to-end **Machine Learning–based Market Risk Monitoring System** designed to identify periods of elevated market risk using historical market data.  
It combines **feature engineering**, **unsupervised learning**, **supervised ML**, and **deep learning (LSTM)** to model and compare different approaches to financial risk prediction.

The system is built with a strong focus on:
- Time-series correctness (no look-ahead bias)
- Realistic financial risk labeling
- Model interpretability and comparison

---

## Project Structure

```
ml_risk_system/
│
├── data/
│   ├── raw/
│   │   └── prices.csv
│   └── processed/
│       ├── features.csv
│       ├── ml_dataset.csv
│       └── lstm_risk_scores.csv
│
├── notebooks/
│   ├── 01_eda.ipynb
│   ├── 02_features.ipynb
│   ├── 03_regimes.ipynb
│   ├── 04_labels.ipynb
│   ├── 05_supervised_model.ipynb
│   ├── 06_prediction_validation.ipynb
│   ├── 07_lstm_model.ipynb
│   └── 09_model_comparison.ipynb
│
├── src/
│   ├── data_ingestion.py
│   ├── features.py
│   ├── regimes.py
│   ├── labels.py
│   ├── models.py
│   ├── xgb_model.py
│   └── lstm_model.py
│
├── requirements.txt
└── README.md
```

---

## Methodology

### 1. Feature Engineering
- Rolling volatility (short & long horizon)
- Drawdown and return-based risk metrics
- Volatility ratios
- Normalized risk indicators

### 2. Regime Detection (Unsupervised Learning)
- K-Means clustering on volatility features
- Identifies distinct market regimes (calm, volatile, stressed)

### 3. Risk Label Construction
- Forward-looking **future drawdown** calculation
- Quantile-based labeling (top 10% worst drawdowns)
- Prevents look-ahead bias

### 4. Supervised Learning Models
- **Random Forest** (baseline)
- **XGBoost** (improved rare-event detection)
- Class imbalance handled via weighted loss

### 5. Deep Learning (LSTM)
- Sequence-based modeling of risk features
- Learns temporal patterns preceding drawdowns
- Produces continuous risk scores

### 6. Model Comparison
- Visual comparison of RF, XGBoost, and LSTM predictions
- Highlights differences in sensitivity and early-warning behavior

---

## Results & Insights

- Tree-based models provide strong point-in-time risk classification
- XGBoost improves recall on rare high-risk periods
- LSTM produces smoother, earlier risk signals by learning temporal dependencies
- Quantile-based thresholds are more appropriate than fixed probability cutoffs

---

## Technologies Used

- Python, Pandas, NumPy
- Scikit-learn
- XGBoost
- PyTorch
- Matplotlib
- Jupyter Notebooks

---

## How to Run

```bash
# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run notebooks in order
notebooks/01_eda.ipynb → notebooks/09_model_comparison.ipynb
```

---

## Key Takeaways

This project demonstrates:
- Practical ML system design for financial time series
- Careful handling of temporal data and leakage prevention
- Comparison of classical ML and deep learning approaches
- Strong emphasis on interpretability and robustness

---

## Author
Raunak Agrawal
