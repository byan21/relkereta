import adxl345
import time

accelerometer = adxl345.ADXL345(i2c_port=1, address=0x53)
accelerometer.load_calib_value()
accelerometer.set_data_rate(data_rate=adxl345.DataRate.R_100)
accelerometer.set_range(g_range=adxl345.Range.G_8, full_res=True)
accelerometer.measure_start()

#accelerometer.calibrate()	# Calibrate only one time


while(True):
    x, y, z = accelerometer.get_3_axis_adjusted()
    print('x: ', x, 'y: ', y, 'z: ', z)
    #print('pitch: ', accelerometer.get_pitch())
    time.sleep(0.2)
