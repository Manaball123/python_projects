import copy
#scope test
l0 = ["hi","1",2]
l1 = []


for i in range(10):
    
    ltmp = []
    ltmp = copy.deepcopy(l0)

    l1.append(ltmp)

l1[1][1] = "2"
print(l1)

