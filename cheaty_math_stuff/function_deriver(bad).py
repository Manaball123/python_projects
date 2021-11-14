import numpy as np


def function(x):

    #put ur function here

    y=x**2
    return(y)


def deriver(x,dx):
    y=function(x)
    print("y for current point is: "+str(y))
    
    d_x=x+dx
    print("dx+x is: "+str(d_x))
    dy=function(d_x)-y
    print("dy for current+dx is: "+str(dy))
    return(dy/dx)



print(deriver(2,0.0000000000001))
