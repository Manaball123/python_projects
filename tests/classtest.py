import numpy as np


class player:
    def __init__(self,x,y,z):
        
        self.coords=np.array([x,y,z])
    
    def getcoords(self):
        return self.coords
    
    def move(self,dx,dy,dz):
        self.coords=self.coords+np.array([dx,dy,dz])



p1=player(0,0,0)


print(p1.getcoords())
p1.move(3,-8,6)
print(p1.getcoords())
p1.move(-2,-1,2)
print(p1.getcoords())






    