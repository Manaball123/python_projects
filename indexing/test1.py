import hashlib
import numpy as np


a1=np.array([1,2,3])
a2=np.array([1,2,3])
hashed=hashlib.sha256()
hashed.update(a2)