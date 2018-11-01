# Private Browsing PII Leakage Research

## Installation instructions

Make sure you have pipenv and python3 installed:

https://pipenv.readthedocs.io/en/latest/install/

Make sure you install mongodb also (brew for Mac)

```
pipenv install
```

To run the app, type the following into a terminal and keep running:

```
mongod --dbpath=./db
```

Type the following into a new terminal

```
pipenv shell
FLASK_APP=app.py flask run
```

Then go to http://localhost:5000 to see the site!

To see the database, open and/or install Robo 3T. 
Create an initial connection with default settings.
The database will be under flask_session -> Collections -> sessions.
In Mongo, a document is like a row and a collection is like a table.
Right click one of the sessions and select "View Document" to see the document. 
The long string under val is base64 encoded, so to see the contents, paste into a base64 decoder. 

To close the app, press ctrl+c in both terminals.