import numpy as np
limitx=130
limity=30
midx=65
midy=15
scale=1
quitprogram=True
#REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
screen=np.array([["  "]*limity]*limitx)

def FUNCTION(x,y):
    output=0
    #PUT UR FUNCTION HERE
    output=x^2
    #END
    return(output)
    
def addPixel(x,y,p):
    x=round(x)
    y=round(y)
    screen[x][y]=p

def translateNumToStr(num):
        if num == 0:
          return(" ")
        elif num == 1:
            return("O")
        elif num == 2:
            return("█")

def createCol(y):
        j=0
        out_str=""
        while j<limitx:
                
                out_str=out_str+screen[j][y]
                
                j=j+1
        return out_str

def printScreen():
        global screen
        i=limity
        output_str=""
        while i>0:
            output_str=output_str+createCol(i)
            output_str=output_str+("\n")
            
            i=i-1
        print(output_str)

#len is for half scale(total size shoud be 2*len)
#ignore this ig
def screenScale():
    global limitx
    global limity
    global midx
    global midy
    midx=round(limitx/2)
    midy=round(limity/2)

def coordsToPixel(n,mode):
    #x=0,y=1
    if mode==0:
        return(n*scale+midx)
    else:
        return(n*scale+midy)
    


def updateGraph(x,z):
    addPixel(coordsToPixel(x,0),coordsToPixel(FUNCTION(x,z),1),1)
#INIT
#i dont have error handling dont b black
print("lol?")
screen[midx]=["█"]*limitx
screen[midy]=["█"]*limity
calib=True
while calib==True:
    limitx=int(input("input x size: "))
    limity=int(input("input y size: "))
    screenScale()
    screen[midx]=["█"]*limity
    screen[midy]=["█"]*limity
    printScreen()
    inp=int(input("end calibration? type 0 for no and 1 for yes "))
    if inp==1:
        calib=False
    
 


while quitprogram==False:
    
    printScreen()










    
