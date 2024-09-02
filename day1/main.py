#  Assignment Nilai

a = 10  # Bilangan niali
y = a +29

print(a)
print("Nilai Y = ", y)
print("Nilai A = ", a)

# Penamaan
nilai_y = 15 # variabel tidak bisa spasi/strip hanya bisa underscore
juta10 = 10000000 # tidak boleh ada variabel angka di depan
nilaiZ = 17.5 

print(nilaiZ)

nilaiZ = 10
b = nilaiZ

print(nilaiZ)
print(b)


# Tipe Data di Python

# angka satuan (integer)
data_integer = 1

print("Data : ", data_integer)
print("- Bertipe : ",type(data_integer))

# angka dengan koma (Float)
data_float = 17.5

print("Data : ", data_float)
print("- Bertipe : ",type(data_float))

# kumpulan karakter (String)
data_string = "Hello Word"

print("Data : ", data_string)
print("- Bertipe : ",type(data_string))

# Tipe data biner true/false (Boolean)
data_boolean = True

print("Data : ", data_boolean)
print("- Bertipe : ",type(data_boolean))

# tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)

print("Data : ", data_complex)
print("- Bertipe : ",type(data_complex))

# tipe data dari bahasa C
from ctypes import c_double

data_c_double = c_double(10.5)

print("Data : ", data_c_double)
print("- Bertipe : ",type(data_c_double))