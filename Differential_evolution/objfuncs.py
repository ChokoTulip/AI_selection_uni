import numpy as np


def rastrigin(x, A=10):
    # x - columns are parameters, rows are whole vectors of parameters
    if len(x.shape) == 2:  # 2D matrix
        axis = 1
    elif len(x.shape) == 1:  # one vector
        axis = 0
    else:
        raise ValueError('2D matrix or vector supported only')

    n = np.size(x, axis)
    y = A * n + np.sum(x ** 2 - A * np.cos(2 * np.pi * x), axis)

    return y

