# 1.mode write = dia akan membuat file baru jika tidak ada
# lalu akan menimpa atau overwrite isinya

with open("day10/externalFile/data.txt","w",encoding="utf-8") as file:
    file.write("Asep Saepudin")

with open("day10/externalFile/data.txt","w",encoding="utf-8") as file:
    file.write("Overwrite")


# mode append
with open("day10/externalFile/data.txt","w",encoding="utf-8") as file:
    file.write("Asep Saepudin\n")

with open("day10/externalFile/data.txt","a",encoding="utf-8") as file:
    file.write("Ucup Budi\n")

with open("day10/externalFile/data.txt","a",encoding="utf-8") as file:
    file.write("Budiooonooo\n")


# mode r+
with open("day10/externalFile/data2.txt","w",encoding="utf-8") as file:
    file.write("data ke 3\n")

with open("day10/externalFile/data2.txt","r+",encoding="utf-8") as file:
    file.write("baris-1\n")
    file.write("baris-2\n")
    file.write("baris-3\n")

with open("day10/externalFile/data2.txt","r+",encoding="utf-8") as file:
    data = file.read()
    print(data)

with open("day10/externalFile/data2.txt","r+",encoding="utf-8") as file:
    file.write("otong")