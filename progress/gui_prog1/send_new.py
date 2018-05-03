import os
import time
import MySQLdb
from math import radians, cos, sin, asin, sqrt

oo = open('log.txt', 'r', os.O_NONBLOCK)
mm = open('log.txt', 'r', os.O_NONBLOCK)
ids = open('add_id.txt', 'r')
baris = open('baris', 'r')
n=0

lat = 0.0
lon = 0.0

x=[]
y=[]
z=[]
v=[]
ep=[]

def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    # Radius of earth in kilometers is 6371
    km = 6371 * c
    return km*1000


def send(Ax, Ay, Az, Av, lon, lat, eps, waktu, petugas, rute):
    b = str(Ax)
    c = str(Ay)
    d = str(Az)
    e = str(Av)
    f = str(lat)
    g = str(lon)
    h = str(eps)
    i = str(petugas)
    j = str(rute)
    waktus = str(waktu)
    print (" x=%s y=%s z=%s va=%s lat=%s lon=%s error=%s petugas=%s rute=%s waktu=%s"%(b,c,d,e,f,g,h,i,j,waktus))
    
    db = MySQLdb.connect(host="sql143.main-hosting.eu",  
                            user="u745172280_byan",         
                            passwd="21byan21",  
                            db="u745172280_ta")       
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO data_indek (x, y, z, va, lat, lon, epx, id_petugas, id_kereta, waktu) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (b, c, d, e, f, g, h, i, j, waktus))
        db.commit()
        print ("sukses")
    except:
        print ("Gagal")
        db.rollback()
    db.close()

for lines in ids:
    print ("%s"%(lines))
    petugas,rute=lines.split(",")

first = mm.readline()
a,b,c,d,e,f,g,epx,waktu=first.split(",")
#print ("no =%s x=%s y=%s z=%s va=%s lat=%s lon=%s error=%s waktu=%s"%(a,b,c,d,e,f,g,epx,waktu))

lat = float(f)
lon = float(g)
xf = float(b)
yf = float(c)
zf = float(d)
vf = float(e)
epxf= float(epx)
waktu_a=waktu
bariske = int(baris)
while 1:
    for lines in oo:
        print ("%s"%(lines))
        a,b,c,d,e,f,g,epx,waktu=lines[baris].split(",")
        #print ("no =%s x=%s y=%s z=%s va=%s lat=%s lon=%s error=%s waktu=%s"%(a,b,c,d,e,f,g,epx,waktu))
        latf = float(f)
        lonf = float(g)
        xf = float(b)
        yf = float(c)
        zf = float(d)
        vf = float(e)
        epxf= float(epx)
        waktu_a=waktu
        
        if(lat==latf and lon==lonf):
            x.append(xf)
            y.append(yf)
            z.append(zf)
            v.append(vf)
            ep.append(epxf)
        else:
            s = haversine(lonf,latf,lon,lat)
            if (s>=1):
                Ax = sum(x)/len(x)
                Ay = sum(y)/len(y)
                Az = sum(z)/len(z)
                Av = sum(v)/len(v)
                Ae = sum(ep)/len(ep)
                send(Ax, Ay, Az, Av, lon, lat, Ae, waktu_a,petugas,rute)
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
