import pandas as pd
import numpy as np
def future_drawdown(prices: pd.Series) -> pd.Series:
    prices = prices.astype(float).sort_index().dropna()
    
    H = 20  # 🔒 HARD-CODED, CANNOT BE SHADOWED
    
    fdd = pd.Series(index=prices.index, dtype=float)

    for i in range(len(prices)):
        window = prices.iloc[i : i + H]

        if len(window) < H:
            fdd.iloc[i] = float("nan")
            continue

        peak = window.max()
        trough = window.min()
        fdd.iloc[i] = (trough - peak) / peak

    return fdd




def build_risk_labels(prices:pd.Series,horizon:int=20,threshold:float= -0.10)->pd.Series:
    """
    Binary risk label:
    1 = high risk, 0 = normal
    """
    fdd = future_drawdown(prices, horizon)
    labels = (fdd <= threshold).astype(int)
    return labels