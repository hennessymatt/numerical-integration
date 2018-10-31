from numpy import *

###################################################################

def my_trapz(x, f):

    h = x[1] - x[0]
    N = len(x)

    I = 0

    for k in range(1, N):

        I += (f[k-1] + f[k])

    return I * h / 2.


###################################################################

N = 1000
a = 0
b = 4

x = linspace(a, b, N)
f = -(x - 2.)**2 + 4

print x[1] - x[0]

print "MH's trapz function gives", my_trapz(x, f)
print "Numpy's trapz function gives", trapz(f, x)


