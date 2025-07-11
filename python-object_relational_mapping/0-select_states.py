#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()
