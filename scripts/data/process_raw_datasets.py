#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:46:54 2026

@author: edmundzhou
"""
# Import Packages
from src import config
import pandas as pd

# %%
# Import AAPL's Market
market_share = pd.read_csv(config.DATA_DIRECTORY / "raw" / "vendor-ww-quarterly-20131-20262.csv")
market_share = (market_share.filter(items = ['Date', 'Apple'])
                .rename(columns = {'Date': 'Quarter'})
                .rename(columns = {'Apple': 'Market_Share'}))

# Reformat Quarter YYYY-q to Qq YYYY
market_share['Quarter'] = market_share['Quarter'].str.replace(r'(\d+)-(\d+)', r'\1Q\2', regex = True)
market_share['Quarter'] = market_share['Quarter'].str.replace(r'(\d+)Q(\d+)', r'Q\2 \1', regex = True)

# %%
# Import Statista's Sales Revenue for IPad AAPL
sales_revenue = (pd.read_excel(config.DATA_DIRECTORY / "raw" / "statistic_id382136_apple-net-sales-quarterly-fy-2012-2026-by-operating-segment.xlsx", 
                              sheet_name = "Data", 
                              header = 4, 
                              index_col = None, usecols="B:G")
                 .rename(columns = {'Unnamed: 1': 'Quarter'})
                 .rename(columns = {'iPad*': 'Sales_Revenue'}))

# Select Quarter and Sales Revenue
sales_revenue = sales_revenue[['Quarter', 'Sales_Revenue']]

# %%
# Import Statista's Total Net Sales % 
net_sales = (pd.read_excel(config.DATA_DIRECTORY / "raw" / "statistic_id253655_ipads-share-of-apples-total-net-sales-quarterly-2010-2026.xlsx", 
                           sheet_name = "Data", 
                           header = 4, 
                           index_col = None, 
                           usecols = "B:C")
             .rename(columns = {'Unnamed: 1' : 'Quarter'})
             .rename(columns = {'Unnamed: 2': 'Net_Sales'}))

# Reformat Quarter from Qq 'YY to Qq YYYY
net_sales['Quarter'] = net_sales['Quarter'].str.replace("'", "20", regex = False)
# %%
tablet_shippment = (pd.read_excel(config.DATA_DIRECTORY / "raw" / "statistic_id268711_ipads-tablet-shipment-share-worldwide-quarterly-2012-2025.xlsx", 
                                  sheet_name = "Data", 
                                  header = 4, index_col = None, 
                                  usecols = "B:C")
                    .rename(columns = {'Unnamed: 1': 'Quarter'})
                    .rename(columns = {'Unnamed: 2': 'Tablet_Shippments'}))

# %%
# Merge dataframes
aapl = pd.merge(sales_revenue, market_share, on = 'Quarter', how = 'inner')

aapl = pd.merge(aapl, net_sales, on = 'Quarter', how = 'inner')

aapl = pd.merge(aapl, tablet_shippment, on = "Quarter", how = 'left')

# Export 'raw' dataset
aapl.to_csv(config.DATA_PROCESSED / "merged_dataset.csv", index = False, columns = ['Quarter', 'Market_Share', 'Sales_Revenue', 'Net_Sales', 'Tablet_Shippments'])