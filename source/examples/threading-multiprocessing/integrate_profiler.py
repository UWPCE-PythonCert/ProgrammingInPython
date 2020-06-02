#!/usr/bin/env python3

from integrate import (f,
                       integrate_numpy as _integrate_numpy,
                       integrate as _integrate
                       )
from decorators import timer


@timer
def integrate(*args):
    return _integrate(*args)


a = 0.0
b = 10.0

# print("running the pure python version")
# for N in (10**i for i in range(1, 8)):
#     print("Numerical solution with N=%(N)d : %(x)f" %
#           {'N': N, 'x': integrate(f, a, b, N)})


# now the numpy version:
@timer
def integrate_numpy(*args):
    return _integrate_numpy(*args)


print("running the numpy version")
for N in (10**i for i in range(1, 8)):
    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': integrate_numpy(f, a, b, N)})
