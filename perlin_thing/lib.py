#my attempt at replicating the perlin waves thing
#core concepts: random vectors at different vertices in some grid
#interpolation to make it smooth
import random
import numpy as np
import Vector2 


class waveMatrix:


    def __init__(self,x,y,min,max,vecMag,gridX,gridY):
        self.matrix = np.array([[0.0] * y] * x)
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
            
    
        



            







