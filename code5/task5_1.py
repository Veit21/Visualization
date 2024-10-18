import numpy as np # math functionality
import matplotlib.pyplot as plt # plotting


# 2D base function exp{-(x^2 + y^2)}
def phi(point):
    return np.exp(-(point[0]**2 + point[1]**2))


# calculates the weights for interpolating a function
def calculate_weights(p, v):
    M = np.zeros((len(p), len(p)))
    for i, point_i in enumerate(p):
        for j, point_j in enumerate(p):
            M[i, j] = phi(abs(point_j - point_i))
    weights = np.linalg.solve(M, v)
    return weights


# interpolated continuous function
def continuous_function(parameters, weights, X, Y):
    result_matrix = np.zeros((len(X), len(Y)))
    for i in range(len(X)):
        for j in range(len(Y)):
            phi_vector = []
            for point in parameters:
                phi_vector.append(phi(abs(point - [X[i][j], Y[i][j]])))
            result_matrix[i, j] = np.dot(weights, phi_vector)
    return result_matrix


points = np.array([[-2, -2], [2, 0], [0, -1], [-1, 2]])
values = np.array([0.2, 0.6, 0.3, 0.5])

# plotting the points (x,y) and their values (z)
fig = plt.figure(figsize=(8, 7))
axs1 = fig.add_subplot(1, 1, 1, projection="3d")
axs1.scatter(points[:, 0], points[:, 1], values, color="Red")

x = y = np.arange(-4, 5, 0.025)
X, Y = np.meshgrid(x, y)
weights = calculate_weights(points, values)
Z = continuous_function(points, weights, X, Y)
axs1.plot_surface(X, Y, Z, cmap="viridis")


# Always run show, to make sure everything is displayed.
plt.show()
