#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 06:55:59 2026

@author: edmundzhou
"""

<<<<<<< HEAD:src/__init__.py
=======
import pandas as pd
import numpy as np

# Load Market Share Dataset.
aapl_market_share = pd.read_csv("datasets/raw/vendor-ww-quarterly-20131-20262.csv")

# Select only Date and Apple
aapl_market_share = (aapl_market_share.filter(items = ['Date', 'Apple'])
                     # Rename Date to Quarter
                     .rename(columns = {'Date': 'Quarter'})
                     # Rename Apple to Market Share
                     .rename(columns = {'Apple': 'Market_Share'}))

# Reformat Quarter
aapl_market_share['Quarter'] = pd.PeriodIndex(aapl_market_share['Quarter'], freq = "Q").strftime('Q%q %Y')

# Load Sales Revenue Dataset
aapl_sales = (pd.read_excel(sheet_name = "Data", 
                           io = "datasets/raw/statistic_id382136_apple-net-sales-quarterly-fy-2012-2026-by-operating-segment.xlsx", 
                           usecols = "B:G", skiprows = 4)
              .rename(columns = {'Unnamed: 1': 'Quarter'})
              .filter(items = ['Quarter', 'iPad*'])
              .rename(columns = {'iPad*': 'Sales_Revenue'})
              .iloc[4:])

aapl = pd.merge(aapl_market_share, aapl_sales, 
                on = "Quarter", 
                how = "inner")
>>>>>>> 9b75acd (Update Repository: Fix Commit History):process_datasets.py
