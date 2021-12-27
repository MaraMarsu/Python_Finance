# -*- coding: utf-8 -*-
"""
Created on Wed Dec 22 22:49:47 2021

@author: Martti
"""

import pandas as pd
import numpy as np
import yfinance as yf
import datetime as dt
from pandas_datareader import data as pdr

yf.pdr_override()
#stock=input("Enter ticker") #BTC-USD is the ticker for Bitcoin
stock="BTC-USD"
print(stock)

startyear=2017
startmonth=1
startday=1

start=dt.datetime(startyear,startmonth,startday)

now=dt.datetime.now()

df=pdr.get_data_yahoo(stock,start,now)

print(df)

ma=50 #moving average
smaString="Sma_"+str(ma)
df[smaString]=df.iloc[:,4].rolling(window=ma).mean()
print(df)
df=df.iloc[ma:] #removes 50 first rows, MA=50 
print(df)
