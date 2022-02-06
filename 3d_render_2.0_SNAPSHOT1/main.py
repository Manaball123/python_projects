
import numpy as np
import keyboard as key
import renderlib as render
import Vector3
import time

camcoords = [0,8,4]
camrotation = [0,0]
camfov = [120,90]
#camRes=np.array([200,70])
#camRes=np.array([64,32])
camRes=np.array([128,100])
elements = {
    0: "  ",
    1: "██",
}
cam1 = render.camera(camcoords,camrotation,camfov,camRes,elements)


cam1.printScreen()
p1 = np.array([10,0,2])
p2 = np.array([15,7,10])

p1t = np.array([5,4])
p2t = np.array([20,5])
p3t = np.array([20,4])
cam1.drawLine(p1t,p2t,1)
#cam1.FillFlatTriangle(p1t,p2t,p3t,1)
#cam1.renderCube(p1,p2,1)
cam1.printScreen()

speed = 0.1
sens = 1

addedRotation = np.array([1,0])


startFrameTime = time.time()
timePerFrame = 0.05

while True:
    if(time.time() > startFrameTime + timePerFrame):
        startFrameTime = time.time()
        try:
            if key.is_pressed("w"):
                cam1.coordinates[0] += speed
            elif key.is_pressed("s"):
                cam1.coordinates[0] -= speed
            elif key.is_pressed("alt"):
                cam1.coordinates[1] += speed
            elif key.is_pressed("ctrl"):
                cam1.coordinates[1] -= speed
            elif key.is_pressed("a"):
                cam1.coordinates[2] -= speed
            elif key.is_pressed("d"):
                cam1.coordinates[2] += speed

            elif key.is_pressed("j"):
                cam1.AddRotation([-sens,0])
            elif key.is_pressed("l"):
                cam1.AddRotation([sens,0])
            elif key.is_pressed("i"):
                cam1.AddRotation([0,sens])
            elif key.is_pressed("k"):
                cam1.AddRotation([0,-sens])
        except:
            pass
        cam1.getTransformMatrix()
        cam1.clearScreen()
        cam1.renderCube(p1,p2,1)
        #cam1.drawLine([100,0],[100,20],1)
        print("position is " + str(cam1.coordinates) +" and rotation is" + str(cam1.baseRotation))
        dirvec = Vector3.ANG2VEC(cam1.baseRotation[0], cam1.baseRotation[1])

        print(str(dirvec) + " is the vector, its length is " + str(Vector3.VectorLength(dirvec)))
        cam1.printScreen()

    


input()
