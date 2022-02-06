import numpy as np
import Vector3


vector1 = np.array([1,0,0])
print(Vector3.MatrixVecMultiplication(Vector3.GetRotationMatrix(90,1),vector1))