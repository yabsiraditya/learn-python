# manipulasi string

# menyambungkan string (concatenate)
nama_depan = "Ucup"
nama_tengah = "D"
nama_akhir = "Family"

nama_lengkap = nama_depan + " " + nama_tengah + "'" + nama_akhir
print(nama_lengkap)

# menghitung panjang string
panjang = len(nama_lengkap)
print("panjang dari", nama_lengkap, "=", str(panjang))

# mengecek apakah ada komponen char atau string di string
d = "d"
status = d in nama_lengkap
print(d, "ada di", nama_lengkap, "=", str(status))

D = "D"
status = D in nama_lengkap
print(D, "ada di", nama_lengkap, "=", str(status))

d = "d"
status = d not in nama_lengkap
print(d, "ada di", nama_lengkap, "=", str(status))

# mengulang string
print("wkwk"*10)
print(15*"wkwk")

# indexing
print("index ke-0 =", nama_lengkap[0])
print("index ke-6 =", nama_lengkap[6])
print("index ke-(-1) =", nama_lengkap[-1]) # jika minus dari belakang
print("index ke-(-2) =", nama_lengkap[-2])
print("index ke-[0,3] =", nama_lengkap[0:4]) # mengambil banyak string
print("index ke-[3,7] =", nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] =", nama_lengkap[0:11:2])

# item paling kecil 
print("paling kecil =", min(nama_lengkap))
# item paling besar
print("paling besar =", max(nama_lengkap))

ascii_code = ord(" ")
print("ASCII code untuk spasi adalah", str(ascii_code))

data = 121
print("char untuk ASCII 121 adalah", chr(data))

# operator method string
data = "otong surotong pararotong"
jumlah = data.count("o")
print("Jumlah o pada", data, "=", str(jumlah))