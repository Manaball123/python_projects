import random
from time import time
import numpy as np


real_names = "real_names.txt"
real_names_num = 18239
igns = "igns.txt"
igns_num = 1182

rn_elements = []
ign_elements = []

out = "out.txt"

email_suffixes = np.array([
    "@mail.com",
    "@gmail.com",
    "@outlook.com",
    "@hotmail.com",
    "@yahoo.com",
    "@icloud.com",
])

pw_suffixes = np.array([
    "!",
    "_",
    "$",

])

def LoadNames():
        global rn_elements
        global ign_elements
        with open(real_names,"r") as rn:
            for i in range(real_names_num):

                rn_elements.append(rn.readline().strip())

        with open(igns,"r") as ig:
            for i in range(igns_num):

                ign_elements.append(ig.readline().strip())
            
        rn_elements = np.array(rn_elements)
        ign_elements = np.array(ign_elements)


def GenNames(num, mode):

    global out
    global rn_elements
    global ign_elements
    global email_suffixes
    out_elements = [""] * num
    #names only

    if(mode == 0):
        pass
    #email-pw 
    elif(mode == 1):
        pass
    
    #username-email-pw
    elif(mode == 2):
        
        for i in range(num):
            un = rn_elements[random.randint(0, real_names_num) - 1] + ign_elements[random.randint(0, igns_num) - 1] + str(random.randint(0, 1000))
            if(len(un) > 16):
                un_old = un
                un = ""
                for j in range(15):
                    un += un_old[j]
            
            res = un + " | " + un + email_suffixes[random.randint(0, len(email_suffixes) - 1)] + " | " + rn_elements[random.randint(0, real_names_num) - 1] + str(random.randint(0, 1000)) + pw_suffixes[random.randint(0, len(pw_suffixes) - 1)]
            out_elements[i] = res
    out_elements = np.array(out_elements)

    with open(out, "w") as o:
        
        for i in range(num):
            o.write(out_elements[i] + "\n")
        

start = time()

LoadNames()

GenNames(65536,2)


end = time()

print("Time taken: ")
print(end - start)


            









