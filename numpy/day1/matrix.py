import numpy as np

a = np.array(([1,2],
              [3,4]))

b = np.ones([2,2])

print("Matrix A:")
print(a)
print("Matrix B:")
print(b)

# perkalian Matrix
c1 = np.dot(a,b)
c2 = a.dot(b)

print("Matrix C1:")
print(c1)
print("Matrix C2:")
print(c2)