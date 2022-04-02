import numpy as np




class vertex:
    def __init__(self):
        #initialize connections
        self.connections = np.array([])
        self.isActive = False
    


    


class network:
    def __init__(self,vertices):
        self.vertices = np.array([vertex() * vertices])
    
    def FindConnections(self, origin, step_size = None):
        """
        Finds all unique connections from a certain point
        origin: the point to originate from
        step_size: the number of steps to arrive a certain point, unspecified by default
        """
        for i in range(len(self.vertices[origin].connections)):
            
