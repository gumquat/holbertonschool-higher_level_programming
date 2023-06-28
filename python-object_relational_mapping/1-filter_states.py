#!/usr/bin/python3
"""
list all states with a name starting with N
from database hbtn_0e_0_USA
"""
import MySQLdb
import sys


def N_states():
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

   # cursor = db.cursor()

   # cursor.execute("SELECT * FROM states WHERE NAME LIKE 'N%' ORDER BY id")

   # rows = cursor.fetchall()

   # for row in rows:
        print(row)

   # cursor.close()
    db.close()


    if __name__ == "__main__":
        N_states()
