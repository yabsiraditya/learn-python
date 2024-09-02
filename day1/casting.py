# Casting = Merubah Tipe Data

# data Integer
print("====Integer====")
data_int = 9

print("Data : ", data_int, "- Bertipe : ",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # akan false jika nilai int = 0

print("Data : ", data_float, "- Bertipe : ",type(data_float))
print("Data : ", data_str, "- Bertipe : ",type(data_str))
print("Data : ", data_bool, "- Bertipe : ",type(data_bool))


# data Float
print("====Float====")
data_float = 9.9

print("Data : ", data_float, "- Bertipe : ",type(data_float))

data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float) # akan false jika nilai float = 0

print("Data : ", data_int, "- Bertipe : ",type(data_int))
print("Data : ", data_str, "- Bertipe : ",type(data_str))
print("Data : ", data_bool, "- Bertipe : ",type(data_bool))


# data Boolean
print("====Boolean====")
data_bool = True

print("Data : ", data_bool, "- Bertipe : ",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool) # akan false jika nilai float = 0

print("Data : ", data_int, "- Bertipe : ",type(data_int))
print("Data : ", data_str, "- Bertipe : ",type(data_str))
print("Data : ", data_float, "- Bertipe : ",type(data_float))


# data String
print("====String====")
data_str = "1"

print("Data : ", data_str, "- Bertipe : ",type(data_str))

data_int = int(data_str) # Nilai String Harus Angka
data_bool = bool(data_str) # Akan False jika String kosoang
data_float = float(data_str) 

print("Data : ", data_int, "- Bertipe : ",type(data_int))
print("Data : ", data_bool, "- Bertipe : ",type(data_bool))
print("Data : ", data_float, "- Bertipe : ",type(data_float))