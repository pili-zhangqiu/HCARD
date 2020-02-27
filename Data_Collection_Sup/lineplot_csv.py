import numpy as np
from matplotlib import pyplot as plt
from matplotlib import style
from mpl_toolkits.mplot3d import Axes3D

filename = "180Sides_1.tsv"
data = np.loadtxt(filename)
#skip row: skiprows=1
#select columns: usecols =[0,1,2]
#tsv file: delimiter = "\\t"

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x = np.asarray(data[:,1])
y = np.asarray(data[:,2])
z = np.asarray(data[:,3])
print('length of x ',len(x))




ax.plot(x, y, z, c='r', marker='o') #3d line plot

ax.set_xlabel('X Label') #[-15 10]
ax.set_ylabel('Y Label') #[-200 200]
ax.set_zlabel('Z Label') #[-0.5 0.5]

plt.show()
