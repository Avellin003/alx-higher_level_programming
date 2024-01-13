#!/usr/bin/python3
"""creation of a script tha lists all states"""

if __name__ == "__name__":

    import MySQLdb
    import sys

    connect = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=f'{sys.argv[1]}',
            passwd=sys.argv[2],
            db=f'{sys.argv[3]}',
            charset='utf8'
            )
    sql = connect.cursor()
    sql.execute('SELECT * FROM states ORDER BY id ASC')
    table = sql.fetchall()
    for i in table:
        print(i)
    sql.close()
    connect.close()
