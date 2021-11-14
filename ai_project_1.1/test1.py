
import numpy as np
import lib as ai
import copy
import matplotlib.pyplot as plt
#simple training data: XOR gate
#I I O
#0 0 0
#1 0 1
#0 1 1
#1 1 1



n0=ai.neuron_layer(2)
n1=ai.neuron_layer(1)


w0=ai.weight_layer(2,1)
b0=ai.weight_layer(2,1)

def propagate():
    n1.activate(w0.weights,n0.neurons)


def getDerivative(weight,index1,index2,currentCost,answer):

    delta=0.00000001
    backup=weight[index1][index2]
    weight[index1][index2]+=delta
    #propagates the function using altered weight
    propagate()
    #gets the cost of said function
    alteredCost=ai.getCost(answer,n1.neurons)
    #gets the delta of the two costs
    deltaCost=alteredCost-currentCost
    #gets the gradient of the function, in one axis
    gradient=deltaCost/delta
    #restores the backup
    weight[index1][index2]=backup
    return(gradient)
    #gets derivative of a singular weight


def deriveWeights(weightArray,derivativeArray,currentCost,answer):
    for i in range(len(weightArray)):
        for j in range(len(weightArray[i])):
            #ADDS THE GRADIENT TO AN EXISTING ONE
            derivativeArray[i][j]+=getDerivative(weightArray,i,j,currentCost,answer)



data=np.array([
    [0.0,0.0],
    [1.0,0.0],
    [0.0,1.0],
    [1.0,1.0]
])

ans=np.array([
    [0],
    [1],
    [1],
    [1]
])


log=False
debug=False
totalCost=0
prevAvg=2147483647
learningRate=1

w0.initweights(-1,1)


counter=0
while counter<=10000000:
    counter+=1
    averageCost=0
    totalCost=0
    print("================================================================STARTING SESSION "+str(counter)+"================================================================")
    for i in range(len(data)):
        w0.initDerivatives()
        n0.neurons=data[i]
        propagate()
        currentCost=ai.getCost(ans[i],n1.neurons)

        if log==True:
            print("--------------------------------Trial "+str(i)+": --------------------------------")
            print("input layer: ")
            print(n0.neurons)
            print("The output is: "+str(n1.neurons[0]))
            print("The correct answer is: "+str(ans[i][0]))
            print("The cost is therefore "+str(currentCost))

        deriveWeights(w0.weights,w0.derivatives,currentCost,ans[i])

        if debug==True:
            print("Weights are currently:")
            print(w0.weights)
            print("derivatives are currently:")
            print(w0.derivatives)

        totalCost+=currentCost
    
    print("================================================================END OF SESSION================================================================")
    w0.clampDerivatives(4)
    print("derivatives are currently:")
    print(w0.derivatives)
    
    averageCost=totalCost/4

    print("The average cost for this session is: "+str(averageCost))
    print("The average cost in the previous trial is: "+str(prevAvg))
    
    #backs up weights, and tweaks them, if the current iteration is better than previous
    if prevAvg<averageCost:
        
        #if current weights are less ideal than previous
        print("Restoring previous backup since average cost increased")
        w0=copy.deepcopy(b0)
        

    else:
        
        #backs up weights first
        print("Backing up weights")
        b0=copy.deepcopy(w0)
        
        #tweaks the weights according to the derivatives(can lead toward more total cost, which is what the backup is for)
        w0.tweakWeights(learningRate)
        
        print("Weights after tweak are currently:")
        print(w0.weights)
        
        #saves the average cost for comparison in the next trial
        
        prevAvg=averageCost
        
    a=input()
    
        






