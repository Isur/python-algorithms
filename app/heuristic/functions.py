# File with functions to use with algorithms

from math import cos, pi


def sphere(args):
    sum = 0
    for arg in args:
        sum += arg * arg
    return sum


def rastragin(args):
    sum = 0
    n = len(args)
    for arg in args:
        sum += arg*arg - 10*cos(2*pi*arg)
    return 10*n + sum


def rosenbrock(args):
    sum = 0
    n = len(args)
    for i in range(n - 1):
        sum += 100*(args[i+1]-args[i]**2)**2+(args[i]-1)**2
    return sum


def hyper_ellipsoid(args):
    sum = 0
    n = len(args)
    for i in range(n):
        for j in range(i):
            sum += args[j]*args[j]
    return sum


def sum_squares(args):
    sum = 0
    n = len(args)
    for i in range(n):
        sum += (i+1) * args[i]**2
    return sum


def styblinski_tang(args):
    sum = 0
    n = len(args)
    for i in range(n):
        sum = args[i]**4 - 16*args[i]**2 + 5*args[i]
    return 1/2 * sum
