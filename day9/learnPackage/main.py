import sains.matematika as math
from sains import fisika
from sains.fisika import gaya as fsk

hasilTambah = math.tambah(2,2,3,5,6)
print(f"Hasil Tambah = {hasilTambah}") 

hasilKali = math.kali(2,2,3,5,6)
print(f"Hasil Kali = {hasilKali}") 

pangkat = math.pangkat(3)
print(f"Hasil Pangkat = {pangkat(5)}")

gaya = fisika.gaya(10,2)
print(f"Gaya adalah = {gaya}")

gaya = fsk(4,2)
print(f"Gaya adalah = {gaya}")