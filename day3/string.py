data = "Ini adalah String"
print(data)
print(type(data))

# pengenalan String

'''
    1. menggunakan single quote '...'
    2. menggunakan double quote "..."
'''

data = 'dengan single quote'
print(data)

data = 'dengan double quote'
print(data)

print('"hello apa kabar?"')
print("'hello apa kabar?'")
print("ini adalah hari jum'at")

# menggunakan tanda \ (backslash)

# membuat tanda '
print('ini adalah hari jum\'at')
print('g\'day, isn\'t it ?')

# backslash
print('C:\\USER\\ASEP')

# tab
print("Udin\tAsep")

# backspace
print("Udin \bAsep")

# new line
print("baris 1\nbaris 2") # LF line feed
print("baris 1\rbaris 2") # CF carriage return
print("baris 1\r\nbaris 2") # CRLF = line feed carriage return 


# string literal atau raw
# salah
print('C:\newfolder') # tidak bisa menggunakan path
# gunakan raw string
print(r'C:\newfolder')

# multiline literal string
print("""
Nama : Asep
Kelas : 1 SMA
""")

# multiline literal string dan raw string
print(r"""
Nama : Asep
Kelas : 1 SMA
profile : C:\newfolder\photo.jpg
""")