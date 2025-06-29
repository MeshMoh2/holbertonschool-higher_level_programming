#!/usr/bin/python3
"""Lists all states from the database where name matches the user input"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Extract arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    cursor = db.cursor()

    # Use string formatting (insecure on purpose for this task)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Print each row exactly as returned
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Cleanup
    cursor.close()
    db.close()
