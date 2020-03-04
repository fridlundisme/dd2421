import numpy as np
import random

np.random.seed(100)

def basic_data():
    classA = np.concatenate(
        (np.random.randn(10,2) * 0.2 + [1.5,0.5], 
        np.random.randn(10,2) * 0.2 + [-1.5, 0.5]))
    classB = np.random.randn(20, 2) * 0.2 + [0.0, -0.5]
    return classA, classB

def linear_data():
    # Linearly separable points
    classA = np.concatenate(
        (np.random.randn(10,2) * 0.2 + [1.5,-0.5],
        np.random.randn(10,2) * 0.2 + [-1.5, 0]))
    classB = np.random.randn(20, 2) * 0.2 + [0.0, -0.5]

    return classA, classB

def spread_data():
    classA = np.concatenate(
        (np.random.randn(10,2) * 0.6 + [1.5,0.5], 
        np.random.randn(10,2) * 0.6 + [-1.5, 0.5]))
    classB = np.random.randn(20, 2) * 0.2 + [0.0, -0.5]
    return classA, classB