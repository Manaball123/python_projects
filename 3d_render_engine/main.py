#imagine uing libs ewwww
#heres how its gonna go down
#rendering engine first
#yay ik how to make stuff render now
#... i think

import math
import numpy as np
limitx=119
limity=30
limitz=64
worldx=32
worldy=32
worldz=8
screen=np.array([[" "]*limity]*limitx)
world=np.array([[[0]*worldz]*worldy]*worldx)
#field of view. this determines scale
fovx=100
fovy=120
ox=worldx/2
oy=worldy/2
oz=0

def translateNumToStr(num):
        if num == 0:
          return(" ")
        elif num == 1:
            return("█")
   

def createCol(y):
        j=0
        out_str=""
        for j in range(limitx):
                
                out_str=out_str+screen[j][y]
                
                j=j+1
        return out_str



def printScreen():
        global screen
        i=0
        output_str=""
        for i in range(limity):
            
            output_str=output_str+createCol(i)
            output_str=output_str+("\n")
            
            i=i+1
        print(output_str)
            
def addPixel(x,y,n):
    global screen
    screen[x][y]=n
    
def addElement(x,y,z,n):
    global world
    world[x][y][z]=n

def createObject(p1,p2,p3,p4,p5,p6,p7,p8):
    pass 
#ADD THIS ASAP


#get a pixel's location on screen from its geometric location
def calcPixel(px,py,pz):
    pos=np.array([0]*2)
    ang=np.array([0.0]*2)
    dx=abs(ox-px)
    dy=abs(oy-py)
    #x/z ratio
    pz=pz+1
    ang[0]=math.degrees(math.atan(dx/pz))
    #y/z
    ang[1]=math.degrees(math.atan(dy/pz))
    #check if location exceeds FOV
    if ang[0]<=fovx and ang[1]<=fovy:
        pos[0]=round(ang[0]/fovx*limitx)
        pos[1]=round(ang[1]/fovy*limity)
    return pos

   

    
#Optimize this by removing unneessasary components(don't calculate places that can't be seen)
def RenderScreen():
    
    k=worldz-1
    while k>=0:
        i=0
        for i in range(worldx):
            j=0
            for j in range(worldy):
                pixelType=world[i][j][k]
                
                if pixelType==1:
                    pos=calcPixel(i,j,k)
                    addPixel(pos[0],pos[1],"█")
                    
                    
        k=k-1
    

            
quitprogram=False
addElement(10,15,1,1)
addElement(11,15,1,1)
addElement(12,15,1,1)
addElement(13,15,1,1)
addElement(14,16,1,1)
addElement(15,16,1,1)
addElement(16,16,1,1)

addElement(10,10,1,1)
addElement(11,11,1,1)
addElement(12,12,1,1)
addElement(13,13,1,1)
addElement(14,14,1,1)
addElement(15,15,1,1)
addElement(16,16,1,1)

#print("Starting Calibration:")


while quitprogram==False:
    RenderScreen()
    printScreen()
    







