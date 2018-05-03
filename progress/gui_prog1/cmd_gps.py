import os
os.system("sudo systemctl stop serial-getty@ttyS0.service")
os.system("sudo systemctl disable serial-getty@ttyS0.service")
os.system("sudo gpsd /dev/ttyS0 -F /var/run/gpsd.sock")
