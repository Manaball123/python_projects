import numpy as np


class screen:


    def __init__(self,w,h,dictionary):
        self.h=h
        self.w=w
        self.screen=np.array([[0]*h]*w)
        
        self.dictionary=dictionary

    def printScreen(self,doIndex):
        #print("started print")
        if doIndex:
            screenString = "    "
            for i in range(self.w):
                if(i < 10):
                    screenString += "0"
                screenString += str(i)
                screenString += "  "
            print(screenString)
        i = self.h - 1
        while i >= 0:
            screenString=""
            if doIndex:
                    if(i < 10):
                        screenString += "0"
                    screenString += str(i)
                    screenString += "  "
            
            for j in range(self.w):

                screenString += self.dictionary[self.screen[j][i]]
                screenString += "  "

            
            if doIndex:

                if(i < 10):
                    screenString += "0"
                screenString += str(i)

            screenString += "\n"
            print(screenString)
            i-=1

        if doIndex:
            screenString = "    "
            for i in range(self.w):
                if(i < 10):
                    screenString += "0"
                screenString += str(i)
                screenString += "  "
   

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





    