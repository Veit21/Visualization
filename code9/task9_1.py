import numpy as np
import matplotlib.pyplot as plt

# Given is a vector field v(x,y) = (-y, x)^T.
# Utility to sample a given position [x,y]:
def v(pos):
    return np.array([-pos[1], pos[0]])

# Show the vector field using a quiver plot
X, Y = np.meshgrid(np.arange(-8, 8), np.arange(-8, 8))
U = -Y
V = X

fig = plt.figure(figsize=(6,6))
ax = fig.add_subplot()
ax.set_title(r'$v(x,y) =  (-y \quad x)^T$')
ax.quiver(X, Y, U, V)


####################
# Task 1           #
####################














plt.show()