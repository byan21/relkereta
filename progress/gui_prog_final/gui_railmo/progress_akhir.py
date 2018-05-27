import adxl345
import time
import os
from gps import *
import threading

accelerometer = adxl345.ADXL345(i2c_port=1, address=0x53)
accelerometer.load_calib_value()
accelerometer.set_data_rate(data_rate=adxl345.DataRate.R_100)
accelerometer.set_range(g_range=adxl345.Range.G_2, full_res=True)
accelerometer.measure_start()

#accelerometer.calibrate()	# Calibrate only one time


gpsd = None #seting the global variable
 
os.system('clear') #clear the terminal (optional)
i=0
a=5
 
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

while(True):
  gpsp = GpsPoller()
  f = open('log.txt','a', os.O_NONBLOCK)
  try:
    gpsp.start() # start it up
    while(a!=0):
      sys.stdout.write("Program akan berjalan dalam: %d   \r" % (a))
      sys.stdout.flush()
      a-=1
      time.sleep(1)
    while True:
      i+=1
      latitude = gpsd.fix.latitude
      longitude = gpsd.fix.longitude
      jam = int(gpsd.utc[11:13])+7
      jams=str(jam)
      waktu = gpsd.utc[0:10]+' '+jams+gpsd.utc[13:19]
      kec= gpsd.fix.speed
      va = kec * 3.6
      sats = gpsd.satellites
      epx=gpsd.fix.epx
                
      os.system('clear')
      print 'latitude    ' , latitude
      print 'longitude   ' , longitude
      print 'time utc +7   ' , waktu
      print 'speed (Km/jam) ' , va
      print 'epx         ' , gpsd.fix.epx
            
      x, y, z = accelerometer.get_3_axis_adjusted()
      ('x: ', x, 'y: ', y, 'z: ', z)
          
      print 'X ' , x
      print 'y ' , y
      print 'z ' , z
      f.write("%s,%s,%s,%s,%s,%s,%s,%s,%s\n" %(i,x,y,z,va,latitude,longitude,epx,waktu))
      f.flush()
      time.sleep(0.5)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
    print "\nKilling Thread..."
    gpsp.running = False
    gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."
