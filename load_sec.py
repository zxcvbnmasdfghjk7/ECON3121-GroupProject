#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 10:48:47 2026

@author: edmundzhou
"""

from edgar import set_identity, Company
import pandas as pd

# Set identity 
set_identity('Edmund Zhou edmund.zhou@student.unsw.edu.au')

aapl = Company("AAPL")
aapl_filings = aapl.get_filings(form = "10-K")