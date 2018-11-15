# This is the solution given by the course moderators.
# It may differs that my own solution. It's been added here just to be reference.

import numpy as np

def cross_entropy(Y, P):
    Y = np.float_(Y)
    P = np.float_(P)
    return -np.sum(Y * np.log(P) + (1 - Y) * np.log(1 - P))