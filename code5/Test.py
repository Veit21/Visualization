import numpy as np

C = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])
D = np.array([[1, 2, 3],
              [1, 2, 3],
              [1, 2, 3]])
E = C @ C
print(C @ C @ C)
print(E @ C)


