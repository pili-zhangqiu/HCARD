import os
import subprocess
import time
import timeit
import threading as thread

raw_cmd = "minimu9-ahrs --mode raw > start_test.tsv"

def hello():
  print(time.ctime()) #current time
  thread.Timer(10.0, hello).start() # called every 10s
  print("Hello, World!")
  print("Recording... ", raw_cmd)
  action = subprocess.Popen(raw_cmd, shell=True)
  time.sleep(2)


hello()
       

#tic = time.perf_counter() #time counter
# print(tic)
#print("Recording... ", raw_cmd)
#action = subprocess.Popen(raw_cmd, shell=True)
#action.wait(10)
#action.terminate()
#toc = time.perf_counter()
#print(toc-tic)
