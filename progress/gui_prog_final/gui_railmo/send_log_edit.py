import os
import time
import MySQLdb
from math import radians, cos, sin, asin, sqrt
import math

oo = open('log.txt', 'r', os.O_NONBLOCK)
ids = open('add_id.txt', 'r')
n=0

lat = 0.0
lon = 0.0
with open ('baris','r') as baris:
    for lines in baris:
        print ("%s"%(lines))
        baris_akhir=int (lines)


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


def send(Ax, Ay, Az, Av, lon, lat, eps, waktu, petugas, rute, indek, vmax, kereta):
    b = str(Ax)
    c = str(Ay)
    d = str(Az)
    e = str(Av)
    f = str(lat)
    g = str(lon)
    h = str(eps)
    i = str(petugas)
    j = str(rute)
    k = str(indek)
    l = str (vmax)
    m = str (kereta)
    waktus = str(waktu)
    print (" x=%s y=%s z=%s va=%s lat=%s lon=%s error=%s petugas=%s rute=%s waktu=%s indek=%s vmax=%s kereta=%s"%(b,c,d,e,f,g,h,i,j,waktus,k,l,m))
    
    db = MySQLdb.connect(host="sql143.main-hosting.eu",  
                            user="u745172280_21rel",         
                            passwd="21rel21",  
                            db="u745172280_rel")       
    cur = db.cursor()
    try:
        cur.execute(
            "INSERT INTO data_indek (x, y, z, va, lat, lon, epx, id_petugas, id_rute, waktu_gps, indek, vmak, id_kereta) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (b, c, d, e, f, g, h, i, j, waktus,k,l,m))
        db.commit()
        print ("sukses")
    except:
        print ("Gagal")
        db.rollback()
    db.close()
    
def index(xi,vi):
    if(xi!=0):
        if(vi>=80):
            nt=15/xi
            return nt
        elif(vi>=40 and vi<80):
            nt = (3*vi)/(16*xi)
            return nt
        else :
            nt = 100
            return nt
    else:
        nt =100
        return nt
def indez(zi,vi):
    za = abs(zi-1)
    print("sumbu z dikurangi = %s"%(za))
    if (za!=0):
        if (vi>=80):
            nt=20/za
            return nt
        elif(vi>=40 and vi<80):
            nt = (4*vi)/(16*za)
            return nt
        else :
            nt = 100
            return nt
    else:
        nt =100
        return nt
        
def nilai_akhir(IX,IZ):
    if (IX is None or IZ is None):
        return None
    else :
        if (IX<=IZ):
            return IX
        else:
            return IZ
def vmak(indek,v):
    vm = v/100*indek
    vmm = math.ceil((vm*100)/100)
    return vmm

for lines in ids:
    print ("%s"%(lines))
    petugas,rute, kereta=lines.split(",")
for _ in xrange(baris_akhir):
    next(oo)
for lines in oo:
    a,b,c,d,e,f,g,epx,waktu=lines.split(",")
    print ("no =%s x=%s y=%s z=%s va=%s lat=%s lon=%s error=%s waktu=%s"%(a,b,c,d,e,f,g,epx,waktu))
    lat = float(f)
    lon = float(g)
    xf = abs(float(b))
    yf = abs(float(c))
    zf = abs(float(d))
    vf = float(e)
    epxf= float(epx)
    x.append(xf)
    y.append(yf)
    z.append(zf)
    v.append(vf)
    ep.append(epxf)
    #next(oo)
    waktu_a=waktu
    break
while 1:
    for lines in oo:
        print ("%s"%(lines))
        a,b,c,d,e,f,g,epx,waktu=lines.split(",")
        print ("no =%s x=%s y=%s z=%s va=%s lat=%s lon=%s error=%s waktu=%s"%(a,b,c,d,e,f,g,epx,waktu))
        latf = float(f)
        lonf = float(g)
        xf = abs(float(b))
        yf = abs(float(c))
        zf = abs(float(d))
        vf = float(e)
        epxf= float(epx)
        waktu_a=waktu
        baris = open ('baris','w')
        baris_akhir += 1
        bariss = str(baris_akhir)
        baris.write(bariss)
        baris.close()
        
        
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
                if(Av>=0):
                    IX=index(Ax,Av)
                    IZ=indez(Az,Av)
                    INDEK=nilai_akhir(IX,IZ)
                    print("rata x= %s"%(Ax))
                    print("rata z= %s"%(Az))
                    print("rata v= %s"%(Av))
                    print("indek x= %s"%(IX))
                    print("indek z= %s"%(IZ))
                    print("indek = %s"%(INDEK))
                    VMAX=vmak(INDEK,Av)
                    send(Ax, Ay, Az, Av, lon, lat, Ae, waktu_a,petugas,rute, INDEK, VMAX, kereta)
                lon = lonf
                lat = latf
                del x[:]
                del y[:]
                del z[:]
                del v[:]
                del ep[:]
                x.append(xf)
                y.append(yf)
                z.append(zf)
                v.append(vf)
                ep.append(epxf)
            # else:
            #     Ax = sum(x)/len(x)
            #     Ay = sum(y)/len(y)
            #     Az = sum(z)/len(z)
            #     Av = sum(v)/len(v)
            #     send(Ax, Ay, Az, Av,lon, lat)
        time.sleep(2)
