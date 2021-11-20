
import numpy as np
import neuralLib as ai
import copy

#simple training data: XOR gate
#I I O
#0 0 0
#1 0 1
#0 1 1
#1 1 1

sizes=[2,1]

network=ai.network(sizes)

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


log=True
debug=True
totalCost=0
prevAvg=2147483647
learningRate=1


network.initweights(1)

counter=0
while counter<=10000000:
    counter+=1
    averageCost=0
    totalCost=0
    print("================================================================STARTING SESSION "+str(counter)+"================================================================")
    network.resetDerivatives()
    for i in range(len(data)):
        
        network.neurons[0]=data[i]
        network.activate()
        currentCost=network.getCost(ans[i])

        if log==True:
            print("--------------------------------Trial "+str(i)+": --------------------------------")
            print("input layer: ")
            print(network.neurons[0])
            print("The output is: "+str(network.neurons[1]))
            print("The correct answer is: "+str(ans[i][0]))
            print("The cost is therefore "+str(currentCost))

        network.getDerivatives(ans[i])

        if debug==True:
            print("Weights are currently:")
            print(network.weights)
            print("derivatives are currently:")
            print(network.derivatives)

        totalCost+=currentCost
    
    print("================================================================END OF SESSION================================================================")
    network.clampDerivatives(4)
    print("derivatives are currently:")
    print(network.derivatives)
    
    averageCost=totalCost/4

    print("The average cost for this session is: "+str(averageCost))
    print("The average cost in the previous trial is: "+str(prevAvg))
    
    #backs up weights, and tweaks them, if the current iteration is better than previous
    if prevAvg<averageCost:
        
        #if current weights are less ideal than previous
        print("Restoring previous backup since average cost increased")
        network.load()
        

    else:
        
        #backs up weights first
        print("Backing up weights")
        network.save()
        
        #tweaks the weights according to the derivatives(can lead toward more total cost, which is what the backup is for)
        network.tweakWeights(learningRate)
        
        print("Weights after tweak are currently:")
        print(network.weights)
        
        #saves the average cost for comparison in the next trial
        
        prevAvg=averageCost
        
    a=input()
    
        






