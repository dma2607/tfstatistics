#!/usr/bin/python
import pandas as pd
import numpy as np
import statsmodels.api as sm
# import scipy as sp
# implementation of newthon's method to solve the MLE
# of y~Binominal(logit(x))
# . sigmoid link

def log_likelihood(x, y, theta):
    sigmoid_probs = getAlpha(x, theta)
    return np.sum(y * np.log(sigmoid_probs) + (1 - y) * np.log(1 - sigmoid_probs))

def sigmoid(x):
    return (1.0/(1.0 + np.exp(-x)))

# . diagonal
def getAlpha(x, theta):
    arr = []
    for e in x:
        arr.append(sigmoid(theta.T.dot(e)))
    return(np.array(arr))
    #return sigmoid(np.dot(theta.T, x.T)).reshape(-1)

# . Gradient function of the MLE
def gradient(A, alpha, y):
    # print('compute gradient')
    return A.T.dot(y - alpha)

# . Hessian function of the MLE
def hessian(A, B):
    # print('compute hessian')
    return (A.T.dot(B)).dot(A)

# .
if __name__ == '__main__':
    print('sketch of logistic regression')
    '''
        The test will be with a subset of the iris dataset
        the formula will be:
    '''
    # .
    test_df = pd.read_csv('~/projects/tfstatistics/data_iris.csv')
    test_df.Species = pd.factorize(test_df.Species)[0]
    y = test_df.Species.values
    x = test_df['Sepal.Length'].values
    x = np.column_stack((np.ones(shape=(x.shape[0])), x))

    glm = sm.GLM(y, x, family=sm.families.Binomial())
    result = glm.fit(maxiter=10)
    print('Stats model:')
    print(result.params)

    # my newthon's method
    Y = np.copy(y)
    X = np.copy(x)
    max_iter = 15
    np.random.seed(2019)
    # theta = np.random.rand(X.shape[1])
    theta = np.zeros(X.shape[1])

    for i in range(max_iter):
        # print('iteration: {}'.format(i))
        alpha = getAlpha(x, theta)
        G = X.T.dot(alpha.T) # gradient .
        S = np.diag(alpha * (1.0 - alpha)) # diganoal matrix
        H = X.T.dot(S).dot(X)
        # first way
        # d = np.linalg.solve(H, -G)
        theta -= np.linalg.inv(H).dot(G)
        # theta += 0.1 * d
        #import pdb; pdb.set_trace()
    print('Mine:')
    print(theta.reshape(-1))
