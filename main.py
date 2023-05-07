from budget import budget
from datetime import datetime
import click
from pprint import pprint

my_budget = budget()

while True:
    feature_options = ['Add an account', 'Add a transaction', 'View transactions or accounts', 'Set a budget limit', 'View budget limits', 'View the remaining budget for the month', 'Quit']
    feature_choice = click.prompt('What would you like to do?: ', type=click.Choice(feature_options))

    if feature_choice == 'Add an account':
        add_account = True
        while add_account:
            account_name = click.prompt('What is the name of the account?', type=str)
            my_budget.add_account(account_name)
            add_account_input = click.prompt('Would you like to add another account? (yes or no): ', type=str).lower()
            if add_account_input == 'no':
                add_account = False
            
    elif feature_choice == 'Add a transaction':
        add_transaction = True
        while add_transaction:
            while True:
                try:
                    transaction_date_str = click.prompt('What is the date of the transaction? (YYYY-MM-DD)', type=str)
                    transaction_date = datetime.strptime(transaction_date_str, '%Y-%m-%d').date()
                    break
                except ValueError:
                    pprint('Invalid date format. Enter the date in the format: YYYY-MM-DD')
            transaction_amount = click.prompt('What is the amount of the transaction?', type=float)
            transaction_description = click.prompt('Write a description for the transaction:', type=str)
            account_names = [account_name for account_name in my_budget.accounts.keys()]
            transaction_account = click.prompt('What account did the transaction occur in?', type=click.Choice(account_names))
            my_budget.add_transaction(transaction_date, transaction_amount, transaction_description, transaction_account)
            add_transaction_input = click.prompt('Would you like to add another transaction? (yes or no): ', type=str).lower()
            if add_transaction_input == 'no':
                add_transaction = False
    
    elif feature_choice == 'Set a budget limit':
        set_limit = True
        while set_limit:
            limit_account = click.prompt('What is the name of the account you would like to set a limit for?', type=str)
            limit_amount = click.prompt('What is the amount of the limit?', type=float)
            my_budget.set_limit(limit_account, limit_amount)
            set_limit_input = click.prompt('Would you like to set another limit? (yes or no): ', type=str).lower()
            if set_limit_input == 'no':
                set_limit = False
    
    elif feature_choice == 'View budget limits':
        my_budget.view_limits()
    
    elif feature_choice == 'View the remaining budget for the month':
        remaining_balance_choice = click.prompt('Which account would you like to see the remaining balance for?', type=click.Choice(account_names))
        my_budget.check_remaining_balance(remaining_balance_choice)

    elif feature_choice == 'Quit':
        SystemExit
    
    
