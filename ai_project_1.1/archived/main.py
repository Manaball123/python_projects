#pattern guesser thingy ig
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

#pattern looks interesting ngl
#but onto important stuff now
#traning data can be generated easily

#           NEURON PATTERN
#AX             A1               O1
#AY             A2               O2
#               A3 

#i like ascii patterns thing dont judge
import copy
import numpy as np
import random

#"generating" weights and biases by hand for now, but i SHOULD write a func to do that for me tbh
#ALSO using GENERATIONS instead of BACKPROPAGATION cuz im dumb(kinda)
#ALSO u should work on functions indead of doing shit manually
#WHO WANTS A RECODE??!?!!!!?!!?!?!

layer1=np.array([0.0]*2)
layer2=np.array([0.0]*3)
layer3=np.array([0.0]*2)

layer1_weight=np.array([[0.0]*2]*3)
layer2_weight=np.array([[0.0]*3]*2)
layer1_bias=np.array([0.0]*3)
layer2_bias=np.array([0.0]*2)
#Array backup(useless soon)
w1Copy=np.array([[0.0]*2]*3)
w2Copy=np.array([[0.0]*3]*2)
b1Copy=np.array([0.0]*3)
b2Copy=np.array([0.0]*2)
#derivatives of vars
w1d=np.array([[0.0]*2]*3)
w2d=np.array([[0.0]*3]*2)
b1d=np.array([0.0]*3)
b2d=np.array([0.0]*2)



output=0
iterationCost=0
cost=0
prevcost=2147483647
changedcost=0

def sigmoid(x):
    return(1/(1+np.exp(-x)))

def initWeight(base):
    global layer1_weight
    global layer2_weight
    i=0
    
    for i in range(3):
        j=0
        for j in range(2):
            layer1_weight[i][j]=base
            j=j+1
        i=i+1

    i=0
    
    for i in range(2):
        j=0
        for j in range(3):
            layer2_weight[i][j]=base
            j=j+1
        i=i+1

def initBias(base):
    global layer1_bias
    global layer2_bias
    i=0
    for i in range(3):
       layer1_bias[i]=base
       i=i+1
    i=0
    for i in range(2):
       layer2_bias[i]=base
       i=i+1

def tweakWeight(multiplier):
    global layer1_weight
    global layer2_weight
    i=0
    
    while i<3:
        j=0
        while j<2:
            layer1_weight[i][j]=layer1_weight[i][j]+sigmoid(random.randint(-1,1))*multiplier
            j=j+1
        i=i+1

    i=0
    
    while i<2:
        j=0
        while j<3:
            layer2_weight[i][j]=layer2_weight[i][j]+sigmoid(random.randint(-1,1))*multiplier
            j=j+1
        i=i+1

def tweakBias(multiplier):
    global layer1_bias
    global layer2_bias
    i=0
    while i<3:
       layer1_bias[i]=layer1_bias[i]+sigmoid(random.randint(-10,10))*multiplier
       i=i+1
    i=0
    while i<2:
       layer2_bias[i]=layer2_bias[i]+sigmoid(random.randint(-10,10))*multiplier
       i=i+1
#this thing is bad also
def calcActivation(i1,i2):
    global layer1
    global layer2
    global layer3
    layer1[0]=i1
    layer1[1]=i2

    
    i=0
    for i in range(3):
       layer2[i]=sigmoid(layer1[0]*layer1_weight[i][0]+layer1[1]*layer1_weight[i][1]+layer1_bias[i])
       i=i+1

    i=0
    for i in range(2):
       layer3[i]=sigmoid(layer2[0]*layer2_weight[i][0]+layer2[1]*layer2_weight[i][1]+layer2[2]*layer2_weight[i][2]+layer2_bias[i])
       i=i+1
    
    

