# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:57:47 2023

@author: FURKAN
"""

import pandas as pd
from scipy.stats import ttest_ind

msft='MSFT.xlsx'
df=pd.read_excel(msft)

Open=df['Open']
Close=df['Adj Close']

t_statistic,p_value=ttest_ind(Open,Close)

print("t-statistic:",t_statistic)
print("p-value:",p_value)
#t-testi
