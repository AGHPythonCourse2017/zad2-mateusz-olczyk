from numpy import empty, zeros
from numpy.linalg import solve
from itertools import product


def approx(base_functions, mapping_xy):
    l = len(base_functions)
    a = empty((l, l))
    b = zeros(l)
    for i, j in product(range(l), repeat=2):
        a[i, j] = sum(map(lambda x: base_functions[i](x) * base_functions[j](x), mapping_xy))
    for i in range(l):
        b[i] = sum(map(lambda x: mapping_xy[x] * base_functions[i](x), mapping_xy))
    return solve(a, b)
