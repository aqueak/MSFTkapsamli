# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 16:13:18 2023

@author: FURKAN
"""

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

sns.set()

data = pd.read_excel("MSFT.xlsx")
print(data.head())

plt.xlabel("Open")
plt.ylabel("Adj Close")
plt.plot(data["Adj Close"])
plt.grid(axis='x',color='blue')
plt.grid(axis='y',color='red')
plt.show()

print(data.corr())
sns.heatmap(data.corr())
plt.show()

X = data[["Open","High","Low"]]
y = data[["Adj Close","Close","Volume"]]
X= X.to_numpy()
y = y.to_numpy()
y = y.reshape(-1,1)
                                                                           
rpredy=(351878425, 
355325284, 
359021662, 
361488976, 
359169509, 
367467858, 
364704794, 
368022285, 
368161203,
374179986)
"zaman"
plt.xlabel("zaman")
plt.ylabel("tahmin")
plt.plot(rpredy)
plt.grid(axis='x',color='blue')
plt.grid(axis='y',color='red')
plt.show()








