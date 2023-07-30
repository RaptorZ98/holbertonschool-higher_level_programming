#!/usr/bin/python3
""" select states """


import MySQLdb
from sys import argv

if __name__ == "main":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        for col in row:
            print ("%s,") % col
        print ("\n")
