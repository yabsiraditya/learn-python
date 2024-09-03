# Operator Bitwise, Operasi Biner, Binary

a = 9
b = 5

# Bitwise OR (|)
c = a | b
print('===== OR =====')
print('Nilai :', a, ' Binary :', format(a,'08b'))
print('Nilai :', b, ' Binary :', format(b,'08b'))
print('-------------------------- (|)')
print('Nilai :', c, ' Binary :', format(c,'08b'))

# Bitwise AND (&)
c = a & b
print('===== AND =====')
print('Nilai :', a, ' Binary :', format(a,'08b'))
print('Nilai :', b, ' Binary :', format(b,'08b'))
print('-------------------------- (&)')
print('Nilai :', c, ' Binary :', format(c,'08b'))

# Bitwise XOR (^)
c = a ^ b
print('===== XOR =====')
print('Nilai :', a, ' Binary :', format(a,'08b'))
print('Nilai :', b, ' Binary :', format(b,'08b'))
print('-------------------------- (^)')
print('Nilai :', c, ' Binary :', format(c,'08b'))

# Bitwise NOT (~)
c = ~a
print('===== NOT =====')
print('Nilai :', a, ' Binary :', format(a,'08b'))
print('-------------------------- (~)')
print('Nilai :', c, ' Binary :', format(c,'08b'))
print('-------------------------- (^)')
d = 0b0000001001
e = 0b1111111111
print('Nilai :', e^b, ' Binary :', format(e^b,'08b'))

# Shifting

# Shift Right (>>)
c = a >> 2
print('===== >> =====')
print('Nilai :', a, ' Binary :', format(a,'08b'))
print('-------------------------- (>>)')
print('Nilai :', c, ' Binary :', format(c,'08b'))

# Shift Left (<<)
c = a << 2
print('===== << =====')
print('Nilai :', a, ' Binary :', format(a,'08b'))
print('-------------------------- (<<)')
print('Nilai :', c, ' Binary :', format(c,'08b'))

