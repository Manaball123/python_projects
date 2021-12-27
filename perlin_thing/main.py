import numpy as np
from lib import waveMatrix



matrix1 = waveMatrix(100,100,0,1,25,50,50)

gridMatrix = matrix1.GenerateGrid()

depth = [" ", ".", ";", "*", "=", "U", "G", "M", "#", "@", "█"]


def GetDepth(value):
    roundedVal = int(np.round(value,1)*10)
    return depth[roundedVal]
    
string = ""
for i in range(len(gridMatrix)):
    for j in range(len(gridMatrix[i])):
        string += GetDepth(gridMatrix[i][j]) + " "
    string += "\n"
    

        

print(string)
input()


