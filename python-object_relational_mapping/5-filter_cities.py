#!/usr/bin/python3
""" select states """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name\
 FROM cities JOIN states ON \
states.id = cities.state_id WHERE states.name = {argv4} \
ORDER BY id ASC;")
    rows = cur.fetchall()
    i = 0
    for row in rows:
        if i == 0:
            print(", ", end="")
        print(row, end="")
    cur.close()
    db.close()
