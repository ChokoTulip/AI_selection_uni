import numpy as np
from matplotlib import pyplot as plt
from diffevol import diffevol
from objfuncs import *


x, fx = diffevol(func=rastrigin,
                 dim=2, lim=[-5.12, 5.12],
                 NP=100, F=0.2, CR=0.7,
                 max_iter=1000,
                 max_iter_eps=10,
                 epsilon=1e-9)

print('found solution:')
print('    x:', x)
print(' fval:', fx)

