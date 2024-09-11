data_0 = [1,2]
data_1 = [3,4]

data_list_biasa = [1,2,3,4]

print(f"List Biasa = {data_list_biasa}")

list_2d = [data_0,data_1,7,1]
print(f"List 2D = {list_2d}")

# Contoh penggunaan nested list
peserta_0 = ["Ucup Bengkel", 10, "Laki-Laki"]
peserta_1 = ["Siti Kue", 11, "Perempuan"]
peserta_2 = ["Asep Kusen", 12, "Laki-Laki"]

list_peserta = [peserta_0,peserta_1,peserta_2]

print(f"Peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"Nama\t: {peserta[0]}")
    print(f"Umur\t: {peserta[1]}")
    print(f"Gender\t: {peserta[2]}\n")


# Permasalahan dengan reference
list_copy = list_peserta.copy()

print(f"Peserta Copy = {list_copy}")

peserta_0[0] = "Michael"

print(f"Peserta = {list_copy}")
print(f"Peserta = {list_peserta}")