# Operator String dalam bentuk method

# merubah ke huruf besar
salam = "bro!"
print("normal =", salam)
salam = salam.upper()
print("upper =", salam)

# merubah ke huruf kecil
alay = "AkU dImAna YA SeKARANG"
print("normal =", alay)
alay = alay.lower()
print("lower =", alay)

# pengecekan dengan isX method
salam = "sist"
apakah_lower = salam.islower() # hasilnya Boolean
print(salam, "is lower =", str(apakah_lower))

apakah_upper = salam.isupper() # hasilnya Boolean
print(salam, "is upper =", str(apakah_upper))

# isalpha() <-- untuk mengecek semua huruf
# isalnum() <-- huruf dan angka
# isdecimal() <-- angka saja
# isspace() <-- spasi, tab, newline

# istitle() <-- semua kata dimulai dengan huruf besar
judul = "Apakah Aku Bersalah"
cek_judul = judul.istitle() # hasil Boolean
print(judul, "is title =", str(cek_judul))

# Cek Komponen startswith() endswith()
cek_start = "Hallo Guys".startswith("Hallo")
print("start =", str(cek_start))

cek_end = "Hallo Guys".endswith("Guys")
print("end =", str(cek_end))

# penggabungan komponen join() split()
pisah = ['aku', 'cinta', 'php']
gabung = ' '.join(pisah)
print(gabung)

gabung = "aku cinta php"
print(gabung.split(' '))

# alokasi karakter rjust() ljust() center()
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

kiri = "kiri".ljust(10)
print("'"+kiri+"'")

tengah = "tengah".center(20,'-')
print("'"+tengah+"'")

# kebalikannya -> strip
tengah = tengah.strip('-') # menghilangkan tanda (-)
print("'"+tengah+"'")
