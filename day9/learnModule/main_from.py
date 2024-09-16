# Module Matematika Dengan Import

from matematika import tambah as add
from matematika import kali as k
from matematika import pangkat as d # as bisa terserah kita

import matematika as math # <--- bisa dilakukan

hasilTambah = add(2,2,3,5,6)
print(f"Hasil Tambah = {hasilTambah}") 

hasilKali = math.kali(2,2,3,5,6)
print(f"Hasil Kali = {hasilKali}") 

pangkat = d(3)
print(f"Hasil Pangkat = {pangkat(5)}")