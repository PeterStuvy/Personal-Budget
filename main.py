from budget import budget
from datetime import datetime
import click

#Create instance for the budget
my_budget = budget()

while True:
    feature_options = ['Add an account', 'Add a transaction', 'View transactions or accounts', 'Set a budget limit', 'View budget limits', 'View the remaining budget for the month', 'Quit']
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

    elif feature_choice == 'View transactions or accounts':
        viewing_options = ['Transactions', 'Accounts']
        viewing_choice = click.prompt('What would you like to view?: ', type=click.Choice(viewing_options))
        
        if viewing_choice == 'Transactions':
            budget.view_transactions()
        
        else:
            budget.view_accounts()
    
    elif feature_choice == 'Set a budget limit':
        set_limit = True
        while set_limit:
            limit_account = click.prompt('What is the name of the account you would like to set a limit for?', type=str)
            limit_amount = click.prompt('What is the amount of the limit?', type=float)
            budget.set_limit(limit_account, limit_amount)
            set_limit_input = click.prompt('Would you like to set another limit? (yes or no): ', type=str).lower()
            if set_limit_input == 'no':
                set_limit = False
