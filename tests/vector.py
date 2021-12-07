import numpy as np

def vectorAdd(v1,v2):
    return v1+v2

def vectorSubtract(v1,v2):
    return v1-v2

def vectorLength(v1):
    return (v1[0]**2+v1[1]**2+v1[2]**2)**(1/2)

def dotProduct(v1,v2):
    return v1[0]*v2[0]+v1[1]*v2[1]+v1[2]*v2[2]

def getDist(v1,v2):
    dot=dotProduct(v1,v2)
    length1=vectorLength(v1)
    length2=vectorLength(v2)
    side=dot/length1
    return (length2**2-side**2)**(1/2)
    

vector1=np.array([5,5,0])
vector2=np.array([-4,5,0])

print(dotProduct(vector1,vector2))
print(getDist(vector1,vector2))







