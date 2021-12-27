import numpy as np
from lib import waveMatrix



matrix1 = waveMatrix(2,2,0,10,32,64,64)
matrix2 = waveMatrix(4,4,1,9,16,32,32)
matrix3 = waveMatrix(8,8,1,9,8,16,16)
matrix4 = waveMatrix(16,16,2,8,4,8,8)
matrix5 = waveMatrix(32,32,3,7,2,4,4)


matrix1.GenerateMatrix()
matrix2.GenerateMatrix()
matrix3.GenerateMatrix()
matrix4.GenerateMatrix()
matrix5.GenerateMatrix()

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
def main1():
    matrix1.InterpolateMatrix(inter1,2,1,2)
    matrix2.InterpolateMatrix(inter1,2,1,2)
    matrix3.InterpolateMatrix(inter1,2,1,2)
    matrix4.InterpolateMatrix(inter1,2,1,2)
    matrix5.InterpolateMatrix(inter1,2,1,2)

    printMatrix(matrix1.matrix)

    matrix1.AddMatrix(matrix2.matrix,5)
    matrix1.InterpolateMatrix(inter2,2,1,2)
    printMatrix(matrix1.matrix)


    matrix1.AddMatrix(matrix3.matrix,5)
    matrix1.InterpolateMatrix(inter2,2,1,2)
    printMatrix(matrix1.matrix)

    matrix1.AddMatrix(matrix4.matrix,5)
    matrix1.InterpolateMatrix(inter2,2,1,2)
    printMatrix(matrix1.matrix)

    matrix1.AddMatrix(matrix5.matrix,5)
    matrix1.InterpolateMatrix(inter2,2,1,2)
    printMatrix(matrix1.matrix)

    matrix1.InterpolateMatrix(50,2,1,2)
    printMatrix(matrix1.matrix)

def main2():
    printMatrix(matrix2.matrix)
    matrix2.InterpolateMatrix(200,0.05,1,1)
    printMatrix(matrix2.matrix)

main1()
input()


