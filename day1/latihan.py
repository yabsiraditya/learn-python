# Latihan

print("===Program Konversi Temperatur Celcius===")

celcius = float(input('Masukan Suhu Dalam Celcius = '))
print('Suhu Dalam Celcius Adalah', celcius, "C")

# Reamur
reamur = (4/5) * celcius
print('Suhu Dalam Reamur Adalah', reamur, "R")

# Fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print('Suhu Dalam Fahrenheit Adalah', fahrenheit, "F")

# Kelvin
kelvin = 273 + celcius
print('Suhu Dalam Kelvin Adalah', kelvin, "K")

# Latihan 
print('===Program Konversi Fahrenheit To Kelvin===')
f = float(input('Masukan Suhu Dalam Fahrenheit = '))

k = 5/9 * (f - 32) + 273.15

print('Suhu Fahrenheit Ke Kelvin Adalan', k, 'K')

print('===Program Konversi Kelvin To Fahrenheit===')
k = float(input('Masukan Suhu Dalam Kelvin = '))

f = 9/5 * (k - 273.15) + 32

print('Suhu Fahrenheit Ke Kelvin Adalan', f, 'F')
