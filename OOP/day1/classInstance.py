class Heroes:   # Template
    # class variable
    jumlah = 0

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Heroes.jumlah += 1
        print("Membuat Hero Dengan Nama : " + inputName)

hero1 = Heroes("Sniper",100,25,4)    # Object / instance (instansiate)
print(Heroes.jumlah)
hero2 = Heroes("Mirana",220,50,7)    # Object / instance (instansiate)
print(Heroes.jumlah)
hero3 = Heroes("Asep",550,30,9)    # Object / instance (instansiate)
print(Heroes.jumlah)
hero4 = Heroes("Udin",330,10,10)    # Object / instance (instansiate)
print(Heroes.jumlah)

# print(hero1.__dict__)
# print(hero2.__dict__)
# print(hero3.__dict__)

