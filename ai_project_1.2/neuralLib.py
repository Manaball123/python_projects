
import numpy as np
import random
import copy




#####################################################CLASSES####################################################


class network:

    #CONSTANTS:
    delta=1e-8




    def __init__(self,sizes):
        """sizes: an array containing every layer's size"""
        #generates empty neurons
        self.neurons=np.empty(len(sizes),dtype=object)
        #must make one array not empty cuz of numpy weird stuff
        for i in range(len(sizes)):
            self.neurons[i]=np.array([0.0]*sizes[i])

        #generates empty weights
        self.weights=np.empty(len(sizes)-1,dtype=object)
        for i in range(len(sizes)-1):
            #what's the size of the current layer?
            fromLayer=sizes[i]
            #what's the size of the next layer?
            toLayer=sizes[i+1]
            #these are the x,y sizes of the array, respectively
            self.weights[i]=np.array([[0.0]*toLayer]*(fromLayer+1))
        
        #generates derivatives
        self.derivatives=copy.deepcopy(self.weights)
        self.backup=copy.deepcopy(self.weights)         
    
    def activate(self):
        for x in range(len(self.neurons)-1):
            for i in range(len(self.neurons[x+1])):
                result=0
                #adds the weighted sum for a SINGLE NEURON
                for j in range(len(self.neurons[x])):          
                    result+=self.weights[x][j][i]*self.neurons[x][j]
                #adds the bias, which is the last element of the array
                result+=self.weights[x][len(self.weights[x])-1][i]
                result=sigmoid(result) 
                self.neurons[x+1][i]=result
                  
    #randomizes weights
    def initweights(self,multiplier):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    self.weights[i][j][k]=sigmoid(random.randint(-2,2))*multiplier
        self.derivatives=copy.deepcopy(self.weights)

    def resetDerivatives(self):
        for i in range(len(self.derivatives)):
            for j in range(len(self.derivatives[i])):
                for k in range(len(self.derivatives[i][j])):
                    self.derivatives[i][j][k]=0.0
   
    
    def clampDerivatives(self,sampleSize):
        """gets the average of derivatives from total sample size"""
        for i in range(len(self.derivatives)):
            for j in range(len(self.derivatives[i])):
                for k in range(len(self.derivatives[i][j])):
                    self.derivatives[i][j][k]=self.derivatives[i][j][k]/sampleSize


    def tweakWeights(self,learningRate):
        #print("The weights are tweaked at this rate:")
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    #tweak weight opposite from gradient

                    self.weights[i][j][k]-=self.derivatives[i][j][k]*learningRate
                #print(-self.derivatives[i][j]*learningRate)

    #USE ONLY FOR DEBUG
    def getCost(self,answer):
        """compares the correct neural activations with the current activations(should be an array), returns a number"""
        
        result=0
        for i in range(len(answer)):
            result=result+abs(answer[i]-self.neurons[len(self.neurons)-1][i])
        return result
    
    def getDerivatives(self,answer):
        cost=0
        #gets cost of current network
        self.activate()
        for a in range(len(answer)):
            cost+=abs(answer[a]-self.neurons[len(self.neurons)-1][a])

        #tweaks every weight in order to get its derivative
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    #saves unchanged weight
                    currentWeight=self.weights[i][j][k]
                    
                    self.weights[i][j][k]+=self.delta
                    self.activate()
                    alteredCost=0
                    for l in range(len(answer)):
                        alteredCost+=abs(answer[l]-self.neurons[len(self.neurons)-1][l])
                    #gets the derivative
                    deltaCost=alteredCost-cost
                    self.derivatives[i][j][k]+=deltaCost/self.delta
                    #restores the backup
                    self.weights[i][j][k]=currentWeight
    
    def save(self):
        """backup weights"""
        self.backup=copy.deepcopy(self.weights)
    
    def load(self):
        """restores backup"""
        self.weights=copy.deepcopy(self.backup)
    
    def saveToData(self):
        """saves the current weights to data file(named weights.txt), which is a plaintext file"""
        writtenStr=""
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    writtenStr+=str(self.weights[i][j][k])
                    writtenStr+=" "
            
            writtenStr+="\n"
        
        
        with open("weights.txt","w") as weightFile:
            weightFile.write(writtenStr)
        

    def loadFromData(self):
        with open("weights.txt","r") as weightFile:
            for i in range(len(self.weights)):
                currentarray=str.split(weightFile.readline())
                index=0
                for j in range(len(self.weights[i])):
                    for k in range(len(self.weights[i][j])):
                        self.weights[i][j][k]=float(currentarray[index])
                        index+=1

            

############################################################FUNCTIONS#####################################################################
def sigmoid(x):
    return(1/(1+np.exp(-x)))




