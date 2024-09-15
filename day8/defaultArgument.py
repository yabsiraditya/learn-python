'''Default Argument

    def fungsi(argument):
    def fungsi(argument = nilai defaultnya):
'''

# Contoh 1
def sayHello(nama = "Ganteng"):
    print(f"Hallo {nama}")

sayHello("Dudung")
sayHello()

# Contoh 2
def sapaDia(nama, pesan = "Apa kabar?"):
    print(f"Hallo {nama}, {pesan}")

sapaDia("Asep","Gimana kabarnya?")
sapaDia("Budi")

# Contoh 3
def hitungPangkat(angka,pangkat = 2):
    hasil = angka**pangkat
    return hasil

print(hitungPangkat(2,4))

hasil = hitungPangkat(pangkat=3, angka=5)
print(hasil)

# Contoh 4
def fungsi(angka1=1,angka2=2,angka3=3,angka4=4):
    hasil = angka1+angka2+angka3+angka4
    return hasil

print(fungsi())
print(fungsi(angka3=10))