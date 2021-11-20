import numpy as np





class graph:

    dictionary = {
        0:" ",
        1:"█",
        2:"|",
        3:"-",
        4:"+"
    }

    def __init__(self,width,height,scaleX,scaleY):
        """
            width/height: self explanatorty,use odd numbers
            scaleX/Y:unit length per pixel
        """
        self.graph=np.array([[0]*height]*width)
        self.height=height
        self.width=width

        self.centerX=round(width/2)-1
        self.centerY=round(height/2)-1

        self.scaleX=scaleX
        self.scaleY=scaleY

    def drawAxis(self):
        for i in range(self.width):
            self.graph[i][self.centerY]=3
        for i in range(self.height):
            self.graph[self.centerX][i]=2
        self.graph[self.centerX][self.centerY]=4


    def dataToCoords(self,x,y):
        pixelX=round(x/self.scaleX)
        pixelY=round(y/self.scaleY)
        pixelX+=self.centerX
        pixelY+=self.centerY
        
        if pixelX<self.width and pixelX>=0 and pixelY<self.height and pixelY>=0:
            self.graph[pixelX][pixelY]=1




    def getGraph(self):
        output=""
        i=self.height-1
        while i>=0:
            for j in range(self.width):
                output+=self.dictionary[self.graph[j][i]]
            output+="\n"
            i-=1
        return(output)






    


