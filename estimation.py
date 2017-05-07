from math import log2
from time import time
from numpy import empty, zeros, logspace
from numpy.linalg import solve
from itertools import product
import matplotlib.pyplot as plt


def approximate(base_functions, mapping_xy):
    l = len(base_functions)
    a = empty((l, l))
    b = zeros(l)
    for i, j in product(range(l), repeat=2):
        a[i, j] = sum(map(lambda x: base_functions[i](x) * base_functions[j](x), mapping_xy))
    for i in range(l):
        b[i] = sum(map(lambda x: mapping_xy[x] * base_functions[i](x), mapping_xy))
    return solve(a, b)


def time_measure(fun):
    start = time()
    fun()
    end = time()
    return end - start


def get_samples(task_class):
    mapping_nt = {}
    for n in logspace(2, 6.6, num=100):
        task = task_class(int(n))
        task.task_init()
        mapping_nt[n] = time_measure(task.task_invoke)
    return mapping_nt


class Estimation:

    functions = {
        "O(1)": lambda _: 1,
        "O(n)": lambda x: x,
        "O(n^2)": lambda x: x**2,
        "O(n^3)": lambda x: x**3,
        "O(log n)": lambda x: log2(x),
        "O(n log n)": lambda x: x*log2(x),
    }
    base_functions = list(functions.values())

    def __init__(self, task_class):
        self.mapping_nt = get_samples(task_class)
        self.coefficients = approximate(Estimation.base_functions, self.mapping_nt)

    def get_time(self, n):
        s = 0
        for i, f in enumerate(Estimation.functions.values()):
            s += self.coefficients[i] * f(n)
        return s

    def show_plot(self):
        x = list(self.mapping_nt.keys())
        y_real = list(self.mapping_nt.values())
        y_est = list(map(self.get_time, x))
        plt.plot(x, y_real, 'b')
        plt.plot(x, y_est, 'r')
        plt.show()
