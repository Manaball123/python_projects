import keyboard as key
import render
import numpy as np







#CONFIG
hitchance=100

#always hit head if false(awp will always baim regardless)
baim=False

#miss chance(100=always miss)(head only)
antiaim=100




class player:
  def __init__(self,x,y,weapon):
    self.x=x
    self.y=y
    self.weapon=weapon
  def move(self,axis,dir):
    #x=0 y=1
    if axis==0 and dir==0 and world[self.x-1][self.y]==0:
      self.x-=1
    elif axis==0 and dir==1 and world[self.x+1][self.y]==0:
      self.x+=1
    elif axis==1 and dir==0 and world[self.x][self.y-1]==0:
      self.y-=1
    elif axis==1 and dir==1 and world[self.x][self.y+1]==0:
      self.y+=1



      
    


    









dictionary = {

  1 : "█",
  2 : "@",
  3 : "Q",
  100: "O",
  101: "f",
  102: "i",
  103: "c",
  104: "e",

  0 : " "



}
w=200
h=53
screen=render.screen(w,h,dictionary)

world=np.array([[0]*h]*w)

def addElement(x,y,e):
  world[x][y]=e
  screen.addElement(x,y,e)


def addBlock(x1,x2,y1,y2,e):
  """adds a block to world"""
  for i in range(x2-x1+1):
    for j in range(y2-y1+1):
      addElement(i+x1,j+y1,e)



######INIT
screen.addBlock(0,w-1,0,0,1)
screen.addBlock(0,0,0,h-1,1)
screen.addBlock(w-1,w-1,0,h-1,1)
screen.addBlock(0,w-1,h-1,h-1,1)
#########################hardcoded:
midpoint=100

screen.addElement(midpoint-2,1,100)
screen.addElement(midpoint-1,1,101)
screen.addElement(midpoint,1,101)
screen.addElement(midpoint+1,1,102)
screen.addElement(midpoint+2,1,103)
screen.addElement(midpoint+3,1,104)




addBlock(3,150,50,50,1)
addBlock(3,3,16,50,1)
addBlock(3,30,16,16,1)
addBlock(30,30,16,20,1)
addBlock(30,55,20,20,1)
addBlock(55,55,3,20,1)
addBlock(55,165,3,3,1)
addBlock(17,17,16,19,1)
addBlock(17,17,23,27,1)
addBlock(17,30,27,27,1)
addBlock(30,30,25,27,1)
#addBlock(17,)

addBlock(56,70,25,27,1)



addBlock(17,30,32,35,1)


addBlock(150,150,25,50,1)
addBlock(150,170,25,25,1)




screen.printScreen()

a=input()

player1=player(50,49,1)


while True:
  
  prevX=player1.x
  prevY=player1.y
  addElement(prevX,prevY,0)

  try:
    if key.is_pressed("w"):
      player1.move(1,0)
    elif key.is_pressed("s"):
      player1.move(1,1)
    elif key.is_pressed("a"):
      player1.move(0,0)
    elif key.is_pressed("d"):
      player1.move(0,1)
  except:
    pass
  
  addElement(player1.x,player1.y,2)
  prevX=player1.x
  prevY=player1.y
  
  

  screen.printScreen()







