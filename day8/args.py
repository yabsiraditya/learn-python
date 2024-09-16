'''Keywor *args'''

# Memasukan data/argument

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",180,75)

def fungsi(dataList):
    data = dataList.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi(["Budi",150,50])


# Menggukan *args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("dudung",160,56)

def tambah(*data):
    output = 0
    for angka in data:
        output += angka

    return output

hasil = tambah(1,2,3,4,5,6,7,8,9)
print(f"hasil = {hasil}")

hasil = tambah(20,5,25)
print(f"hasil = {hasil}")