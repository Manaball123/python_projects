import random
import numpy as np
import lib as ai
import copy

#if x*y>=25
#return 1
#0 1 2 3 4 5 6 7 8 9 A
#1 O O O O O O O O O O
#2 O O O O O O O O O O
#3 O O O O O O O O I I
#4 O O O O O O I I I I
#5 O O O O I I I I I I
#6 O O O O I I I I I I
#7 O O O I I I I I I I
#8 O O O I I I I I I I
#9 O O I I I I I I I I
#A O O I I I I I I I I 

#NOW WITH CLASSES(TM)

# I1    N11      N21     O1
# I2    N12      N22     O2
#       N13      N23
#       N14      N24


#THE LAST ELEMENT IN WEIGHT ARRAY IS ALWAYS THE BIAS

n0=ai.neuron_layer(2)
n1=ai.neuron_layer(4)
n2=ai.neuron_layer(4)
n3=ai.neuron_layer(2)

w0=ai.weight_layer(2,4)
w1=ai.weight_layer(4,4)
w2=ai.weight_layer(4,2)

#backups in case total cost increased
b0=ai.weight_layer(2,4)
b1=ai.weight_layer(4,4)
b2=ai.weight_layer(4,2)


#generates training data
def genData():
    """returns array with data, in the following format:[x,y,answer]"""
    x=random.randint(1,10)
    y=random.randint(1,10)
    if x*y>=25:
        answer=1
    else:
        answer=0
    return(np.array([x,y,answer]))

#gets the output of a network
def propagate():
    n1.activate(w0.weights,n0.neurons)
    n2.activate(w1.weights,n1.neurons)
    n3.activate(w2.weights,n2.neurons)

#converts answers in 0,1 format to an array, for better comparison
def answerConverter(answer):
    if answer==0:
        return np.array([1.0,0.0])
    else:
        return np.array([0.0,1.0])

#gets the derivative of ONE WEIGHT
def getDerivative(weight,index1,index2,currentCost,answer):

    delta=0.00000001
    backup=weight[index1][index2]
    weight[index1][index2]+=delta
    #propagates the function using altered weight
    propagate()

    #gets the cost of said function
    alteredCost=ai.getCost(answer,n3.neurons)

    #gets the delta of the two costs
    deltaCost=alteredCost-currentCost

    #gets the gradient of the function, in one axis
    gradient=deltaCost/delta
    #restores the backup
    weight[index1][index2]=backup
    return(gradient)

#gets derivative of a singular weight
def deriveWeights(weightArray,derivativeArray,currentCost,answer):
    for i in range(len(weightArray)):
        for j in range(len(weightArray[i])):
            #ADDS THE GRADIENT TO AN EXISTING ONE
            derivativeArray[i][j]+=getDerivative(weightArray,i,j,currentCost,answer)

#adjusts weights according to the gradient
def tweakWeights(weightArray,derivativeArray,learningRate):
    for i in range(len(weightArray)):
        for j in range(len(weightArray[i])):
            #tweak weight opposite from gradient
            weightArray[i][j]-=derivativeArray[i][j]*learningRate







#####################################################################PROGRAM SEQUENCE#################################################################################

#initialize(randomize) weights
w0.initweights(-10,10)
w1.initweights(-10,10)
w2.initweights(-10,10)

#variable declaration
counter=1
sampleSize=0
data=0
learningRate=0
totalCost=0
prevAvg=2147483647

debug=False

while counter<=100:
    #resets total cost for a session
    totalCost=0
    print("================================================================STARTING SESSION "+str(counter)+"================================================================")
    i=1
    
    w0.resetDerivatives()
    w1.resetDerivatives()
    w2.resetDerivatives()

    
    
    #data=genData()

    sampleSize=1000
    learningRate=1
    """
    sampleSize=int(input("Enter Training Sample Size: "))
    learningRate=float(input("Enter Learning Rate: "))
    """
    while i<=sampleSize:
        #generates training data
        data=genData()
        answer=answerConverter(data[2])

        #inputs the data
        n0.neurons[0]=data[0]
        n0.neurons[1]=data[1]
        
        #gets output of the network
        propagate()
        #gets cost of current sample
        currentCost=ai.getCost(answer,n3.neurons)
        #print logs
        """
        print("--------------------------------Trial "+str(i)+": --------------------------------")
        print("input layer: ")
        print(n0.neurons)
        print("1st layer: ")
        print(n1.neurons)
        print("output layer:")
        print(n2.neurons)
        print("The output is: "+str(n3.neurons[0])+","+str(n3.neurons[1]))
        print("The correct answer is: "+str(answer[0])+","+str(answer[1]))
        print("The cost is therefore "+str(currentCost))
        """
        #gets the gradient of every weight
        deriveWeights(w0.weights,w0.derivatives,currentCost,answer)
        deriveWeights(w1.weights,w1.derivatives,currentCost,answer)
        deriveWeights(w2.weights,w2.derivatives,currentCost,answer)
        
        #prints detailed logs for every sample processed
        if debug==True:
            print("Weights are currently:")
            print(w0.weights)
            print(w1.weights)
            print(w2.weights)
            print("derivatives are currently:")
            print(w0.derivatives)
            print(w1.derivatives)
            print(w2.derivatives)
            
        #adds current cost to the total cost
        totalCost+=currentCost
    
        

       

        i+=1

    #gets the average cost 
    averageCost=totalCost/sampleSize
    #prints log for current trial
    print("================================================================END OF SESSION================================================================")
    print("derivatives are currently:")
    print(w0.derivatives)
    print(w1.derivatives)
    print(w2.derivatives)

    print("The average cost for this session is: "+str(averageCost))
    print("The average cost in the pervious trial is: "+str(prevAvg))
    
    #backs up weights, and tweaks them, if the current iteration is better than previous
    if prevAvg<averageCost:
        
        #if current weights are less ideal than previous
        print("Restoring previous backup since average cost increased")
        w0=copy.deepcopy(b0)
        w1=copy.deepcopy(b1)
        w2=copy.deepcopy(b2)


    else:
        #backs up weights first
        print("Backing up weights")
        b0=copy.deepcopy(w0)
        b1=copy.deepcopy(w1)
        b2=copy.deepcopy(w2)

        #tweaks the weights according to the derivatives(can lead toward more total cost, which is what the backup is for)
        tweakWeights(w0.weights,w0.derivatives,learningRate)
        tweakWeights(w1.weights,w1.derivatives,learningRate)
        tweakWeights(w2.weights,w2.derivatives,learningRate)
        print("Weights after tweak are currently:")
        print(w0.weights)
        print(w1.weights)
        print(w2.weights)
        #saves the average cost for comparison in the next trial
        prevAvg=averageCost



    counter+=1

a=input()






