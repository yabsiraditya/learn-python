'''Latihan Fungsi'''

import os

# Program menghitung luas dan keliling persegi panjang


# Header Program 
# os.system("clear")
# print(f"{'Program Menghitung Luas':^40}")
# print(f"{'Dan Keliling Persegi Panjang':^40}")
# print(f"{'-'*40:^40}")

# # Mengambil Input User 
# lebar = int(input("Masukan Nilai Lebar : "))
# panjang = int(input("Masukan Nilai panjang : "))

# # Program Menghitung Luas
# luas = panjang*lebar
# keliling = 2*(panjang+lebar)

# # Tampilkan Hasilnya
# print(f"Hasil Dari Luas = {luas}")
# print(f"Hasil Dari Keliling = {keliling}")

def header():
    os.system("clear")
    print(f"{'Program Menghitung Luas':^40}")
    print(f"{'Dan Keliling Persegi Panjang':^40}")
    print(f"{'-'*40:^40}")

def inputUser():
    lebar = int(input("Masukan Nilai Lebar : "))
    panjang = int(input("Masukan Nilai panjang : "))

    return lebar,panjang

def hitungLuas(lebar,panjang):
    return lebar*panjang

def hitungKeliling(lebar,panjang):
    return 2*(panjang+lebar)

def display(message,value):
    print(f"Hasil Perhitungan {message} = {value}")

while True:
    header()

    opsi = int(input("Harap Pilih Opsi:\n1. Luas\n2. Keliling\n (1/2) = "))
    if opsi == 1:
        lebar,panjang = inputUser()
        luas = hitungLuas(lebar,panjang)
        display("Luas",luas)
    elif opsi == 2:
        lebar,panjang = inputUser()
        keliling = hitungKeliling(lebar,panjang)
        display("Keliling",keliling)
    else:
        print("Mohon Input Dengan Benar")

    isContinue = input("Apakan Lanjut y/n ")

    if isContinue == "n":
        break

print("Program Selesai, Terima Kasih")