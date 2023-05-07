import pandas as pd
from pprint import pprint
from datetime import datetime
import csv

class budget:
    def __init__(self):
        self.accounts = {}
        self.limits = {}
    
    #Add and remove accounts abd transactions

    def add_account(self, name, balance=0):
        self.accounts[name] = balance
    
    def add_transaction(self, date, amount, description, account):
        #add some error handling for whether the account exists
        self.accounts[account] += amount
        self._append_transaction_to_csv(date, amount, description, account)
    
    def view_transactions(self):
        data_frame = pd.read_csv('transactions.csv', parse_dates=['Date'])
        pprint(data_frame)
    
    def view_accounts(self):
        pprint(self.accounts)

    def _append_transaction_to_csv(self, date, amount, description, account):
        with open('transactions.csv', mode='a', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([date, amount, description, account])
    
    #Still to include ability to remove accounts and transactions


    #Set limit for transaction types

    def set_limit(self, category, amount):
        self.limits[category] = amount

    def view_limit(self):
        pprint(self.limits)
    
    def check_limit(self, category):
        if category not in self.limits:
            raise ValueError(f'Limit for category {category} has not been set.')
        return self.limits[category]
    
    def check_total_expenses(self, start_date=None, end_date=None):
        data_frame = pd.read_csv('transactions.csv', parse_dates=['Date'])
        if start_date and end_date:
            mask = (data_frame['Date'] >= start_date) & (data_frame['Date'] <= end_date)
            data_frame = data_frame.loc[mask]
        return data_frame['Amount'].sum()

