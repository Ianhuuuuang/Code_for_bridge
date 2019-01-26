import numpy as np
# from numpy import *
# a = random.randint(50, 100, (5, 5))
# print(a)
# a = np.zeros((2, 2))
# print(a)

List = range(6)
it = iter(List)
a = np.fromiter(it, dtype=complex)
print(a)

