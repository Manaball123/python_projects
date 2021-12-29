
import numpy as np
import keyboard as key
import renderlib as render
import Vector3
import time

camcoords = [-10,5,5]
camrotation = [0,0,90]
camfov = [120,90]
#camRes=np.array([200,70])
#camRes=np.array([64,32])
camRes=np.array([128,100])
elements = {
    0: "  ",
    1: "██",
}
cam1 = render.camera(camcoords,camrotation,camfov,camRes,elements)


gridWidth = 10
gridHeight = 10
edge1Points = np.array([[0, 0, 0]] * gridWidth)
edge2Points = np.array([[0, 0, 0]] * gridHeight)
edge3Points = np.array([[0, 0, 0]] * gridWidth)
edge4Points = np.array([[0, 0, 0]] * gridHeight)
gap = 5

for i in range(gridWidth):
    edge1Points[i] = np.array([i * gap, 0, 0])
    edge3Points[i] = np.array([i * gap, 0, gridWidth * gap])

for i in range(gridHeight):
    edge2Points[i] = np.array([0, 0, i * gap])
    edge4Points[i] = np.array([gridHeight * gap, 0, i * gap])

def drawGrid():
    for i in range(gridWidth):
        point1Pos = cam1.worldToScreen(edge1Points[i])
        point2Pos = cam1.worldToScreen(edge3Points[i])
        cam1.drawLine(point1Pos, point2Pos, 1)
    
    for i in range(gridHeight):
        point1Pos = cam1.worldToScreen(edge2Points[i])
        point2Pos = cam1.worldToScreen(edge4Points[i])
        cam1.drawLine(point1Pos, point2Pos, 1)




cam1.printScreen()
p1 = np.array([10,0,0])
p2 = np.array([15,8,10])

p3 = np.array([1,0,1])
p4 = np.array([2,2,2])

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
            elif key.is_pressed("space"):
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
        cam1.renderCube(p3,p4,1)
        drawGrid()
        #cam1.drawLine([100,0],[100,20],1)
        print("position is " + str(cam1.coordinates) +" and rotation is" + str(cam1.baseRotation))
        dirvec = Vector3.ANG2VEC(cam1.baseRotation[0], cam1.baseRotation[1])

        print(str(np.round(cam1.transformMatrix,3)) + " is the matrix, its length is " + str(Vector3.VectorLength(cam1.transformMatrix[0])) + ", " + str(Vector3.VectorLength(cam1.transformMatrix[1])) + ", " + str(Vector3.VectorLength(cam1.transformMatrix[2])))
        cam1.printScreen()

    


input()
