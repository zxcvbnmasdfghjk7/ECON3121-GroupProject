#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 11:46:54 2026

@author: edmundzhou
"""
# Import Packages
from src import config
import pandas as pd

# Import AAPL's Market
market_share = pd.read_csv(config.DATA_DIRECTORY / "raw" / "vendor-ww-quarterly-20131-20262.csv")
market_share = (market_share.filter(items = ['Date', 'Apple'])
                .rename(columns = {'Date': 'Quarter'})
                .rename(columns = {'Apple': 'Market_Share'}))

market_share['Quarter'] = pd.PeriodIndex(market_share['Quarter'], freq = "Q").strftime('Q%q %Y')

# Import Statista's Sales Revenue for IPad AAPL
sales_revenue = (pd.read_excel(config.DATA_DIRECTORY / "raw" / "statistic_id382136_apple-net-sales-quarterly-fy-2012-2026-by-operating-segment.xlsx", 
                              sheet_name = "Data", 
                              header = 4, 
                              index_col = None, usecols="B:G")
                 .rename(columns = {'Unnamed: 1': 'Quarter'})
                 .rename(columns = {'iPad*': 'Sales_Revenue'}))

sales_revenue = sales_revenue[['Quarter', 'Sales_Revenue']]

aapl = pd.merge(sales_revenue, market_share, on = 'Quarter', how = 'inner')