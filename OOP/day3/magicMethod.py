class buah:

    def __init__(self,nama,jumlah):
        self.nama = nama
        self.jumlah = jumlah

    # untuk debug
    def __repr__(self):
        return "Buah : {}, Jumlah : {}".format(self.nama,self.jumlah)

    def __add__(self,objek):
        return self.jumlah + objek.jumlah
    
    @property
    def __dict__(self):
        return "Objek ini memiliki nama dan jumlah"
    
    # untuk production
    def __str__(self):
        return "Buah : {}, Jumlah : {}".format(self.nama,self.jumlah)
    

belanja1 = buah("Mangga", 10)
belanja2 = buah("Apel", 3)
belanja3 = buah("Pisang", 5)

print(repr(belanja1))
print(belanja2)
print(belanja3)

print(belanja1 + belanja2)

print(belanja1.__dict__)