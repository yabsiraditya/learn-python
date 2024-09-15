'''Fungsi Dengan Argument (Input)'''

def helloWorld(name):
    # Badan Fungsi
    print(f"Hello World {name}")
    
helloWorld("Samlong")
helloWorld("Asep")


# Program Tambah 
def tambah(angka1,angka2):
    hasil = angka1 + angka2
    print(f"{angka1} + {angka2} = {hasil}")

tambah(1,2)
tambah(1,5)


def sayHi(peserta):
    dataPeserta = peserta.copy()
    for liPeserta in dataPeserta:
        print(f"Yang Terhormat {liPeserta}")

anggotPeserta = ["Ucup","Otong","Saipul"]

sayHi(anggotPeserta)