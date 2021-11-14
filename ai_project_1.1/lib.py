
import numpy as np
import random


#####################################################CLASSES####################################################

class neuron_layer:

    def __init__(self,num):
        self.neurons=np.array([0.0]*num)
        

    #both w.a and p.l is an ARRAY!!!! <-important
    def activate(self,weightarray,prevlayer):
        for i in range(len(self.neurons)):
            result=0
            #adds the weighted sum for a SINGLE NEURON
            for j in range(len(prevlayer)):
                result+=weightarray[i][j]*prevlayer[j]
            
            #adds the bias, which is the last element of the array
            
            
            result+=weightarray[i][len(weightarray[i])-1]
            result=sigmoid(result) 
            self.neurons[i]=result
            

            

class weight_layer:
    #x*prev layer neurons directly

    #x=count of prev neurons
    #y=count of next neurons
    #dont change this
    def __init__(self,x,y):
        self.weights=np.array([[0.0]*(x+1)]*y)
        self.derivatives=np.array([[0.0]*(x+1)]*y)


    #randomizes weights
    def initweights(self,minnum,maxnum):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j]=sigmoid(random.randint(-5,5))*random.randint(minnum,maxnum)
   
    def initDerivatives(self):
        for i in range(len(self.derivatives)):
            for j in range(len(self.derivatives[i])):
                self.derivatives[i][j]=0.0

    def clampDerivatives(self,sampleSize):
        """gets the average of derivatives from total sample size"""
        for i in range(len(self.derivatives)):
            for j in range(len(self.derivatives[i])):
                self.derivatives[i][j]=self.derivatives[i][j]/sampleSize

    def tweakWeights(self,learningRate):
        #print("The weights are tweaked at this rate:")
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                #tweak weight opposite from gradient

                self.weights[i][j]-=self.derivatives[i][j]*learningRate
                #print(-self.derivatives[i][j]*learningRate)
            

############################################################FUNCTIONS#####################################################################
def sigmoid(x):
    return(1/(1+np.exp(-x)))

def getCost(answer,output):
    """compares the correct neural activations with the current activations(should both be arrays), returns a number"""
    result=0
    for i in range(len(answer)):
        result=result+abs(answer[i]-output[i])

    return result


#TODO: IMPORT AND EXPORT WEIGHTS

#TODO(MAYBE): MAKE ONE GIANT CLASS AND HAVE NEURONS+WEIGHTS AS SUBCLASSES



    
    




