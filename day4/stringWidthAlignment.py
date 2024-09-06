data_nama = "Asep Sudrajat"
data_umur = 20
data_tinggi = 163
data_nomor_sepatu = 45

# String standard
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, sepatu = {data_nomor_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (dengan menggunakan enter newline (\n))
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nsepatu = {data_nomor_sepatu}"
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# String multiline (kutip tripleks)
data_string = f"""Nama = {data_nama}
Umur = {data_umur}
Tinggi = {data_tinggi}
Sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_nama = "Asep Sumardi"
data_tinggi = 171.14
data_string = f"""
Nama   = {data_nama:>5}
Umur   = {data_umur:>5}
Tinggi = {data_tinggi:>5}
Sepatu = {data_nomor_sepatu:>5}
"""
print("\n"+5*"="+"Data String"+5*"=")
print(data_string)