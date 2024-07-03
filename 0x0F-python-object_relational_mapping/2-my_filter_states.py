#!/usr/bin/python3
"""
Script to filter and display states from the database `hbtn_0e_0_usa`.

This script connects to a MySQL database using MySQLdb, executes a query to
retrieve states that match a user-specified name, and prints the results in
ascending order by `id`.

Command-line arguments:
    - mysql_username: MySQL username
    - mysql_password: MySQL password
    - db_name: Name of the MySQL database
    - state_name: State name to search for
"""

import sys
import MySQLdb


def main():
    """
    Main entry point of the script.

    This function retrieves command-line arguments, connects to the MySQL
    database, executes a query to filter states, and prints the results
    in ascending order by `id`.

    Raises:
        MySQLdb.OperationalError: If there is an error connecting to
        the database.
        MySQLdb.Error: If there is an error executing the query.
    """
    # Command-line arguments: mysql username, password, db name, state name
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    try:
        db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_username,
            passwd=mysql_password,
            db=db_name
        )
    except MySQLdb.OperationalError as e:
        print(f"Connection Error: {e}")
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
    finally:
        cursor.close()
        db.close()


if __name__ == "__main__":
    """
    If the script is run directly, the `main` function is executed.
    """
    main()
