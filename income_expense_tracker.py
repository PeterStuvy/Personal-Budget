import pandas as pd
from pprint import pprint
from datetime import datetime

class income_expense_tracker:
    def __init__(self):
        self.accounts = {}

    def add_account(self, name, balance=0):
        self.accounts[name] = balance
    