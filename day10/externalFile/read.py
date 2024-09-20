# Tutorial membaca file eksternal

print(3*"=", "Membaca file text", 3*"=")

file = open("day10/externalFile/data.txt",mode="r")

print(f"Status Read : {file.readable()}")
print(f"Status Write : {file.writable()}")

# baca seluruh file
print(file.read())

# baca perbaris
# print(file.readline(),end="") # baca baris pertama
# print(file.readline(),end="") # baca baris kedua
# print(file.readline()) # baca baris ketiga

# baca semua baris sebagai list
# print(file.readlines())

# file close 
print(f"apakah file sudah diclose : {file.closed}")
file.close()
print(f"apakah file sudah diclose : {file.closed}")

# salah satu teknik membuat file di python
print("\n",3*"=", "Membaca file text dengan with", 3*"=")

with open("day10/externalFile/data.txt","r") as file:
    content = file.readline()
    print(content,end="")
    print(f"apakah file sudah diclose : {file.closed}")

print(f"apakah file sudah diclose : {file.closed}")