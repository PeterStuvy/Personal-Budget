import pandas as pd
from pprint import pprint
from datetime import datetime

class income_expense_tracker:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0):
        self.accounts[name] = balance
    
    def add_transaction(self, date, amount, description, account):
        #add some error handling for whether the account exists
        self.accounts[account] += amount
        self._append_transaction_to_csv(date, amount, description, account)
    
    def view_transactions(self):
        data_frame = pd.read_csv('transactions.csv', parse_dates=['Date'])
        pprint(data_frame)
    
    