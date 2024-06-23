#!/usr/bin/python3

"""
This script connects to a MySQL database and lists all states in
the database hbtn_0e_0_usa.
It takes three arguments:
- MySQL username
- MySQL password
- Database name

The script fetches and displays all states,
ordered by states.id in ascending order.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve all states ordered by id
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC")

    # Fetch all rows from the executed query
    states = cursor.fetchall()

    # Iterate and print each state as per the format (id, 'name')
    for state in states:
        print(state)

    # Close the cursor and the database connection
    cursor.close()
    db.close()
