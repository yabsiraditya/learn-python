data_angka = [1,4,6,8,2,4,6,2,7,8,3,5,9,6,2,3,4,5,6,8]

print(f"data angka = \n{data_angka}")


# Count Data jumlah angka pada data
jumlah_data_4 = data_angka.count(4)
jumlah_data_3 = data_angka.count(3)

print(f"Jumlah angka 4 = {jumlah_data_4}")
print(f"Jumlah angka 3 = {jumlah_data_3}")

# ambil posisi data (index)
data = ["Asep", "Ujang", "Ucup", "Dudung"]

index_dudung = data.index("Dudung")
index_asep = data.index("Asep")


print(f"index si Dudung = {index_dudung}")
print(f"index si Dudung = {index_asep}")

# mengurutkan list
print(f"data angka sebelum di sort = \n{data_angka}")
data_angka.sort()
print(f"data angka di sort = \n{data_angka}")

print(f"data = \n{data}")
data.sort()
print(f"data sort = \n{data}")

# Balik listnya
data_angka.reverse()
data.reverse()
print(f"data di reverse = \n{data_angka} \n{data}")