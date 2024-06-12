import sqlite3

# create a database connection
conn = sqlite3.connect("db/database.db")

# get access to the cursor object
cursor = conn.cursor()
