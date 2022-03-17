#fixed "neural network"
#aka network for evolver
#only changes every generation

#inputs of 
import numpy as np
import random


#mini network managing each neuron, use this for concept 1(decentralized networking)
class learnerNetwork:
    def __init__(self,outputs):
        self.layer0 = np.array([0.0] * 2)
        self.layer1 = np.array([0.0] * outputs)
        self.weights = np.array([[0.0] * 2] * outputs)

    def initWeights(self,randRange):
        for i in range(len(self.weights)):
            for j in range(len(self.weights[i])):
                self.weights[i][j] = random.uniform(-randRange,randRange)


    #ticks the network, call when "learning" is needed(AFTER propagation is complete)
    def propagate(self):
        self.layer[0] = self.data0 
        self.layer[0] = self.data1 
        for i in range(len(self.layer1)):
            self.layer1[i] = self.layer0[0] * self.weights[i][0] + self.layer0[1] * self.weights[i][1]

    
    









