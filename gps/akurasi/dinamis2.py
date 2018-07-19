#! /usr/bin/python
# Written by Dan Mandle http://dan.mandle.me September 2012
# License: GPL 2.0
 
import os
from gps import *
from time import *
import time
import threading
from math import radians, cos, sin, asin, sqrt
import math
 
gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)

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
 
class GpsPoller(threading.Thread):
  def __init__(self):
    threading.Thread.__init__(self)
    global gpsd #bring it in scope
    gpsd = gps(mode=WATCH_ENABLE) #starting the stream of info
    self.current_value = None
    self.running = True #setting the thread running to true
 
  def run(self):
    global gpsd
    while gpsp.running:
      gpsd.next() #this will continue to loop and grab EACH set of gpsd info to clear the buffer
 
if __name__ == '__main__':
  gpsp = GpsPoller() # create the thread
  try:
    gpsp.start() # start it up
    f = open('dinamis2.txt','a', os.O_NONBLOCK)
    t0=time.time()
    while True:
      x= int(input())
      if x == 1:
        print
        print ' GPS reading'
        print '----------------------------------------'
        print 'latitude    ' , gpsd.fix.latitude
        print 'longitude   ' , gpsd.fix.longitude
        print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
        print 'altitude (m)' , gpsd.fix.altitude
        print 'speed (m/s) ' , gpsd.fix.speed
        jarak=haversine(gpsd.fix.longitude,gpsd.fix.latitude,112.79023510326242,-7.276424504554041)
        print 'Jarak ' , jarak
        if(jarak<=5):
          t1=time.time()
          t2=t1-t0
          print'Delay',t2
          lats=str(gpsd.fix.latitude)
          lots=str(gpsd.fix.longitude)
          waktu=str(t2)
          vs=str(gpsd.fix.speed)
          f.write("%s,%s,%s,%s\n" %( vs, lats,lots,waktu))
          f.flush()
      
 
      time.sleep(1) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
