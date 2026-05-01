#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May  1 02:30:32 2026

@author: eddie
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from src import config
import numpy as np

# Import dataset
data = pd.read_csv(config.DATA_PROCESSED / "final_dataset.csv")

# %%
fig, axes = plt.subplots(2, 3, figsize = (12, 6))

fig.suptitle("Regression Plots of Market_Share v. IV")

# Plot all variables
sns.regplot(data = data, y = "Market_Share", x = "Gross_Margin", order = 2, ax = axes[0,0])
axes[0,0].set_title("Market Share v. Gross_Margin")

sns.regplot(data = data, y = "Market_Share", x = "SGA_Expense", order = 2, ax = axes[0, 1])
axes[0, 1].set_title("Market Share v. SGA_Expense")

sns.regplot(data = data, y = "Market_Share", x = "Sales_Revenue", logx = True, ax = axes[0, 2])
axes[0, 2].set_title("Market Share v. Sales_Revenue")

sns.regplot(data = data, y = "Market_Share", x = "Tablet_Shippments", logx = True, ax = axes[1, 0])
axes[1, 0].set_title("Market Share v. Tablet_Shippments")

sns.regplot(data = data, y = "Market_Share", x = "RD_Expense", order = 2, ax = axes[1, 1])
axes[1,1].set_title("Market Share v. RD_Expense")

# Remove last plot
fig.delaxes(axes[1,2])
# Adjust spacing between plots and display plot
plt.tight_layout()
plt.show()

# %%
fig, axes = plt.subplots(2, 3, figsize = (12, 6))

fig.suptitle("Residual Plots of Market_Share v. IV")

# Plot all variables
sns.residplot(data = data, y = "Market_Share", x = "Gross_Margin", ax = axes[0,0], lowess=True)
axes[0,0].set_title("Market Share v. Gross_Margin")

sns.residplot(data = data, y = "Market_Share", x = "SGA_Expense", ax = axes[0, 1], lowess=True)
axes[0, 1].set_title("Market Share v. SGA_Expense")

sns.residplot(y = data["Market_Share"], x = data["Sales_Revenue"], ax = axes[0, 2], lowess=True)
axes[0, 2].set_title("Market Share v. Sales_Revenue")

sns.residplot(data = data, y = "Market_Share", x = "Tablet_Shippments", ax = axes[1, 0], lowess=True)
axes[1, 0].set_title("Market Share v. Tablet_Shippments")

sns.residplot(data = data, y = "Market_Share", x = "RD_Expense", ax = axes[1, 1], lowess=True)
axes[1,1].set_title("Market Share v. RD_Expense")

# Remove last plot
fig.delaxes(axes[1,2])
# Adjust spacing between plots and display plot
plt.tight_layout()
plt.show()