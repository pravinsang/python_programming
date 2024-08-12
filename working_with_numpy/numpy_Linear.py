'''Consider the following system of linear equations:
                    2𝑥+3𝑦=13
                    4𝑥+9𝑦=30
    A system of linear equations can be represented in matrix form as:
                    A⋅X=B'''

import numpy as np
a = np.array([[2, 3],
              [4, 9]])
b = np.array([13 , 30])
x = np.linalg.solve(a, b)
print(f'Solutions = {x}')