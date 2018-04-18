import os
import time
import MySQLdb
from math import radians, cos, sin, asin, sqrt

f = open('Da1.txt', 'r', os.O_NONBLOCK)
j = open('dWa1.txt','a', os.O_NONBLOCK)
n = 0

lat = 0.0
lon = 0.0

x = [0]
y = [0]
z = [0]
v = [0]

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c * 1000
    return km

def send(Ax, Ay, Az, Av, lon, lat, lonf, latf):
    jarak = haversine(lon, lat, lonf, latf)
    b = str(Ax)
    c = str(Ay)
    d = str(Az)
    e = str(Av)
    f = str(lat)
    g = str(lon)
    h = str(latf)
    i = str(lonf)
    k = str(jarak)
    j.write("%s, %s, %s, %s, %s, %s, %s, %s, %s\n" %(b,c,d,e,f,g,h,i,k))
    j.flush()



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
            send(Ax, Ay, Az, Av, lon, lat, lonf, latf)
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
