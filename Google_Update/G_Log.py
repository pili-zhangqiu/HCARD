# Import libraries
from __future__ import print_function  
import datetime
import time

# Import the function to update Google Sheet
from G_UpdateSheet import update_sheet

# Import the function reading the acc, gyro values from IMU
from Get_IMU import readSensorData

print("hi")

def main():  
  
    #while True:
        
        # Read air quality values from the MQ135 sensors
        SensorData = readSensorData()

        Accel_X = SensorData[0]    # Air Quality Inside
        Accel_Y = SensorData[1]    # Air Quality Inside
        Accel_Z = SensorData[2]    # Air Quality Inside

        Gyro_X = SensorData[3]    # Air Quality Inside
        Gyro_Y = SensorData[4]    # Air Quality Inside
        Gyro_Z = SensorData[5]    # Air Quality Inside


        # Print values on the command prompt
        print('IMU Values')
        print('Accel_X={0:0.1f}  Accel_Y={1:0.1f}   Accel_Z={2:0.1f}%'.format(Accel_X, Accel_Y, Accel_Z))  
        print('Gyro_X={0:0.1f}  Gyro_Y={1:0.1f}   Gyro_Z={2:0.1f}%'.format(Gyro_X, Gyro_Y, Gyro_Z))  
        print(' ')
        print ('-' *30)

        update_sheet("Trial01", Accel_X, Accel_Y, Accel_Z, Gyro_X, Gyro_Y, Gyro_Z)
          
       # time.sleep(60)

if __name__ == '__main__':  
    main()