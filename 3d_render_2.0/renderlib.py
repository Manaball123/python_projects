import numpy as np
import Vector2
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
        #useless for now
        
    def drawLine(self,p1,p2,element):
        """
        draws a line from a point(on the screen) to another,to the screen
        """
        length = Vector2.VectorDist(p1,p2)
        #print(length)
        if(length == 0):
            self.screen[p1[0]][p1[1]] = element
            return
        vector = np.array([(p2[0] - p1[0])/length, (p2[1] - p1[1])/length])
        #print(vector)


        
        currentCoords = np.array([p1[0],p1[1]])
        i = 0
        while i < length:
            i += 1
            currentCoords = np.array([round(p1[0] + vector[0] * i), round(p1[1] + vector[1] * i)])
            if(currentCoords[0] < self.resolution[0] and currentCoords[1] < self.resolution[1] and currentCoords[0] >= 0 and currentCoords[1] >= 0):
                self.screen[currentCoords[0]][currentCoords[1]] = element
                #print("added element at " + str(currentCoords))
            else:
                return
                
                

        
    def printScreen(self):
        """
        prints the screen in console
        """
        outputStr = ""
        #print by column
        i = self.resolution[1] - 1
        while i >= 0:
            for j in range(self.resolution[0]):
                outputStr += self.elements[self.screen[j][i]]
            outputStr += "\n" 
            i -= 1

        print(outputStr)
    

    def worldToScreen(self,pointCoords):
        deltaX = pointCoords[0] - self.coordinates[0]
        deltaY = pointCoords[1] - self.coordinates[1]
        deltaZ = pointCoords[2] - self.coordinates[2]

        yaw = np.rad2deg(np.tanh(deltaZ/deltaX)) - self.baseRotation[0]
        pitch = np.rad2deg(np.tanh(deltaY/deltaX)) - self.baseRotation[1]
        #print(yaw)
        #print(pitch)

        return [round((yaw / self.fov[0]) * (self.resolution[0]) + self.resolution[0]/2) , round((pitch / self.fov[1]) * (self.resolution[1]) + self.resolution[1]/2)]


    def renderCube(self,vertices):
        """
        renders a 8 vertices pologon(can be in weird shape)
        vertices: array that has 8 vectors
        """
        screenPoints = np.array([np.array([0,0])]*8)
        for i in range(8):
            screenPoints[i] = self.worldToScreen(vertices[i])


        self.drawLine(screenPoints[0],screenPoints[1],1)
        self.drawLine(screenPoints[0],screenPoints[3],1)
        self.drawLine(screenPoints[0],screenPoints[4],1)

        self.drawLine(screenPoints[2],screenPoints[1],1)
        self.drawLine(screenPoints[2],screenPoints[3],1)
        self.drawLine(screenPoints[2],screenPoints[6],1)

        self.drawLine(screenPoints[5],screenPoints[1],1)
        self.drawLine(screenPoints[5],screenPoints[4],1)
        self.drawLine(screenPoints[5],screenPoints[6],1)

        self.drawLine(screenPoints[7],screenPoints[3],1)
        self.drawLine(screenPoints[7],screenPoints[4],1)
        self.drawLine(screenPoints[7],screenPoints[6],1)

        
        
            
            
        

            
        




