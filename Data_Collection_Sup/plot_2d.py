import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from mpl_toolkits.mplot3d import Axes3D


filename = "180Sides_1.tsv"
#filename = "180Top_1.tsv"
#filename = "360Sides_1.tsv"
#ilename = "360Top_1.tsv"
data = np.loadtxt(filename)
#skip row: skiprows=1
#select columns: usecols =[0,1,2]
#tsv file: delimiter = "\\t"

x = np.asarray(data[:,1]) #don't necessarily need np.asarray() function 
y = np.asarray(data[:,2])
z = np.asarray(data[:,3])
t = np.arange(0.0, len(x))




ax1 = plt.subplot(311)
ax2 = plt.subplot(312)
ax3 = plt.subplot(313)

ax1.plot(t,x)
ax1.set_title('plot from file: '+filename+ ', data#' + str(len(x)+1))
#total #of data points
ax1.set_ylabel('x (roll)')

ax2.plot(t,y)
#ax2.set_ylim((-180, 180))
ax2.set_ylabel('y (pitch)')

ax3.plot(t,z)
ax3.set_ylabel('z (yaw)')

#plt.setp(ax1.get_xticklabels(), visible=False) #invisible x ticks for plot 1

plt.tight_layout()
plt.show()
