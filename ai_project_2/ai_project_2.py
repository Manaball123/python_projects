import numpy as np
import random
import json
import os
#About:simple pathfinding ai(8x8, with 64 inputs, either being 1 or 0, 1 meaning that it is blocked and 0 meaning that it isnt)
#start is at 0,0, end is at 8,8
#output would be 4, BUT it would keep outputing until goal is reached.
#2 hidden layers, both with 16 neurons
#64*16+16*16+16*4=1344weights in total(bruh)
#USING GENERATIONS TO LEARN INSTEAD
#16 MEMBERS FOR EVERY GENERATION
#EACH MEMBER HAS A SET WEIGHT, WITH EACH VARYING IN WEIGHTS
#PICK MEMBER THAT HAS THE LEAST MOVES(MOST OPTIMAL)
#BASE WEIGHTS OFF OF SAID MEMBER

#RECODING THIS USING CLASSES(based ngl)
member0=[None]*3
member1=[None]*4
member2=[None]*3
member3=[None]*3
member4=[None]*3
member5=[None]*3
member6=[None]*3
member7=[None]*3
member8=[None]*3
member9=[None]*3
member10=[None]*3
member11=[None]*3
member12=[None]*3
member13=[None]*3
member14=[None]*3
member15=[None]*3


GlobalArray=[member0,member1,member2,member3,member4,member5,member6,member7,member8,member9,member10,member11,member12,member13,member14,member15]

maze_matrix=np.array([[[0]*8]*8])
layer1=np.array([0]*16)
layer2=np.array([0]*16)

weight0=np.array([0])
weight1=np.array([0])


layer_length=16
def initweight(weight_matrix):
    i=0
    while i<=layer_length:
      j=0
      while j<=layer_length:
          weight_matrix[i][j]=random.random()



def sigmoid(x):
    return(1/(1+np.exp(-x)))



def sum(layer,weight_array):
    length=len(layer)
    i=0
    sum_array=layer*weight_array

    result=0
    while i<=length:
        result=result+sum_array[i]


def OverwriteArray(weight_array,weight_number,value):
    weight_array[weight_number]=value



def initArray(aNum,fNum):
    #GLOBALARRAY[x][y]SHOULD BE A NUMPY ARRAY
    fileName=str(fNum)
    i=0
    
    with open(fileName,"r") as f:
        #64*16weights here:
        while i<=1024:
        
            GlobalArray[aNum][1][i]=f.readline()
        #16*16weights here:
        i=0
        while i<=256:
        
            GlobalArray[aNum][2][i]=f.readline()
        #16*4weights here:
        i=0
        while i<=64:
        
            GlobalArray[aNum][3][i]=f.readline()

    

def writeArrayToFile(aNum,fNum):
    fileName=str(fNum)
    with open(fileName,"w") as f:
        i=0
        while i<=1024:
        
            f.write(str(GlobalArray[aNum][1][i])+"\n")
        #16*16weights here:
        i=0
        while i<=256:
        
            f.write(str(GlobalArray[aNum][2][i])+"\n")
        #16*4weights here:
        i=0
        while i<=64:
        
            f.write(str(GlobalArray[aNum][3][i])+"\n")
    print("write array executed")


def TweakWeights(aNum,tweakDelta):
    i=0
    while i<=1024:
        
        GlobalArray[aNum][1][i]=GlobalArray[aNum][1][i]+random.randint(-tweakDelta,tweakDelta)
        print(str(i)+"/1024")
        i=i+1
    #16*16weights here:
    i=0
    while i<=256:
        
        GlobalArray[aNum][2][i]=GlobalArray[aNum][2][i]+random.randint(-tweakDelta,tweakDelta)
        print(str(i)+"/256")
        i=i+1
    #16*4weights here:
    i=0
    while i<=64:
        
        GlobalArray[aNum][3][i]=GlobalArray[aNum][3][i]+random.randint(-tweakDelta,tweakDelta)
        print(str(i)+"/64")


    


#initializes weight array


GlobalArray[1][1]=np.array([0]*1024)
GlobalArray[1][2]=np.array([0]*256)
GlobalArray[1][3]=np.array([0]*64)

TweakWeights(1,255)
print("kek")
writeArrayToFile(1,1)




