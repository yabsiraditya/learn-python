# Latihan 1
inputUser = float(input("Masukan Angak :"))

h1 = inputUser > 0
h2 = inputUser < 5
h3 = inputUser > 8
h4 = inputUser < 11

isCorrect = h1 and h2 or h3 and h4
print(isCorrect)

# Latihan 2
inputUser = float(input("Masukan Angak :"))

h1 = inputUser < 0
h2 = inputUser > 5
h3 = inputUser < 8
h4 = inputUser > 11

isCorrect = h1 or h2 and h3 or h4
print(isCorrect)