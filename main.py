#####################################################

# Import libraries at the beginning as this will take a while (especially Google API)
from __future__ import print_function
from datetime import datetime
import time
import subprocess

print("Initializing ...")
# Import CSV Library
import csv

# Import pygame
import pygame
#from pygame import mixer

# Import the function reading the acc, gyro values from IMU
from Get_IMU import readSensorData
from jerk_analysis import jscore, calcJerk

#####################################################

print("Libraries imported correctly.")
print(' ')
time.sleep(1)

# Initialize pygame mixer
#mixer.init()
pygame.mixer.pre_init(44100, 16, 2, 4096) #frequency, size, channels, buffersize
pygame.init() #turn all of pygame on.
# Load the sounds
# sound = pygame.mixer.Sound('xylop-c4.wav')

# Grand Piano Acoustic
sound = pygame.mixer.Sound('Piano_1.wav')
sound = pygame.mixer.Sound('Piano_2.wav')
sound = pygame.mixer.Sound('Piano_3.wav')
sound = pygame.mixer.Sound('Piano_4.wav')
sound = pygame.mixer.Sound('Piano_5.wav')
sound = pygame.mixer.Sound('Piano_6.wav')
sound = pygame.mixer.Sound('Piano_7.wav')



# Spanish Guitar
sound = pygame.mixer.Sound('A1QQ.wav')
sound = pygame.mixer.Sound('A2QQ.wav')
sound = pygame.mixer.Sound('A3QQ.wav')
sound = pygame.mixer.Sound('A4QQ.wav')
sound = pygame.mixer.Sound('A5QQ.wav')

# Kalimba
sound = pygame.mixer.Sound('3_01QQ.wav')
sound = pygame.mixer.Sound('3_02QQ.wav')
sound = pygame.mixer.Sound('3_03QQ.wav')

sound = pygame.mixer.Sound('1_05QQ.wav')
sound = pygame.mixer.Sound('2_04QQ.wav')
sound = pygame.mixer.Sound('6_02QQ.wav')
sound = pygame.mixer.Sound('7_01QQ.wav')


#sound.play()
subprocess.Popen('aplay piano-c5.wav',shell=True)

# Create a csv with timestamp as filename
# name = datetime.now().strftime('IMU-%Y-%m-%d--%H:%M.csv')
savename ='/var/www/html/data/live.csv'

with open(savename, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['Timestamp', 'Raw Accel X', 'Raw Accel Y', 'Raw Accel Z', 'Raw Gyro X', 'Raw Gyro Y', 'Raw Gyro Z', 'JScore X','JScore Y','JScore Z','JScore Total','Jerk X','Jerk Y','Jerk Z'])
    filewriter.writerow([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0])

#######################################################

