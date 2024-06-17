from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
from sklearn.metrics import classification_report,confusion_matrix

def calc_main(N,P,K,temperature,humidity,ph,rainfall):
    df=pd.read_csv("Crop_recommendation.csv")
    X=df.iloc[:,:7].values
    y=df[["label"]].values.ravel()

    X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=1/3,random_state=0)


    mod=KNeighborsClassifier(n_neighbors=10)
    mod.fit(X_train,y_train)
    y_pred_test=mod.predict(X_test)
    print(classification_report(y_test,y_pred_test))

    return mod.predict([[N,P,K,temperature,humidity,ph,rainfall]])
