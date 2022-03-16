import copy
import json
import random
import numpy as np
import math


#TODO: implement sequence check
#implement evolver
#make it work
#ALL connections IN NETWORK: 0.5n^2 - 0.5n, n being number of neurons
#conns per neuron: n-1

#CONCEPT: SIGNAL TRACING
#instead of propagating everything at once, signals are followed instead and activates "dormant" neurons


#CONCEPT1. DECENTRALIZED MONITORING
#0. MEASURE ACTIVATION A0
#1. CHANGE WEIGHT RANDOMLY
#2. MEASURE ACTIVATION A1
#3. CHANGE WEIGHT BASED ON A1-A0, PROPAGATE THROUGH "EVOLVE"  NETWORK
#4. MEASURE ACTIVATION A2
#5. CHANGE WEIGHT BASED ON A2-A1, PROPAGATE THROUGH "EVOLVE"  NETWORK
#etc etc

#pros: mimicks human brains better
#      easier to make
#      (maybe) less resource intensive

#cons: (maybe) doesn't scale well, not flexible
#      doesn't evaluate the entire network




#CONCEPT2: 


#probably will be a mess initially but MAYBE its possible to get some meaningful connection thing from it



def signal(x):
    y = 1/(1 + np.exp(-x))
    return y

class neuron:
    def __init__(self,connections,isInput = False, isOutput = False):
        self.isActive = False
        self.activeBuffer = False
        #determines if the neuron is readOnly/writeOnly
        self.isInput = isInput
        self.isOutput = isOutput
        self.activation = 0.0
        #activation written into buffer first, moves to activation after further propagation, if the neuron remains active
        self.buffer = 0.0
        
        #make connections if not out-only
        if(not isOutput):
            #addresses to output
            self.connections = connections
            self.addresses = np.array([-1] * connections)
            self.weights = np.array([np.nan] * connections)

        
        
    def InitConnections(self,genRange,inputsRange,weightRange):
        """
        genRange : max neuron index
        """
        #generate i connections
        for i in range(self.connections):
            #initialize connection address
            self.addresses[i] = random.randint(0,genRange)
            #print("attempted to use address " + str(self.addresses[i]))
            #if repeat exists, regenerate
            while(not self.CheckValid(self.addresses[i], inputsRange)):
                self.addresses[i] = random.randint(0,genRange)
                #print("already taken, regenning to" + str(self.addresses[i]))
                #print(self.addresses)
            #initialize weight
            self.weights[i] = random.uniform(-weightRange, weightRange)




                
    
    def CheckValid(self,value,inputsRange):
        #if writing to read-only neurons
        if(value <= inputsRange):
            return False

        elif(len(np.where(self.addresses == value)[0]) > 1):
                return False
        else:      
            return True
                

"""
        #if everything is initialized(in evolve sequence)
        elif(self.initRequired == None):
            if(len(np.unique(self.addresses)) != np.count(self.addresses)):
                return True
            else:
                return False
            

        #if init required
        else:
            #uninitialized addresses
            uninits = len(np.where(self.addresses == -1)[0])
            if(uninits != 0):
                #if uninits exists
                if(len(np.unique(self.addresses)) - 1 != len(self.addresses) - uninits):
                    return True
                else:
                    return False
            elif(len(np.unique(self.addresses)) != len(self.addresses)):
                return True
            else:
                return False
"""









class Network:
    def __init__(self, neurons, connections, inputs, hiddens, outputs, identifier):
        """
        neurons: total number of neurons
        inputs: number of input neurons(should be read-only by the network)
        hiddens: number of hidden neurons aka ones that do stuff
        outputs: number of output neurons
        connections: number of conenctions PER NEURON
        """
        #used to keep track of neuron save files
        self.identifier = identifier
        self.maxNeurons = neurons
        self.maxConnections = connections

       
        self.inputRange = inputs - 1
        self.hiddenRange = self.inputRange + hiddens
        self.outputRange = self.hiddenRange + outputs
        neuronsList = []
        for i in range(neurons):
            if(i <= self.inputRange):
                neuronsList.append(neuron(connections, isInput= True))
            elif(i <= self.hiddenRange):
                neuronsList.append(neuron(connections))
            else:
                neuronsList.append(neuron(connections, isOutput = True))
            
        self.neurons = np.array(neuronsList)
        del neuronsList
    
    def InitNetwork(self,weightRange):
        for i in range(len(self.neurons)):
            if(not self.neurons[i].isOutput):
                self.neurons[i].InitConnections(self.maxNeurons - 1, self.inputRange, weightRange)


    #"ticks" the network once
    def Propagate(self):

        #FIRST ITERATION: PROPAGATES NETWORK AND PUTS STUFF IN BUFFER

        #iterates through every neuron before output
        for i in range(self.outputRange - 1):
            #if neuron is active aka able to send data
            if(self.neurons[i].isActive == True):
                #if not reading write only neurons or writing read only neurons
                #deactivates the neuron, unless re-activated by other connections
                self.neurons[i].isActive = False
                #iterate through every connection
                for j in range(self.maxConnections):
                    target = self.neurons[i].addresses[j]
                    weight = self.neurons[i].weights[j]
                    self.neurons[target].activeBuffer = True
                    self.neurons[target].buffer += self.neurons[i].activation * weight

                    

        #SECOND ITERATION: MOVES STUFF OUT OF BUFFER AND RUNS THROUGH SIGNAL FUNCTION
        for i in range(self.maxNeurons):
            #if the neuron should be activated
            if(self.neurons[i].activeBuffer == True):
                self.neurons[i].activeBuffer = False
                self.neurons[i].isActive = True
                self.neurons[i].activation = signal(self.neurons[i].buffer)
            else:
                self.neurons[i].activation = 0.0
        

    def ClearAll(self):
        self.neurons = np.array([0.0] * self.maxNeurons)

    def GetOutput(self):
        pass

    #dont save too often as it is resource intensive(py array bad)
    def SaveNeurons(self):
        neuronsData = []
        config = copy.deepcopy(self.__dict__)
        del config["neurons"]
        for i in range(self.maxNeurons):
            
            neuronsData.append(copy.deepcopy(self.neurons[i].__dict__))
            if(self.neurons[i].isOutput == False):
                
                neuronsData[i]["addresses"] = self.neurons[i].addresses.tolist()
                neuronsData[i]["weights"] = self.neurons[i].weights.tolist()
        saveFile = {
            "NETWORKCFG" : config, 
            "NEURONS" : neuronsData,
        }
        with open("NETWORK_DATA_" + str(self.identifier) + ".json", "w+") as networkData:
            networkData.write(json.dumps(saveFile,indent=4, sort_keys=True, separators=(',', ': ')))

    def LoadNeurons(self):
        with open("NETWORK_DATA_" + str(self.identifier) + ".json", "r") as networkData:
            saveFile = json.loads(networkData.read())
            config = saveFile["NETWORKCFG"]
            neuronsData = saveFile["NEURONS"]
            for i in config:
                setattr(self, i, config[i])
            for i in range(self.maxNeurons):
                #load neuron attributes
                for j in neuronsData[i]:
                    setattr(self.neurons[i], j, neuronsData[i][j])

                if(neuronsData[i]["isOutput"] == False):
                    self.neurons[i].addresses = np.array(neuronsData[i]["addresses"])
                    self.neurons[i].weights = np.array(neuronsData[i]["weights"])
