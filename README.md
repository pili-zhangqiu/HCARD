# HCARD
Cerebral Palsy Assessment Device - For Babies

This is the README for the "Peared with HINE" Baby Toy for Cerebral Palsy assessment, developed for the Human Centred Design of Assistive and Rehabilitation Devices module at Imperial College London. 

Authors:
- Pilar Zhang Qiu
- Xian Zhang
- Zoe Chu
- Mun Han
- Ryan Satnarine
- Samradnyee Kolas

The main folder contains:
- The primary script running the Raspberry Pi named.py: this script combines other scripts in the main folder allowing to read the data from the sensor, calculating the jerk score and storing it in a .csv file later read by the web server script.
- GetIMU.py contains the function readsensordata which reads the IMU values from the I2C bus address.
- jerk_analysis.py contains the code calculating the jerk score and the code for plotting the respective graphs.

The web server folder contains:
- The front-end code (index.html) that defines the style and appearance of the website.
- The back-end code for accessing the csv file live is found in the javascript folder, create-graph-xxxx.
