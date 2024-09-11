# Latihan List

list_barang = []

while True:
    print("\nMasukan Data Barang")
    nama = input("nama Barang\t = ")
    harga = int(input("Harga Barang\t = "))

    barang_masuk = [nama,harga]
    list_barang.append(barang_masuk)

    print("\n","="*10,"List Barang","="*10)
    for index,barang in enumerate(list_barang):
        print(f"{index+1} | {barang[0]} | {barang[1]}")

    print("\n","="*20)
    isLanjut = input("Apakah Ingin Lanjut? (y/n) ")

    if isLanjut == "n":
        break

print("="*10,"Program Selesai","="*10)