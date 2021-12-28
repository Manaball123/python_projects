
import numpy as np
import renderlib as render


camcoords = [0,8,4]
camrotation = [0,0]
camfov = [120,90]
#camRes=np.array([200,70])
#camRes=np.array([64,32])
camRes=np.array([128,64])
elements = {
    0: "  ",
    1: "██",
}
cam1 = render.camera(camcoords,camrotation,camfov,camRes,elements)


cam1.printScreen()
p1 = np.array([10,0,2])
p2 = np.array([15,7,10])


cam1.renderCube(p1,p2)

cam1.printScreen()

input()
