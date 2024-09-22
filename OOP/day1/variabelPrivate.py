class Heroes:   # Template
    #class varibale 
    jumlah = 0
    __privateJumlah = 0

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

        # variabel instance private
        self.__private = "Private"

        # variabel instance protected
        self._protected = "Protected"

sniper = Heroes("Sniper",120,10,5)
mirana = Heroes("Mirana",100,20,10)

print(Heroes.__dict__)
print(Heroes.__privateJumlah)
