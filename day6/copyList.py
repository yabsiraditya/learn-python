# teknik menduplikat list

a = ["Asep", "Ujang", "Ucup", "Dudung"]
print(f"a = {a}")

b = a
print(f"b = {b}")

# merubah member dari a

# ini akan merubah kedua list
a[1] = "Michael"
b.sort()

print(f"a = {a}")
print(f"b = {b}")

# address dari kedua list a dan b
print(f"address a = {hex(id(a))}")
print(f"address a = {hex(id(a))}")

# menduplikat list dengan copy  
print("Membuat list c denfan a.copy()")
c = a.copy()

print(f"address a = {hex(id(a))}")
print(f"address b = {hex(id(b))}")
print(f"address c = {hex(id(c))}")

# merubah data list dengan copy
print("Merubah data index ke 0 dan 1")
c[1] = "Dindang"
c[0] = "Dono"

print(f"a = {a}")
print(f"b = {b}")
print(f"c = {c}")
