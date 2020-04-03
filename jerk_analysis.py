# -*- coding: utf-8 -*-
import math
import statistics
import numpy as np
import pdb
#repl.it debugger, use pdb.set_trace() to add breakpoint. # c : continue,
# n : step to the next line within the same function
# s : step to the next line in this function or a called function
# q : quit the debugger/execution
"""
Created on Mon Mar  9 17:44:51 2020

@author: rsatn
"""
# data = np.genfromtxt("/var/www/html/data/live.csv", delimiter=",", skip_header=1)
# data = np.genfromtxt("live.csv", delimiter=",", skip_header=1)

#rows, cols = (3, 0)
#acc = [[0]*cols]*rows
dt = 0.0015

def calcJerk(acc, dt):
    n = 0
    if acc < 0:
	    n = abs(acc)
    else:
	    n = acc

    #lleft = dt**3
    #right = n*dt
    lleft = dt**3
    right = n*dt
    jerkpre = lleft*right*10

    # Math domain error ---------------------------------
    # jerk = abs((math.log(jerkpre)))
    jerk = abs((math.log(jerkpre)))
    return jerk


def jscore(input_data, prev_jerkx, prev_jerky, prev_jerkz, prev_jscorexp, prev_jscoreyp, prev_jscorezp, i):

    '''
    jerkx = []
    jerky = []
    jerkz = []

    jscorexp = 0
    jscoreyp = 0
    jscorezp = 0
    '''
    # Var 7,8,9 jerk
    # Var 10,11,12 jerkscore
    # Var 13,14,151,16 jerkscorexp
    
    #data = np.genfromtxt("/var/www/html/data/live.csv", delimiter=",", skip_header=1)

    #for i in range(0,len(data)):
    if i == 0:
        jerkx = calcJerk(input_data[0],dt)
        jerky = calcJerk(input_data[1],dt)
        jerkz = calcJerk(input_data[2],dt)

        jscorexp = abs(jerkx - jerkx)   # So that it is 0
        jscoreyp = abs(jerky - jerky)
        jscorezp = abs(jerkz - jerkz)

        jscorex = (jscorexp)*10 #Factor of 10 is added to make numbers more intuitive, instead of sub 1 numbers
        jscorey = (jscoreyp)*10
        jscorez = (jscorezp)*10

        jarr = [jscorex, jscorey, jscorez]
        jscoretot = statistics.mean(jarr)

    else:
        jerkx = calcJerk(input_data[0],dt)
        jerky = calcJerk(input_data[1],dt)
        jerkz = calcJerk(input_data[2],dt)

        jscorexp = prev_jscorexp + abs(jerkx - prev_jerkx)
        jscoreyp = prev_jscoreyp + abs(jerky - prev_jerky)
        jscorezp = prev_jscorezp + abs(jerkz - prev_jerkz)
        
        jscorex = ((20-(jscorexp/6))**2)  # Squared to make difference more noticeable
        jscorey = ((20-(jscoreyp/6))**2) 
        jscorez = ((20-(jscorezp/6))**2) 

        jarr = [jscorex, jscorey, jscorez]
        jscoretot = statistics.mean(jarr) - 7 # the mean total value when stationary is 7

    return jerkx, jerky, jerkz, jscorexp, jscoreyp, jscorezp, jscorex, jscorey, jscorez, jscoretot


#jscore(data,i)


#print("jerk x ",jerkx)
# print("score x", jscorex)

#print("jerk y ", jerky)
# print("score y", jscorey)

#print("jerk z", jerkz)
# print("score z", jscorez)
