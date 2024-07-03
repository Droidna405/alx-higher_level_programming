#!/usr/bin/python3
"""
Script to filter states from the database by name argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Get the arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        # Connect to the database
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )
    except MySQLdb._exceptions.OperationalError as e:
        print(f"Error: {e}")
        sys.exit(1)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create the SQL query
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        # Execute the query
        cursor.execute(query, (state_name,))

        # Fetch all results
        rows = cursor.fetchall()

        # Print the results
        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Query Error: {e}")

    # Close the cursor and the connection
    cursor.close()
    db.close()
