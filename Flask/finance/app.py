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
    total = db.execute("SELECT SUM(total) FROM purchase WHERE user_id = ?", session["user_id"])[0]['SUM(total)'] + cash
    return render_template("index.html", purchases=purchases, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        symbol = request.form.get("symbol").upper()
        shares = int(request.form.get("shares"))

        if symbol == "":
            return apology("Missing symbol")
        elif not lookup(symbol):
            return apology("Invalid symbol")
        else:
            price = (lookup(symbol)["price"]) * shares
            balance = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))[0]['cash']

            if balance < price:
                return apology("Can't afford")
            else:
                new_balance = balance - price
                db.execute("INSERT INTO purchase(symbol, shares, price, total, user_id) VALUES(?, ?, ?, ?, ?)", symbol, shares, lookup(symbol)["price"], price, session.get("user_id"))
                db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, session.get("user_id"))
                return redirect('/')


    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    return apology("TODO")


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
        elif not request.form.get("password"):
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

        # Look up the stock quote using the provided symbol
        quote = lookup(symbol)

        # If the lookup fails return an error message
        if not quote:
            return apology("Invalid symbol")

        # Otherwise, render the quoted.html template with the quote and symbol
        return render_template("quoted.html", quote=quote, symbol=symbol)

    # If accessed via a GET request, render the quote.html template
    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        name = request.form.get("username")
        password = request.form.get("password")
        password_again = request.form.get("confirmation")

        existing_user = db.execute("SELECT * FROM users WHERE username = ?", name)

        if existing_user:
            # Inform the user that the username is taken or blank
            return apology("Username already taken")
        elif name == "":
            return apology("Username cannot be blank")
        else:
            if password != password_again:
                # Inform the user that password doesn't match
                return apology("Password doesn't match")
            else:
                hashed_password = generate_password_hash(password)
                db.execute("INSERT INTO users(username, hash) VALUES(?, ?)", name, hashed_password)

                # Retrieve the newly inserted user ID
                user_id = db.execute("SELECT id FROM users WHERE username = ?", name)[0]['id']
                session["user_id"] = user_id
                print("User id:", user_id)

                # Redirect user to home page
                return redirect("/")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    return apology("TODO")
