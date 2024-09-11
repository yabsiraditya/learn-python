# Manipulasi list
data = ["Asep", "Ujang", "Ucup", "Dudung"]

# Mengambil data dari List
print(f"Data Ketiga adalah {data[1]}")
print(f"Data Terakhir adalah {data[-1]}")

# mengambil jumlah data List
panjang_data = len(data)
print(panjang_data)

# manipulasi data List

# menambahkan item pada list sesuai posisi
print(f"data sebelum ditambah = \n{data}")

# data.insert(Posisi input, Data input)
data.insert(0, "Nunung")
print(f"data sesudah ditambah = \n{data}")

# Append = Menambah data diakhir list 
data.append("Budi")
print(f"data sesudah ditambah lagi = \n{data}")

# menambahkan list dengan list extend = untuk menggabungkan list dengan list
data_baru = ["Dwi", "Andi", "Soni"]
data.extend(data_baru)
print(f"data sesudah digabungkan = \n{data}")

# merubah data dari list dengan index list
data[2] = "Michael"
print(f"data index 2 sesudah dirubah = \n{data}")

# menghapus data
# huruf harus sesuai agar tidak error
data.remove("Michael")
print(f"data remove = \n{data}")

# menghapus data paling akhir
data.pop()
print(f"data remove akhir = \n{data}")
