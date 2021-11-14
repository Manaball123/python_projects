import numpy as np
import random
layer1=np.array([0]*2)
layer2=np.array([0]*3)
layer3=np.array([0]*2)
layer1_weight=np.array([[0]*2]*3)
layer2_weight=np.array([[0]*3]*2)
layer1_bias=np.array([0]*3)
layer2_bias=np.array([0]*2)
seed=128

def sigmoid(x):
    return(1/(1+np.exp(-x)))

def initWeight():
    global layer1_weight
    global layer2_weight
    i=0
    
    while i<3:
        j=0
        while j<2:
            layer1_weight[i][j]=random.randint(-10,10)
            #seed=seed+layer1_weight[i][j]
            j=j+1
        i=i+1

    i=0
    
    while i<2:
        j=0
        while j<3:
            layer2_weight[i][j]=random.randint(-10,10)
            
            j=j+1
        i=i+1
    
def initBias():
    global layer1_bias
    global layer2_bias
    i=0
    while i<3:
       layer1_bias[i]=random.randint(-10,10)
       i=i+1

    i=0
    while i<2:
       layer2_bias[i]=random.randint(-10,10)
       i=i+1

initWeight()
initBias()
print("LAYER 1 WEIGHT")
print(layer1_weight)
print("LAYER 2 WEIGHT")
print(layer2_weight)
print("LAYER 1 BIAS")
print(layer1_bias)
print("LAYER 2 BIAS")
print(layer2_bias)

layer2[0]=layer1[0]*layer1_weight[0][0]+layer1[1]*layer1_weight[0][1]+layer1_bias[0]
layer2[1]=layer1[0]*layer1_weight[1][0]+layer1[1]*layer1_weight[1][1]+layer1_bias[0]
layer2[2]=layer1[0]*layer1_weight[2][0]+layer1[1]*layer1_weight[2][1]+layer1_bias[0]

layer3[0]=layer2[0]*layer2_weight[0][0]+layer2[1]*layer2_weight[0][1]+layer2[2]*layer2_weight[0][2]+layer2_bias[0]
layer3[1]=layer2[0]*layer2_weight[1][0]+layer2[1]*layer2_weight[1][1]+layer2[2]*layer2_weight[1][2]+layer2_bias[1]

print("LAYER 2")
print(layer2)
print("LAYER 3")
print(layer3)