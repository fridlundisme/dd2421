import numpy as np
import random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import itertools

np.random.seed(100)

classA = np.concatenate(
    (np.random.randn(10,2) * 0.2 + [1.5,0.5], 
    np.random.randn(10,2) * 0.2 + [-1.5, 0.5]))
classB = np.random.randn(20, 2) * 0.2 + [0.0, -0.5]
inputs = np.concatenate((classA,classB))
t = np.concatenate((np.ones(classA.shape[0]), -np.ones(classB.shape[0])))
N = inputs.shape[0] # Number of rows (samples)

permute = list(range(N))
random.shuffle(permute)
inputs = inputs[permute,:]
t = t[permute]
P = np.empty([N,N])

def kernel(x1,x2):
    return np.dot(x1,x2)

def precompute():
    T = []
    for i in range(N):
        pTemp = []
        for j in range(N):
            pTemp.append(t[i]*t[j]*kernel(inputs[i],inputs[j]))
        T.append(np.array(pTemp))
    return np.array(T)

def objective(vector_a):
    alpha_sum = -np.sum(vector_a)
    sum = 0
    for i in range(N):
        for j in range(N):
            sum = 0.5* np.dot(np.dot(vector_a[i],vector_a[j]),P[i][j])
            alpha_sum += sum
    return alpha_sum


def zerofun(vector_a):
    return np.dot(vector_a,inputs)

def indicator(x, y, supportVectors):
    b = threshold(supportVectors)
    sum = 0
    for vector in supportVectors:
        sum += np.dot(np.dot(vector[0],vector[2]),kernel(np.array([x,y]),vector[1]))
    return sum - b

def threshold(sv):
    s0 = sv[0][1]
    sum = 0

    for vector in sv:
        sum += np.dot(np.dot(vector[0],vector[2]),kernel(s0,vector[1]))
    return sum - sv[0][2]

if __name__ == "__main__":

    P = precompute()
    XC={'type':'eq','fun':zerofun}
    C = 10
    B = [(0,C) for b in range(N)]
    start = np.zeros(N)
    cutoff = math.pow(10,-5)

    ret = minimize(objective,start,bounds=B,constraints=XC)
    alpha = ret['x']

    supportVectors = []
    for i,a in enumerate(alpha):
        if a >= cutoff:
            supportVectors.append([a,inputs[i],t[i]])

    b = threshold(supportVectors)
    

    xgrid = np.linspace(-5,5)
    ygrid = np.linspace(-4,4)
    
    grid = np.array([[indicator(x,y,supportVectors)
                    for x in xgrid]
                    for y in ygrid])

    plt.contour(xgrid, ygrid, grid,
                (-1.0, 0.0, 1.0),
                colors=('red', 'black', 'blue'),
                linewidths=(1, 3, 1))

    plt.plot([p[0] for p in classA],
        [p[1] for p in classA],
        'b.')

    plt.plot([p[0] for p in classB],
        [p[1] for p in classB],
        'r.')


    plt.axis('equal') # Force same scale on both axes
    plt.show()