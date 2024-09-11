# Continue, pass, Break

# Pass -> dia berfungsi sebagai dummy, tidak akan dieksekusi

angka = 0

while angka < 5:
    angka += 1

    if angka == 3:
        pass

    print(angka)

print("Akhir Program\n")


# Continue

angka = 0
print(f"angka = {angka}")

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("Niceee")
        continue        # akan membuat loop ke step selanjutnya

    print("Wassap") # aksi 2

print("Akhir Program\n")


# Break

angka = 0

while angka < 5:
    angka += 1
    print(f"angka sekarang -> {angka}") # aksi 1

    if angka == 3:
        print("Niceee")
        break        # akan membuat loop ke step selanjutnya

    print("Wassap") # aksi 2

print("Akhir Program\n")


data_int = int(input("Hitung Sampai ="))

angka = 0

while True:
    angka += 1
    print(f"Countdown = {angka}") # aksi 1

    if angka == data_int:
        print("Niceee")
        break        # akan membuat loop ke step selanjutnya

    print("Wassap") # aksi 2

print("Akhir Program\n")