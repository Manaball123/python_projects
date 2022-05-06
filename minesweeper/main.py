import numpy as np
from msrender import screen
import random

w = 64
h = 64
max_mines = 128
mines_ctr = max_mines

game_over = False

rec_lim = 512


dict1 = {
    
    0 : "██",
    #1 : "  ",
    1 : "██",
    2 : "XX",
    3 : "??",
    10 : " 0",
    11 : " 1",
    12 : " 2",
    13 : " 3",
    14 : " 4",
    15 : " 5",
    16 : " 6",
    17 : " 7",
    18 : " 8",
    
}

world = np.array([[0]*h]*w)
screen1 = screen(w,h,dict1)
screen1.screen = world

def GenMines():
    ctr = 0
    for i in range(max_mines):
        gen = False
        while not gen:
            mx = random.randint(0, w - 1)
            my = random.randint(0, h - 1)
            if(world[mx][my] == 0):
                world[mx][my] = 1
                gen = True

def GetAdj(x,y):
    ctr = 0
    curr_x = 0
    curr_y = 0

   # print("START: x : " + str(x) + " y: " + str(y))
    for i in range(3):
        for j in range(3):
            curr_x = i + x - 1
            curr_y = j + y - 1
            #if(curr_x > 0 and curr_y > 0 and curr_x < w - 1 and curr_y < h - 1):

            #print("x : " + str(curr_x) + " y: " + str(curr_y) + " ctr: " + str(ctr))
            if(curr_x >= 0 and curr_y >= 0 and curr_x < w and curr_y < h):
                if(world[curr_x][curr_y] == 1):
                    ctr += 1
                    #print("ctr++: " + str(ctr))

    return ctr
    


def scan(x,y):
    global game_over
    if(world[x][y] == 1):
        game_over = True

    else:
        RemoveAdj(x,y)
    
def flag(x,y):
    global game_over
    if(world[x][y] == 1):
        mines_ctr -= 1
        screen1.addElement(x,y,2)

    else:
        game_over = 1



def RemoveAdj(x,y, ctr = 0):
    global screen1
    ctr += 1
    #print("x : " + str(x) + " y: " + str(y) + " ctr: " + str(ctr))
    if(world[x][y] == 0 and ctr < rec_lim):
        screen1.addElement(x,y,GetAdj(x, y) + 10)
        if(GetAdj(x, y) == 0):
            if(x > 0):
                RemoveAdj(x - 1, y, ctr)
            if(y > 0):
                RemoveAdj(x, y - 1, ctr)
            if(x < w - 1):
                RemoveAdj(x + 1, y, ctr)
            if(y < h - 1):
                RemoveAdj(x, y + 1, ctr)
   

def main():
    global game_over
    GenMines()
    
    while not game_over:
        validInp = False
        #screen1.screen = world
        
        screen1.printScreen(True)
        print(str(mines_ctr) + " Mines left")
        while not validInp:
            try:
                mode = int(input("Enter Mode(0 = scan, 1 = flag, 2 = mark): "))
                ix = int(input("Enter x: "))
                iy = int(input("Enter y: "))
                if(mode == 0):
                    scan(ix,iy)
                elif(mode == 1):
                    flag(ix,iy)
                elif(mode == 2):
                    screen1.addElement(ix, iy, 3)

                validInp = True
            except:
                print("invalid input")

    print("GAME OVER")
    input()


main()





        


















