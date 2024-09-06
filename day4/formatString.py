# Format string

# String
nama = "Asep"
format_str = f"Hello {nama}"
print(format_str)

# boolean
boolean = False
format_str = f"Nilai = {boolean}"
print(format_str)

#  angka
angka = 247.6
format_str = f"Angka = {angka}"
print(format_str)

# bilangan bulat 
angka = 15
format_str = f"Bilang Bulat = {angka:d}"
print(format_str)

# bilangan dengan ordo ribuan
angka = 1500000
format_str = f"Jutaan = {angka:,}"
print(format_str)

# bilangan desimal
angka = 247.6709
format_str = f"Angka = {angka:.2f}"
print(format_str)

# menampilkan leading zero
angka = 247.6709
format_str = f"Angka = {angka:08.2f}"
print(format_str)

# menampilkan tanda + dan -
angka_minus = -10
angka_plus = +10.132
format_minus = f"Minus = {angka_minus:+d}"
format_plus = f"Plus = {angka_plus:+.2f}"

print(format_minus)
print(format_plus)

# memformat persen
persentase = 0.045
format_persen = f"Persen = {persentase:.2%}"
print(format_persen)

# melakukan operasi aritmatika di dalam placeholder
harga = 15000
jumlah = 5
format_string = f"Harga Total = Rp.{harga*jumlah:,}"
print(format_string)

# format angka lain (Binary, Octal, Hexadecimal)
angka = 285
format_binary = f"Binnary = {bin(angka)}"
format_octal = f"Octal = {oct(angka)}"
format_hex = f"Hex = {hex(angka)}"

print(format_binary)
print(format_octal)
print(format_hex)