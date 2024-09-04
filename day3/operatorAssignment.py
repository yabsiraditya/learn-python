# Operasi yang dapat dilakukan dengan penyingkatan
# Opearsi ditambah dengan Assignment

a = 5 # adalah Assignment
print('nilai a =', a)

a += 1 # artinya adalah a = a + 1
print('nilai a += 1, nilai a menjadi', a)

a -= 2 # artinya adalah a = a - 2
print('nilai a -= 2, nilai a menjadi', a)

a *= 5 # artinya adalah a = a * 5
print('nilai a *= 5, nilai a menjadi', a)

a /= 2 # artinya adalah a = a / 2
print('nilai a /= 2, nilai a menjadi', a)

b = 10
print('\nnilai b =', b)

# modulus dan floor division
b %= 3
print('Nilai b %= 3, nilai b menjadi', b)

b = 10
print('\nnilai b =', b)

b //= 3
print('Nilai b //= 3, nilai b menjadi', b)

# Pangkat atau eksponen
a = 5
print('\nnilai b =', a)

a **= 3
print('Nilai a **= 3, nilai a menjadi', a)

# Operasi Bitwise
# OR
c = True
print('\nnilai c =', c)
c |= False
print('Nilai c |= False, nilai c menjadi', c)
c = False
print('nilai c =', c)
c |= False
print('Nilai c |= False, nilai c menjadi', c)

# AND
c = True
print('\nnilai c =', c)
c &= False
print('Nilai c &= False, nilai c menjadi', c)
c = True
print('nilai c =', c)
c &= True
print('Nilai c &= True, nilai c menjadi', c)

# XOR
c = True
print('\nnilai c =', c)
c ^= False
print('Nilai c ^= False, nilai c menjadi', c)
c = True
print('nilai c =', c)
c ^= True
print('Nilai c ^= True, nilai c menjadi', c)

# Geser Angka Biner
d = 0b0100
print('\nnilai d =', format(d,'04b'))

d >>= 2
print('nilai d >>= 2, nilai d menjadi', format(d,'04b'))

d <<= 1
print('nilai d <<= 1, nilai d menjadi', format(d,'04b'))