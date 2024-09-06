# If and Else Statement

"""
    1. if Nya
    2. kondisinya 
    3. aksinya
"""

nama = input("Siapa Nama Anda? ")

# program sebelumnya
# if kondisi: aksi
# program selanjutnya

# 1. Program if inline
if nama == "asep" : print(f"kamu ganteng abiezzz {nama}!!!!")
print(f"Terima Kasih {nama}")

# 2. program if identation
if nama == "asep":
    print(f"Keren abiezzz {nama}!!!")
print(f"Teima Kasih {nama}")

# 3, Else statement
if nama == "otong":
    print("Kamu beneran otong!")
else:
    print("kamu bukan otong!")

print("Akhir Program")