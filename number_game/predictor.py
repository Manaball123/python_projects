import gamelib as gl
import copy
import numpy as np

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


        




        
print(Eval1D(3,5))
    














