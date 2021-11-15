import numpy as np


sub1=np.array([0])
sub2=np.array([[[1]*3]*2])
sub3=np.array([[[2]*2]*3]*1)
e=np.array([])
a1=np.array([e,e],dtype=object)

print(a1)
a1[1]=sub3
print(a1)
a1[0]=e
print(a1)
a1[0]=sub2
print(a1)