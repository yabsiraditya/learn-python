# Lambda Function

def fKuadrat(angka):
    return angka**2

print(f"hasil fungsi kuadrat = {fKuadrat(3)}")

# dengan lamnda
# output = lambda argument: expression
lKuadrat = lambda angka:angka**2

print(f"hasil lambda kuadrat = {fKuadrat(5)}")

pangkat = lambda num,pow : num**pow

print(f"hasil lambda kuadrat = {pangkat(2,2)}")

# Sorting List Biasa 
dataList = ["Otong","Dudung","Asep","Budi"]
dataList.sort()
print(f"Sorting List = {dataList}")

# sorting fungsi biasa 
def pNama(nama):
    return len(nama)

dataList.sort(key=pNama)
print(f"Sorting List Fungsi = {dataList}")

# sorting dengan lambda
dataList = ["Otong","Dudung","Asep","Budi"]
dataList.sort(key=lambda nama:len(nama))
print(f"Sorting List Lambda = {dataList}")


# filter
dataAngka = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

def kurangDari(angka):
    return angka < 5

dataAngkaBaru = list(filter(kurangDari,dataAngka))
print(dataAngkaBaru)

dataAngkaBaru = list(filter(lambda x:x <12,dataAngka))
print(dataAngkaBaru)

# genap 
dataGenap = list(filter(lambda x:(x%2==0),dataAngka))
print(dataGenap)

# ganjil
dataGanjil = list(filter(lambda x:(x%2!=0),dataAngka))
print(dataGanjil)

# kelipatan tiga 
data3 = list(filter(lambda x:(x%3==0),dataAngka))
print(data3)