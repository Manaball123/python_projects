import numpy as np
import time
#TODO:
#PRECALCULATE THE SINE MAP
void=9

class camera:
    

    def __init__(self,coordinates,baseRotation,fov,resolution):
        """
        Coordinates: array object containing coordinates(x=[0],y=[1],z=[2])
        baseRotation: array object containing rotations(yaw=0,pitch=1),
        fov: array object containing fov(yaw=0,pitch=1)
        resolution:array object containing h and w for resolution(w=0,h=1)
        resolution MUST BE AN EVEN NUMBER
        """
        self.coordinates=coordinates
        self.baseRotation=baseRotation
        self.fov=fov
        self.resolution=resolution
        self.world=np.array([])
        self.rayMap=np.array([])
        #print each row first
        self.screen=np.array([[0]*self.resolution[0]]*self.resolution[1])
        #useless for now
        self.screenMap=np.array([[[0]*2]*self.resolution[0]]*self.resolution[1])
        #SCREEN LOOKS LIKE THIS
        #- 0 1 2 3 4 5 6 7 8 9
        #0 
        #1
        #2
        #3
        #4

        

    def updateWorld(self,world):
        """uses the world array as a parameter,updates the world in the class object"""
        self.world=world

    def updateRayMap(self,raymap):
        self.rayMap=raymap

    def mapAngles(self):
        yawDelta=self.fov[0]/self.resolution[0]
        pitchDelta=self.fov[1]/self.resolution[1]
        startYaw=self.fov[0]/2+self.baseRotation[0]
        startPitch=self.fov[1]/2+self.baseRotation[1]
        currentRotation=np.array([startYaw,startPitch])
        
        for i in range(self.resolution[1]):
            currentRotation[0]=startYaw
            j=0
            for j in range(self.resolution[0]):
                self.screen[i][j]=self.castRay(np.round(currentRotation,2))

                currentRotation[0]-=yawDelta
            currentRotation[1]-=pitchDelta

        


    def castRay(self,screenPoint):
        """casts ray in specific rotation,returns the pixel type that the ray collided to"""
        #maybe return coordinates in the future for better world optimization
        #initializes target coords
        
        targetCoords=np.array([0,0,0])
        
        #relative positions below(x=0,y=1,z=2), convert to abseloute ones afterwards
        rCoords=np.array([0,0,0])
        
        angles=np.array([0,0])
        angles=np.round(np.deg2rad(degAng),2)
        
        #this is angles in radians
        
        
        tangents=np.round(np.tan(angles),2)
       
        #print("which has the tangents x y:"+str(tangents[0])+", "+str(tangents[1]))

        while targetCoords[0]<len(self.world)-1:
            targetCoords[0]=rCoords[0]+self.coordinates[0]
            
            if self.rayMap[targetCoords[0]]==True:


                rCoords[1]=rCoords[0]*tangents[1]
                rCoords[2]=rCoords[0]*tangents[0]

                #check if collided with anything
                targetCoords=np.round(rCoords)+self.coordinates
                
            

                #print("Checking "+str(targetCoords))

                #if the coords needs clamping, it hit the void already
                if targetCoords[1]>len(self.world[0])-1:
                    return void
 
                elif targetCoords[1]<0:
                    return void

                if targetCoords[2]>len(self.world[0][0])-1:
                    return void
                
                elif targetCoords[2]<0:
                    return void

                #check range after clamp
                pixelType=self.world[targetCoords[0]][targetCoords[1]][targetCoords[2]]
            
                #if hit
            
                if pixelType!=0:
                    
                    return(pixelType)

            #increment by 1 
            
            rCoords[0]=rCoords[0]+1

        #if loop ends and no hit
        return void

    def renderScreen(self):
        """populates the self.screen object"""
        startTime=time.time()
        #halfW=self.resolution[0]/2
        #halfH=self.resolution[1]/2
        yawDelta=self.fov[0]/self.resolution[0]
        pitchDelta=self.fov[1]/self.resolution[1]
        startYaw=self.fov[0]/2+self.baseRotation[0]
        startPitch=self.fov[1]/2+self.baseRotation[1]
        currentRotation=np.array([startYaw,startPitch])
        
        for i in range(self.resolution[1]):
            currentRotation[0]=startYaw
            j=0
            for j in range(self.resolution[0]):
                self.screen[i][j]=self.castRay(np.round(currentRotation,2))

                currentRotation[0]-=yawDelta
            currentRotation[1]-=pitchDelta
        
        endTime=time.time()
        deltaTime=endTime-startTime
        print("Time took to render the screen is: "+str(deltaTime))

    





        
        


