# Anonymouse Function
# currying <- Haskell Curry

def pangkat(angka,n):
    hasil = angka**n
    return hasil

data_hasil = pangkat(5,2)
print(f"fungsi biasa = {data_hasil}")

# dengan Currying menjadi

def pangkat(n):
    return lambda angka:angka**n

pangkat2 = pangkat(2)
print(f"pangkat 2 = {pangkat2(5)}")

pangkat3 = pangkat(3)
print(f"pangkat 3 = {pangkat3(5)}")

print(f"pangkat bebas = {pangkat(4)(5)}")