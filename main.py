from random import random
from numpy import linspace
from approx import approx

mapping = {}
for x in linspace(0, 5, 51):
    mapping[x] = -2*x*x+.5*x+1+random()
print(approx([lambda x: x*x, lambda x: x, lambda _: 1], mapping))
