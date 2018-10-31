# import numpy as np



def mytrapz(x):
    return -(x-2)**2+4


def integral(x1,x2,n):
    y0=0
    dx=(x2-x1)/n
    x_l=x1
    x_r = x1 + dx
    dx = (x2 - x1) / n

    while x_r<x2:
        y0=y0+(mytrapz(x_l)+mytrapz(x_r))*dx/2
        x_l=x_r
        x_r=x_l+dx
    return y0

print(integral(0,4,100))

