#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 05:02:30 2026

@author: eddie
"""

import pandas as pd
from src import config

# Import raw dataset for vendors market share
data = (pd.read_csv(config.DATA_RAW / "vendor-ww-quarterly-20131-20262.csv")
        .rename(columns = {'Date': 'Quarter'})) 

# Convert Columns into Vendors
data = pd.melt(data, id_vars = "Quarter", var_name = "Market_Vendor", value_name = "Market_Share")

# Reformat Quarter
data['Quarter'] = data['Quarter'].str.replace(r'(\d+)-(\d)', r'\1Q\2', regex = True)

data.to_csv(config.DATA_PROCESSED / "clean_vendor_market_share.csv", index = False, columns = ['Quarter', 'Market_Vendor', 'Market_Share'])