import numpy as np


# calculates the euclidean distance between two n-dimensional vectors
def dist(x, y):
    sumSR = 0.0
    for i in range(len(x)):
        sumSR += (x[i]-y[i])*(x[i]-y[i])

    return np.sqrt(sumSR)

A = np.array([1, 2, 3])
B = np.zeros(3)
print(dist(A, B))

