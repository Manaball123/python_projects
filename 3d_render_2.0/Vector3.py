import numpy as np
from numpy.core.numeric import rollaxis
#for rotating Y axis


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
    
def MatrixVecMultiplication(m,v):

    return np.array([
        m[0][0] * v[0] + m[1][0] * v[1] + m[2][0] * v[2],
        m[0][1] * v[0] + m[1][1] * v[1] + m[2][1] * v[2], 
        m[0][2] * v[0] + m[1][2] * v[1] + m[2][2] * v[2]
        ])

def GetRotationMatrix(angle,type):
    """
    0: yaw
    1: pitch
    2: roll(who tf uses roll lmfao)
    """
    if(type == 0):
        return np.array([
            [np.cos(np.deg2rad(angle)), 0, np.sin(np.deg2rad(angle))],
            [0, 1, 0],
            [-np.sin(np.deg2rad(angle)), 0, np.cos(np.deg2rad(angle))]
        ])
    elif(type == 1):
        return np.array([
            [np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle)), 0],
            [np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle)), 0],
            [0, 0, 1]
        ])
    #gay + retarded + cancelled + ratio + urblack
    #dont use this pls
    elif(type == 2):
        return np.array([
            [1, 0, 0],
            [0, np.cos(np.deg2rad(angle)), -np.sin(np.deg2rad(angle))],
            [0, np.sin(np.deg2rad(angle)), np.cos(np.deg2rad(angle))]
        ])

def GetDirectionVector(v):
    length = VectorLength(v)
    return np.array([v[0] / length, v[1] / length, v[2] / length])

def ANG2VEC(yaw, pitch):
    yawSin = np.sin(np.deg2rad(yaw))
    yawCos = np.cos(np.deg2rad(yaw))
    pitchSin = np.sin(np.deg2rad(pitch))
    pitchCos = np.cos(np.deg2rad(pitch))
    return np.array([yawCos * pitchCos, pitchSin , pitchCos * yawSin])

#credits: https://stackoverflow.com/questions/1568568/how-to-convert-euler-angles-to-directional-vector/1568687
#>A pitch is a counterclockwise rotation of angle about the y-axis
#huh? says who? im gonna make it clockwise 
#SUCK IT BAHAHAHAHAH
#(yes im going insane from this thing)

def ANG2MATRIX(yaw, pitch, roll):
    
    sinYaw = np.sin(np.deg2rad(-yaw))
    cosYaw = np.cos(np.deg2rad(-yaw))
    sinPitch = np.sin(np.deg2rad(-pitch))
    cosPitch = np.cos(np.deg2rad(-pitch))
    sinRoll= np.sin(np.deg2rad(-roll))
    cosRoll = np.cos(np.deg2rad(-roll))
    
    return np.array([
            [
                cosYaw * cosPitch,
                sinPitch,
                sinYaw * cosPitch, 
                
            ],

            [
                -cosYaw * sinPitch * sinRoll - sinYaw * cosRoll,
                cosPitch * sinRoll,
                -sinYaw * sinPitch * sinRoll + cosYaw * cosRoll,
                
            ],

            [
                -cosYaw * sinPitch * cosRoll + sinYaw * sinRoll,
                cosPitch * cosRoll,
                -sinYaw * sinPitch * cosRoll - cosYaw * sinRoll,
                
            ]
        ])
        
    """
    return np.array([
            [
                cosYaw * cosPitch,
                -sinPitch,
                sinYaw * cosPitch, 
                
            ],

            [
                cosYaw * sinPitch * sinRoll - sinYaw * cosRoll,
                cosPitch * sinRoll,
                sinYaw * sinPitch * sinRoll + cosYaw * cosRoll,
                
            ],

            [
                cosYaw * sinPitch * cosRoll + sinYaw * sinRoll,
                cosPitch * cosRoll,
                sinYaw * sinPitch * cosRoll - cosYaw * sinRoll,
                
            ]
        ])
        """

def ANG2XVEC(yaw, pitch, roll):
    yawSin = np.sin(np.deg2rad(yaw))
    yawCos = np.cos(np.deg2rad(yaw))
    pitchSin = np.sin(np.deg2rad(pitch))
    pitchCos = np.cos(np.deg2rad(pitch))
    rollSin = np.sin(np.deg2rad(roll))
    rollCos = np.cos(np.deg2rad(roll))
    return np.array([np.cos(np.deg2rad(pitch)) * np.cos(np.deg2rad(yaw)), np.sin(np.deg2rad(pitch)), np.cos(np.deg2rad(pitch)) * np.sin(np.deg2rad(yaw))])


