import neuralLib as neural_network
import numpy as np
import random

sizes=np.array([20,10,5,1])
network=neural_network.network(sizes)

def genData():
    """returns array with data, in the following format:[(inputs0~19),answer]"""
    x=random.randint(1,10)
    y=random.randint(1,10)
    dataArr=np.array([0]*21)
    if x*y>=25:
        answer=1
    else:
        answer=0
    dataArr[20]=answer
    dataArr[x-1]=1
    dataArr[y+9]=1
    return(dataArr)
    

def answerConverter(answer):
    if answer==0:
        return np.array([1.0,0.0])
    else:
        return np.array([0.0,1.0])

network.initweights(1)

counter=1
sampleSize=100
data=np.array([0]*21)
learningRate=1
totalCost=0
prevAvg=2147483647
#not detailed log
log=False
#detailed log
debug=False
#summary
summary=True

#network.loadFromData()

print(network.weights)



while True:
    counter=0
    while counter<=99999:
        #resets total cost for a session
        totalCost=0
        print("================================================================STARTING SESSION "+str(counter)+"================================================================")
        seed=0
        #random.seed(seed)
        i=1
        
        network.resetDerivatives()
        """
        sampleSize=int(input("Enter Training Sample Size: "))
        learningRate=float(input("Enter Learning Rate: "))
        """
        sampleSize=50
        learningRate=1
        while i<=sampleSize:
            #generates training data
            data=genData()
            #seed=seed+1
            #random.seed(seed)
            answer=np.array([data[20]])

            #inputs the data
            for j in range(len(network.neurons[0])):
                network.neurons[0][j]=data[j]
            
            #gets output of the network
            network.activate()
            #gets cost of current sample
            currentCost=network.getCost(answer)
            #print logs
            
            
            if log==True:
                print("--------------------------------Trial "+str(i)+": --------------------------------")
                print("input layer: ")
                print(network.neurons[0])
                print("1st layer: ")
                print(network.neurons[1])
                print("2nd layer:")
                print(network.neurons[2])
                print("The output is: "+str(network.neurons[3][0]))
                print("The correct answer is: "+str(answer))
                print("The cost is therefore "+str(currentCost))
            
            
            #gets the gradient of every weight
            network.getDerivatives(answer)
            
            #prints detailed logs for every sample processed
            if debug==True:
                print("Weights are currently:")
                print(network.weights)
                print("derivatives are currently:")
                print(network.derivatives)
                
            #adds current cost to the total cost
            totalCost+=currentCost
            i+=1
            #a=input()

        #gets the average cost and clamps derivative
        averageCost=totalCost/sampleSize
        network.clampDerivatives(sampleSize)
        #prints log for current trial
        if summary==True:
            print("================================================================END OF SESSION================================================================")
            
            print("derivatives are currently:")
            print(network.derivatives)

        

        print("The average cost for this session is: "+str(averageCost))
        print("The average cost in the pervious trial is: "+str(prevAvg))
        
        #backs up weights, and tweaks them, if the current iteration is better than previous
        if prevAvg<averageCost:
            #if current weights are less ideal than previous
            print("Restoring previous backup since average cost increased")
            network.load()
        else:        
            #backs up weights first
            print("Backing up weights")
            network.save()
            network.saveToData()
            

            #tweaks the weights according to the derivatives(can lead toward more total cost, which is what the backup is for)
            network.tweakWeights(learningRate)
            if summary==True:
                print("Weights after tweak are currently:")
                print(network.weights)

            #saves the average cost for comparison in the next trial
            averageCost=totalCost/sampleSize
            prevAvg=averageCost

        counter+=1

    a=input()

