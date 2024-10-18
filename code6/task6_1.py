import numpy as np # math functionality
import matplotlib.pyplot as plt # plotting

fig = plt.figure(figsize=(8, 7))

ax = fig.add_subplot()
ax.set_title("Marching Squares")

# G holds some scalar values of a grid
G = np.array([[-1, -3, -3, -6, -9],
              [1, 1, -3, -6, -9],
              [2, 3, 3, -9, -9],
              [2, 3, 3, -9, -9],
              [9, 6, 6, -6, -9]])
G_rows = G.shape[0]
G_cols = G.shape[1]

# Build a grid 
x = np.linspace(0, G_cols-1, G_cols)
y = np.linspace(G_rows-1, 0, G_rows)
X, Y = np.meshgrid(x, y)
X /= G_cols-1
Y /= G_rows-1

####################
# Task 1           #
####################


# finds the point on the edge with an isovalue of 0
def find_zero(v1, v2):
    if v1 != v2:
        lam = v2/(v2 - v1)
        return lam
    else:
        return 0


# marching squares algorithm
def marching_squares():
    x_coordinates = []
    y_coordinates = []
    for i in range(G_rows):
        for j in range(G_cols):
            if (j + 1) <= (G_cols - 1):
                x = X[i][j]
                y = Y[i][j]
                x_next = X[i][j + 1]
                if G[i][j] != G[i][j + 1] and G[i][j] * G[i][j + 1] < 0:
                    lam = find_zero(G[i][j], G[i][j + 1])
                    if lam > 0:
                        point = [(x_next - x) * (1 - lam) + x, y]
                        x_coordinates.append(point[0])
                        y_coordinates.append(point[1])
            if (j + 1) <= (G_rows - 1):
                x = X[j][i]
                y = Y[j][i]
                y_next = Y[j + 1][i]
                if G[j][i] != G[j + 1][i] and G[j][i] * G[j + 1][i] < 0:
                    lam = find_zero(G[j][i], G[j + 1][i])
                    if lam > 0:
                        point = [x, (y_next - y) * (1 - lam) + y]
                        x_coordinates.append(point[0])
                        y_coordinates.append(point[1])
    ax.plot(x_coordinates, y_coordinates, 'ro', linestyle='-')


# run the algorithm
marching_squares()

####################
# Plot the grid    #
####################
# set XY-ticks to resemble grid lines
ax.set_xticks(np.linspace(0, 1, G_cols))
ax.set_yticks(np.linspace(0, 1, G_rows))
ax.grid(True)
ax.set_axisbelow(True)
ax.get_xaxis().set_ticklabels([])
ax.get_yaxis().set_ticklabels([])

# annotate each gridpoint with the scalar value in G
ax.scatter(X, Y, s=200)
for i in range(G_rows):
    for j in range(G_cols):
        ax.annotate(G[i][j], xy=(X[i][j], Y[i][j]), ha='center', va='center', c='white')

# Always run show, to make sure everything is displayed.
plt.show()
