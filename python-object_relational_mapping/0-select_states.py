#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Get MySQL credentials and database name from command line arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to the MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=db_name)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SELECT query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them
    for row in cursor.fetchall():
        print(row)

    # Clean up
    cursor.close()
    db.close()
