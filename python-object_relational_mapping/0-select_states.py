#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys



def list_states(username, password, database):
    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, password=password, db=database)

    """Create a cursor object to execute SQL queries"""
    cursor = db.cursor()

    """Execute the query to fetch all states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all the rows returned by the query"""
    rows = cursor.fetchall()

    """Display the results"""
    for row in rows:
        print(row) # this will not output in the format desired

    """Close the cursor and database connection"""
    cursor.close()
    db.close()

"""Provide the MySQL username, password, and database name"""
username = "your_username"
password = "your_password"
database = "hbtn_0e_0_usa"

if __name__ == "__main__":
    list_states()