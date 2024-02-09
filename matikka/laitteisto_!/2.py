import numpy as np
import numpy.linalg as la
import matplotlib.pyplot as plt


A = np.array([[5, 3], [2, 1]])
B = np.array([[9], [4]])

X = la.inv(A).dot(B)

print(X)

A = np.array([[2, 1, 1], [1, 3, 1], [2, 1, 2]])
B = np.array([[6], [2], [9]])

X = la.inv(A).dot(B)

print(X)

A = np.array([[1, 1, 3], [3, 1, 1], [2, 1, 2]])
B = np.array([[-1], [5], [2]])

X = la.inv(A).dot(B)

print(X)
