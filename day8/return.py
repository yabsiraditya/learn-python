'''Fungsi Dari Return

    Template fungsi dengan Return 
    def nama_fungsi(argument):
        badan fungsi
        return output
'''

# fungsi kuadrat

def kuadrat(intputNum):
    outputQuad = intputNum**2
    return outputQuad

y = kuadrat(5)
print(y)

print(kuadrat(6))

z = 20 + kuadrat(5)
print(z)


# Return multi input

def fungsiTambah(angka1,angka2):
    return angka1 + angka2

a = fungsiTambah(10,10)
print(a)


# Fungsi dengan banyak Return

def operasiMath(angka1,angka2):
    tambah = angka1 + angka2
    kurang = angka1 - angka2
    kali = angka1 * angka2
    bagi = angka1 / angka2

    return tambah,kurang,kali,bagi

k,l,m,n = operasiMath(10,10)

print(f"Hasil tambah = {k}")
print(f"Hasil kurang = {l}")
print(f"Hasil kali = {m}")
print(f"Hasil bagi = {n}")