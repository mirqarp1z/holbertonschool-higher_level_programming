#!/usr/bin/python3
"""
a script that lists all states with a name starting with N from the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=db_name,
        port=3306
    )

    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states "
        "WHERE BINARY name LIKE 'N%' "
        "ORDER BY id ASC"
    )

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
