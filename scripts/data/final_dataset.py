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

# Merge sec and merged dataset
final_dataset = (pd.concat([sec_dataset, merged_dataset], axis = 1)
                 .dropna())

final_dataset.to_csv(config.DATA_PROCESSED / "final_dataset.csv", index = True)