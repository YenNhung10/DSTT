import numpy as np
M1 = np.array([ [9, 12], [23,30] ])
u = np.array([ 2, 1]) 
tichM1u = M1.dot(u)
print(tichM1u)
np.dot(M1, u)
np.dot(u, M1)
mat1 = np.zeros( [5,5])
mat2 = np.ones( [5,5]) 
mat3 = mat1 + 2* mat2
mat4 = mat3
mat3[3][2] = 10 
mat5 = np.copy(mat3)
mat3[3][2] = 10
mat6 = np.empty([4, 5]) 
mat7 = np.identity(4) 
mat8 = np.random.random([4,5])
print(mat1)
print(mat2)
print(mat3)
print(mat4)
print(mat5)
print(mat6)
print(mat7)
print(mat8)


