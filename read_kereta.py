import os
import time
f = open('data.txt', 'r', os.O_NONBLOCK)
n=0
while 1:
    lines=f.readline()
    print ("%s"%(lines))
    a,b,c,d=lines.split(",")
    print ("a=%s b=%s c=%s d=%s"%(a,b,c))
    time.sleep(2)
    