# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 21:00:30 2026

@author: edmundzhou
"""

# Import package
import yfinance

# Load Ticker object
yf_apple = yfinance.Ticker('AAPL')
# %%

print(yf_apple.quarterly_income_stmt)
