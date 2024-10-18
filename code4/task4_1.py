import numpy as np # math functionality
import matplotlib.pyplot as plt # plotting
import matplotlib.image as mpimg # loading images

fig = plt.figure(figsize=(8, 7))

# show the first chart
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title("Skalarfeld kontinuierlich\n" + r'$f(x,y) = 3x^2 - 4y^2$')

# build and show the function f(x,y) = 3x^2 - 4y^2
delta = 0.025
x = y = np.arange(-3.0, 3.0, delta)
X, Y = np.meshgrid(x, y)
Z = 3 * np.power(X, 2) - 4 * np.power(Y, 2)
img1 = ax1.imshow(Z, extent=[-3, 3, -3, 3], vmin=-30, vmax=30, cmap='coolwarm')

# visualize gradient with arrows
step = 0.5
x_pos = y_pos = np.arange(-3.0, 3.0, step)
X_pos, Y_pos = np.meshgrid(x_pos, y_pos)
x_dir = 6 * X_pos
y_dir = -8 * Y_pos
ax1.quiver(X_pos, Y_pos, x_dir, y_dir)

# extreme value - calculated manually on paper: set the first derivative to x and y of the function
# (which essentially is the gradient) equal to 0 and solve the equation system.
ax1.scatter(0, 0, color="Green")

# show the second chart
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title("Skalarfeld diskret")

# load the test image
circle_png = mpimg.imread('circle.png')
circle_bw = circle_png[:, :, 0]
img2 = ax2.imshow(circle_bw, cmap="gray", vmin="0", vmax="1")

# visualize gradient on discrete structure
x_bw = y_bw = np.arange(10, len(circle_bw), 10)
X_bw, Y_bw = np.meshgrid(x_bw, y_bw)

X_dir_bw = circle_bw[Y_bw, X_bw] - circle_bw[Y_bw, X_bw - 1]
Y_dir_bw = circle_bw[Y_bw - 1, X_bw] - circle_bw[Y_bw, X_bw]
ax2.quiver(X_bw, Y_bw, X_dir_bw, Y_dir_bw, scale=0.5)

# add colorbars
fig.colorbar(img1, ax=ax1, orientation='horizontal', pad=0.06)
fig.colorbar(img2, ax=ax2, orientation='horizontal', pad=0.06)

# Always run show, to make sure everything is displayed.
plt.show()
