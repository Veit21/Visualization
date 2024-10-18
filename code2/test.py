import numpy as np

x = np.arange(-3.0, 3.0, 0.025)
y = np.arange(-3.0, 3.0, 0.025)

x = y = np.arange(0 ,100, 10)

X, Y = np.meshgrid(x, y)
print(X)
print(Y)


