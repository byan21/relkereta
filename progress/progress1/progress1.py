import adxl345
import time
import os
from gps import *
import threading

accelerometer = adxl345.ADXL345(i2c_port=1, address=0x53)
accelerometer.load_calib_value()
accelerometer.set_data_rate(data_rate=adxl345.DataRate.R_100)
accelerometer.set_range(g_range=adxl345.Range.G_16, full_res=True)
accelerometer.measure_start()

#accelerometer.calibrate()	# Calibrate only one time


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

def index(SPEED, AX):
    nh=0

    if (SPEED >= 80):
        nh=15//AX
    elif (SPEED >= 40 and 80 > SPEED):
        nh=(3 * SPEED) // (16 * AX)
    elif (40 > SPEED):
        nh=1
    return nh

def indey(kecepatan, ay):
    ny=0
    if (kecepatan >=80):
        ny=20//ay
    elif (kecepatan >=40 and 80 > kecepatan):
        ny=(4 * kecepatan)//(16* ay)
    elif (40 > kecepatan):
        ny=1
    return ny

def indek (nx, ny):
    if(nx>ny):
        n=ny
    elif(nx<ny):
        n=nx
    elif(nx==ny):
        n=nx
    return n

def max_kec(N,Vact):
    VRmax=(Vact/100)*N
    return VRmax

while(True):
  gpsp = GpsPoller()
  f = open('data1.txt','a', os.O_NONBLOCK)
  try:
      gpsp.start() # start it up
      while True:
          latitude = gpsd.fix.latitude
          longitude = gpsd.fix.longitude
          waktu = gpsd.utc,' + ', gpsd.fix.time
          va = gpsd.fix.speed * 3.6
          sats = gpsd.satellites
            
            #os.system('clear')
          print 'latitude    ' , latitude
          print 'longitude   ' , longitude
          print 'time utc    ' , waktu
          print 'speed (m/s) ' , va
            #print 'sats        ' , sats
            
          x, y, z = accelerometer.get_3_axis_adjusted()
          ('x: ', x, 'y: ', y, 'z: ', z)
            #print('pitch: ', accelerometer.get_pitch())
          xa=abs(x)
          ya=abs(y)
          za=abs(z)
          
          print 'X ' , xa
          print 'y ' , ya
          print 'z ' , za
          IX=index(va, xa)
          IY=index(va, ya)
          IZ=indey(va, za)
          print 'nx = ' , IX
          print 'ny = ' , IY
          print 'nz = ' , IZ
          #INDEK=indek(IX,IY)
          #Vmax=max_kec(INDEK, va)
          #indeks=str(INDEK)
          #vmaxs=str(Vmax)
          if (vmaxs == 'nan'):
              vmaxs = '0.0'
          f.write("%s,%s,%s,%s,%s,%s,%s,%s\n" %( x,y,va,indeks, vmaxs, latitude,longitude,waktu))
          f.flush()
          time.sleep(1)
  except (KeyboardInterrupt, SystemExit): #when you press ctrl+c
      print "\nKilling Thread..."
      gpsp.running = False
      gpsp.join() # wait for the thread to finish what it's doing
  print "Done.\nExiting."