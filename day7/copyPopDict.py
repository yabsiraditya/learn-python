# Copy Dictionary

temanTeman  = {
    "cup":"ucup",
    "tong":"otong",
    "dung":"dudung",
    "sep":"asep",
    "cuy":"ucuy"
}

friends = temanTeman.copy()

print(f"temanTeman = {temanTeman}\n")
print(f"freind = {friends}\n")

temanTeman["cup"] = "ucup si keren"
print(f"temanTeman = {temanTeman}\n")
print(f"freind = {friends}\n")

# pop dictionary (mengambil berdasrkan value)
dataAsep = friends.pop("sep")
print(f"data asep = {dataAsep}\n")
print(f"freind = {friends}\n")

# popitem dictionary (mengambil yang paling akhir)
dataTerakhir = friends.popitem()
print(f"data asep = {dataTerakhir}\n")
print(f"freind = {friends}\n")