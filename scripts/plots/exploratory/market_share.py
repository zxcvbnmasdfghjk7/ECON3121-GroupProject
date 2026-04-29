#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:01:53 2026

@author: eddie
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src import config
import numpy as np

# Import dataset
data = pd.read_csv(config.DATA_PROCESSED / "clean_vendor_market_share.csv")

# Convert it into PeriodIndex Object
data['Quarter'] = pd.PeriodIndex(data['Quarter'], freq = "Q").to_timestamp()
# %%
# Set seed
np.random.seed(237895)

fig, ax = plt.subplots(figsize = (15, 12))

sns.lineplot(data = data, x = "Quarter", y = "Market_Share", hue = "Market_Vendor")

ax.set_xlabel('Period (Quarter)')
ax.set_ylabel('Market Share (%)')
ax.set_title('Market Share for Apple iPad')

plt.show()