#!/usr/bin/python3
""" Lists all states starting with 'N' from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    # Connect to database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Execute query
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # Print results
    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
