import numpy as np
import Vector2
import Vector3
class camera:
    def __init__(self,coordinates,baseRotation,fov,resolution,elements):
        """
        coordinates: array object containing coordinates(x=[0],y=[1],z=[2])
        baseRotation: array object containing rotations(yaw=0,pitch=1),
        fov: array object containing fov(yaw=0,pitch=1)
        resolution:array object containing h and w for resolution(w=0,h=1)
        resolution MUST BE AN EVEN NUMBER
        elements: object with int key : string value
        """
        self.coordinates = coordinates
        self.baseRotation = baseRotation
        self.fov = fov
        self.resolution = resolution
        self.elements = elements
        
        self.screen = np.array([[0]*self.resolution[1]]*self.resolution[0])
        self.transformMatrix = np.array([[0]*3]*3)
        #useless for now
        
    def drawLine(self,p1,p2,element):
        """
        draws a line from a point(on the screen) to another,to the screen
        """
        length = Vector2.VectorDist(p1,p2)
        #print(length)
        if(length == 0):
            return
        vector = np.array([(p2[0] - p1[0])/length, (p2[1] - p1[1])/length])
        #print(vector)


        
        currentCoords = np.array([p1[0],p1[1]])
        i = 0
        while i < length:
            i += 1
            currentCoords = np.array([round(p1[0] + vector[0] * i), round(p1[1] + vector[1] * i)])
            if(0 <= currentCoords[0] < self.resolution[0] and 0 <= currentCoords[1] < self.resolution[1]):
                self.screen[currentCoords[0]][currentCoords[1]] = element
                #print("added element at " + str(currentCoords))
            else:
                return
                
                
    def clearScreen(self):
        self.screen = np.array([[0]*self.resolution[1]]*self.resolution[0])

    def AddRotation(self,rotations):
        self.getTransformMatrix()
        """
        rotations: rotations added(yaw=0, pitch=1, DO NOT EXCEED 180)
        """
        self.baseRotation[0] += rotations[0]
        self.baseRotation[1] += rotations[1]
        if(self.baseRotation[0] > 180):
            self.baseRotation[0] = self.baseRotation[0] - 360
        elif(self.baseRotation[0] < -180):
            self.baseRotation[0] = self.baseRotation[0] + 360

        if(self.baseRotation[1] > 180):
            self.baseRotation[1] = self.baseRotation[1] - 360
        elif(self.baseRotation[1] < -180):
            self.baseRotation[1] = self.baseRotation[1] + 360

    #DO NOT USE THIS DIRECTLY
    def FillFlatTriangle(self,start,end1,end2,element):
        """
        end 1 and 2 must have the same x value, end2 must have a lower y than end1
        """
        endX = end1[0]
        vec1 = Vector2.GetDirectionVector(Vector2.VectorSubtract(end1, start))
        vec2 = Vector2.GetDirectionVector(Vector2.VectorSubtract(end2, start))
        if(vec1[0] != 0):
            increment1 = vec1[1] / vec1[0]
        else:
            increment1 = 0
            
        if(vec2[0] != 0):
            increment2 = vec2[1] / vec2[0]
        else:
            increment2 = 0

        print(increment1)
        print(increment2)
        for i in range(endX + 1):
            yInc1 = round(increment1 * i)
            yInc2 = round(increment2 * i)

            #drawline but more optimized, cuz its straight
            if(0 <= yInc1 < self.resolution[1] and 0 <= yInc2 < self.resolution[1]):
                for j in range(yInc1 - yInc2 + 1):
                    self.screen[i + start[0]][j + yInc2] = element
                #print("added element at " + str(currentCoords))
            else:
                return
            

    #NOTE:
    #GHETTO SOLUTION, FIGURE OUT WHY ITS INVERTED
    def printScreen(self):
        """
        prints the screen in console
        """
        outputStr = ""
        #print by column
        
        """
        i = self.resolution[1] - 1
        while i >= 0:
            for j in range(self.resolution[0]):
                outputStr += self.elements[self.screen[j][i]]
            outputStr += "\n" 
            i -= 1
        """
        for i in range(self.resolution[1]):
            for j in range(self.resolution[0]):
                outputStr += self.elements[self.screen[j][i]]
            outputStr += "\n" 
        

        print(outputStr)
    
    def getTransformMatrix(self):
        rotations = np.deg2rad(self.baseRotation)
        sinYaw = np.sin(rotations[0])
        cosYaw = np.cos(rotations[0])
        sinPitch = np.sin(rotations[1])
        cosPitch = np.cos(rotations[1])
        xVector = np.array([cosYaw * cosPitch, sinPitch, sinYaw * cosPitch])
        yVector = Vector3.MatrixVecMultiplication(np.array([[0,1,0],[-1,0,0],[0,0,1]]),xVector)
        zVector = Vector3.MatrixVecMultiplication(np.array([[0,0,1],[0,1,0],[-1,0,0]]),xVector)

        #self.transformMatrix = np.array([xVector,yVector,zVector])
        self.transformMatrix = Vector3.ANG2MATRIX(self.baseRotation[0],self.baseRotation[1],self.baseRotation[2])
        

    def worldToScreen(self,pointCoords):

        relativePosition = Vector3.VectorSubtract(pointCoords, self.coordinates)
        transformedPosition = Vector3.MatrixVecMultiplication(self.transformMatrix, relativePosition)

        #relative to camera
        
        yaw = np.rad2deg(np.tanh(transformedPosition[2] / transformedPosition[0]))
        pitch = np.rad2deg(np.tanh(transformedPosition[1] / transformedPosition[0]))
        #print(yaw)
        #print(pitch)
        return [round((yaw / self.fov[0]) * self.resolution[0] + self.resolution[0] / 2) , round((pitch / self.fov[1]) * self.resolution[1] + self.resolution[1] / 2), transformedPosition[0]]

    def renderCube(self,start,end,element):

        """
        renders a cube
        start: a 3d vector
        end: a 3d vector
        """
    
        screenPoints = np.array([np.array([0,0])] * 8)
        vertices = np.array([np.array([0,0,0])] * 8)

        vertices[0] = [start[0], start[1], start[2]]
        vertices[1] = [start[0], end[1], start[2]]
        vertices[2] = [start[0], end[1], end[2]]
        vertices[3] = [start[0], start[1], end[2]]
        vertices[4] = [end[0], start[1], start[2]]
        vertices[5] = [end[0], end[1], start[2]]
        vertices[6] = [end[0], end[1], end[2]]
        vertices[7] = [end[0], start[1], end[2]]
        for i in range(8):
            screenPoints[i] = self.worldToScreen(vertices[i])




        self.drawLine(screenPoints[0], screenPoints[1], element)
        self.drawLine(screenPoints[0], screenPoints[3], element)
        self.drawLine(screenPoints[0], screenPoints[4], element)

        self.drawLine(screenPoints[2], screenPoints[1], element)
        self.drawLine(screenPoints[2], screenPoints[3], element)
        self.drawLine(screenPoints[2], screenPoints[6], element)

        self.drawLine(screenPoints[5], screenPoints[1], element)
        self.drawLine(screenPoints[5], screenPoints[4], element)
        self.drawLine(screenPoints[5], screenPoints[6], element)

        self.drawLine(screenPoints[7], screenPoints[3], element)
        self.drawLine(screenPoints[7], screenPoints[4], element)
        self.drawLine(screenPoints[7], screenPoints[6], element)

        
        
            
            
        

            
        




