import yfinance as yf
import pandas as pd
from typing import List

def fetch_prices(tickers:List[str],start:str,end:str)->pd.DataFrame:
    data=yf.download(tickers,start=start,end=end,auto_adjust=True)
    prices=data['Close']
    return prices.dropna()
if __name__ == "__main__":
    tickers = ["SPY", "QQQ", "AAPL", "MSFT"]
    prices = fetch_prices(tickers, "2015-01-01", "2024-12-31")
    prices.to_csv("data/raw/prices.csv")