import numpy as np
from lib import waveMatrix



matrix1 = waveMatrix(8,8,0,1,8,16,16)

matrix1.GenerateMatrix()

depth = ["  ", " .", " -", " *", " +", " M", " 0", "[[", "##", "@@", "██"]


def GetDepth(value):
    roundedVal = int(np.round(value,1)*10)
    return depth[roundedVal]
    
string = ""
for i in range(len(matrix1.matrix)):
    for j in range(len(matrix1.matrix[i])):
        string += GetDepth(matrix1.matrix[i][j]) + ""
    string += "\n"
print(string)
for i in range(25):
    matrix1.InterpolateMatrix(1)


string = ""
for i in range(len(matrix1.matrix)):
    for j in range(len(matrix1.matrix[i])):
        string += GetDepth(matrix1.matrix[i][j]) + ""
    string += "\n"
print(string)

input()


