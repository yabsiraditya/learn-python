import datetime

mahasiswa1 = {
    'nama':'Asep Saepudin',
    'nim':'2045623423',
    'sks_lulus':134,
    'beasiswa':False,
    'lahir':datetime.datetime(2002,1,9)
}

mahasiswa2 = {
    'nama':'Rizal Saepudin',
    'nim':'2445653427',
    'sks_lulus':140,
    'beasiswa':True,
    'lahir':datetime.datetime(2000,12,12)
}

mahasiswa3 = {
    'nama':'Ucup Saepudin',
    'nim':'1245263429',
    'sks_lulus':120,
    'beasiswa':False,
    'lahir':datetime.datetime(2003,7,8)
}

data_mahasiswa = {
    'MHA001':mahasiswa1,
    'MHA002':mahasiswa2,
    'MHA003':mahasiswa3
}

print(f"{'KEY':<6} {'Nim':<12} {'Nama':<17} {'SKS':<3} {'Beasiswa':<9} {'Lahir':<10}")
print("-"*65)

for mhs in data_mahasiswa:
    key = mhs

    nama = data_mahasiswa[key]['nama']
    nim = data_mahasiswa[key]['nim']
    sks_lulus = data_mahasiswa[key]['sks_lulus']
    beasiswa = data_mahasiswa[key]['beasiswa']
    lahir = data_mahasiswa[key]['lahir'].strftime("%x")

    print(f"{key:<6} {nim:<12} {nama:<17} {sks_lulus:<3} {beasiswa:^9} {lahir:<10}")