def main():
    
    dt = 0.002
    counter = 5
    acc_thres = 2000
    
    # Initialise history array for raw jerk
    zero = 0
        
    jerkx_past = []
    jerky_past = []
    jerkz_past = []

    for x in range (0,6):
        jerkx_past.append(zero)
        jerky_past.append(zero)
        jerkz_past.append(zero)

    # Initialise history array for difference in jerk between current and previous
    jscorexp_past = []
    jscoreyp_past = []
    jscorezp_past = []

    '''
    jscorexp_past.append(zero)
    jscoreyp_past.append(zero)
    jscorezp_past.append(zero)
    
    '''

    while True:
    #while (counter < 20):
        CurrentTime = datetime.now().strftime('%Y-%m-%d,%H:%M')

        # Read acceleration and gyroscope raw data
        SensorData = readSensorData()

        Accel_X = SensorData[0]    # Acceleration raw x
        Accel_Y = SensorData[1]    # Acceleration raw y
        Accel_Z = SensorData[2]    # Acceleration raw z

        Gyro_X = SensorData[3]    # Gyro raw x
        Gyro_Y = SensorData[4]    # Gyro raw y
        Gyro_Z = SensorData[5]    # Gyro raw z

        '''
        # Read previous values
        with open('/var/www/html/data/live.csv', newline='') as csvfile:
            data = list(csv.reader(csvfile))
        '''

        # Compute Jerk Score
        prev_jerkx = jerkx_past[counter]
        prev_jerky = jerky_past[counter]
        prev_jerkz = jerkz_past[counter]

        # Only take into account last 10 datapoints
        '''
        prev_jscorexp = jscorexp_past[counter]
        prev_jscoreyp = jscoreyp_past[counter]
        prev_jscorezp = jscorezp_past[counter]
        '''
    
        prev_jscorexp = (jerkx_past[counter] - jerkx_past[counter-1]) + (jerkx_past[counter-1] - jerkx_past[counter-2]) + (jerkx_past[counter-2] + jerkx_past[counter-3]) + (jerkx_past[counter-3] + jerkx_past[counter-4]) + (jerkx_past[counter-4] + jerkx_past[counter-5])
        prev_jscoreyp = (jerky_past[counter] - jerky_past[counter-1]) + (jerky_past[counter-1] - jerky_past[counter-2]) + (jerky_past[counter-2] + jerky_past[counter-3]) + (jerky_past[counter-3] + jerky_past[counter-4]) + (jerky_past[counter-4] + jerky_past[counter-5])
        prev_jscorezp = (jerkz_past[counter] - jerkz_past[counter-1]) + (jerkz_past[counter-1] - jerkz_past[counter-2]) + (jerkz_past[counter-2] + jerkz_past[counter-3]) + (jerkz_past[counter-3] + jerkz_past[counter-4]) + (jerkz_past[counter-4] + jerkz_past[counter-5])

        jerkx, jerky, jerkz, jscorexp, jscoreyp, jscorezp, jscorex, jscorey, jscorez, jscoretot = jscore(SensorData, prev_jerkx, prev_jerky, prev_jerkz, prev_jscorexp, prev_jscoreyp, prev_jscorezp, counter)

        jerkx_past.append(jerkx)
        jerky_past.append(jerky)
        jerkz_past.append(jerkz)
        
        '''
        jscorexp_past.append(jscorexp)
        jscoreyp_past.append(jscoreyp)
        jscorezp_past.append(jscorezp)
'''
        # Print values on the command prompt
        print(CurrentTime)
        print('IMU Values')
        print('Accel_X={0:0.1f}  Accel_Y={1:0.1f}   Accel_Z={2:0.1f}'.format(Accel_X, Accel_Y, Accel_Z))
        print('Gyro_X={0:0.1f}  Gyro_Y={1:0.1f}   Gyro_Z={2:0.1f}'.format(Gyro_X, Gyro_Y, Gyro_Z))
        print('Jerk_X={0:0.1f}  Jerk_Y={1:0.1f}   Jerk_Z={2:0.1f}'.format(jerkx, jerky, jerkz))
        print('JerkScore_X={0:0.1f}  JerkScore_Y={1:0.1f}   JerkScore_Z={2:0.1f}   Total_JerkScore={3:0.1f}'.format(jscorex, jscorey, jscorez, jscoretot))
        
        print(' ')
        print ('-' *30)

        #sound.play()
        # Play C5 at small accelerations within acceleration threshold
        if (jscoretot <= 1 ):
            subprocess.Popen('aplay 1_05QQ.wav',shell=True)
        # band one acceleration within 1000
        elif (jscoretot <= 2) and (jscoretot >1): # acceleration more than 2000:
            subprocess.Popen('aplay 2_04QQ.wav',shell=True)
        elif (jscoretot <= 3) and (jscoretot >2): # acceleration more than 2000
            subprocess.Popen('aplay 3_03QQ.wav',shell=True)
        elif (jscoretot <= 4.5) and (jscoretot >3): # acceleration more than 2000
            subprocess.Popen('aplay 6_02QQ.wav',shell=True)
        elif (jscoretot <= 7) and (jscoretot >4.5): # acceleration more than 2000
            subprocess.Popen('aplay 7_01QQ.wav',shell=True)
        elif (jscoretot > 7): # acceleration more than 2000
            subprocess.Popen('aplay 3_03QQ.wav',shell=True)

        # save to csv ------------------------------------------------------------------------------------
        save2CSV(savename, CurrentTime, Accel_X, Accel_Y, Accel_Z, Gyro_X, Gyro_Y, Gyro_Z, jerkx, jerky, jerkz, jscorexp, jscoreyp, jscorezp, jscorex, jscorey, jscorez, jscoretot)
        counter = counter+1

    #update_sheet("Trial01", Accel_X, Accel_Y, Accel_Z, Gyro_X, Gyro_Y, Gyro_Z)
        time.sleep(0.1)



# Var 7,8,9 jerk
# Var 10,11,12 jerkscore
# Var 13,14,151,16 jerkscorexp
def save2CSV(savename, datetime, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16):
    # List of strings
    row_contents = [datetime, var1, var2, var3, var4, var5, var6, var7, var8, var9, var10, var11, var12, var13, var14, var15, var16]

    # Append a list as new line to an old csv file
    append_list_as_row(savename, row_contents)

def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = csv.writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)

#######################################################

if __name__ == '__main__':
    main()
