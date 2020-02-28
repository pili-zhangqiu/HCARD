import numpy as np

import matplotlib
# IMPORTANT to export figures w/o x-server
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


filename_180S = "180Sides_1.tsv"
filename_360S = "360Sides_1.tsv"
filename_180T = "180Top_1.tsv"
filename_360T = "360Top_1.tsv"

filename = [filename_180S, filename_360S, filename_180T, filename_360T]

data_180S = np.loadtxt(filename_180S)
data_360S = np.loadtxt(filename_360S)
data_180T = np.loadtxt(filename_180T)
data_360T = np.loadtxt(filename_360T)

data = [data_180S, data_360S, data_180T, data_360T]

#skip row: skiprows=1
#select columns: usecols =[0,1,2]
#tsv file: delimiter = "\\t"

for i in range(4):
    x=[]    # empty arrays
    y=[]
    z=[]
    
    x = np.asarray(data[i][:,0])
    y = np.asarray(data[i][:,1])
    z = np.asarray(data[i][:,2])
    t = np.arange(0.0, len(x))

    ax1 = plt.subplot(311)
    ax2 = plt.subplot(312)
    ax3 = plt.subplot(313)

    ax1.plot(t,x)
    ax1.set_title('plot from file: '+filename[i]+ ', data#' + str(len(x)+1))
    #total #of data points
    ax1.set_ylabel('x (roll)')

    ax2.plot(t,y)
    #ax2.set_ylim((-180, 180))
    ax2.set_ylabel('y (pitch)')

    ax3.plot(t,z)
    ax3.set_ylabel('z (yaw)')

    #plt.setp(ax1.get_xticklabels(), visible=False) #invisible x ticks for plot 1

    plt.tight_layout()

    #plt.show()

    num = "%i.png" % i
    plt.savefig(num, format='png')
