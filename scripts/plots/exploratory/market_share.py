#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 19:01:53 2026

@author: eddie
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as matdates
import seaborn as sns
from src import config
import numpy as np

# Import dataset
data = pd.read_csv(config.DATA_PROCESSED / "clean_vendor_market_share.csv")

# Convert it to timestamp()
data['Quarter'] = pd.PeriodIndex(data['Quarter'], freq = "Q").to_timestamp()
# %%
# Set seed
np.random.seed(237895)

fig, ax = plt.subplots(figsize = (9, 5))

vendors = ['Apple', 'Samsung', 'Huawei', 'Amazon', 'Google', 'Microsoft', 'Lenovo']
# Query only Apple
data = data.query("Market_Vendor in @vendors")

# plot returns Axis object
sns.lineplot(x = data['Quarter'], y = data['Market_Share'], hue = data["Market_Vendor"])

# Label axis and Set titles
ax.set_xlabel('Time Period (Quarter)')
ax.set_ylabel('Market Share (%)')
ax.set_title("Vendor's Share in Tablet Market")
plt.legend(title = "Vendors")


# Rotate xlabels by 45 degrees to fit
plt.xticks(rotation = 45)

# Save Plot
plt.tight_layout()
plt.savefig(config.REPORT_FIG / "vender_market_share.png")
plt.show()