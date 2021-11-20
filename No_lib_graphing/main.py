import numpy as np
import graph
width=300
height=80

quitprogram=True

screen=graph.graph(width,height,0.1,0.1)

def FUNCTION(x):
    output=0
    #PUT UR FUNCTION HERE
    output=2**x
    #END
    return(output)
    
screen.drawAxis()


i=-150
while i<=150:
    if i!=0:
        screen.dataToCoords(i,FUNCTION(i))
    i+=0.001

print(screen.getGraph())
a=input()









    
