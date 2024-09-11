data_0 = [1,2]
data_1 = [3,4]

data_2D = [data_0,data_1,10]
data_2D_copy = data_2D.copy()

print(f"Data = {data_2D}")
print(f"Data Copy = {data_2D_copy}")

# Mengambil dari nested list
data = data_2D[1][1]
print(f"Data = {data}")

# Semua Address
print(f"Addres Asli = {hex(id(data_2D))}")
print(f"Addres Copy = {hex(id(data_2D_copy))}")

print("Address dari member ke 1")
print(f"Addres Asli = {hex(id(data_2D[0]))}")
print(f"Addres Copy = {hex(id(data_2D_copy[0]))}")

data_2D[1][1] = 9
data_2D[2] = 5
print(f"Data = {data_2D}")
print(f"Data Copy = {data_2D_copy}")

# Menggunakan Deep Copy
from copy import deepcopy

data_2D = [data_0,data_1,10]
data_2D_deepcopy = deepcopy(data_2D)

print(f"Addres Asli = {hex(id(data_2D))}")
print(f"Addres Deep = {hex(id(data_2D_deepcopy))}")

print("Address dari member ke 1")
print(f"Addres Asli = {hex(id(data_2D[0]))}")
print(f"Addres Copy = {hex(id(data_2D_deepcopy[0]))}")

data_2D[1][1] = 30
print(f"Data = {data_2D}")
print(f"Data Copy = {data_2D_copy}")
print(f"Data Deep = {data_2D_deepcopy}")