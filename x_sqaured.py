import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
import math


def f(x):
    return x * x

xlist = list(range(-100, 100, 1))
ylist = []
for x in xlist:
    ylist.append(f(x))

pyplot.plot(xlist, ylist)
pyplot.savefig('myplot3.png')
pyplot.close() 