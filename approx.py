import numpy as np
from random import random


def sumWith(fun, vector):
    s = 0
    for e in vector:
        s += fun(e)
    return s

functions = [lambda x: x**3, lambda x: x, lambda _: 1]
lenF = len(functions)

N = 2000
X = np.linspace(0, 5, N)
Y = np.empty(N)
for i in range(N): Y[i] = (.5+random())*X[i]+1 #.5*X[i]+1+random()

A = np.empty((lenF,lenF))
B = np.zeros(lenF)

for i in range(lenF):
    for j in range(lenF):
        A[i,j] = sumWith(lambda x: functions[i](x)*functions[j](x), X)
for i in range(lenF):
    for j in range(N):
        B[i] += Y[j]*functions[i](X[j])

W = np.linalg.solve(A, B)
print(W)

