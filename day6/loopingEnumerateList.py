# Looping dari list

# for loop
print("For Loop")
kumpulan_angka = [4,2,6,8,1]

for angka in kumpulan_angka:
    print(f"angka = {angka}")


peserta = ["asep","ucup","badrun","budi"]

for nama in peserta:
    print(f"nama = {nama}")


# for loop dan range
print("\nFor Loop dan Range")
kumpulan_angka = [20,51,53,12,76]

panjang = len(kumpulan_angka)

for i in range(panjang):
    print(f"Angka = {kumpulan_angka[i]}")


# While 
print("\nWhile Loop")
kumpulan_angka = [20,51,53,12,76]

panjang = len(kumpulan_angka)
i=0

while i < panjang:
    print(f"Angka = {kumpulan_angka[i]}")
    i += 1


# list comprehension
print("\nList Comprehension")
data = ["Asep", 1,2,3,"Budi"]

[print(f"data={i}") for i in data]

angka = [20,51,53,12,76]

angka_kuadrat = [i**2 for i in angka]
print(angka_kuadrat)

# enumerate
print("\nEnumerate")
data_list = ["Asep", 1,2,3,"Budi"]

for index,data in enumerate(data_list):
    print(f"index= {index}, data = {data}")