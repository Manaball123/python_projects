
import neuralLib as neuralNetwork
import numpy as np
import random
import Vector2
import multiprocessing
import os

sizes = np.array([100,50,25,20])
network = neuralNetwork.network(sizes)

class trainingData:
    def __init__(self):
        x = random.randint(0,9)
        y = random.randint(0,9)
        coordinates = np.array([x,y])
        self.inputData = np.array([0]*100)
        for i in range(10):
            for j in range(10):
                index = i * 10 + j
                self.inputData[index] = Vector2.VectorDist(np.array([i,j]), coordinates)
    
        self.answer = np.array([0]*20)
        self.answer[x] = 1
        self.answer[10 + y] = 1
        



network.initweights(0.01)

counter = 1
sampleSize = 100

learningRate = 1
totalCost = 0
prevAvg = 2147483647
#not detailed log
log = False
#detailed log
debug = False
#summary
summary = False
totalCost = 0
poolSize = 10
subPoolSize = 10
#uncomment if you want data loaded from file
#network.loadFromData("weights.txt")
def executeTrial(i,network):
    print("--------------------------------Thread " + str(os.getpid()) + ", Trial "+str(i+1)+": -------------------------------- \n")
    data = trainingData()
    #gets output of the network
    neuralNetwork.propagateNetwork(network.neurons,network.weights)
    #gets cost of current sample
    currentCost = neuralNetwork.getCost(network.neurons,data.answer)
    #gets the gradient of every weight 
    currentDerivatives = neuralNetwork.getDerivatives(network.weights, network.neurons, data.answer, subPoolSize)
    #print logs
    
    
    """
    if log == True:
        print("--------------------------------Thread " + str(os.getpid()) + ", Trial "+str(i)+": --------------------------------")
        print("Inputs: " + str(data.inputData))
        print("Outputs: "+str())
        print("The correct answer is: " + str(data.answer))
        print("The cost is therefore " + str(currentCost))
    """
    
    #prints detailed logs for every sample processed
    """
    if debug == True:
        print("Weights are currently:")
        print(network.weights)
        print("derivatives are currently:")
        print(network.derivatives)
    """
    #returns derivatives and cost
    return [currentDerivatives,currentCost]
    

processes = []

maxProcesses = 10
if __name__ == "__main__":
    while True: 
        counter = 0
        while counter <= 99999:
            #resets total cost for a session
            totalCost=0
            print("================================================================STARTING SESSION "+str(counter)+"================================================================")
            seed = 0
            random.seed(seed)
            i = 1
            
            network.resetDerivatives()

            """
            sampleSize=int(input("Enter Training Sample Size: "))
            learningRate=float(input("Enter Learning Rate: "))
            """
            #sample size:
            sampleSize = 50
            learningRate = 1
            networkIterator = np.array([network] * sampleSize)

            iteratorObject = zip(range(sampleSize), networkIterator)
            
            neuralNetwork.propagateNetwork(network.neurons,network.weights)
            pool = multiprocessing.Pool(processes = poolSize)
            print(str((iteratorObject))
            results = pool.starmap(executeTrial, iteratorObject)
            
            for i in range(len(results)):
                network.derivatives = np.add(network.derivatives,results[i][1])
                totalCost += results[i][2]
                
                #a=input()

            #gets the average cost and clamps derivative
            averageCost = totalCost/sampleSize
            network.clampDerivatives(sampleSize)
            #prints log for current trial

            if summary == True:
                print("================================================================END OF SESSION================================================================")
                
                print("derivatives are currently:")
                print(network.derivatives)

            

            print("The average cost for this session is: " + str(averageCost))
            print("The average cost in the pervious trial is: " + str(prevAvg))
            
            #backs up weights, and tweaks them, if the current iteration is better than previous
            if prevAvg < averageCost:
                #if current weights are less ideal than previous
                print("Restoring previous backup since average cost increased")
                network.load()
            else:        
                #backs up weights first
                print("Backing up weights")
                network.save()
                network.saveToData("weights.txt")
                

                #tweaks the weights according to the derivatives(can lead toward more total cost, which is what the backup is for)
                network.tweakWeights(learningRate)
                if summary == True:
                    print("Weights after tweak are currently:")
                    print(network.weights)

                #saves the average cost for comparison in the next trial
                averageCost = totalCost/sampleSize
                prevAvg = averageCost

            counter += 1

            a=input()

