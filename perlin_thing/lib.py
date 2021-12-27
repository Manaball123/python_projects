#my attempt at replicating the perlin waves thing
#core concepts: random vectors at different vertices in some grid
#interpolation to make it smooth
import random
import numpy as np
import Vector2 
import copy

class waveMatrix:


    def __init__(self,xGrids,yGrids,min,max,vecMag,gridX,gridY):
        self.xGrids = xGrids
        self.yGrids = yGrids
        self.matrix = np.array([[0.0] * (yGrids * gridY)] * (xGrids * gridX))
        #attempt at interpolating
        self.matrixCache = np.array([[0.0] * (yGrids * gridY)] * (xGrids * gridX))
        self.min = min
        self.max = max
        self.vecMag = vecMag
        self.gridX = gridX
        self.gridY = gridY
        self.maxMag = vecMag + Vector2.VectorLength(np.array([(gridX/2), (gridY/2)]))
        #print(self.maxMag)

    def GetDirection(self,value):
        if(value == 0):
            return -1
        else:
            return 1

    def GenerateGrid(self,startX,startY):
        gridMatrix = np.array([[0.0] * self.gridY] * self.gridX)
        vectorX = random.uniform(-self.vecMag, self.vecMag)
        vectorY = Vector2.GetVectorFromLength(self.vecMag, vectorX) * self.GetDirection(random.randint(0,1))
        
        vector = np.array([vectorX,vectorY])
        #print(vector)
        for i in range(len(gridMatrix)):
            for j in range(len(gridMatrix[i])):
                #print("x is " + str(i - (self.gridX/2)) + ", y is " + str(j - (self.gridY/2)) + ", distance is " + str(Vector2.VectorDist(np.array([i - (self.gridX/2), j - (self.gridY/2)]), vector)))
                #gridMatrix[i][j] = 1 - (Vector2.VectorDist(np.array([i - (self.gridX/2), j - (self.gridY/2)]), vector)/self.maxMag)
                self.matrix[startX + i][startY + j] = 1 - (Vector2.VectorDist(np.array([i - (self.gridX/2), j - (self.gridY/2)]), vector)/self.maxMag)
    
    def GenerateMatrix(self):
        for i in range(self.xGrids - 1):
            for j in range(self.yGrids - 1):
                self.GenerateGrid(i * self.gridX, j * self.gridY)

    #range is not used rn, cba
    def InterpolateMatrix(self,interpRange):
        self.matrixCache = copy.deepcopy(self.matrix)
        
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
                
            
    
        



            







