import numpy as np
from lib import waveMatrix

seed = input("Enter Seed: ")


#CHANGE THIS TO WHATEVER
matrix1 = waveMatrix(2,2,0,10,32,64,64)
matrix2 = waveMatrix(4,4,1,9,16,32,32)
matrix3 = waveMatrix(8,8,1,9,8,16,16)
matrix4 = waveMatrix(16,16,2,8,4,8,8)
matrix5 = waveMatrix(32,32,3,7,2,4,4)



matrix1.GenerateMatrix(seed)
matrix2.GenerateMatrix(seed)
matrix3.GenerateMatrix(seed)
matrix4.GenerateMatrix(seed)
matrix5.GenerateMatrix(seed)

depth = ["  ", " .", " -", " *", " +", " M", " 0", "[[", "##", "@@", "██"]


def GetDepth(value):
    roundedVal = int(np.round(value,1))
    return depth[roundedVal]
    
def printMatrix(matrix):
    string = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            string += GetDepth(matrix[i][j]) + ""
        string += "\n"
    print(string)

inter1 = 25
inter2 = 25

#CHANGE THIS TO WHATEVER

def main1():
    matrix1.InterpolateMatrix(inter1)
    matrix2.InterpolateMatrix(inter1)
    matrix3.InterpolateMatrix(inter1)
    matrix4.InterpolateMatrix(inter1)
    matrix5.InterpolateMatrix(inter1)

    printMatrix(matrix1.matrix)

    matrix1.AddMatrix(matrix2.matrix,5)
    matrix1.InterpolateMatrix(inter2)
    printMatrix(matrix1.matrix)


    matrix1.AddMatrix(matrix3.matrix,5)
    matrix1.InterpolateMatrix(inter2)
    printMatrix(matrix1.matrix)

    matrix1.AddMatrix(matrix4.matrix,5)
    matrix1.InterpolateMatrix(inter2)
    printMatrix(matrix1.matrix)

    matrix1.AddMatrix(matrix5.matrix,5)
    matrix1.InterpolateMatrix(inter2)
    printMatrix(matrix1.matrix)

    matrix1.InterpolateMatrix(50)
    printMatrix(matrix1.matrix)

main1()
input()


