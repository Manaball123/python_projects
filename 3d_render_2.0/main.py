
import numpy as np
import renderlib as render


camcoords = [0,0,0]
camrotation = [0,90]
camfov = [120,90]
#camRes=np.array([200,70])
#camRes=np.array([64,32])
camRes=np.array([20,10])
elements = {
    0: " ",
    1: "█",
}
cam1 = render.camera(camcoords,camrotation,camfov,camRes,elements)


cam1.printScreen()
p1 = np.array([2,1,2])
p2 = np.array([2,1,3])

p1c = cam1.worldToScreen(p1)
p2c = cam1.worldToScreen(p2)

p1c = np.array([1,1])
p2c = np.array([20,10])

cam1.drawLine(p1c,p2c,1)

print("line drew")
cam1.printScreen()

