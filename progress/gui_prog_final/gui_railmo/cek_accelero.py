#!/usr/bin/python
import sys
import os
import time
i=5
os.system("sudo i2cdetect -y 1")
while(i!=0):
    sys.stdout.write("Program akan otomatis tertutup dalam: %d   \r" % (i))
    sys.stdout.flush()
    i-=1
    time.sleep(1)
os.system('clear')
sys.exit('\nProgram cek akselerometer selesai')
