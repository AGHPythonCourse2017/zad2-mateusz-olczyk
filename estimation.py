from math import log2
from time import time
from numpy import logspace
import matplotlib.pyplot as plt
from operator import itemgetter


# Decorator
def binary_inverse(fun):
    def inverted(self, t):
        left = 0
        right = 1
        while fun(self, right) < t:
            right *= 2
        while right - left > 1:
            middle = (left+right)/2
            if fun(self, middle) > t:
                right = middle
            else:
                left = middle
        return (left+right)/2
    return inverted


def approximate(base_function, mapping_xy):
    a = sum(map(lambda x: base_function(x)**2, mapping_xy))
    b = sum(map(lambda x: mapping_xy[x] * base_function(x), mapping_xy))
    return lambda x: b/a * base_function(x)


def approximation_cost(approx_function, mapping_xy):
    return sum(map(lambda x: (mapping_xy[x]-approx_function(x))**2, mapping_xy))


def time_measure(fun):
    start = time()
    fun()
    end = time()
    return end - start


def get_samples(task_class, num=100):
    mapping_nt = {}
    for n in logspace(2, 6, num):
        task = task_class(int(n))
        task.task_init()
        mapping_nt[n] = time_measure(task.task_invoke)
        task.task_finalize()
    return mapping_nt


class Estimation:

    complexities = {
        "O(1)": lambda _: 1,
        "O(n)": lambda x: x,
        "O(n^2)": lambda x: x**2,
        "O(n^3)": lambda x: x**3,
        "O(log n)": log2,
        "O(n log n)": lambda x: x*log2(x),
    }

    def best_approximation(self):
        approximations = []
        for complexity in self.complexities:
            approx_function = approximate(self.complexities[complexity], self.mapping_ntime)
            approximations.append((
                complexity,
                approx_function,
                approximation_cost(approx_function, self.mapping_ntime)
            ))
        best_complexity = min(approximations, key=itemgetter(2))
        return best_complexity[:2]

    def __init__(self, task_class):
        self.mapping_ntime = get_samples(task_class)
        self.complexity, self.get_time_for_n = self.best_approximation()

    @binary_inverse
    def get_n_for_time(self, t):
        return self.get_time_for_n(t)

    def show_plot(self):
        x = list(self.mapping_ntime.keys())
        y_real = list(self.mapping_ntime.values())
        y_est = list(map(self.get_time_for_n, x))
        plt.plot(x, y_real, 'b')
        plt.plot(x, y_est, 'r')
        plt.show()
