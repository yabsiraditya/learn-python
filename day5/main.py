# Latihan Perulangan 

sisi = 11

# 1. menggunakan For

# dummy varibale
print("Menggunakan For")
count = 1
for i in range(sisi):
    print("+"*count)
    count += 1

print("Akhir Program\n")


# 2. menggunakan While
print("Menggunakan While")
count = 1
while True:
    print("+"*count)
    count += 1

    if count > sisi:
        break

print("Akhir Program\n")


# 3. Hanya Ganjil Saja
print("Menggunakan While")
count = 1
while True:
    if count%2:
        print("+"*count)
        count += 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("Akhir Program\n")


# 3. Hanya Ganjil Saja Segitiga
print("Menggunakan While")
count = 1
spasi = int(sisi/2)
while True:
    if count%2:
        print(" "*spasi,"+"*count)
        count += 1
        spasi -= 1
    else:
        count += 1
        continue

    if count > sisi:
        break

print("Akhir Program\n")


# Looping Ketupat
print("Looping Ketupat For")
for i in range(0, 11):
    print(" "*(11-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()
for i in range(11, 0, -1):
    print(" "*(11-i), end='')
    for x in range(i):
        print("+ ", end='')
    print()