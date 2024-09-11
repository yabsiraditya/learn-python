# List

# Kumpulan data numbers
data_angka = [1,2,3,4,5]
print(data_angka)

# Kumpulan data string
data_string = ["Asep", "Ujang", "Ucup"]
print(data_string)

# Kumpulan data boolean
data_boolean = [True, False, True, False]
print(data_boolean)

# Kumpulan data campuran
data_campuran = [1, "Asep", 3, "Cireng", "Ujang", False]
print(data_campuran)

# Cara alternatif membuat lis
data_range = range(0,10,2)
print(data_range)
data_list = list(data_range)
print(data_list)

# membuat list dengan for loop, list comprehension
list_pake_for = [i**2 for i in range(0,10)]
print(list_pake_for)

# membuat list dengan for pake if
list_pake_for_if = [i for i in range(0,10) if i != 5]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 == 0]
print(list_pake_for_if)

list_pake_for_if = [i for i in range(0,10) if i % 2 != 0]
print(list_pake_for_if)