# Finance
This project is a web application designed to help users manage their finances by allowing them to register, log in, view stock quotes, buy and sell stocks, view transaction history, and manage their cash balance.

## Getting Started
To run the application, follow these steps:
Start Flask's built-in web server by navigating to the finance/ directory and running the command:
`$ flask run`.
Visit the URL outputted by Flask to access the application.

## Database Setup
Navigate to the `finance/` directory.
Run `sqlite3 finance.db` to open `finance.db` with SQLite.
Run `.schema` in the SQLite prompt to view the structure of the `finance.db` database and inspect the users table.

## Understanding the Code
`app.py`

This file contains the main application logic and route implementations.
It handles user authentication, registration, stock quotes, buying and selling stocks, and displaying transaction history.

`helpers.py`

This file contains helper functions used throughout the application, such as rendering apologies, requiring user login, and formatting values.

`requirements.txt`

Lists the required Python packages for the application.

`static/`

Contains static files including CSS styles.

`templates/`

Contains HTML templates for different pages of the application.

## Implementation Details
### Register
Allows users to register for an account via a form.
Validates input fields for username and password.
Hashes the user's password before storing it in the database.
### Quote
Allows users to look up a stock's current price by entering its symbol.
Renders an HTML form for users to input the stock symbol.
Displays the current price of the stock after submitting the form.
### Buy
Enables users to buy stocks by entering the stock symbol and number of shares.
Validates input fields and checks if the user can afford the purchase.
Updates the user's cash balance and records the transaction in the database.
### Sell
Allows users to sell shares of a stock they own.
Validates input fields and checks if the user owns enough shares to sell.
Updates the user's cash balance and records the transaction in the database.
### Index
Displays a summary of the user's portfolio, including owned stocks, number of shares, current prices, and total values.
Also displays the user's current cash balance and the overall portfolio value.
### History
Displays a table summarizing all of a user's past transactions, including buys, sells, deposits and withdrawals.
Provides details such as the stock symbol, transaction type, price, number of shares, and transaction date.
### Deposits
Allows users to add additional cash to their account to manage their balance effectively.
### Withdrawal
Enables users to withdraw cash from their account as needed.

## Conclusion
This README provides an overview of the project structure, how to run the application, and details about its implementation. Explore the codebase further to understand specific functionalities