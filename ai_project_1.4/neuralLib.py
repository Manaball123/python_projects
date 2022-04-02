
import numpy as np
import random
import copy
import multiprocessing
from functools import partial


#CONSTANTS
delta=1e-5


#∂w(L)∂C0​​=a(L−1)σ′(z(L))2(a(L)−y)

############################################################FUNCTIONS#####################################################################
def Signal(x):
    return(1/(1 + np.exp(-x)))

#derivative of signal function
def DSignal(x):
    return Signal(x) * (1 - Signal(x))

def CountArray(a):
    counter = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            for k in range(len(a[i][j])):
                counter += 1
    return counter



        

def GetDerivativeOfWeight(neurons,weights,answer,cost,index):
    """
    returns the derivative of a given weight
    weights: pointer of the weights array
    neurons: pointer of the neurons array
    """
    #saves unchanged weight
    weightsCopy = copy.deepcopy(weights)
    currentWeight = weightsCopy[index[0]][index[1]][index[2]]
                    
    weightsCopy[index[0]][index[1]][index[2]] += delta
    PropagateNetwork(neurons,weightsCopy)
    alteredCost = 0
    for l in range(len(answer)):
        #proper way to get costs
        alteredCost += (answer[l] - neurons[len(neurons) - 1][l]) ** 2
        #gets the derivative
    deltaCost = alteredCost-cost
    #trashes the weights
    del weightsCopy
    #print("finished processing index: " + str(index))
    return deltaCost/delta
    
def GetDerivatives(neurons,weights,answer,poolSize):
    """returns array of derivatives"""
    cost = 0
    #gets cost of current network
    initPropResults = PropagateNetwork(neurons,weights)
    #gets the intial cost
    for a in range(len(answer)):
        cost += (answer[a] - initPropResults[a]) ** 2

    
    weightsCount = CountArray(weights)
    #iterates through every weight
    indexIterator = np.array([np.array([0,0,0])] * weightsCount)

    #print(indexIterator)
    counter = 0
    
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            for k in range(len(weights[i][j])):
                indexIterator[counter][0] = i
                indexIterator[counter][1] = j
                indexIterator[counter][2] = k

                #print("i: "+str(i)+" j: "+str(j)+" k: "+str(k))
                counter += 1
        
    #creates a partial function

    getDerivative_partial = partial(GetDerivativeOfWeight,neurons,weights,answer,cost)
    pool = multiprocessing.Pool(processes = poolSize)
    results = pool.map(getDerivative_partial, indexIterator)   
    derivatives = copy.deepcopy(weights)
    print("Finished calculating derivatives!")
    for i in range(weightsCount):
        derivatives[indexIterator[i][0]][indexIterator[i][0]][indexIterator[i][0]] = results[i]
    del results
    pool.close()
    return derivatives

    
    """
    derivatives = copy.deepcopy(weights)
    for i in range(len(weights)):
        for j in range(len(weights[i])):
            for k in range(len(weights[i][j])):
                derivatives[i][j][k] = getDerivativeOfWeight(neurons,weights,answer,cost,np.array([i,j,k]))[0]
    
    return derivatives
    """
                


#USE ONLY FOR DEBUG
def GetCost(output,answer):
    """compares the correct neural activations with the current activations(should be an array), returns a number"""
    result = 0
    for i in range(len(answer)):
        result = result + (answer[i] - output[i]) ** 2
    return result
    

#####################################################CLASSES####################################################


