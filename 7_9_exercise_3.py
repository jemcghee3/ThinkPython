"""Exercise 3

The mathematician Srinivasa Ramanujan found an infinite series that can be used
to generate a numerical approximation of 1 / π:

1
π
	 =
2	√
2
9801

∞
∑
k=0

(4k)!(1103+26390k)
(k!)4 3964k


Write a function called estimate_pi that uses this formula to compute and return an estimate of π.
It should use a while loop to compute terms of the summation until the last term is smaller than 1e-15
(which is Python notation for 10^−15). You can check the result by comparing it to math.pi.

Solution: http://thinkpython2.com/code/pi.py."""

import math

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result

def estimate_pi():
    k = 0
    est_pi = 0
    while len(str(est_pi)) < len(str(10**-15)):
        summation = ((factorial(4*k)*(1103+26390*k))/(factorial(k)**4*396**(4*k)))
        k += 1
        est_pi = est_pi + summation
    est_pi = est_pi * ((2 * math.sqrt(2)) / 9801)
    print(est_pi**-1)
    print(math.pi)

estimate_pi()