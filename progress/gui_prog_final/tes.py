import os
import time
import MySQLdb

f = open('log.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    for lines in f:
        print ("%s"%(lines))
        a,b,c,d,e,f,g,epx,waktu=lines.split(",")
        print ("no %s x=%s y=%s z=%s va=%s lat=%s lon=%s epx %s waktu %s "%(a,b,c,d,e,f,g, epx, waktu))
