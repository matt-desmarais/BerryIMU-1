
import time
import datetime
import smbus
import RPi.GPIO as GPIO
from BerryImu import BerryImu

bus = smbus.SMBus(1)
imu = BerryImu(bus)
imu.initialise()

# Pin Setup:
GPIO.setmode(GPIO.BCM)   # Broadcom pin-numbering scheme. This uses the pin num$
GPIO.setup(16, GPIO.OUT)   # Green LED pin set as output
GPIO.setup(20, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


print("delta_t [s], ACC_X [mg], ACC_Y [mg], ACC_Z [mg], GYR_X [deg/s],  GYR_Y [deg/s],  GYR_Z [deg/s], MAG_X [mgauss],  MAG_Y [mgauss],  MAG_Z [mgauss]")

while True:
        time_at_loop_start = datetime.datetime.now()
#        time.sleep(0.03)

        #Read  accelerometer,gyroscope and magnetometer  values
        acc_meas = imu.read_acc_data()
        gyr_meas = imu.read_gyr_data()
        mag_meas = imu.read_mag_data()
	
	time.sleep(0.25)
	
	GPIO.output(16, False)  # Turns off the Green LED
	GPIO.output(21, False)  # Turns off the Green LED
	GPIO.output(20, False)  # Turns off the Green LED
	gyr_meas2 = imu.read_gyr_data()

        # Flip acceleration to match Raspberry Pi frame (rotate around Y_ACC)
        acc_meas[2] = -acc_meas[2]
        acc_meas[0] = -acc_meas[0]

        time_at_loop_end = datetime.datetime.now()
        loop_time = time_at_loop_end - time_at_loop_start
        loop_time = loop_time.microseconds/1e6 # convert to seconds

	value = abs(gyr_meas[1] - gyr_meas2[1])

	if  (value <= 2):
	     GPIO.output(16, True)  # Turns on the Green LED
	elif(value <= 12):
	     GPIO.output(21, True)  # Turns on the Yellow LED
	elif(value > 12):
	     GPIO.output(20, True)  # Turns on the Red LED

#	print(value)

#        print("%5.3f, %5.2f, %5.2f, %5.2f, %5.2f, %5.2f, %5.2f , %5.2f, %5.2f, %5.2f" % (loop_time,
#            acc_meas[0], acc_meas[1], acc_meas[2],
#            gyr_meas[0], gyr_meas[1],gyr_meas[2], mag_meas[0],
#            mag_meas[1],mag_meas[2])



