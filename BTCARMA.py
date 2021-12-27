#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 27 11:07:39 2021

@author: maramarsu
"""

from pandas_datareader import data
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.dates as mdates
from statsmodels.graphics.tsaplots import plot_acf
sp500 = pd.read_csv('https://query1.finance.yahoo.com/v7/finance/download/%5EGSPC?period1=1513728000&period2=1584780625&interval=1d&events=history')

