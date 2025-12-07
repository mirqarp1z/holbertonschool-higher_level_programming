#!/usr/bin/python3
"""
Lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=database,
        port=3306
    )

    kursor = db.cursor()

    kursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = kursor.fetchall()

    for row in rows:
        print(row)

    kursor.close()
    db.close()
