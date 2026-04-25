#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:17:09 2026

@author: eddie
"""

import pandas as pd 
from src import config
import statsmodels.api as sm
import numpy as np
from patsy import dmatrices
import matplotlib.pyplot as plt
# Import dataset
data = pd.read_csv(config.DATA_PROCESSED / "final_dataset.csv")

# %%
# Construct Matrix
y, X = dmatrices('Market_Share ~ Gross_Margin + SGA_Expense + Sales_Revenue', 
                 data = data, return_type = 'dataframe')

# Regression
linear_reg = sm.OLS(y, X).fit()
 
# Print Results
print(linear_reg.summary())
# %%
