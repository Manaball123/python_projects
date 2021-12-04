import lib as render
import keyboard as key
import numpy as np
import time


camCoords=np.array([0,5,5])
camRotation=np.array([0,-5])
camFOV=np.array([100,45])
#camRes=np.array([200,70])
#camRes=np.array([64,32])
camRes=np.array([20,10])
cam1=render.camera(camCoords,camRotation,camFOV,camRes)

#REWORK RAYCAST SYSTEM




wx=21
wy=11
wz=11

world=np.array([[[0]*wz]*wy]*wx)
rayMap=np.array([False]*wx)
dictionary = {
  
  1 : "█",
  render.void : " "
}



def addElement(x,y,z,e):
    """adds an element in the world"""
    global world
    world[x][y][z]=e
    rayMap[x]=True
    #print("added element "+str(e)+" at "+str(x)+", "+str(y)+", "+str(z))

def addCube(x1,x2,y1,y2,z1,z2,e):
    """adds a cube to world"""
    for i in range(x2-x1+1):
        j=0
        for j in range(y2-y1+1):
            k=0
            for k in range(z2-z1+1):
                addElement(i+x1,j+y1,k+z1,e)
            

 

def printScreen():
    global cam1
    screenString=""
    startTime=time.time()
    for i in range(cam1.resolution[1]):
        for j in range(cam1.resolution[0]):
            

            screenString+=dictionary[cam1.screen[i][j]]
        screenString+="\n"
    print(screenString)
    endTime=time.time()
    deltaTime=endTime-startTime
    print("Time took to concat the strings is: "+str(deltaTime))


addCube(0,20,3,3,5,5,1)
addCube(0,20,4,4,2,2,1)
addCube(0,20,4,4,8,8,1)
addElement(5,6,5,1)
cam1.updateWorld(world)
cam1.updateRayMap(rayMap)
cam1.renderScreen()

printScreen()


a=input("Press enter to start looping:")
i=1

#TODO add a buffer/optimize to make this run in real time


while True:
    


    """addElement(i-1,5,5,0)
    addElement(i,5,5,1)

    addElement(i-1,3,5,0)
    addElement(i,3,5,1)

    addElement(i-1,7,5,0)
    addElement(i,7,5,1)

    addElement(i-1,5,7,0)
    addElement(i,5,7,1)

    addElement(i-1,5,3,0)
    addElement(i,5,3,1)"""



    
    cam1.updateWorld(world)
    cam1.updateRayMap(rayMap)
    cam1.renderScreen()
    printScreen()
    #cam1.coordinates[0]+=1
    cam1.baseRotation[0]-=1

    i+=1

            



    