import numpy as np

# QUIZ: Write a function that takes as input two lists Y, P,
# and returns the float corresponding to their cross-entropy.

def cross_entropy(Y, P):
    # input: Y - list, indicate the presence of the events as 1 or 0 in the list
    #        P - list, the probabilites of the events between 0 and 1 in the list
    # output: CE - float, the cross-entropy of the events

    sum = 0.0 
    CE = 0.0
    for i in range(len(Y)):
        sum += Y[i]*np.log(P[i]) + (1-Y[i])*np.log(1-P[i])
    CE = -1 * sum
    return CE