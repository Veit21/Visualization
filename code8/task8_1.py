import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# compute a 2D function f(x,y) = sin(x^2 + y^2)
x = y = np.linspace(-2, 2, 200)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# Note that the function can be expressed as sin(x^2 + y^2) - z = 0.
# This allows to derive the normal and the Hessian.


####################
# Task 1a          #
####################
# H = [[d2f/dxdx, d2f/dxdy, d2f/dxdz], [d2f/dydx, d2f/dydy, d2f/dydz], [d2f/dzdx, d2f/dzdy, d2f/dzdz]]
# H = [[2*cos(x^2 + y^2) - 4x^2*sin(x^2 + y^2), -4xy*sin(x^2 + y^2), 0],
#      [-4xy*sin(x^2 + y^2), 2*cos(x^2 + y^2) - 4y^2*sin(x^2 + y^2), 0],
#      [0, 0, 0]]
def hessian(x, y, z):
    H = np.array([[2 * np.cos(x**2 + y**2) - 4*x**2 * np.sin(x**2 + y**2), -4*x*y * np.sin(x**2 + y**2), 0],
                  [-4*x*y * np.sin(x**2 + y**2), 2*np.cos(x**2 + y**2) - 4*y**2 * np.sin(x**2 + y**2), 0],
                  [0, 0, 0]])
    return H


####################
# Task 1b          #
####################
# nabla_f = (df/dx, df/dy, df/dz)^T
# n = -(nabla_f)/magnitude(nabla_f)
def get_P(x, y, z):
    nabla_f = np.array([2*x*np.cos(x**2 + y**2), 2*y*np.cos(x**2 + y**2), -1])
    magnitude_nabla_f = np.linalg.norm(nabla_f)
    normal = -(nabla_f / magnitude_nabla_f)
    identity = np.identity(len(normal))
    return identity - np.outer(normal, normal)


####################
# Task 1c          #
####################
def get_abs_nabla(x, y, z):
    nabla_f = np.array([2*x*np.cos(x**2 + y**2), 2*y*np.cos(x**2 + y**2), -1])
    return np.linalg.norm(nabla_f)


def get_G(P, H, abs_nabla):
    return -(P @ H @ P)


####################
# Task 1d          #
####################
def get_T(G):
    return np.trace(G)


####################
# Task 1e          #
####################
def get_F(G):
    squared_sum = 0
    for i in range(len(G)):
        for j in range(len(G[i])):
            squared_sum += G[i][j]**2
    return np.sqrt(squared_sum)


####################
# Task 1f          #
####################
def get_kappa(T, F):
    kappa_1 = (T + np.sqrt(2*F**2 + T**2)) / 2
    kappa_2 = (T - np.sqrt(2*F**2 + T**2)) / 2
    return kappa_1, kappa_2


def mean_kappa(i, j):
    # get sample values
    x = X[i, j]
    y = Y[i, j]
    z = Z[i, j]

    # TODO: put everything together
    hess = hessian(x, y, z)
    P = get_P(x, y, z)
    magnitude_nabla_f = get_abs_nabla(x, y, z)
    G = get_G(P, hess, magnitude_nabla_f)
    T = get_T(G)
    F = get_F(G)
    kappa_1, kappa_2 = get_kappa(T, F)

    return 0.5*(kappa_1 + kappa_2)


####################
# Display Result   #
####################
fig = plt.figure(figsize=(9, 7))
ax = fig.add_subplot(projection='3d')

# matrix that will hold mean kappa values for each point
mean_kappa_matrix = np.zeros(np.shape(X))

# probe each sample point of the function
# calculate mean kappa value and save
for i in range(np.shape(X)[0]):
    for j in range(np.shape(X)[1]):
        mean_kappa_matrix[i, j] = mean_kappa(i, j)

# normalize mean kappa_matrix from [minval, maxval] to [0, 1]
minval = -1
maxval = 1
kappa_normalized = (mean_kappa_matrix - minval) / (maxval - minval)

# plot result
surface = ax.plot_surface(X, Y, Z,
    rcount=100,
    ccount=100,
    facecolors=mpl.cm.cool(kappa_normalized))

# add a colorbar
cmap = mpl.cm.cool
norm = mpl.colors.Normalize(vmin=minval, vmax=maxval)
fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
    ax=ax,
    orientation='horizontal',
    label=r'$(\kappa_1 + \kappa_2)/2$',
    extend='both')

plt.show()
