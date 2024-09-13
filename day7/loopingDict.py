# looping dictionary

friends  = {
    "cup":"ucup",
    "tong":"otong",
    "dung":"dudung",
    "sep":"asep",
    "cuy":"ucuy"
}

# looping first try (yang keluar adalah keynya)
for friend in friends :
    print(friend)

# operator untuk mengambil item/iterables
keys = friends.keys()
print(keys)

for key in friends.keys():
    print(friends.get(key))

values = friends.values()
print(values)

for value in friends.values():
    print(value)

items = friends.items()
print(items)

for item in friends.items():
    print(item)

for item in friends.items():
    print(item)

for key,value in friends.items():
    print(f"Key = {key}, Value = {value}")