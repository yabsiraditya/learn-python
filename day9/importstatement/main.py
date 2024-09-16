# import

# fungsi adalah untuk mengambil program dari file external .py

# 1. Menyambung program eksternal 
import printTest
import printUcup

# 2. Import degan data
import variable
import variable2

# data ada di namespace variable
print(variable.data)
print(variable2.data)

# 3. Import dengan fungsi
import matematika
hasil = matematika.tambah(3,5)
print(hasil)