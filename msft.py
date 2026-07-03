# -*- coding: utf-8 -*-
"""
Created on Sat Nov 18 04:10:28 2023

@author: Aqueak
"""

import pandas as pd
from sklearn import preprocessing, datasets, neighbors
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df=pd.read_excel('MSFT.xlsx')
print(df)

x=df[["Open","High"]]
y=df[["Adj Close","Close"]]


from sklearn.naive_bayes import GaussianNB
gnb=GaussianNB()

from sklearn.metrics import mean_squared_error
mean_squared_error(x, y)
df.shape
df.head()
df.isnull().sum()

from sklearn.linear_model import LinearRegression
lr=LinearRegression()


accuracy_score()




model=neighbors.KNeighborsClassifier(n_neighbors=5)
model.fit(x,y)
tahmin=model.predict(y)
