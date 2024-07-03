#!/usr/bin/python3
"""
Script to filter states from the database by name argument.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    """
    Main entry point of the script. It retrieves command-line arguments,
    connects to the MySQL database, executes the query to filter states,
    and prints the results in ascending order by `id`.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        """
        Establish a connection to the MySQL database.
        """
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )
    except MySQLdb._exceptions.OperationalError as e:
        """
        Handle errors that occur during the connection attempt.
        """
        print(f"Error: {e}")
        sys.exit(1)

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    try:
        cursor.execute(query, (state_name,))

        rows = cursor.fetchall()

        for row in rows:
            print(row)
    except MySQLdb.Error as e:
        print(f"Query Error: {e}")

    cursor.close()
    db.close()
