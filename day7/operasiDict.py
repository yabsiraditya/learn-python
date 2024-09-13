# operator dictionary

data_dict = {
    'cup':'ucup',
    'tong':'otong',
    'dung':"dudung"
}

# panjang dictionary

lendict = len(data_dict)

print(f"Pajang dari Dict adalah {lendict}")

# mengecek key exist atau tidak
key = "dung"

checkKey = key in data_dict

print(f"Apakah {key} ada di data_dict: {checkKey}")

# mengakses value (read) dengan get 
print(data_dict["cup"])
print(data_dict.get("tong"))
print(data_dict.get("kis","key tidak ditemukan")) # cek key dengan message tidak ditemukan

# mengupdate data
data_dict["cup"] = "ucup siganteng"
print(data_dict)
data_dict["sep"] = "asep"
print(data_dict)

data_dict.update({"cup":"ucup surs"})
print(data_dict)

data_dict.update({"dit":"adit"})
print(data_dict)

# mendelet data pada dictionary
del data_dict["dit"]
print(data_dict)