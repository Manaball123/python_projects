import numpy as np

def VectorAdd(v1,v2):
    return np.array([ v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2] ])

def VectorSubtract(v1,v2):
    return np.array([ v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2] ])

def VectorLength(v):
    return (v[0] ** 2 + v[1] ** 2 + v[2] ** 2) ** (1/2) 

def VectorDist(v1,v2):
    return ((v1[0] - v2[0]) ** 2 + (v1[1] - v2[1]) ** 2 + (v1[2] - v2[2]) ** 2) ** (1/2)

def VectorExtend(v, magnitude):
    return np.array([v[0] * magnitude, v[1] * magnitude, v[2] * magnitude])

def DotProduct(v1,v2):
    return v1[0] * v2[0] + v1[1] * v2[1] + v1[2] * v2[2]

def CrossProduct(v1,v2):
    return
    
def matrixVecMultiplication(m,v):
    col1 = m[0][0] * v[0] + m[0][1] * v[1] + m[0][2] * v[2]
    col2 = m[1][0] * v[0] + m[1][1] * v[1] + m[1][2] * v[2]
    col3 = m[2][0] * v[0] + m[2][1] * v[1] + m[2][2] * v[2]
    return np.array([col1, col2, col3])

def GetDirectionVector(v):
    length = VectorLength(v)
    return np.array([v[0] / length, v[1] / length, v[2] / length])



#courtesy to dhdj for the thing below(modified but still cool)
def ANG2VEC(yaw,pitch):
    return np.array([np.cos(np.deg2rad(pitch)) * np.cos(np.deg2rad(yaw)), np.sin(np.deg2rad(pitch)), np.cos(np.deg2rad(pitch)) * np.sin(np.deg2rad(yaw))])