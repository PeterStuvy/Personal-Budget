import pandas as pd
from pprint import pprint
from datetime import datetime
import csv

class budget:
    def __init__(self):
        self.accounts = {}
        self.limits = {}
    
    def add_account(self, name, balance=0):
        self.accounts[name] = balance
    
    def add_transaction(self, date, amount, description, account):
        self.accounts[account] += amount
        self._append_transaction_to_csv(date, amount, description, account)

    def _append_transaction_to_csv(self, date, amount, description, account):
        with open('transactions.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([date, amount, description, account])

    def set_limit(self, category, amount):
        self.limits[category] = amount

    def view_limits(self):
        pprint(self.limits)
    
    def check_limit(self, category):
        if category not in self.limits:
            raise ValueError(f'Limit for category {category} has not been set.')
        return self.limits[category]
    
    def check_total_expenses(self, start_date=None, end_date=None):
        df = pd.read_csv('transactions.csv', parse_dates=['Date'])
        if start_date and end_date:
            mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
            df = df.loc[mask]
        return df['Amount'].sum()

    def check_category_expenses(self, category, start_date=None, end_date=None):
        data_frame = pd.read_csv('transactions.csv', parse_dates=['Date'])
        if start_date and end_date:
            mask = (data_frame['Date'] >= start_date) & (data_frame['Date'] <= end_date)
            df = data_frame.loc[mask]
        return df[df['Category'] == category]['Amount'].sum()
    
    def check_remaining_balance(self, category):
        category_expenses = self.check_category_expenses(category)
        limit = self.check_limit
        remaining_balance = limit - category_expenses
        pprint(f'The remaining balance for {category} is {remaining_balance}.')