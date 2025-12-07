#!/usr/bin/python3
"""Lists all values in states table matching the argument
"""

import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    cur = db.cursor()

    state_name = sys.argv[4]

    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cur.execute(query, (state_name,))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
