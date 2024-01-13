#!/usr/bin/python3
"""create MySQLdb"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            port=3306)
    cr = db.cursor()
    cr.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'"
            .format(sys.argv[4]))
    rs = cr.fetchall()
    for r in rs:
        print(r)
    cr.close()
    db.close()
