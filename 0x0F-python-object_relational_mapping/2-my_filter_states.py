#!/usr/bin/python3

"""create MySQLdb"""

import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306,
            charset='utf8')
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
            .format(sys.argv[4]))
    tables = cr.fetchall()
    for i in tables:
        print(i)
    cr.close()
    db.close()
