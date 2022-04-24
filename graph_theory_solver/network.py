
import numpy as np



class vertex:
    def __init__(self):
        #initialize connections
        self.connections = []
    

    
    



    


class network:
    def __init__(self,vertices):
        self.vertices = []
        for i in range(vertices):
            self.vertices.append(vertex())
        self.vertices = np.array(self.vertices)
    
    def FindConnectionsTo(self, origin, step_size):
        """
        Finds all unique connections from a certain point
        origin: index of the point to originate from
        step_size: the number of steps to arrive a certain point
        
        """
        pass

    

    def FindConnections(self, origin, max_layer, current_layer = 0):
        #Only executes if max recursion layer isnt reached
        if(current_layer < max_layer - 1):
            ctr = 0
            for i in range(len(self.vertices[origin].connections)):
                ctr += self.FindConnections(self.vertices[origin].connections[i], max_layer, current_layer + 1)
            return ctr
        else:
            return len(self.vertices[origin].connections)
    
    def FindTotalConnections(self,max_layer):
        ctr = 0

        for i in range(len(self.vertices)):
            ctr += self.FindConnections(i, max_layer)
        return ctr
            


            
