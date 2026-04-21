#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:31:31 2026

@author: edmundzhou
"""

from edgar.xbrl import XBRLS
from edgar import set_identity, Company

# Set Identity for access
set_identity('Edmund Zhou edmund.zhou@student.unsw.edu.au')

# Define Apple as a Object
apple = Company('AAPL')
# %%
# Print income statement
print(apple.income_statement())

# %%
tenQ = apple.get_filings(year = range(2012, 2026), form = "10-Q")
tenQ_xbrls = XBRLS.from_filings(tenQ)

print(tenQ_xbrls)
