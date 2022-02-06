import numpy as np


class screen:


    def __init__(self,w,h,dictionary):
        self.h=h
        self.w=w
        self.screen=np.array([[0]*h]*w)
        
        self.dictionary=dictionary

    def printScreen(self,doBorder):
        #print("started print")
        screenString=""
        i = self.h - 1
        while i >= 0:
            for j in range(self.w):
                screenString+=self.dictionary[self.screen[j][i]]
            if doBorder == True:
                screenString += "X"
            screenString+="\n"
            i-=1
        if doBorder == True:
            screenString += ("XX" * (self.w + 1))
        print(screenString)
        #print("ended print")

    def clear(self):
        self.screen=np.array([[0]*self.h]*self.w)

    def addElement(self,x,y,e):
        self.screen[x][y]=e

    def addBlock(self,x1,x2,y1,y2,e):
        """adds a block to world"""
        for i in range(x2-x1+1):
            for j in range(y2-y1+1):
                self.addElement(i+x1,j+y1,e)





    