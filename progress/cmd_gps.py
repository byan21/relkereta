import os
os.system("sudo systemctl stop gpsd.socket")
os.system("sudo systemctl disable gpsd.socket")
os.system("sudo gpsd /dev/ttyUSB0 -F /var/run/gpsd.sock")
os.system("cgps -s")