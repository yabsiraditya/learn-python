angka1 = float(input("Masukan angak 1 = "))
operator = input("Masukan Operator (+,-,*,/,%) = ")
angka2 = float(input("Masukan angak 2 = "))

if operator == "+": # kondisi 1
    hasil = angka1 + angka2
    print(f"Hasil {angka1} {operator} {angka2} = {hasil}") # aksi true 1
elif operator == "-": # kondisi 2
    hasil = angka1 - angka2
    print(f"Hasil {angka1} {operator} {angka2} = {hasil}") # aksi true 2
elif operator == "*": # kondisi 3
    hasil = angka1 * angka2
    print(f"Hasil {angka1} {operator} {angka2} = {hasil}") # aksi true 3
elif operator == "/": # kondisi 4
    hasil = angka1 / angka2
    print(f"Hasil {angka1} {operator} {angka2} = {hasil}") # aksi true 4
elif operator == "%": # kondisi 5
    hasil = angka1 % angka2
    print(f"Hasil {angka1} {operator} {angka2} = {hasil}") # aksi true 5
else:
    print("Operator yang anda masukan salah!") # aksi false

print("Akhir Program") 