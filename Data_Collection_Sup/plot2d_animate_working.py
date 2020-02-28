import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_axis = []
y_axis = []

fig, ax = plt.subplots()
ax.set_xlim(0, 300)
ax.set_ylim(-180, 180)
line, = ax.plot(0, 0)

filename = "180Sides_1.tsv"
data = np.loadtxt(filename)
x = np.asarray(data[:,1]) #don't necessarily need np.asarray() function 
y = np.asarray(data[:,2])
z = np.asarray(data[:,3])
t = np.arange(0.0, len(x))
def animation_frame(i):
    x_axis.append(i) #i is determined by the range in frames
    y_axis.append(y[i])
    line.set_xdata(x_axis)
    line.set_ydata(y_axis)
    ax.set_title('plot from file: '+filename+ ', data#' + str(i))
    print(x_axis[i],y_axis[i])
    return line, 

animation = FuncAnimation(fig, func=animation_frame, frames=np.arange(0, len(x), 1),
                          interval=10, repeat=False)
ax.set_ylabel('y(pitch)')

plt.show()
