#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 02:17:09 2026

@author: eddie
"""

import pandas as pd 
from src import config
import statsmodels.api as sm
from statsmodels.stats import diagnostic
from statsmodels.compat import lzip
import numpy as np
from patsy import dmatrices
import matplotlib.pyplot as plt
import seaborn as sns

# Import dataset
data = pd.read_csv(config.DATA_PROCESSED / "final_dataset.csv")

# %%
# Construct Matrix
y, X = dmatrices('Market_Share ~ Gross_Margin + SGA_Expense + Sales_Revenue + Net_Sales + Tablet_Shippments', 
                 data = data, return_type = 'dataframe')

# Regression
linear_reg = sm.OLS(y, X).fit()
 
# Print Results
print(linear_reg.summary())
# %%
# Residuals
residual = linear_reg.resid
# Variables
var_exog = linear_reg.model.exog

bp_test = diagnostic.het_breuschpagan(residual, var_exog)

# Label metrics for BP test
bp_names = ['Lagrange Multiplier Statistic', 'P-value', 'F-statistic', 'p-value']

print("--------------------------------------------------")
print("BP test results:")
print(lzip(bp_names, bp_test))
print("--------------------------------------------------")
# %%
# Confirm that model is heteroscedastic using White Test
white_test = diagnostic.het_white(residual, var_exog)
white_names = ['Lagrange Multiplier Statistic', 'P-value', 'F-statistic', 'p-value']
print("--------------------------------------------------")
print("White test results:")
print(lzip(white_names, white_test))
print("--------------------------------------------------")
# %%
# Wald's Test for OVB
wald_test = linear_reg.wald_test('(Gross_Margin = 0, SGA_Expense = 0, Sales_Revenue = 0)', use_f = True)

print(wald_test)

# %%
# Set residual and actual datapoints
residual = linear_reg.resid
fitted = linear_reg.predict(X)

# Plot Residual v. Fitted Plot
fig, ax = plt.subplots(figsize = (5, 4))

sns.residplot(y = residual, x = fitted, color = "g", lowess = True)
ax.set_title('Residual v. Fitted Values')
ax.set_xlabel('Fitted Values')
ax.set_ylabel('Residual Values')

plt.show()
