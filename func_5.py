import matplotlib
matplotlib.use("Agg")
from matplotlib import pyplot
from math import sin
import numpy as np

def f(x):
    return math.sin(x)
x = np.arange(-5, 5, 1);
y = np.sin(x)
pyplot.plot(x, y)
pyplot.savefig('sin.png')
pyplot.close()