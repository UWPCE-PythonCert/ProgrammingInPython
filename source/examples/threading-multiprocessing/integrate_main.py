#!/usr/bin/env python

# from integrate import integrate_f_with_functional_tools as integrate_f
from integrate import integrate, f

a = 0.0
b = 10.0

for N in (10**i for i in range(1, 8)):
    print("Numerical solution with N=%(N)d : %(x)f" %
          {'N': N, 'x': integrate(f, a, b, N)})
