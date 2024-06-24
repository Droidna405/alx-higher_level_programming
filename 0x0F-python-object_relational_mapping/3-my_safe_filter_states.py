#!/usr/bin/python3

"""
This script connects to a MySQL database and retrieves all rows
from the states table
in the database hbtn_0e_0_usa where the name matches a specified argument.
It takes four arguments:
- MySQL username
- MySQL password
- Database name
- State name to search for

The script is safe from SQL injection attacks.
It fetches and displays results ordered by states.id in ascending order.
"""

import MySQLdb
import sys


def filter_states_by_name(username, password, database, state_name):
    try:
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

        # Prepare SQL query using placeholders to prevent SQL injection
        query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
        cursor.execute(query, (state_name,))

        # Fetch all rows from the executed query
        states = cursor.fetchall()

        # Print results in the format (id, 'name')
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        # Close the cursor and the database connection
        cursor.close()
        db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./3-my_safe_filter_states.py <mysql_username> " +
              "<mysql_password> <database_name> <state_name>")
        sys.exit(1)

        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        filter_states_by_name(username, password, database, state_name)
