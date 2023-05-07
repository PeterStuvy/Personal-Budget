# Testing Procedures

Two tests have been designed to test the functionality of this application. They are as follows:

## Test 1 - Add an Account and a Transaction

The following tests the ability to add an account and a transaction.

1. Run the main.py file.
2. Enter: Add an account
3. Enter: Main Bank Account
4. Enter: no
5. Enter: Add a transaction
6. Enter: 2022-05-07
7. Enter: 560
8. Enter: Groceries
9. Enter: Main Bank Account
10. Enter: no

transactions.csv should show the following if executed correctly

```
Date,Amount,Description,Account\n2022-05-07,560.0,Groceries,Main Bank Account
```

## Test 2 - Set a budget limit

1. Without quitting from the previous test, enter: Set a budget limit
2. Enter: Groceries
3. Enter: 600
4. Enter: no
5. Enter: View budget limits
6. Enter: View the remaining budget for the month
7. Enter: Groceries
7. Enter: Quit

If executed correctly, after selecting 'View budget limits', the following should be displayed:

```
{'Groceries': 600.0}
```

After selecting 'View the remaining budget for the month' and 'Groceries', the following should be displayed:

```
The remaining balance for Groceries is 40.
```