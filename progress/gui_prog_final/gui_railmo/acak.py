import random
import os
import time
def main():
    try:
        i=0
        outfile = open ('log.txt','a', os.O_NONBLOCK)
        for count in range (500):
            i+=1
            x = round(random.uniform(0.0,2.0),2)
            y = round(random.uniform(0.0,2.0),2)
            z = round(random.uniform(0.0,2.0),2)
            va = random.randint(1,100)
            lat = random.randint(1,100)
            lon = random.randint(1,100)
            epx = random.randint(1,100)
            waktu = random.randint(1,100)
            print("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(i,x,y,z,va,lat,lon, epx, waktu))
        
            outfile.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(i,x,y,z,va,lat,lon,epx, waktu))
            outfile.flush()
            time.sleep(1)
    except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
        print "\nKilling Thread..."
main()
