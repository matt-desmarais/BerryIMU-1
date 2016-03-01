import time
import datetime
import smbus
from BerryImu import BerryImu

bus = smbus.SMBus(1)
imu = BerryImu(bus)
imu.initialise()


print("delta_t [s], ACC_X [mg], ACC_Y [mg], ACC_Z [mg], GYR_X [deg/s],  GYR_Y [deg/s],  GYR_Z [deg/s], MAG_X [mgauss],  MAG_Y [mgauss],  MAG_Z [mgauss]")

while True:
        time_at_loop_start = datetime.datetime.now()
        time.sleep(0.03)

        #Read  accelerometer,gyroscope and magnetometer  values
        acc_meas = imu.read_acc_data()
        gyr_meas = imu.read_gyr_data()
        mag_meas = imu.read_mag_data()

        # Flip acceleration to match Raspberry Pi frame (rotate around Y_ACC)
        acc_meas[2] = -acc_meas[2]
        acc_meas[0] = -acc_meas[0]

        time_at_loop_end = datetime.datetime.now()
        loop_time = time_at_loop_end - time_at_loop_start
        loop_time = loop_time.microseconds/1e6 # convert to seconds

        print("%5.3f, %5.2f, %5.2f, %5.2f, %5.2f, %5.2f, %5.2f , %5.2f, %5.2f, %5.2f" % (loop_time,
            acc_meas[0], acc_meas[1], acc_meas[2],
            gyr_meas[0], gyr_meas[1],gyr_meas[2], mag_meas[0],
            mag_meas[1],mag_meas[2]))





