import numpy as np

# list python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

# list numpy
anp = np.array([1,2,3,4,5])
bnp = np.array([6,7,8,9,10])

# penjumlahan python biasa
hasil = a+b
print(hasil)

# penjumlahan ELEMENTWISE operation
hasil = anp + bnp
print(hasil)

# pengurangan 
hasil = anp - bnp
print(hasil)

# pengurangan 
hasil = anp * bnp
print(hasil)

# pembagian
hasil = anp / bnp
print(hasil)

# kuadrat
hasil = anp**2
print(hasil)


c = np.array([(1,2,3),(4,5,6)])
d = np.array([(7,8,9),(-1,-2,-3)])

hasil = c + d
print(hasil)

hasil = c * d
print(hasil)