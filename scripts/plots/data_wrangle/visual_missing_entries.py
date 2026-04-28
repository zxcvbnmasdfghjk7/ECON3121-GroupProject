#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 19:19:38 2026

@author: eddie
"""

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from src import config

# Import 'raw' unmerged datasets
sec_dataset = pd.read_csv(config.DATA_PROCESSED / "sec_dataset.csv")
merged_dataset = pd.read_csv(config.DATA_PROCESSED / "merged_dataset.csv")

# Set index to Quarter
sec_dataset = sec_dataset.set_index('Quarter')
merged_dataset = merged_dataset.set_index('Quarter')

# Merge Dataset
visual_dataset = pd.concat([sec_dataset, merged_dataset], axis = 1)

# Remove 2012, not relevant for our case (1 Year = 4 Quarters).
visual_dataset = visual_dataset.iloc[:(57-4)]

# %%
# Print variables with missing entries
print(visual_dataset.isna().sum())

# %%
# Plot Density Histogram for Market_Share
sns.displot(x = visual_dataset['Market_Share'], kind = "kde")

# %%
# Plot Density Hist for Sales_Revenue
sns.displot(x = visual_dataset['Sales_Revenue'], kind = "kde")

# %%
sns.displot(x = visual_dataset['Net_Sales'], kind = "kde")

# %%
sns.displot(x = visual_dataset['Tablet_Shippments'], kind = "kde")

# %%
# Plot Boxplot
visual_dataset[['Market_Share', 'Sales_Revenue', 'Net_Sales', 'Tablet_Shippments']].boxplot()