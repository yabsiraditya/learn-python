# Operasi Logika atau Boolean

# NOT, OR, AND, XOR(^)

# NOT
print('==== NOT ====')
a = False
c = not a

print('Data A =', a)
print('------ NOT')
print('Data C =', c)

# OR (Jika salah satu true hasilnya true)
print('==== OR ====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
print('---------------------')
a = False
b = True
c = a or b
print(a, 'OR', b, '=', c)
print('---------------------')
a = True
b = False
c = a or b
print(a, 'OR', b, '=', c)
print('---------------------')
a = True
b = True
c = a or b
print(a, 'OR', b, '=', c)

# AND (Jika salah satu false hasilnya false)
print('==== AND ====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
print('---------------------')
a = False
b = True
c = a and b
print(a, 'AND', b, '=', c)
print('---------------------')
a = True
b = False
c = a and b
print(a, 'AND', b, '=', c)
print('---------------------')
a = True
b = True
c = a and b
print(a, 'AND', b, '=', c)

# XOR (^) akan true jika salah satunya true sisanya false
print('==== XOR ====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------------')
a = False
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------------')
a = True
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
print('---------------------')
a = True
b = True
c = a ^ b
print(a, 'XOR', b, '=', c)