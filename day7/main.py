import datetime
import os
import string
import random

# Template Dict Mahasiswa
mahasiswa_template = {
    'nama':'nama',
    'nim':'00000000',
    'sks_lulus':0,
    'lahir':datetime.datetime(1111,1,11)
}

data_mahasiswa = {}

while True:
    os.system("cls")
    # os.system("clear")
    print(f"{'Selamat Datang':^20}")
    print(f"{'Data Mahasiswa':^20}")
    print("-"*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input("Nama Mahasiswa : ")
    mahasiswa['nim'] = input("NIM Mahasiswa : ")
    mahasiswa['sks_lulus'] = input("SKS Lulus : ")
    tahunLahir = int(input("Tahun Lahir (yyyy) : "))
    bulanLahir = int(input("Bulan Lahir (1-12) : "))
    tanggalLahir = int(input("Tanggal Lahir (1-31) : "))
    mahasiswa['lahir'] = datetime.datetime(tahunLahir,bulanLahir,tanggalLahir)

    key = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({key:mahasiswa})

    print(f"{'KEY':<6} {'Nim':<12} {'Nama':<17} {'SKS':<3} {'Lahir':<10}")
    print("-"*56)
    
    for mhs in data_mahasiswa:
        key = mhs

        nama = data_mahasiswa[key]['nama']
        nim = data_mahasiswa[key]['nim']
        sks_lulus = data_mahasiswa[key]['sks_lulus']
        lahir = data_mahasiswa[key]['lahir'].strftime("%x")

        print(f"{key:<6} {nim:<12} {nama:<17} {sks_lulus:<3} {lahir:<10}")
    
    print("\n")
    isDone = input("Apakah Mau Menambah Data (y/n)? ")
    if isDone == "n":
        break

print("Program Selesai, Terima Kasih")