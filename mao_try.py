import numpy as np
import  scipy.sparse as sp

a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[1,9], [3,9]])

c = sp.vstack((a,b))
print(c)
d = c.tolil()
print(d)

a[1,:]=100
print(a)