def answerChecker(x,y):
    global iterationCost
    global cost
    if x*y>=25:
        iterationCost=costChecker(0.0,1.0)
        cost=cost+iterationCost
        return 1.0
    else:
        iterationCost=costChecker(1.0,0.0)
        cost=cost+iterationCost
        return 0.0


#if answer is 0, set a1 to 1 and vice versa
def costChecker(a1,a2):
    #print(layer3)
    #print(a1)
    val=abs(a1-layer3[0])+abs(a2-layer3[1])
    return val
    
def backup():
    print("Backing up weights...")
    global w1Copy
    global w2Copy
    global b1Copy
    global b2Copy
    global layer1_weight
    global layer2_weight
    global layer1_bias
    global layer2_bias
    w1Copy=copy.deepcopy(layer1_weight)
    w2Copy=copy.deepcopy(layer2_weight)
    b1Copy=copy.deepcopy(layer1_bias)
    b2Copy=copy.deepcopy(layer2_bias)
    print("Backup done")

def restore():
    global w1Copy
    global w2Copy
    global b1Copy
    global b2Copy
    global layer1_weight
    global layer2_weight
    global layer1_bias
    global layer2_bias
    print("Restoring previous backup since it is more optimal")
    layer1_weight=copy.deepcopy(w1Copy)
    layer2_weight=copy.deepcopy(w2Copy)
    layer1_bias=copy.deepcopy(b1Copy)
    layer2_bias=copy.deepcopy(b2Copy)
    print("Backup Restored")

def printVarInfo():
    print("Current Weights:")
    print("Layer1 Weights:")
    print(layer1_weight)
    print("Layer2 Weights:")
    print(layer2_weight)
    print("Current Biases:")
    print("Layer1 Biases:")
    print(layer1_bias)
    print("Layer2 Biases:")
    print(layer2_bias)
#this gets the derivative of a single variable, NOT an array
#derivative = output * (1.0 - output)
#For SIGMOID FUNC ONLY afaik

def deriveVar(var):
    
    iterationCost

    changedcost
    delta=iterationCost-changedcost
    return(var/delta)
#HOW TO GET PERFERABLE CHANGE 101:


#were using random methods for the time being, but we will start using backprop as soon as i knowhow to

programEnd=False
cost_depleted=False
baseWeightInput=float(input("Enter base weight: "))
baseBiasInput=float(input("Enter base bias: "))


initWeight(baseWeightInput)
initBias(baseBiasInput)

print("Neuron 1 represents output 0 and Neuron 2 represents output 1")

while programEnd==False:
    
    random.seed=(128)
    print("███████████████████████████████████████████████████████████████████████████████████████████████████████████████████████")
    print("                                                STARTING NEW SESSION")
    printVarInfo()
    print("\n \n \n \n \n")
    maxdeltaWeightInput=float(input("Enter max delta of weight tweaking: "))
    maxdeltaBiasInput=float(input("Enter max delta of bias tweaking: "))
    testCount=int(input("Enter tests done this session: "))
    i=0
    cost_depleted=False
    while cost_depleted==False:
        tweakWeight(maxdeltaWeightInput) 
        tweakBias(maxdeltaBiasInput)
        i=0
        for i in range(testCount):
            input1=random.randint(0,10)/10
            input2=random.randint(0,10)/10
            calcActivation(input1,input2)
            correct_output=answerChecker(input1,input2)
            random.seed=(str(sum(layer1)))
            print("Layer 3 activations:")
            print(layer3)
            print("Answer:")
            print(correct_output)
            print("The cost of test number "+str(i)+" is: "+str(iterationCost))
            print("The total cost is currently: "+str(cost))
            i=i+1
        cost=cost/testCount
        print("The average cost is: "+str(cost))
        print("The previous average cost is: "+str(prevcost))
        
        if cost>prevcost:
            restore()  
            print("Restarting since cost increased")
            printVarInfo()
            input("Press Enter to continue...")
            
    
        else:
            backup()
            cost_depleted=True
            prevcost=cost

    

    
    
    

    
    

    


