import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    purchases = db.execute("SELECT * FROM purchase WHERE user_id = ?", session["user_id"])
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])[0]['cash']
    total = db.execute("SELECT SUM(total) FROM purchase WHERE user_id = ?", session["user_id"])[0]['SUM(total)']
    if total is None:
        total = 0
    grand_total = cash + total
    return render_template("index.html", purchases=purchases, cash=cash, total=grand_total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper().strip()
        shares = request.form.get("shares")
        user_id = session["user_id"]

        try:
            shares = float(shares)
        except ValueError:
            return apology("Shares must be a whole number")

        if float(shares) != int(shares):
            return apology("Shares must be a whole number")
        if not symbol:
            return apology("Missing symbol")
        if not shares:
            return apology("Missing shares")
        shares = int(shares)
        if shares <= 0:
            return apology("Not a positive shares")
        try:
            shares = float(request.form.get("shares"))
        except ValueError:
            return apology("Shares must be a number")

        stock = lookup(symbol)
        if stock is None:
            return apology("Invalid symbol")

        transaction = shares * stock["price"]

        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']

        if cash < transaction:
            return apology("Can't afford")

        new_cash = cash - transaction
        type = "BUY"
        symbols = db.execute("SELECT * FROM purchase WHERE user_id = ? AND symbol = ?", user_id, symbol)
        if symbols:
            db.execute("UPDATE purchase SET shares = shares + ?, total = total + ? WHERE user_id = ? AND symbol = ?", shares, transaction, user_id, symbol)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)
            db.execute("INSERT INTO history(symbol, type, shares, price, trans_id) VALUES(?, ?, ?, ?, ?)", symbol, type, shares, stock["price"], user_id)
        else:
            db.execute("INSERT INTO purchase(symbol, shares, price, total, user_id) VALUES(?, ?, ?, ?, ?)", symbol, shares, stock["price"], transaction, user_id)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_cash, user_id)
            db.execute("INSERT INTO history(symbol, type, shares, price, trans_id) VALUES(?, ?, ?, ?, ?)", symbol, type, shares, stock["price"], user_id)
        flash('Bought!')
        return redirect('/')

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    transactions = db.execute("SELECT * FROM history WHERE trans_id = ?", session["user_id"])
    print(transactions)
    return render_template("history.html", transactions=transactions)

@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Increase cash amount"""
    if request.method == "POST":
        deposit = int(request.form.get("deposit"))

        if deposit <= 0:
            return apology("Enter positive number")
        if not deposit:
            return apology("Missing amount")

        symbol, type, shares = "-", "DEPOSIT", "-"
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']
        if (cash + deposit) > 1000000:
            return apology("Maximum cash balance allowed is $1M")
        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", deposit, user_id)
        db.execute("INSERT INTO history(symbol, type, shares, price, trans_id) VALUES(?, ?, ?, ?, ?)", symbol, type, shares, deposit, user_id)
        flash('Deposit Succesful')
        return redirect('/')

    return render_template("deposit.html")

@app.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    """Withdraw cash amount"""
    if request.method == "POST":
        withdraw = int(request.form.get("withdraw"))

        if withdraw <= 0:
            return apology("Enter positive number")
        if not withdraw:
            return apology("Missing amount")

        symbol, type, shares = "-", "WITHDRAW", "-"
        user_id = session["user_id"]
        cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        if withdraw > cash[0]['cash']:
            return apology("Insufficient fund")
        db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", withdraw, user_id)
        db.execute("INSERT INTO history(symbol, type, shares, price, trans_id) VALUES(?, ?, ?, ?, ?)", symbol, type, shares, withdraw, user_id)
        flash('Withdrawal Succesful')
        return redirect('/')

    return render_template("withdraw.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        if not request.form.get("password"):
            return apology("must provide password", 403)


        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)


        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    # If the user submitted the form
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()

        if not symbol:
            return apology("Missing symbol")
        # Look up the stock quote using the provided symbol
        quote = lookup(symbol)

        # If the lookup fails return an error message
        if not quote:
            return apology("Invalid symbol")

        # Otherwise, render the quoted.html template with the quote and symbol
        return render_template("quoted.html", price=quote['price'], symbol=quote['symbol'])

    # If accessed via a GET request, render the quote.html template
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        if not name:
            return apology("Username cannot be blank")
        if not password:
            return apology("Username cannot be blank")
        if password != confirmation:
             return apology("Password don't match")

        existing_user = db.execute("SELECT * FROM users WHERE username = ?", name)

        if existing_user:
            # Inform the user that the username is taken or blank
            return apology("Username already taken")
        else:
            hashed_password = generate_password_hash(password)
            db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", name, hashed_password)

            # Retrieve the newly inserted user ID
            user_id = db.execute("SELECT id FROM users WHERE username = ?", name)[0]['id']
            session["user_id"] = user_id

            flash('Registered Successful')

            # Redirect user to home page
            return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "GET":
        symbols = db.execute("SELECT symbol FROM purchase WHERE user_id = ? GROUP BY symbol HAVING SUM(shares) > 0", session["user_id"])
        return render_template("sell.html", symbols=[row['symbol'] for row in symbols])
    else:
        user_id = session["user_id"]
        symbol = request.form.get("symbol")
        shares = int(request.form.get("shares"))

        if not symbol:
            return apology("Missing symbol")
        elif shares < 1:
            return apology("Shares must be positive")
        else:
            type = "SELL"
            price = (lookup(symbol)["price"])
            total = price * shares
            balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]['cash']
            symbols = db.execute("SELECT * FROM purchase WHERE user_id = ? AND symbol = ?", user_id, symbol)
            if shares > symbols[0]['shares']:
                return apology("Too many shares")
            elif symbols:
                new_balance = balance + total
                db.execute("UPDATE purchase SET shares = shares - ?, total = total - ? WHERE user_id = ? AND symbol = ?", shares, total, user_id, symbol)
                db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, user_id)
                db.execute("INSERT INTO history(symbol, type, shares, price, trans_id) VALUES(?, ?, ?, ?, ?)", symbol, type, shares, price, user_id)
                updated_shares = db.execute("SELECT shares FROM purchase WHERE user_id = ? AND symbol = ?", user_id, symbol)[0]['shares']
                if updated_shares == 0:
                    db.execute("DELETE FROM purchase WHERE user_id = ? AND symbol = ?", user_id, symbol)
                flash('Sold!')
                return redirect('/')

