from budget import budget
from datetime import datetime
import click

#Create instance for the budget
my_budget = budget()

feature_options = ['Add an account', 'Add a transaction', 'View transactions or accounts', 'Set a budget limit', 'View budget limits', 'View the remaining budget for the month']
feature_choice = click.prompt('What would you like to do?: ', type=click.Choice(feature_options))

if feature_choice == 'Add an account':
    add_account = True
    while add_account:
        account_name = click.prompt('What is the name of the account?', type=str)
        budget.add_account(account_name)
        add_account_input = click.prompt('Would you like to add another account? (yes or no): ', type=str).lower()
        #add error handling for the input
        if add_account_input == 'no':
            add_account = False
        