class Network:
    def __init__(self,sizes):
        """sizes: an array object containing every layer's size"""
        #generates empty neurons
        #DO NOT USE THIS OBJECT DIRECTLY
        self.neurons = np.empty(len(sizes), dtype = object)
        #must make one array not empty cuz of numpy weird stuff
        for i in range(len(sizes)):
            self.neurons[i] = np.array([0.0] * sizes[i])

        #generates empty weights
        self.weights = np.empty(len(sizes)-1,dtype=object)
        for i in range(len(sizes) - 1):
            #what's the size of the current layer?
            fromLayer = sizes[i]
            #what's the size of the next layer?
            toLayer = sizes[i + 1]
            #these are the x,y sizes of the array, respectively
            self.weights[i] = np.array([[0.0] * toLayer] * (fromLayer + 1))
        
        #generates derivatives

        #array of derivatives for each weight, for each cost(get average of this)
        #self.derivatives = np.array([copy.deepcopy(self.weights) * sizes[len(sizes)]])
        #average of derivatives for all weights
        self.derivatives = copy.deepcopy(self.weights)


        self.sums = copy.deepcopy(self.neurons)

        #generates backup for weights
        backup = copy.deepcopy(self.weights)

        def PropagateNetwork(self):
            """
            propagates a network, returns the cost
            """
            #iterates though every layer
            for x in range(len(self.neurons) - 1):

                #iterates though every neuron
                for i in range(len(self.neurons[x + 1])):
                    result=0
                    #adds the weighted sum for a SINGLE NEURON
                    for j in range(len(self.neurons[x])):          
                        result += self.weights[x][j][i] * self.neurons[x][j]

                    #adds the bias, which is the last element of the array
                    result += self.weights[x][len(self.weights[x])-1][i]
                    
                    #saves the un-signaled value first, useful for calculating derivatives
                    self.sums[x + 1][i] = result
                    #passes the result though a sigal function
                    result = Signal(result) 
                    #assigns the result to the next layer
                    self.neurons[x + 1][i] = result
            
            #MAY mess things up, make sure to check
            d0 = len(neuronsCopy) - 1
            output = copy.deepcopy(neuronsCopy[d0]) 
            del neuronsCopy
            return output


    def AddInputs(self,inputs):
        "returns the neurons object with added inputs"
        neuronsCopy = copy.deepcopy(self.neurons)
        for i in range(len(inputs)):
            neuronsCopy[0][i] = inputs[i]

        return neuronsCopy
                 

    #randomizes weights
    def Initweights(self,multiplier):
        "randomizes the weights"
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    self.weights[i][j][k] = Signal(random.uniform(-1,1)) * multiplier
        self.derivatives = copy.deepcopy(self.weights)

    def ResetDerivatives(self):
        """sets all derivatives to 0"""
        for i in range(len(self.derivatives)):
            for j in range(len(self.derivatives[i])):
                for k in range(len(self.derivatives[i][j])):
                    self.derivatives[i][j][k] = 0.0
   
    
    def ClampDerivatives(self,sampleSize):
        """gets the average of derivatives from total sample size"""
        for i in range(len(self.derivatives)):
            for j in range(len(self.derivatives[i])):
                for k in range(len(self.derivatives[i][j])):
                    self.derivatives[i][j][k] = self.derivatives[i][j][k]/sampleSize


    def TweakWeights(self,learningRate):
        """adjust weights based on derivatives"""
        #print("The weights are tweaked at this rate:")
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    #tweak weight opposite from gradient

                    self.weights[i][j][k] -= self.derivatives[i][j][k] * learningRate
                #print(-self.derivatives[i][j]*learningRate)

                    
    
    def Save(self):
        """backup weights"""
        self.backup = copy.deepcopy(self.weights)
    
    def Load(self):
        """restores backup"""
        self.weights = copy.deepcopy(self.backup)
    
    #cant use jsons due to np objects not being able to be converted
    def SaveToData(self,name):
        """saves the current weights to data file"""
        writtenStr=""
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    writtenStr+=str(self.weights[i][j][k])
                    writtenStr+=" "
            
            writtenStr+="\n"
        
        
        with open(name,"w") as weightFile:
            weightFile.write(writtenStr)
        

    def LoadFromData(self,name):
        """loads the data from the file to weight arrays"""
        with open(name,"r") as weightFile:
            for i in range(len(self.weights)):
                currentarray=str.split(weightFile.readline())
                index=0
                for j in range(len(self.weights[i])):
                    for k in range(len(self.weights[i][j])):
                        self.weights[i][j][k]=float(currentarray[index])
                        index+=1

            






