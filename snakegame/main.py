from re import L
import render
import numpy as np
import time
import keyboard as key
import random
dictionary = {
    0 : "  ",
    1 : "██",
    2 : "@@"
}

w = 71
h = 71
screen1 = render.screen(w,h,dictionary)

ticktime = 1/30
frametime = 1/30

ticktimer = time.time()
frametimer = time.time()

checkCD = 0
#ik the elifs are cancer but i aint got no switch
#its a minigame wtf do u expect

#0=up, 1=down, 2=left, 3=right
class snake:
    def __init__(self,headx,heady):
        self.headx = headx
        self.heady = heady
        self.headDirection = 0
        self.deathState = False
        self.grow = False
        self.segments = [np.array([headx,heady])]
        self.retractSnake = True
        self.length = 1
    
    #might need some sleeping for this idk
    def moveHead(self):
        try:
            if key.is_pressed("w") and self.headDirection != 1:
                self.headDirection = 0
            elif key.is_pressed("s") and self.headDirection != 0:
                self.headDirection = 1
            elif key.is_pressed("a") and self.headDirection != 3:
                self.headDirection = 2
            elif key.is_pressed("d") and self.headDirection != 2:
                self.headDirection = 3
        except:
            pass
    
    def collisionCheck(self):
        #walls
        if(self.headDirection == 0 and self.heady == h - 1):
            self.deathState = True
        elif(self.headDirection == 1 and self.heady == 0):
            self.deathState = True
        elif(self.headDirection == 2 and self.headx == 0):
            self.deathState = True
        elif(self.headDirection == 3 and self.headx == w - 1):
            self.deathState = True
        if self.length > 1:
            
            for i in range(self.length - 1):
                #print("i is")
                #print(i)
                if(self.headx == self.segments[i][0] and self.heady == self.segments[i][1]):
                    
                    self.deathState = True
                    #print(self.segments[0])
                    #print(self.segments[1])
                    #print(self.headx)
                    #print(self.heady)
        
            
        

        
    def dotCheck(self,dotx,doty):
        if(self.headDirection == 0 and self.heady == doty - 1 and self.headx == dotx):
            self.grow = True
        elif(self.headDirection == 1 and self.heady == doty + 1 and self.headx == dotx):
            self.grow = True
        elif(self.headDirection == 2 and self.headx == dotx + 1 and self.heady == doty):
            self.grow = True
        elif(self.headDirection == 3 and self.headx == dotx - 1 and self.heady == doty):
            self.grow = True

    def growSnake(self):
        if(self.grow == True):
            self.retractSnake = False
            self.grow = False
            self.length += 1

    def moveSnake(self):
        if(self.headDirection == 0):
            self.heady += 1
        elif(self.headDirection == 1):
            self.heady -= 1
        elif(self.headDirection == 2):
            self.headx -= 1
        elif(self.headDirection == 3):
            self.headx += 1

        #print(self.segments)
        #print(self.length)
        self.segments.append(np.array([self.headx,self.heady]))

        if(self.retractSnake == True):
            self.segments.pop(0)
        else:
            self.retractSnake = True
    
    def pauseCheck(self):
        global checkCD
        if(checkCD > 60):
            if(key.is_pressed("p")):
                print("GAME PAUSED")
                checkCD = 0
                time.sleep(1)
                while (key.is_pressed("p")) == False:
                    time.sleep(1)
        else:
            checkCD += 1
                


snake1 = snake(25,25)

dotx = 0
doty = 0
genDot = False



while genDot == False:
    dotx = random.randint(0,50)
    doty = random.randint(0,50)
    genDot = True
    for i in range(len(snake1.segments)):
        if(dotx == snake1.segments[i][0] or doty == snake1.segments[i][1]):

            genDot = False
            break



while snake1.deathState == False:
    
    if ticktime + ticktimer < time.time():
        
        snake1.pauseCheck()
        snake1.moveHead()

        snake1.dotCheck(dotx,doty)
        snake1.collisionCheck()
        if snake1.deathState == True:
            break
        #print(snake1.headx)
        #print(snake1.heady)
        #print(snake1.headDirection)
        #regen dot if dot eaten
        if(snake1.grow == True):
            genDot = False
            while genDot == False:
                dotx = random.randint(0,50)
                doty = random.randint(0,50)
                #print("called")
                genDot = True
                for i in range(len(snake1.segments)):
                    if(dotx == snake1.segments[i][0] or doty == snake1.segments[i][1]):
                        genDot = False
                        break
            

        snake1.growSnake()
        snake1.moveSnake()

        screen1.clear()
        for i in range(len(snake1.segments)):
            screen1.addElement(snake1.segments[i][0],snake1.segments[i][1],1)
        
        screen1.addElement(dotx,doty,2)


        ticktimer = time.time()
        #print("ticked")
        

    


    if frametime + frametimer < time.time():
        screen1.printScreen(True)
        #print("printed")
        frametimer = time.time()
        



input("GAME OVER")
