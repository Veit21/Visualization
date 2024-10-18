import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# we only need one subplot
fig, ax = plt.subplots(figsize=(13,8))

# fix axis limits to prevent jumpy animations
ax.set(xlim=(-3,3), ylim=(-1,1))

# positions for 2 points in time
#               point 1     point 2  
p0 = np.array([[-0.5, 0.8], [1.5, 0.5]])
p1 = np.array([[ 0.7, 0.9], [1.6, 0.4]])
p2 = np.array([[-2.0,-0.7], [2.5, 0.0]])
p = [p0, p1, p2, p0]

# sizes for 2 points in time
s0 = np.array([50.0, 30.0])
s1 = np.array([50.0, 200.0])
s2 = np.array([50.0, 500.0])
s = [s0, s1, s2, s0]

# scalar values for 3 points in time (for colormap)
c0 = np.array([0.0, 0.0])
c1 = np.array([0.5, 0.0])
c2 = np.array([1.0, 0.0])
c = [c0, c1, c2, c0]

# create an initial scatterplot of first time point
scatterplot = ax.scatter(p0[:,0], p0[:,1], s=s[0], c=c[0], vmin=0.0, vmax=1.0)

# animation parameters
time_res = 10 # interpolation steps between keyframes
time_speed = 1.0 # seconds between each keyframe 
time_steps = time_res*(len(p)-1) # number of global timesteps

def animate(i):
    # linear interpolation parameters
    t = i / time_res  # current point in time (e.g. 2.15)
    t_low = int(t)    # lower discrete time (e.g. 2)
    f = t - t_low     # interpolation factor (e.g. 0.15)

    # set the new positions
    p_interp = (1-f) * p[t_low] + f * p[t_low + 1]
    scatterplot.set_offsets(p_interp)

    # set the new sizes
    s_interp = (1-f) * s[t_low] + f * s[t_low + 1]
    scatterplot.set_sizes(s_interp)

    # set the new colors
    c_interp = (1-f) * c[t_low] + f * c[t_low + 1]
    scatterplot.set_array(c_interp)


# show the animation with a call to FuncAnimation
# this needs to be stored in a variable (here: 'anim') to prevent garbage collection
anim = FuncAnimation(fig, animate, interval=(1000*time_speed)/time_res, frames=time_steps)
plt.show()