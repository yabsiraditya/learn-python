# Operasi Komparasi

# Setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

# Lebih besar dari >
print('==== Lebih besar dari (>)')
hasil = a > 3
print(a, '>', 3, '=', hasil)
hasil = b > 3
print(b, '>', 3, '=', hasil)
hasil = b > 2
print(b, '>', 2, '=', hasil) # harus lebih besar tidak boleh sama

# Kurang dari <
print('==== Kurang dari (<)')
hasil = a < 3
print(a, '<', 3, '=', hasil)
hasil = b < 3
print(b, '<', 3, '=', hasil)
hasil = b < 2
print(b, '<', 2, '=', hasil) # harus kurang dari tidak boleh sama


# Lebih dari sama dengan >=
print('==== Lebih dari sama dengan (>=)')
hasil = a >= 3
print(a, '>=', 3, '=', hasil)
hasil = b >= 3
print(b, '>=', 3, '=', hasil)
hasil = b >= 2
print(b, '>=', 2, '=', hasil)


# kurang dari sama dengan >=
print('==== Lebih dari sama dengan (<=)')
hasil = a <= 3
print(a, '<=', 3, '=', hasil)
hasil = b <= 3
print(b, '<=', 3, '=', hasil)
hasil = b <= 2
print(b, '<=', 2, '=', hasil)

# Sama dengan == 
print('==== Sama dengan (==)')
hasil = a == 4
print(a, '==', 4, hasil)

hasil = b == 4
print(b, '==', 4, hasil)

# Tidak sama dengan != 
print('==== Tidak sama dengan (!=)')
hasil = a != 4
print(a, '!=', 4, hasil)

hasil = b != 4
print(b, '!=', 4, hasil)

# 'is' sebagai komparasi objek identity
print('==== Objek identity (is)')
x = 5
y = 5

print('Nilai x =', x, 'Id =', hex(id(x)))
print('Nilai y =', y, 'Id =', hex(id(y)))

hasil = x is y
print('Nilai x is y =', hasil)

x = 5
y = 6

print('Nilai x =', x, 'Id =', hex(id(x)))
print('Nilai y =', y, 'Id =', hex(id(y)))

hasil = x is y
print('Nilai x is y =', hasil)

# 'is not' sebagai komparasi objek identity
print('==== Objek identity (is not)')
x = 5
y = 5

print('Nilai x =', x, 'Id =', hex(id(x)))
print('Nilai y =', y, 'Id =', hex(id(y)))

hasil = x is not y
print('Nilai x is not y =', hasil)

x = 5
y = 6

print('Nilai x =', x, 'Id =', hex(id(x)))
print('Nilai y =', y, 'Id =', hex(id(y)))

hasil = x is not y
print('Nilai x is not y =', hasil)