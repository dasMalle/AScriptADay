import numpy as np

cvalues = [25.3, 24.8, 26.9, 23.9]
C = np.array(cvalues)
print(C)

# np array can be seen as vectors
print(C * 9/5 +32) # to fahrenheit

x = np.array([ [67, 63, 87],
               [77, 69, 59],
               [85, 87, 99],
               [79, 72, 71],
               [63, 89, 93],
               [68, 92, 78] ])
print(np.shape(x))

B = np.array([ [[111, 112], [121, 122]],
               [[211, 212], [221, 222]],
               [[311, 312], [321, 322]] ])
print(np.shape(B))

id = np.identity(4, dtype=int)
print(id)

