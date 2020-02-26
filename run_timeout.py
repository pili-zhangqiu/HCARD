import os
import sys
import time

os.system("minimu9-ahrs --mode raw > output_supinate.csv")
sys.stdout.write("Recording...")

time.sleep(1)  # In seconds

sys.stdout.write("Exiting")
sys.exit(0)
sys.stdout.write("Exited")


'''
def job():
  os.system("minimu9-ahrs --mode raw > output_supinate.csv")
  time.sleep(10)

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
'''
