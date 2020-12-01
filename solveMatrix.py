import numpy as np

A = [[1,2], [7,8]]
B = [[7,4], [8,5]]

sol = np.linalg.solve(A,B)
print(sol)

# a = 1 if (2 < 0) else 0
# print (a)