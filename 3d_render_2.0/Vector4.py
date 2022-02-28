import numpy as np


def PERSPMATRIX(x,y,z,yaw,pitch,roll):
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
                x,
                
            ],

            [
                -cosYaw * sinPitch * sinRoll - sinYaw * cosRoll,
                cosPitch * sinRoll,
                -sinYaw * sinPitch * sinRoll + cosYaw * cosRoll,
                y,
                
            ],

            [
                -cosYaw * sinPitch * cosRoll + sinYaw * sinRoll,
                cosPitch * cosRoll,
                -sinYaw * sinPitch * cosRoll - cosYaw * sinRoll,
                z,
            ],
            [0,0,0,1]

    ])

def Transform(v,m):
    return np.array([
        m[0][0] * v[0] + m[0][1] * v[1] + m[0][2] * v[2] + m[0][3] * v[3],
        m[1][0] * v[0] + m[1][1] * v[1] + m[1][2] * v[2] + m[1][3] * v[3],
        m[2][0] * v[0] + m[2][1] * v[1] + m[2][2] * v[2] + m[2][3] * v[3],
        m[3][0] * v[0] + m[3][1] * v[1] + m[3][2] * v[2] + m[3][3] * v[3],
        ])