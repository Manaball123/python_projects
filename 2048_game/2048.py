import numpy as np
import random


gridX=int(input("Enter Grid X size: "))
gridY=int(input("Enter Grid Y size: "))
padLength=8

gameGrid=np.array([[0]*gridY]*gridX)

def printGrid():
    string=""
    string+="\n"
    i=gridY-1
    while i>=0:
        currentStr=str(i)
        length=padLength-len(currentStr)
        outputStr=" "*(length-1)+currentStr+"|"
        string+=outputStr
        
        
        for j in range(gridX):
            currentStr=str(gameGrid[j][i])
            if currentStr=="0":
                currentStr=" "

            length=padLength-len(currentStr)
            outputStr=" "*length+currentStr
            string+=outputStr
        string+="\n"
        string+=" "*(padLength-1)+"|"
        string+="\n"
        string+=" "*(padLength-1)+"|"
        string+="\n"
        i-=1
    string+=" "*(padLength-1)+"|"
    string+="\n"
    string+=" "*(padLength-1)+"|"
    string+="_"*(padLength*gridX)
    string+="\n"
    string+=" "*(padLength)
    for j in range(gridX):
            currentStr=str(j)
            length=padLength-len(currentStr)
            outputStr=" "*length+currentStr
            string+=outputStr
    print(string)
        
#4 0 0 0 0
#3 0 0 0 0
#2 0 0 0 0
#1 0 0 0 0
#  1 2 3 4

def elementShift(direction):
    """directions:
    0:up
    1:down
    2:left
    3:right"""
    if direction==0:
        #layer refers to y layer
        layer=gridY-2
        while layer>=0:
            for i in range(gridX):
                currentE=gameGrid[i][layer]
                if currentE!=0:
                    if gameGrid[i][layer+1]==0:
                    #replaces the element if empty
                        gameGrid[i][layer+1]=currentE
                    #removes the element
                        gameGrid[i][layer]=0

                    elif gameGrid[i][layer+1]==currentE:
                        #multiplies the target element by 2
                        gameGrid[i][layer+1]=currentE*2
                        #removes the current element
                        gameGrid[i][layer]=0
            layer-=1

    elif direction==1:
        #layer refers to y layer
        layer=1
        while layer<=gridY-1:
            for i in range(gridX):
                currentE=gameGrid[i][layer]
                if currentE!=0:
                    if gameGrid[i][layer-1]==0:
                    #replaces the element if empty
                        gameGrid[i][layer-1]=currentE
                    #removes the element
                        gameGrid[i][layer]=0
                    elif gameGrid[i][layer-1]==currentE:
                        #multiplies the target element by 2
                        gameGrid[i][layer-1]=currentE*2
                        #removes the current element
                        gameGrid[i][layer]=0
            layer+=1
    elif direction==2:
        #layer refers to x layer
        layer=1
        while layer<=gridX-1:
            for i in range(gridY):
                currentE=gameGrid[layer][i]
                if currentE!=0:
                    if gameGrid[layer-1][i]==0:
                    #replaces the element if empty
                        gameGrid[layer-1][i]=currentE
                    #removes the element
                        gameGrid[layer][i]=0
                    elif gameGrid[layer-1][i]==currentE:
                        #multiplies the target element by 2
                        gameGrid[layer-1][i]=currentE*2
                        #removes the current element
                        gameGrid[layer][i]=0
            layer+=1
            
    elif direction==3:
        #layer refers to x layer
        layer=gridX-2
        while layer>=0:
            for i in range(gridY):

                currentE=gameGrid[layer][i]
                if currentE!=0:
                    if gameGrid[layer+1][i]==0:
                    #replaces the element if empty
                        gameGrid[layer+1][i]=currentE
                    #removes the element
                        gameGrid[layer][i]=0
                    elif gameGrid[layer+1][i]==currentE:
                        #multiplies the target element by 2
                        gameGrid[layer+1][i]=currentE*2
                        #removes the current element
                        gameGrid[layer][i]=0
            layer-=1


def generateRandom():
    generated=False
    while generated==False:
        x=random.randint(0,gridX-1)
        y=random.randint(0,gridY-1)
        if gameGrid[x][y]==0:
            
            element=random.randint(0,1)
          
            if element==0:
                gameGrid[x][y]=2
               
            if element==1:
                gameGrid[x][y]=4
                
            
            generated=True
            break

def checkFull():
    full=True
    for i in range(gridX):
        for j in range(gridY):
            if gameGrid[i][j]==0:
                full=False
                return(full)
            
    return(full)

            
counter=0

while True:
    
    printGrid()
    print(str(counter)+" steps made")
    raw=input("Enter direction for shifting(w=up,s=down,a=left,d=right): ")
    
    if raw=="w":
        direction=0
    elif raw=="s":
        direction=1
    elif raw=="a":
        direction=2
    elif raw=="d":
        direction=3
    else:
        direction=4
    if direction==0 or 1:
        for i in range(gridY):
            elementShift(direction)
    else:
        for i in range(gridX):
            elementShift(direction)
    counter+=1
    if(checkFull())==False:
        generateRandom()

    
    





