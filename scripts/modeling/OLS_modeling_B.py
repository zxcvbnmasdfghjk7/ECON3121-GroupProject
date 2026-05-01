#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:31:26 2026

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
y, X = dmatrices('Market_Share ~ Gross_Margin + np.square(Gross_Margin) + SGA_Expense + np.square(SGA_Expense) + np.log(Sales_Revenue) + np.log(Tablet_Shippments) + RD_Expense + np.square(RD_Expense) + Gross_Margin * RD_Expense', 
                 data = data, return_type = 'dataframe')
 
# Regression
linear_reg = sm.OLS(y, X).fit()
 
# Print Results
print(linear_reg.summary())

# Export results as html
with open((config.REPORT / "OLS_Results_B.csv"), "w") as file:
    file.write(linear_reg.summary().as_csv())
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
# Ramsay RESET test
reset_test = diagnostic.linear_reset(res = linear_reg, use_f = True)
reset_names = ['F_test', 'p_value', 'df_denom', 'df_num']

print("--------------------------------------------------")
print("Ramsay RESET test:")
print(reset_test.summary())
print("--------------------------------------------------")


# %%
fig, axes = plt.subplots(1, 2, figsize = (10,5))

fig.suptitle("Plots for Model B")

sns.residplot(y = linear_reg.resid, x = linear_reg.predict(X), color = "g", lowess = True, ax = axes[0])
axes[0].set_title('Residual Plot')
axes[0].set_xlabel('Fitted Values')
axes[0].set_ylabel('Residuals')

sns.regplot(y = linear_reg.predict(X), x = data['Market_Share'], ax = axes[1])

axes[1].set_title("Predicted vs. Actual Values for Market Share")
axes[1].set_xlabel("Actual Market Share (%)")
axes[1].set_ylabel("Predicted Market Share (%)")

plt.savefig(config.REPORT_FIG / "Plot_model_B.png")
plt.tight_layout()
plt.show()

# %%
# Hypothesis test
hypo = 'SGA_Expense = 0'

results = linear_reg

print(results.t_test(hypo))