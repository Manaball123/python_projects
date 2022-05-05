from pandas import to_datetime
import gamelib as gl
import copy
import numpy as np
import threading
import random

#evaluate in a 1 dimentional situation
def Eval1D(num1, num2):
    num1_i = num1
    num2_i = num2
    while True:
        num1 = gl.Addition(num1, num2)
        if(num1 == 0):
            return 1
        num2 = gl.Addition(num1, num2)
        if(num2 == 0):
            return 2
        if(num1 == num1_i and num2_i == num2):
            return 0

#very resource intensive for more predicted steps
"""
def Eval2D(n1, n2, steps):
    tree = []
    branches_per_eval = len(n1) * len(n2)
    i = 0
    #initial evaluation(none)
    tree.append(np.array[n1, n2])
    i += 1
    while i <= steps:
        curr_iter = np.array([[0,0],[0,0]] * (branches_per_eval ** i))
        for i in range(len(curr_iter)):
"""

#generates a game matrix based on game instance
#example: each player has 2 numbers, 3 players
# x-number    0 1 
# y-player  0 A B  
#           1 C D 
#           2 E F

#array:[
#    [A, B],
#    [C, D],
#    [E, F],
# ]
class Step:
    def __init__(self, self_index, to, target_index, curr_gm):
        self.self_index = self_index     #index of self
        self.to = to                     #
        self.target_index = target_index #target number index
        self.curr_gm = curr_gm           #current game matrix

def PrintSteps(steps_arr, game_inst):
    for i in range(len(steps_arr)):
        print("Player " + str(i % game_inst.players_count) + " Used the number at its " + str(steps_arr[i].self_index) + " index, against Player " + str(steps_arr[i].to) + "'s number " + str(steps_arr[i].target_index))
        print("The current game looks like this: \n" + str(steps_arr[i].curr_gm))
        


def GenerateGM(game_instance):
    matrix_lst = []
    
    for i in range(game_instance.players_count):
        plr_list = []
        for j in range(game_instance.numbers_count):
            plr_list.append(game_instance.players[i].numbers[j])
        matrix_lst.append(copy.deepcopy(plr_list))
    return np.array(matrix_lst)


G_results = []
G_ctr = 0

class Thread (threading.Thread):
   def __init__(self, threadID, name, counter, args = ()):
      threading.Thread.__init__(self)
      self.threadID = threadID
      self.name = name
      self.counter = counter
      self.args = args
   def run(self):
       Evaluate(*self.args)

def Evaluate(turn, game_instance, game_matrix, max_depth, current_depth = 0, steps = []):
    global G_results
    global G_ctr
    G_ctr += 1
    #print(game_matrix)
    #print()
    print("\nProcessing " + str(G_ctr))
    if(current_depth < max_depth):
        #iterate through all potential player choices
        for i in range(game_instance.players_count):
            #cannot add with itself
            if i != turn:
                #iterate through all avaliable to opponent number choices
                for j in range(game_instance.numbers_count):
                    #if target is nonzero
                    if(game_matrix[i][j] != 0):
                        #iterate through all from self choices
                        for k in range(game_instance.numbers_count):
                            #if self target is nonzero
                            if(game_matrix[i][k] != 0): 
                                #copy the original game matrix
                                gm = copy.deepcopy(game_matrix)
                                #make the step
                                new_steps = copy.deepcopy(steps)
                                new_steps.append(Step(k,i,j,gm))
                                gm[turn][k] = gl.Addition(gm[turn][k], gm[i][j])
                                if(gm[turn][k] == 0):
                                    
                                    ctr = 0
                                    #count sum of self player

                                    for l in range(game_instance.numbers_count):
                                        ctr += gm[turn][l]

                                    
                                    #if the player won from this
                                    if(ctr == 0):

                                        #append this to the global results
                                        G_results.append(new_steps)
                                        print("Result found at layer "+ str(current_depth))
                                #if no one won after this
                                else:
                                    #go down 
                                    
                                    if(current_depth < 4):
                                        #spawn new threads if depth is low enough
                                        tid = current_depth * 1000 + i * 100 + j * 10 + k

                                        t = Thread(tid, str(tid), tid, ((turn + 1) % game_instance.players_count, game_instance, gm, max_depth, current_depth + 1, new_steps))
                                        t.start()
                                    else:
                                    
                                        Evaluate((turn + 1) % game_instance.players_count, game_instance, gm, max_depth, current_depth + 1, new_steps)






game1 = gl.Game(2,2)

if __name__ == "__main__":
    Evaluate(0, game1,GenerateGM(game1), 8)
    print("finished")
    for i in range(len(G_results)):
        PrintSteps(G_results[i], game1)


    input()









