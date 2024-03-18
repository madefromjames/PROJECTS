# Birthday Tracker Web Application
This is a simple web application built using Flask and SQLite that allows users to store and keep track of birthdays.

##  Understanding
In `app.py`, you’ll find the start of a Flask web application. The application has one route (`/`) that accepts both `POST` requests (after the if) and `GET` requests (after the else). When the `/` route is requested via `GET`, the index.html template is rendered, displaying all the people in the database along with their birthdays in a table. When the `/` route is requested via `POST`, the user is redirected back to `/` via `GET`.

The `birthdays.db` SQLite database has one table, `birthdays`, with four columns: `id`, `name`, `month`, and `day`. The table already contains a few rows, and the application supports the ability to insert new rows into this table.

The static directory contains a `styles.css` file with the CSS code for this web application. The templates directory contains an `index.html` file that will be rendered when the user views the web application.

## Implementation Details
The following implementation details have been completed:

When the `/` route is requested via `GET`, the web application displays all the people in the database along with their birthdays in a table.
In `app.py`, logic has been added in the `GET` request handling to query the `birthdays.db` database for all birthdays. The data is then passed to the `index.html` template.
In `index.html`, logic has been added to render each birthday as a row in the table. Each row has two columns: one for the person's name and another for the person's birthday.
When the `/` route is requested via `POST`, a new birthday is added to the database, and the index page is re-rendered.
In `index.html`, an HTML form has been added that lets users type in a name, a birthday month, and a birthday day. The form submits to `/` with a method of post.
In `app.py`, logic has been added in the `POST` request handling to INSERT a new row into the birthdays table based on the data supplied by the user.

## Additional Features
The following additional features have been added:

The ability to delete birthday entries has been added.
The ability to edit birthday entries has been added.
The application has been styled using the `styles.css` file.
The application has been tested and validated using the Flask framework and SQLite.

## Usage
To use the application, simply run the `app.py` file using a Python interpreter. The application will start a local server on port 5000. To access the application, open a web browser and navigate to http://localhost:5000/.

To add a new birthday, simply fill out the form on the index page and submit it. The new birthday will be added to the database and displayed on the page.

To delete a birthday, click on the "Delete" button next to the birthday in the table. The birthday will be removed from the database and the page will be re-rendered.

To edit a birthday, click on the "Edit" button next to the birthday in the table. The birthday details will be displayed in a form, which can be edited and submitted to update the database.

## Dependencies
The following dependencies are required to run the application:

Python<br>
Flask<br>
SQLite<br>