
import numpy as np
import renderlib as render


camcoords = [0,4,4]
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
p2 = np.array([8,1,6])
p3 = np.array([6,2,2])
p4 = np.array([8,3,6])

p5 = np.array([20,1,2])
p6 = np.array([20,4,6])
p7 = np.array([20,6,2])
p8 = np.array([20,1,6])

cube1 = np.array([p1,p2,p3,p4,p5,p6,p7,p8])

cam1.renderCube(cube1)

cam1.printScreen()

input()
