#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa.
Takes three arguments:
- MySQL username
- MySQL password
- Database name

Example usage:
./4-cities_by_state.py root root hbtn_0e_4_usa
"""

import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql_username> " +
              "<mysql_password> <database_name>")
        sys.exit(1)

        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        try:
            # Connect to the MySQL database
            db = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=mysql_username,
                passwd=mysql_password,
                db=database_name,
                charset="utf8"
            )

            # Create a cursor object to interact with the database
            cursor = db.cursor()
            query = (
                "SELECT cities.id, cities.name, states.name "
                "FROM cities "
                "JOIN states ON cities.state_id = states.id "
                "ORDER BY cities.id ASC"
            )
            cursor.execute(query)

            cities = cursor.fetchall()

            # Print the results in the format (id, 'city_name', 'state_name')
            for city in cities:
                print(city)

        except MySQLdb.Error as e:
            print(f"Error: {e}")

        finally:
            # Close the cursor and the database connection
            if cursor:
                cursor.close()
            if db:
                db.close()
