import os
import time
import MySQLdb

f = open('data.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    for lines in f:
        #lines=f.readline()
        print ("%s"%(lines))
        a,b,c,d,e=lines.split(",")
        print ("a=%s b=%s c=%s d=%s e=%s"%(a,b,c,d,e))
        db = MySQLdb.connect(host="sql143.main-hosting.eu",   # your host, usually localhost
                         user="u745172280_byan",         # your username
                         passwd="21byan21",  # your password
                         db="u745172280_ta")        # name of the data base
        cur = db.cursor()
        try:
            cur.execute("INSERT INTO masuk_tb (vmax, lat, lon, colx, coly) VALUES (%s,%s,%s,%s,%s)",(a, b, c,d,e))
            db.commit()
            print ("sukses")
        except:
            print ("gagal")
            db.rollback()
        db.close()
        time.sleep(2)
    
