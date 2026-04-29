#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 12:31:31 2026

@author: edmundzhou
"""

from edgar import set_identity, Company
from src import config

# Set Identity for access
set_identity(config.edgar_identity())

# Define Apple as a Object
apple = Company('AAPL')
# %%
# Print income statement
print(apple.income_statement(periods = 14, annual = True))

# %%
# Extract Apple's Income Statement
# Quarterly Periods for 14 years = 14 x 4
apple_income_statement = apple.income_statement(as_dataframe=True, periods = 57, annual = False)

# %%
# Extract Series 'SellingGeneralAndAdministrativeExpense' from Q1 2012 to Q1 2026
sga_expense = (apple_income_statement.loc['SellingGeneralAndAdministrativeExpense']
               .iloc[6:63]
               .to_frame(name = 'SellingGeneralAndAdministrativeExpense')
               .rename(columns = {'SellingGeneralAndAdministrativeExpense': 'SGA_Expense'}))

# Convert Index Column into Quarter
sga_expense = (sga_expense.reset_index()
               .rename(columns = {'index': 'Quarter'}))

# Transform the Units into Billions
sga_expense['SGA_Expense'] = (sga_expense['SGA_Expense'] / 1000000000)

# Export SGA_Expense 
sga_expense.to_csv(config.DATA_SEC / "sga_expense.csv", index = False, columns = ['Quarter', 'SGA_Expense'])

# %%
# Extract Series 'Gross Profit' - Basically a component of Gross Margin
gross_profit = (apple_income_statement.loc['GrossProfit']
                .iloc[6:63]
                .to_frame(name = 'GrossProfit')
                .rename(columns = {'GrossProfit': 'Gross_Profit'}))

# Convert Index to Quarter
gross_profit = (gross_profit.reset_index()
                .rename(columns = {'index': 'Quarter'}))

# Extract Series 'Total Revenue' as label for concept 'RevenueFromContractWithCustomerExcludingAssessedTax'
total_revenue = (apple_income_statement.loc['RevenueFromContractWithCustomerExcludingAssessedTax']
                 .iloc[6:63]
                 .to_frame(name = 'RevenueFromContractWithCustomerExcludingAssessedTax')
                 .rename(columns = {'RevenueFromContractWithCustomerExcludingAssessedTax': 'Total_Revenue'})
                 .reset_index()
                 .rename(columns = {'index': 'Quarter'}))

# Use formula (Gross_Profit / Total_Revenue) * 100
gross_margin = ((gross_profit['Gross_Profit'] / total_revenue['Total_Revenue']) * 100)
gross_margin = (gross_margin.to_frame(name = "Gross_Margin")
                .set_index(gross_profit['Quarter'])
                .reset_index())

# Export Gross_Margin
gross_margin.to_csv(config.DATA_SEC / "gross_margin.csv", index = False, columns = ['Quarter', 'Gross_Margin'])
# %%
# Extract R&D Expense
rd_expense = (apple_income_statement.loc['ResearchAndDevelopmentExpense']
              .iloc[6:63]
              .to_frame(name = 'ResearchAndDevelopmentExpense')
              .rename(columns = {'ResearchAndDevelopmentExpense': 'RD_Expense'})
              .reset_index()
              .rename(columns = {'index': 'Quarter'}))

# Transform units into billions
rd_expense['RD_Expense'] = (rd_expense['RD_Expense'] / 1000000000)

# Export RD_Expense 
rd_expense.to_csv(config.DATA_SEC / "rd_expense.csv", index = False, columns = ['Quarter', 'RD_Expense'])
# %%
# Set Index to Quarter
gross_margin_m = gross_margin.set_index('Quarter')
sga_expense_m = sga_expense.set_index('Quarter')
rd_expense_m = rd_expense.set_index('Quarter')

# Merge
sec_dataset = (gross_margin_m.join(sga_expense_m, on = 'Quarter', how = 'inner'))

sec_dataset = (sec_dataset.join(rd_expense_m, on = 'Quarter', how = 'inner'))

# Export SEC dataset
sec_dataset.to_csv(config.DATA_PROCESSED / "sec_dataset.csv", index = True, columns = ['Gross_Margin', 'SGA_Expense', 'RD_Expense'])

# Save Memory by removing unnecessary variables
del gross_margin_m, sga_expense_m, rd_expense_m