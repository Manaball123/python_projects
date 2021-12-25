import numpy as np

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
        self.coordinates=coordinates
        self.baseRotation=baseRotation
        self.fov=fov
        self.resolution=resolution
        self.elements=elements
        
        self.screen=np.array([[0]*self.resolution[1]]*self.resolution[0])
        #useless for now
        
    def drawLine(self,p1,p2,element):
        """
        draws a line from a point(on the screen) to another,to the screen
        """
        print(p1)
        print(p2)
        deltaX = round(p2[0]-p1[0])
        deltaY = round(p2[1]-p1[1])
        
        #scale  by this
        scaleX = 0
        scaleY = 0
        if(deltaY != 0):
            scaleX = deltaX/deltaY
        if(deltaX != 0):
            scaleY = deltaY/deltaX

        currentCoords = np.array([p1[0],p1[1]])
        
        for i in range(abs(deltaX+1)):
            if(currentCoords[0] < self.resolution[0] and currentCoords[1] < self.resolution[1] and currentCoords[0]>=0 and currentCoords[1]>=1):
                self.screen[currentCoords[0]][currentCoords[1]] = element
                print("added element at")
                print(currentCoords)

            else:
                break

            currentCoords[0] = p1[0] + i * (deltaX/abs(deltaX))
            currentCoords[1] = p1[1] + round(i * scaleY)
            
        #resets coords
        currentCoords = np.array([p1[0],p1[1]])

        for i in range(abs(deltaY+1)):
            if(currentCoords[0] < self.resolution[0] and currentCoords[1] < self.resolution[1] and self.resolution[0]>=0 and self.resolution[1]>=1):
                self.screen[currentCoords[0]][currentCoords[1]] = element
                print("added element at")
                print(currentCoords)

            else:
                break

            currentCoords[0] = p1[0] + round(i * scaleX)
            currentCoords[1] = p1[1] + i * (deltaY/abs(deltaY))
            print("added element at")
            print(currentCoords)
        
    def printScreen(self):
        """
        prints the screen in console
        """
        outputStr = ""
        #print by column
        i=self.resolution[1]-1
        while i>=0:
            for j in range(self.resolution[0]):
                outputStr += self.elements[self.screen[j][i]]
            outputStr += "\n"
            i-=1

        print(outputStr)
    

    def worldToScreen(self,pointCoords):
        deltaX = pointCoords[0]-self.coordinates[0]
        deltaY = pointCoords[1]-self.coordinates[1]
        deltaZ = pointCoords[2]-self.coordinates[2]

        yaw = np.rad2deg(np.cosh(deltaX/deltaZ))+self.baseRotation[0]
        pitch = np.rad2deg(np.cosh(deltaX/deltaY))+self.baseRotation[1]
        print(yaw)
        print(pitch)

        return [round((yaw/self.fov[0])*(self.resolution[0]-1)),round((pitch/self.fov[1])*(self.resolution[1]-1))]

        
        
            
            
        

            
        




