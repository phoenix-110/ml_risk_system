import pandas as pd
import  xgboost as xgb
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split


def train_xgb_risk_model(
    X: pd.DataFrame,
    y: pd.Series,
    test_size: float = 0.30
):
    """
    Train an XGBoost classifier to predict high-risk market periods.

    Parameters
    ----------
    X : pd.DataFrame
        Feature matrix (time-indexed).
    y : pd.Series
        Binary risk labels (0 = normal, 1 = high risk).
    test_size : float
        Fraction of data reserved for testing (time-based split).

    Returns
    -------
    model : xgb.XGBClassifier
        Trained XGBoost model.
    """

    # --- Time-aware split (NO SHUFFLING) ---
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=test_size,
        shuffle=False
    )

    # --- Handle class imbalance ---
    n_neg = (y_train == 0).sum()
    n_pos = (y_train == 1).sum()

    scale_pos_weight = n_neg / max(n_pos, 1)

    # --- XGBoost model ---
    model = xgb.XGBClassifier(
        n_estimators=300,
        max_depth=4,
        learning_rate=0.05,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="binary:logistic",
        eval_metric="logloss",
        scale_pos_weight=scale_pos_weight,
        random_state=42,
        n_jobs=-1
    )

    # --- Train ---
    model.fit(X_train, y_train)

    # --- Evaluate ---
    preds = model.predict(X_test)

    print("\nXGBoost Risk Model – Classification Report")
    print(classification_report(y_test, preds))

    return model
