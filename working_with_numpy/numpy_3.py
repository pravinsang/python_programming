import numpy as np

array = np.array([1, 2, 3, 4, '5'])
array_copy_1 = array                #shallow
array_copy_2 = array.copy()         #deep
print(array_copy_1)
print(array_copy_2)
array[2] = 20
print(array_copy_1)
print(array_copy_2)