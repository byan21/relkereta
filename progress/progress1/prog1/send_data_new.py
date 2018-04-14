import os
import time
import MySQLdb

f = open('log.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    for lines in f:
        #lines=f.readline()
        print ("%s"%(lines))
        a,b,c,d,e,f,g=lines.split(",")
        print ("no =%s x=%s y=%s z=%s va=%s lat=%s lon=%s"%(a,b,c,d,e,f,g))
        db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                         user="u745172280_byan",         # your username
                         passwd="21byan21",  # your password
                         db="u745172280_ta")        # name of the data base
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO data_tes (x, y, z, va, lat, lon) VALUES (%s,%s,%s,%s,%s,%s)",(b, c, d, e,f,g))
            db.commit()
            print ("sukses")
        except:
            print ("Gagal")
            db.rollback()
        db.close()
        time.sleep(2)