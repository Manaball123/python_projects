
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
    
    

    

    def FindConnections(self, origin, max_depth, current_depth = 0):
        #Only executes if max recursion layer isnt reached
        if(current_depth < max_depth - 1):
            ctr = 0
            for i in range(len(self.vertices[origin].connections)):
                ctr += self.FindConnections(self.vertices[origin].connections[i], max_depth, current_depth + 1)
            return ctr
        else:
            return len(self.vertices[origin].connections)
    
    def FindConnectionsTo(self, origin, target, max_depth, current_depth = 0):

        if(current_depth == max_depth):
            if(origin == target):
                return 1
            else:
                return 0
        else:
            for i in range(len(self.vertices[origin].connections)):
                ctr += self.FindConnectionsTo(self.vertices[origin].connections[i], max_depth, current_depth + 1)
                
        return ctr

            

        
    
    def FindTotalConnections(self,max_depth):
        ctr = 0

        for i in range(len(self.vertices)):
            ctr += self.FindConnections(i, max_depth)
        return ctr
            


            
