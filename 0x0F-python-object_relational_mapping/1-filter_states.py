#!/usr/bin/python3

"""
This script connects to a MySQL database and lists
 all states in the database hbtn_0e_0_usa
whose names start with 'N'. It takes three arguments:
- MySQL username
- MySQL password
- Database name

The script fetches and displays states ordered by states.id in ascending order.
Only states whose names start with 'N' are displayed.
"""

import MySQLdb
import sys


def filter_states_by_name_starting_with_N(username, password, database):
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

        # Execute the query to retrieve states starting with 'N' ordered by id
        query = "SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
        cursor.execute(query)

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
    # Get MySQL credentials and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to filter and print states starting with 'N'
    filter_states_by_name_starting_with_N(username, password, database)
