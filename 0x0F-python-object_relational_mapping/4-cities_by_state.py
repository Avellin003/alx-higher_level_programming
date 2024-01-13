#!/usr/bin/python3
"""Lists all the states"""
import MySQLdb
import sys


if __name__ = "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cr = db.cursor()
    cr.execute("""SELECT cities.id, cities.name, states.name FROM
    citie INNER JOIN states ON  states.id=cities.state_id""")
    tables = cr.fetchall()
    for i in tables:
        print(i)
    cr.close()
    db.close()
