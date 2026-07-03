# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 11:10:30 2023

@author: Aqueak
"""

import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import statsmodels.api as sm
import matplotlib.pyplot as plt


data=pd.read_excel('MSFT.xlsx')
print(data)

df = pd.DataFrame(data)


summary = df.describe()
print(summary)

sns.pairplot(df)
plt.show()


X = df[['Open']]
y = df['Adj Close']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = LinearRegression()
model.fit(X_train, y_train)


predictions = model.predict(X_test)

X=sm.add_constant(X)
model2=sm.OLS(y,X).fit()

print(model2.summary())




