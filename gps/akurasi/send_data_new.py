import os
import time
import MySQLdb

f = open('data.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    for lines in f:
        #lines=f.readline()
        print ("%s"%(lines))
        a,b,c=lines.split(",")
        print ("Kecepatan= %s lat= %s lon= %s"%(a,b,c))
        db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                         user="u745172280_byan",         # your username
                         passwd="21byan21",  # your password
                         db="u745172280_ta")        # name of the data base
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO akurasi_gps (kec, lat, lon) VALUES (%s,%s,%s)",(a, b, c))
            db.commit()
            print ("sukses")
        except:
            db.rollback()
        db.close()
        time.sleep(2)
    

