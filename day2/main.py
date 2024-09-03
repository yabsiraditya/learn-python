# Latihan Logika dan Komparasi

# ++++++++++3-----------10++++++++++

inputUser = float(input("Masukan angkan yang bernilai\nkurang dari 3\natau\nlebih besar dari 10\n:"))

# ++++++++++3----------
# Kurang dari 3
isKurangDari = (inputUser < 3)
print(isKurangDari)

# ----------10++++++++++
# Lebih dari 10
isLebihDari = (inputUser > 10)
print(isLebihDari)

isCorrect = isKurangDari or isLebihDari
print(isCorrect)

print("\n", 10*"=", "\n")

# ----------3++++++++++10----------

inputUser = float(input("Masukan angkan yang bernilai\nlebih dari 3\ndan\nkurang dari 10\n:"))

# ----------3++++++++++
# Lebih dari 3
isKurangDari = (inputUser > 3)
print(isKurangDari)

# +++++++++10----------
# Kurang dari 10
isLebihDari = (inputUser < 10)
print(isLebihDari)

isCorrect = isKurangDari or isLebihDari
print(isCorrect)