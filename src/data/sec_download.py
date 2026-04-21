#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:31:31 2026

@author: edmundzhou
"""

from edgar import set_identity, Company

# Set Identity for access
set_identity('Edmund Zhou edmund.zhou@student.unsw.edu.au')

# Define Apple as a Object
apple = Company('AAPL')

apple_filings = apple.get_filings(year = range(2012, 2026), form = "10-K")
finance = apple.get_financials()


