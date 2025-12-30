import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

class RegimeDetector:
    """
    Unsupervised market regime detector using KMeans.
    """
    def __init__(self,n_regimes:int =3,random_state:int=42):
        self.n_regimes=n_regimes
        self.scalar=StandardScaler()
        self.model=KMeans(n_clusters=self.n_regimes,n_init=20,random_state=random_state)
    def fit(self,X:pd.DataFrame)->None:
        X_scaled=self.scalar.fit_transform(X)
        self.model.fit(X_scaled)
    def predict(self,X:pd.DataFrame)->pd.Series:
        X_scaled=self.scalar.transform(X)
        regimes=self.model.predict(X_scaled)
        return pd.Series(regimes,index=X.index,name='regime')
    def fit_predict(self,X:pd.DataFrame)->pd.Series:
        self.fit(X)
        return self.predict(X)
    