class Heroes:   # Template
    # private class variabel
    __jumlah = 0

    def __init__(self, inputName, inputHealth, inputPower):
        # instance variable
        self.__name = inputName
        self.__health = inputHealth
        self.__power = inputPower
        Heroes.__jumlah += 1
    
    # getter
    # method ini hanya berlaku untuk objek
    def getJumlah(self):
        return Heroes.__jumlah
    
    # method ini tidak berlaku untuk objek tapi berlaku untuk class
    def getJumlah1():
        return Heroes.__jumlah
    
    # method static (decorator) nempel ke objek dan class nya
    @staticmethod
    def getJumlah2():
        return Heroes.__jumlah
    
    @classmethod
    def getJumlah3(cls):
        return cls.__jumlah


# awala dari game
miya = Heroes("Miya",120,30)
print(Heroes.getJumlah2())
wukong = Heroes("Wukong",100,20)
print(wukong.getJumlah2())
may = Heroes("May",150,5)
print(miya.getJumlah3())