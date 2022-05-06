
import neuralLib as neuralNetwork
import numpy as np
import random
import Vector2
import multiprocessing
import os
import time

sizes = np.array([25,20,15,10])
network = neuralNetwork.network(sizes)

class trainingData:
    def __init__(self):
        x = random.randint(0,4)
        y = random.randint(0,4)
        coordinates = np.array([x,y])
        self.inputData = np.array([0.0]*25)
        for i in range(5):
            for j in range(5):
                index = i * 5 + j
                self.inputData[index] = Vector2.VectorDist(np.array([i,j]), coordinates)/5
    
        self.answer = np.array([0.0]*10)
        self.answer[x] = 1.0
        self.answer[5 + y] = 1.0


network.initweights(0.01)

counter = 1
sampleSize = 100

learningRate = 1
totalCost = 0
prevAvg = 2147483647
#not detailed log
log = True
#detailed log
debug = False
#summary
summary = False
totalCost = 0
#poolSize = 20 deprecated :^(

#6 is ideal
subPoolSize = 6
#uncomment if you want data loaded from file
#network.loadFromData("weights.txt")

#NOT USING MULTITHREAIDNG FOR THIS
def executeTrial(i,network):
    #print("--------------------------------Thread " + str(os.getpid()) + ", Trial "+str(i+1)+": -------------------------------- \n")
    data = trainingData()
    
    #gets output of the network
    #print(data.inputData)
    neurons = network.addInputs(data.inputData)
    #print(neurons)
    #print(network.weights)
    output = neuralNetwork.propagateNetwork(neurons, network.weights)
    #gets cost of current sample
    currentCost = neuralNetwork.getCost(output,data.answer)
    #gets the gradient of every weight 
    currentDerivatives = neuralNetwork.getDerivatives(neurons, network.weights, data.answer, subPoolSize)
    #print("hi")
    #print("ended")
    #print logs
    
    
    
    if log == True:
        print("--------------------------------PID " + str(os.getpid()) + ", Trial "+str(i + 1)+": --------------------------------")
        print("Inputs: " + str(neurons[0]))
        print("Outputs: "+str(output))
        print("The correct answer is: " + str(data.answer))
        print("The cost is therefore " + str(currentCost))
    
    
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
maxProcesses = 16

if __name__ == "__main__":
    while True: 
        counter = 0
        while counter <= 99999:
            #resets total cost for a session
            totalCost=0
            print("================================================================STARTING SESSION "+str(counter)+"================================================================")
            startTime = time.time()
            seed = 0
            random.seed(seed)
            i = 1
            
            network.resetDerivatives()

            """
            sampleSize=int(input("Enter Training Sample Size: "))
            learningRate=float(input("Enter Learning Rate: "))
            """
            #sample size:
            sampleSize = 100
            learningRate = 1
            #networkIterator = np.array([network] * sampleSize)

            #iteratorObject = zip(range(sampleSize), networkIterator)
            for i in range(sampleSize):
                results = executeTrial(i,network)
                network.derivatives = np.add(network.derivatives,results[1])
                totalCost += results[1]
                del results
            

            #neuralNetwork.propagateNetwork(network.neurons,network.weights)
            #neuralNetwork.getDerivatives(network,[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],subPoolSize)
            #pool = multiprocessing.Pool(processes = poolSize)

            #print(str(iteratorObject))
            #results = pool.starmap(executeTrial, iteratorObject)
            
            #for i in range(len(results)):
            #    network.derivatives = np.add(network.derivatives,results[i][1])
            #    totalCost += results[i][2]
                
                #a=input()

            #gets the average cost and clamps derivative
            averageCost = totalCost/sampleSize
            network.clampDerivatives(sampleSize)
            #prints log for current trial

            if summary == True:
                print("================================================================END OF SESSION================================================================")
                
                #print("derivatives are currently:")
                #print(network.derivatives)

            endTime = time.time()
            print("Time Taken: "+ str(endTime-startTime))

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

            input()

