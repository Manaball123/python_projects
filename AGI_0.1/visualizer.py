

import math


depth = ["  ", " .", " -", " *", " +", " M", " 0", "[[", "##", "@@", "██"]
def GetDepth(value):
    roundedVal = int(round(value * 10))
    return depth[roundedVal]

def PrintStates(networkObj, ticks, width):
    height = round((networkObj.maxNeurons - networkObj.inputRange - 1) / width)
    outStr = "--------------------------------NETWORK " + str(networkObj.identifier) + " ITERATION " + str(ticks) +": --------------------------------\n Multiply Y axis by " + str(width) + " and add X to obtain neuron index\n    "
    
    #top bar
    for i in range(width):
        outStr += " "
        if(i < 10):
            outStr += "0"
        outStr += str(i) + " "
    outStr += "\n"
    for i in range(height):
        #print axis
        if(i < 10):
            outStr += "0"
        outStr += str(i) + " "
        #print neuron depth pixels, in rows
        for j in range(width):
            outStr += GetDepth(networkObj.neurons[i * 32 + j].activation) * 2
        outStr += "\n   "
        for j in range(width):
            outStr += GetDepth(networkObj.neurons[i * 32 + j].activation) * 2

        outStr += "\n"

    print(outStr)
















