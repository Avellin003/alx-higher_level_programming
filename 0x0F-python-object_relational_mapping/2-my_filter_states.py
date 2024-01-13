#!/usr/bin/python3
"""create MySQLdb"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            port=3306,
            passwd=sys.argv[2],
            charset='utf8',
            db=sys.argv[3]
            )
    cr = db.cursor()
    cr.execute(f'SELECT * FROM states\
            WHERE name = "{sys.argv[4]}"\
            ORDER BY id ASC')
    tables = cr.fetchall()
    for i in tables:
        print(i)
    cr.close()
    db.close()
