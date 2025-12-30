import pandas as pd
import numpy as np

def compute_log_returns(prices:pd.DataFrame)->pd.DataFrame:
    """
    Compute log returns from price data.
    """
    returns=np.log(prices/prices.shift(1))
    return returns
def rolling_volatility(returns:pd.DataFrame,window:int,annualize:bool=True)->pd.Series:
    """
    Cross-asset rolling volatility.
    """
    vol=returns.rolling(window).std().mean(axis=1)
    if annualize:
        vol*=np.sqrt(252)
    return vol
def rolling_skewness(returns:pd.DataFrame,window:int)->pd.Series:
    """
    Rolling skewness (tail risk proxy).
    """
    return returns.rolling(window).skew().mean(axis=1)
def drawdown(prices:pd.Series)->pd.Series:
    """
    Compute drawdown series.
    """
    cumulative=prices/prices.iloc[0]
    peak=cumulative.cummax()
    return (cumulative-peak)/peak
def build_feature_matrix(prices:pd.DataFrame)->pd.DataFrame:
    returns=compute_log_returns(prices)
    X=pd.DataFrame(index=returns.index)
    X['vol_20']=rolling_volatility(returns,20)
    X['vol_60']=rolling_volatility(returns,60)
    X['vol_120']=rolling_volatility(returns,120)
    X["vol_ratio_20_60"]=X['vol_20']/X['vol_60']
    X['vol_ratio_60_120']=X['vol_60']/X['vol_120']
    X['skew_60']=rolling_skewness(returns,60)
    market_price=prices.mean(axis=1)
    X['drawdown']=drawdown(market_price)
    return X.dropna()


