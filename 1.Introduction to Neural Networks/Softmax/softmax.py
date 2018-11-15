import numpy as np

# QUIZ: Write a function that takes as input a list of numbers, and returns
# the list of values given by the softmax function.


# calculate the sum of the exponential of each score
def sumOfExp(L):
    # input: L - list, the list of lineer function scores
    # output: sum - integer, the sum of the exponentials of each scores

    sum = 0
    for score in L:
        sum += np.exp(score)
    return sum

# calculates the probability of the score
def probability(score,L):
    # input: score - float, the lineer function score
    #        L - list, the list of lineer function scores
    # output: prob - the probability of the score
    
    prob = np.exp(score) / sumOfExp(L)
    return prob

# gives the probabilities of the scores as a list
def softmax(L):
    # input: L - list, the list of lineer function scores
    # output: probs - list, the list of probabilites of the scores in the list L
    
    probs = []
    sizeOfListOfScores = len(L)
    for score in L:
        probs.append(probability(score,L))

    return probs
