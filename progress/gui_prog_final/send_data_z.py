import os
import time
import MySQLdb
from math import radians, cos, sin, asin, sqrt

f = open('dz1.txt', 'r', os.O_NONBLOCK)
n = 0

lat = 0.0
lon = 0.0

x = [0]
y = [0]
z = [0]
v = [0]



def send(Ax, Ay, Az, Av, lon, lat):
    b = str(Ax)
    c = str(Ay)
    d = str(Az)
    e = str(Av)
    f = str(lat)
    g = str(lon)
    db = MySQLdb.connect(host="sql143.main-hosting.eu",
                         user="u745172280_byan",
                         passwd="21byan21",
                         db="u745172280_ta")
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO data_tes1 (x, y, z, va, lat, lon) VALUES (%s,%s,%s,%s,%s,%s)", (b, c, d, e, f, g))
        db.commit()
        print ("sukses")
    except:
        print ("Gagal")
        db.rollback()
    db.close()


while 1:
    for lines in f:
        #lines=f.readline()
        print ("%s" % (lines))
        a, b, c, d, e, f, g = lines.split(",")
        print ("no =%s x=%s y=%s z=%s va=%s lat=%s lon=%s" %
               (a, b, c, d, e, f, g))
        latf = float(f)
        lonf = float(g)
        xf = float(b)
        yf = float(c)
        zf = float(d)
        vf = float(e)

        if(lat == latf and lon == lonf):
            x.append(xf)
            y.append(yf)
            z.append(zf)
            v.append(vf)
        else:
            Ax = sum(x)/len(x)
            Ay = sum(y)/len(y)
            Az = sum(z)/len(z)
            Av = sum(v)/len(v)
            send(Ax, Ay, Az, Av, lon, lat)
            lon = lonf
            lat = latf
            del x[:]
            del y[:]
            del z[:]
            del v[:]
            x.append(xf)
            y.append(yf)
            z.append(zf)
            v.append(vf)
            # else:
            #     Ax = sum(x)/len(x)
            #     Ay = sum(y)/len(y)
            #     Az = sum(z)/len(z)
            #     Av = sum(v)/len(v)
            #     send(Ax, Ay, Az, Av,lon, lat)
        time.sleep(0.5)