#some useful functions for 2d vectors

import re
import numpy as np

def VectorAdd(v1,v2):
    return np.array([ v1[0] + v2[0], v1[1] + v2[1] ])

def VectorSubtract(v1,v2):
    return np.array([ v1[0] - v2[0], v1[1] - v2[1] ])

def VectorLength(v):
    return (v[0] ** 2 + v[1] ** 2) ** (1/2) 

def VectorDist(v1,v2):
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2) ** (1/2)

def DotProduct(v1,v2):
    return v1[0] * v2[0] + v1[1] * v2[1]

def GetVectorFromLength(length,x):
    return (length ** 2 - x ** 2) ** (1/2)

def GetDirectionVector(v):
    length = VectorLength(v)
    return np.array([v[0] / length, v[1] / length])
    
def GetPerpVector(v):
    return np.array([-v[1], v[0]])


    
def ANG2VEC(angle):
    return np.array([np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))])

