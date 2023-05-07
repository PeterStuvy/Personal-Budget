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
        
elif feature_choice == 'Add a transaction':
    add_transaction = True
    while add_transaction:
        transaction_date = click.prompt('What is the date of the transaction?', type=str)
        transaction_amount = click.prompt('What is the amount of the transaction?', type=float)
        transaction_description = click.prompt('Write a description for the transaction:', type=str)
        budget.add_transaction(transaction_date, transaction_amount, transaction_description)
        #Add some error handling for the inputs
        add_transaction_input = click.prompt('Would you like to add another transaction? (yes or no): ', type=str).lower()
        if add_transaction_input == 'no':
            add_transaction = False