'''**kwargs'''

def fungsi(nama,tinggi,berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")

fungsi("ucup",180,75)


# Menggukana Keyword Args 
def fungsi(**kwargs):
    nama = kwargs["nama"]
    tinggi = kwargs["tinggi"]
    berat = kwargs["berat"]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat}")


fungsi(nama="ucup",tinggi=180,berat=75)

# Studi Kasus
def math(*args,**kwargs):
    output = 0
    if kwargs["option"] == "tambah":
        for angka in args:
            output += angka
    elif kwargs["option"] == "kali":
        output = 1
        for angka in args:
            output *= angka

    return output

hasil = math(1,2,3,4,option="tambah")
print(f"hasil tambah = {hasil}")
hasil = math(1,2,3,4,option="kali")
print(f"hasil kali = {hasil}")