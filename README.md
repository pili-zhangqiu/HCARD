# HCARD - Cerebral Palsy Assessment Device For Babies
This is a project from students at Imperial College London, under the module of H-CARD (Bioengineering Department).

Authors:
  - Xian Zhang
  - Pilar Zhang Qiu
  - Zoe Chu
  - Mun Han
  - Samradnyee Kolas
  - Ryan Satnarine

## Communication Protocol:
The RPi Zero is connected to the computer through SSH. Both devices are currently connected to the Samsung S9+ hoptspot:
  - Connection name: PiliZQ
  - Passcode: helloimpili
  
Current RPi IP in the connection above is: 192.168.43.250

## BOM:
  - The MCU used is the RPi Zero W, which embedded WiFi and BLE modules.
  - The IMU used is the Pololu Minimu-9 with 3-axis gyroscope, 3-axis accelerometer and 3-axis magnetometer.

## Libraries used:
Before starting the project, git clone the following libraries:
  - minimu-9ahrs I2C connection: https://github.com/DavidEGrayson/minimu9-ahrs.git
  - 
