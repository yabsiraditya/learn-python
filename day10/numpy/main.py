import numpy as np

list_a = [1,2,3,4]
vector_a = np.array([1,2,3,4])

print(f"list a = {list_a}")
# print(f"list a = {list_a**2}") <- ini akan gagal

print(f"vector a = {vector_a}")
print(f"vector a = {vector_a**2}")

print(f"vector a = {vector_a*5}")
print(f"list a = {list_a*2}")

matrix_b = np.array([(1,2),(3,4)])
print(f"matrix b = \n{matrix_b}")
print(f"matrix b = \n{matrix_b**2}")

zeros_c = np.zeros((2,2))
print(f"zeros c = \n{zeros_c}")

ones_d = np.ones((2,2))
print(f"ones d = \n{ones_d}")

jumlah = matrix_b + matrix_b**2 + ones_d
print(f"Jumlah = \n{jumlah}")