#!/usr/bin/python3
"""a script that takes in the name of a state as an argument
and lists all cities of that state
"""
import sys
import MySQLdb

if __name__ == "__main__":
    user_name = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        user=user_name,
        passwd=password,
        db=db_name,
        port=3306
    )

    curs = db.cursor()
    curs.execute(
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s ORDER BY cities.id ASC",
        (state_name,)
        )

    rows = curs.fetchall()

    cities = [row[1] for row in rows]
    print(", ".join(cities))
    curs.close()
    db.close()
