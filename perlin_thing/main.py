import numpy as np
from lib import waveMatrix



matrix1 = waveMatrix(100,100,0,1,25,50,50)

gridMatrix = matrix1.GenerateGrid(0,0)
gridMatrix = matrix1.GenerateGrid(0,50)
gridMatrix = matrix1.GenerateGrid(50,0)
gridMatrix = matrix1.GenerateGrid(50,50)

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
input()


