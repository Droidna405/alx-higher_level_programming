#!/usr/bin/python3
"""
This script connects to a MySQL database and displays all values in the
`states` table of the `hbtn_0e_0_usa` database where the `name` column
matches a user-provided argument. It sorts the results by `id` in
ascending order.

Command-line arguments:
    - sys.argv[1]: MySQL username
    - sys.argv[2]: MySQL password
    - sys.argv[3]: Database name
    - sys.argv[4]: State name to search for
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Connects to the MySQL database, retrieves matching state entries,
    and prints them.
    """

    # Connect to the MySQL database using command-line arguments
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        charset="utf8"
    )

    # Create a cursor object to interact with the database
    cur = conn.cursor()

    # Prepare the query to select states that match the provided name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        cur.execute(query, (sys.argv[4],))

        # Fetch all the results
        query_rows = cur.fetchall()

        # Print each row of the result
        for row in query_rows:
            print(row)
    except MySQLdb.Error as e:
        # Handle any errors that occur during the query execution
        print(f"Error: {e}")

    # Close the cursor and the connection
    cur.close()
    conn.close()
