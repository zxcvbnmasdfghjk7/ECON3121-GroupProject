#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 01:49:27 2026

@author: eddie
"""

from src import config
import pandas as pd

sec_dataset = pd.read_csv(config.DATA_PROCESSED / "sec_dataset.csv")
merged_dataset = pd.read_csv(config.DATA_PROCESSED / "merged_dataset.csv")

# Set index to Quarter
sec_dataset = sec_dataset.set_index('Quarter')
merged_dataset = merged_dataset.set_index('Quarter')


# Merge Dataset
final_dataset = pd.concat([sec_dataset, merged_dataset], axis = 1)

# Remove 2012, not relevant for our case (1 Year = 4 Quarters).
final_dataset = final_dataset.iloc[:(57-4)]

# Data Cleaning
# Handle missing rows
# Impute missing entries with median
median_sales_rev = final_dataset['Sales_Revenue'].median()
median_net_sales = final_dataset['Net_Sales'].median()
median_market_share = final_dataset['Market_Share'].median()

# Impute missing entries using mean for Tablet_Shippment
mean_tablet_ship = final_dataset['Tablet_Shippments'].mean()

final_dataset['Sales_Revenue'] = final_dataset['Sales_Revenue'].fillna(median_sales_rev)
final_dataset['Net_Sales'] = final_dataset['Net_Sales'].fillna(median_net_sales)
final_dataset['Tablet_Shippments'] = final_dataset['Tablet_Shippments'].fillna(mean_tablet_ship)
final_dataset['Market_Share'] = final_dataset['Market_Share'].fillna(median_market_share)

# Export
final_dataset.to_csv(config.DATA_PROCESSED / "final_dataset.csv", index = True)