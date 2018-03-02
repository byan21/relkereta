import os
import time
import MySQLdb

f = open('dhoho5.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    for lines in f:
        #lines=f.readline()
        print ("%s"%(lines))
        a,b,c,d,e,f=lines.split(",")
        print ("x=%s y=%s z=%s va=%s lat=%s lon=%s"%(a,b,c,d,e,f))
        db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                         user="u745172280_byan",         # your username
                         passwd="21byan21",  # your password
                         db="u745172280_ta")        # name of the data base
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO data1_tb (x, y, z, va, lat, lon) VALUES (%s,%s,%s,%s,%s,%s)",(a, b, c, d, e, f))
            db.commit()
            print ("sukses")
        except:
            db.rollback()
        db.close()
        time.sleep(2)
    
