# dataInput = int(input("Masukan Angka = "))

# hasil =  10/dataInput

# print(hasil)

# file = open("day10/exception/data2.txt","r")

# exception akan terjadi saat program mengalami error saat runtime
from math import nan

# contoh sederhana
# dataInput = int(input("Masukan Angka = "))
# hasil = nan
# try:
#     hasil = 10/dataInput
# except:
#     print("Input Tidak Boleh 0")


# print(f"Hasil = {hasil}")


# contoh diaplikasi

while True:
    dataInput = int(input("Masukan Angka = "))
    hasil = nan
    try:
        hasil = 10/dataInput
        print(f"Hasil = {hasil}")
        isDone = input("Lanjutkan (y/n)? ")
        if isDone == "n":
            break
    except:
        print("Input Tidak Boleh 0")

print("Akhir dari program")

try:
    with open("day10/exception/data.txt","r") as file:
        print(file.read())
except:
    print("data.txt tidak ditemukan akan dibuat baru")
    with open("day10/exception/data.txt","w") as file:
        file.write("File Baru")

print("Akhir dari program")