#my attempt at replicating the perlin waves thing
#core concepts: random vectors at different vertices in some grid
#interpolation to make it smooth
import random
import numpy as np
from numpy.lib.function_base import average
import Vector2 
import copy



def clamp(value, min, max):
    if(value > max):
        return max
    elif(value < min):
        return min
    return value

class waveMatrix:


    def __init__(self,xGrids,yGrids,min,max,vecMag,gridX,gridY):
        """
        xGrids: amount of grids on the x axis
        yGrids: amount of grids on the y axis
        min: the minimum level of the wave
        max: the maximum level of the wave
        vecMag: the longest distance a vector can be(on one axis)
        gridX: the x length of each grid
        gridY: the y length of each grid
        """
        self.xGrids = xGrids
        self.yGrids = yGrids
        self.matrix = np.array([[0.0] * (yGrids * gridY)] * (xGrids * gridX))
        #attempt at interpolating
        self.matrixCache = np.array([[0.0] * (yGrids * gridY)] * (xGrids * gridX))
        self.min = min
        self.max = max
        self.valueRange = self.max - self.min
        self.vecMag = vecMag
        self.gridX = gridX
        self.gridY = gridY
        self.maxMag = vecMag + Vector2.VectorLength(np.array([(gridX/2), (gridY/2)]))
        self.poses = np.array([np.array([1,0]), np.array([-1,0]), np.array([0,1]), np.array([0,-1])])
        #print(self.maxMag)

    def GetDirection(self,value):
        if(value == 0):
            return -1
        else:
            return 1

    def GenerateMatrix(self, seed):
        random.seed(seed)
        for i in range(self.xGrids):
            for j in range(self.yGrids):
                gridMatrix = np.array([[0.0] * self.gridY] * self.gridX)
                vectorX = random.uniform(-self.vecMag, self.vecMag)
                
                #vectorY = Vector2.GetVectorFromLength(self.vecMag, vectorX) * self.GetDirection(random.randint(0,1))
                vectorY=  random.uniform(-self.vecMag, self.vecMag)
                vector = np.array([vectorX,vectorY])
                for k in range(len(gridMatrix)):
                    for h in range(len(gridMatrix[k])):
                        #breaking it down to avoid confusion
                        #gets distance from vector
                        vecDist = Vector2.VectorDist(np.array([k - (self.gridX/2), h - (self.gridY/2)]), vector)
                        

                        self.matrix[i * self.gridX + k][j * self.gridY + h] = ((1 - (vecDist/self.maxMag)) * self.valueRange) + self.min

    def InterpolateMatrix(self, times):
        """
        times: times to repeat interpolation
        """
        for a in range(times):
            self.matrixCache = copy.deepcopy(self.matrix)
            print(a)
            for i in range(len(self.matrix)):
                for j in range(len(self.matrix[i])):

                    sum = self.matrixCache[i][j]
                    elements = 1
                    if(i - 1 >= 0):
                        sum += self.matrixCache[i - 1][j]
                        elements += 1

                    if(i + 1 < len(self.matrix)):
                        sum += self.matrixCache[i + 1][j]
                        elements += 1

                    if(j - 1 >= 0):
                        sum += self.matrixCache[i][j - 1]
                        elements += 1

                    if(j + 1 < len(self.matrix[i])):
                        sum += self.matrixCache[i][j + 1]
                        elements += 1
                        
                    

                    self.matrix[i][j] = sum/elements
                    
            
    def AddMatrix(self, newMatrix, base):
        """
        newMatrix: the matrix to add on to the base matrix
        base: baseline value for the added matrix(add if higher than base, subtract if lower, clamped to min,max)
        """
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                self.matrix[i][j] = clamp(self.matrix[i][j] + newMatrix[i][j] - base, self.min, self.max)
    
        



            







