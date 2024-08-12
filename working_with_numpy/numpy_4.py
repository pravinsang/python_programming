import numpy as np
a = np.array([[1, 2], [3, 4], [5, 6]])
b = np.array([[7, 8], [9, 10], [11, 12]])

v_stack = np.vstack((a, b))
print(v_stack)  

h_stack = np.hstack((a, b))
print(h_stack)  
print(a)
reshaped = a.reshape((2, 3))
print(reshaped)
