import os
import time
import MySQLdb

f = open('data.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    for lines in f:
        #lines=f.readline()
        print ("%s"%(lines))
        a,b,c,d,e,f,g,h,i=lines.split(",")
        print ("x=%s y=%s va=%s indeks=%s lat=%s lon=%s"%(a,b,c,d,f,g))
        db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                         user="u745172280_byan",         # your username
                         passwd="21byan21",  # your password
                         db="u745172280_ta")        # name of the data base
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO data2_tb (x, y, va,indek, lat, lon) VALUES (%s,%s,%s,%s,%s,%s)",(a, b, c, d, f,g))
            db.commit()
            print ("sukses")
        except:
            db.rollback()
        db.close()
        time.sleep(2)
    

