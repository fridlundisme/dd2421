import numpy as np
import random, math
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import itertools
import datapoints as dt


# Chosing dataset
# dt.basic_data()
# dt.linear_data()
# dt.spread_data()
classA, classB = dt.linear_data()

inputs = np.concatenate((classA,classB))
t = np.concatenate((np.ones(classA.shape[0]), -np.ones(classB.shape[0])))
N = inputs.shape[0] # Number of rows (samples)

permute = list(range(N))
random.shuffle(permute)
inputs = inputs[permute,:]
t = t[permute]
P = np.empty([N,N])

def lin_kernel(x1,x2):
    return np.dot(x1,x2)

def poly_kernel(x1,x2, p=2):
    return np.power((np.dot(x1,x2) + 1), p)

def radi_kernel(x1,x2, sigma=1):
    diff = np.subtract(x1, x2)
    return math.exp((-np.dot(diff, diff)) / (2*math.pow(sigma, 2)))

def precompute(kernel):
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

def indicator(x, y, supportVectors, kernel):
    b = threshold(supportVectors, kernel)
    sum = 0
    for vector in supportVectors:
        sum += np.dot(np.dot(vector[0],vector[2]),kernel(np.array([x,y]),vector[1]))
    return sum - b

def threshold(sv, kernel):
    if len(sv) == 0:
        return 0
    s0 = sv[0][1]
    sum = 0


    for vector in sv:
        sum += np.dot(np.dot(vector[0],vector[2]),kernel(s0,vector[1]))
    return sum - sv[0][2]

if __name__ == "__main__":
    # Chosing kernel
    # kernel = lin_kernel
    # kernel = poly_kernel
    # kernel = radi_kernel
    kernel = radi_kernel
    
    P = precompute(kernel)

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

    xgrid = np.linspace(-5,5)
    ygrid = np.linspace(-4,4)
    
    grid = np.array([[indicator(x,y,supportVectors, kernel)
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

    plotname = "C: %0.2f, kernel: %s" % (C,kernel.__name__)
    plt.title(plotname)
    plt.axis('equal') # Force same scale on both axes

    plt.savefig('plots/linear_data/%s.png' % (plotname))
    plt.show()