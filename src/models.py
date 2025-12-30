import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

def train_risk_model(X:pd.DataFrame,y:pd.Series):
    """
    Train a supervised ML model to predict high-risk periods.
    """
    
    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,shuffle=False)
    print(len(X_train))
    model=RandomForestClassifier(n_estimators=300,max_depth=5,random_state=42,class_weight='balanced')
    model.fit(X_train,y_train)
    preds=model.predict(X_test)
    print("Classification Report:")
    print(classification_report(y_test, preds))
    return model