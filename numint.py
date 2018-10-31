import numpy as np
#import scipy as sp

def mytrapz(x,y):
    I=0
    dx = abs(x[1]-x[0])
    for i in range(1,len(y)):
         I += 0.5*(y[i-1]+y[i])*dx
    return I

N = 50
x = np.linspace(0,4,N)
y = -(x-2)**2 + 4

I = mytrapz(x,y)
print("My function gives I = %s" % I)
print("Numpy trapz gives I = %s" % np.trapz(y,x))


