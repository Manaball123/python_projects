import numpy as np

#TODO: implement sequence check
#implement evolver
#make it work



class network:
    def __init__(self, neurons, inputs, hiddens, memory, outputs, connections):
        """
        neurons: total number of neurons
        inputs: number of input neurons(should be read-only by the network)
        hiddens: number of hidden neurons aka ones that do stuff
        memory: number of neurons that have non-volatile memories(everything else resets to 0)
        outputs: number of output neurons
        connections: number of conenctions
        """
        self.maxNeurons = neurons
        self.maxConnections = connections
        self.neurons = np.array([0.0] * neurons)
        self.inputRange = inputs - 1
        self.hiddenRange = self.inputRange + hiddens
        self.memoryRange = self.hiddenRange + memory
        self.outputRange = self.memoryRange + outputs
        self.fromAddrs = np.array([0] * connections)
        self.toAddrs = np.array([0] * connections)
        self.weights = np.array([0] * connections)

    
    def propagate(self):
        for i in range(self.maxConnections):
            fromAddr = self.fromAddrs[i]
            toAddr = self.toAddrs[i]
            
            #if not reading  write only or writing read only
            if(fromAddr <= self.memoryRange and toAddr > self.inputRange):
                self.neurons[toAddr] += self.neurons[fromAddr] * self.weights[i]


    def reset(self):
        for i in range(len(self.neurons)):
            if(i <= self.hiddenRange or i > self.memoryRange):
                self.neurons[i] = 0.0

    def clearAll(self):
        self.neurons = np.array([0.0] * self.maxNeurons)

    def getOutput(self):
        
