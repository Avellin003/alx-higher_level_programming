#!/usr/bin/python3
"""lists all states"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306
            )

    cr = db.cursor()
    cr.execute(f"SELECT * FROM states WHERE name LIKE BINARY '{sys.argv[4]}'")
    tables = cr.fetchall()
    for i in tables:
        print(i)
    cr.close()
    db.close()
