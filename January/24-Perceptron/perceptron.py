# reference code: https://blog.dbrgn.ch/2013/3/26/perceptrons-in-python/
from random import choice
from numpy import array, dot, random
import pylab as pl
unit_step = lambda x: 0 if x < 0 else 1 # step function

training_data = [  # maps to OR
    (array([0, 0, 1]), 0),
    (array([0, 1, 1]), 1),
    (array([1, 0, 1]), 1),
    (array([1, 1 ,1]), 1),
]

w = random.rand(3)  # random values for initial weights
errors = []
eta = 0.2           # learning rate
n = 100             # number of iterations

for i in range(n):
    x, expected = choice(training_data)
    result = dot(w, x)      # dot product of input and weight
    error = expected - unit_step(result)
    errors.append(error)
    w += eta * error * x    # new weight = learning rate * error * input vector

    for x, _ in training_data:
        result = dot(x, w)
        print("{}: {} -> {}".format(x[:2], result, unit_step(result)))

pl.ylim([-1, 1])
pl.plot(errors)
pl.show()

