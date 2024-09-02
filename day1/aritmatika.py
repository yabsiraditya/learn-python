# Operasi Aritmatika

a = 10
b = 3

# Operasi Tambah +
hasil = a - b
print(a, "+", b, "=", hasil)

# Operasi Kurang -
hasil = a - b
print(a, "-", b, "=", hasil)

# Operasi Kali *
hasil = a - b
print(a, "*", b, "=", hasil)

# Operasi Bagi /
hasil = a / b
print(a, "/", b, "=", hasil)

# Operasi Eksponen (Pangkat) **
hasil = a ** b
print(a, "**", b, "=", hasil)

# Operasi Modulus %
hasil = a % b
print(a, "%", b, "=", hasil)

# Operasi Floor Division //
hasil = a // b
print(a, "//", b, "=", hasil)

# Prioritas Operasi / Operational Precedence

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x

print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil)

hasil = x + y * z
print(x, '+', y, '*', z, ' =', hasil)

hasil = (x + y) * z
print('(', x, '+', y, ')', '*', z, '=', hasil)

"""
    Prioritas Operasi 
    1. ()
    2. Eksponen **
    3. Perkalian Dan Teman-Teman * / ** % //
    4. Pertambahan dan Pengurangan + -
"""