import numpy as np

a = np.arange(10)**2

print(a)

# mengambil nilai
print(f"elemen ke 1 dari a adalah {a[0]}")
print(f"elemen ke 7 dari a adalah {a[6]}")
print(f"elemen terakhir dari a adalah {a[-1]}")


# slicing 
print(f"elemen dari 1-6 dari a adalah {a[0:6]}")
print(f"elemen dari 4 sampai akhir dari a adalah {a[3:]}")
print(f"elemen dari awal sampai 5 dari a adalah {a[:5]}")


# iterasi

for i in a:
    print(f"Value = {i}")