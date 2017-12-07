#!/usr/bin/python
import MySQLdb
import time

db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                     user="u745172280_byan",         # your username
                     passwd="21byan21",  # your password
                     db="u745172280_ta")        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

try:
    cur.execute("INSERT INTO masuk (indek, vmax, lat, lon) VALUES (10,24.3,-10.449784, 112.148438)")
    db.commit()
except:
    db.rollback()

# Use all the SQL you like



# print all the first cell of all the rows
#for row in cur.fetchall():
    #print row[0]
    #print row[1]

db.close()