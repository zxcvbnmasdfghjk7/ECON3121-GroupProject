#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 06:56:43 2026

@author: edmundzhou
"""

from pathlib import Path 
import tomllib

# Define Project Root
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Data Directories
DATA_DIRECTORY = PROJECT_ROOT / "datasets"

DATA_PROCESSED = DATA_DIRECTORY / "processed"

DATA_RAW = DATA_DIRECTORY / "raw"

DATA_EXTERNAL = DATA_DIRECTORY / "external"

DATA_SEC = DATA_EXTERNAL / "sec"

# Config File
CONFIG_FILE = PROJECT_ROOT / "config.toml"

# Define load_config for toml
def load_toml_config():
    with open(CONFIG_FILE, "rb") as f:
        return tomllib.load(f) 

# Read set Edgar Identity
def edgar_identity():
    config_file = load_toml_config()
    return config_file.get('edgar').get('IDENTITY')

# Figures
REPORT_FIG = PROJECT_ROOT / "reports" / "figures"

# Report directory
REPORT = PROJECT_ROOT / "reports"