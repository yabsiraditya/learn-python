# Global dan Local Scope

# Variabel Global Scope 

namaGlobal = "otong" # <- variabel global

def fungsi1():
    print(f"fungsi menampilkan {namaGlobal}")

fungsi1()

# Variable Global Dalam Loop
for i in range(0,5):
    i += 1
    print(f"Loop {i} - {namaGlobal}")

# Percabangan 
if True:
    print(f"IF Menampilkan {namaGlobal}")


# Variabel Local Scope
def fungsi2():
    namaLocal = "Ucup"

fungsi2()
# print(namaLocal) Tidak bisa dipanggil

# contoh 1 penggunaan akses variable
def sayHi():
    print(f"Hai, {nama}")

nama = "Budi"
sayHi()

# contoh 2 merubah variabel global
angka = 0
nama = "Asep"

def ubah(angkaBaru,namaBaru):
    global angka
    global nama

    angka = angkaBaru
    nama = namaBaru

print(f"Sebelum {angka,nama}")
ubah(19,"Yono")
print(f"Sebelum {angka,nama}")

# contoh 3 
angka = 0

for i in range(0,5):
    angka += i
    angkaDummy = 0

print(angka)
print(angkaDummy)

if True:
    angka = 5
    angkaDummy = 10

print(angka)
print(angkaDummy)