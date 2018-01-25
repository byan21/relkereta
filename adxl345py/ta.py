from adxl345 import ADXL345
import os
from gps import *
from time import *
import time
import threading
  
adxl345 = ADXL345()

gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
 
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
    f = open('data.txt','a', os.O_NONBLOCK)

    while True:
      axes = adxl345.getAxes(True)
      print "ADXL345 on address 0x%x:" % (adxl345.address)
      print "   x = %.3fG" % ( axes['x'] )
      print "   y = %.3fG" % ( axes['y'] )
      print "   z = %.3fG" % ( axes['z'] )
      print
      print ' GPS reading'
      print 'latitude    ' , gpsd.fix.latitude
      print 'longitude   ' , gpsd.fix.longitude
      print 'time utc    ' , gpsd.utc,' + ', gpsd.fix.time
      print 'altitude (m)' , gpsd.fix.altitude
      print 'speed (m/s) ' , gpsd.fix.speed
      print 'speed (m/s) ' , gpsd.fix.speed
      lats=str(gpsd.fix.latitude)
      lots=str(gpsd.fix.longitude)
      vs=str(gpsd.fix.speed)
      xs=str(axes['x'])
      ys=str(axes['y'])
      f.write("%s,%s,%s,%s,%s\n" %( vs, lats,lots,xs,ys))
      f.flush()
      time.sleep(1) #set to whatever
 
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
    print "Done.\nExiting."