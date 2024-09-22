class Heroes:   # Template

    def __init__(self, inputName, inputHealth, inputArmor):
        # instance variable
        self.name = inputName
        self.__health = inputHealth
        self.__armor = inputArmor
        # self.info = "Name {} : \n\tHealth : {}".format(self.__name,self.__health)

    @property
    def getInfo(self):
        return "Name {} : \n\tHealth : {}".format(self.name,self.__health)
    
    # getter
    @property
    def getArmor(self):
        pass

    @getArmor.getter
    def getArmor(self):
        return self.__armor
    
    @getArmor.setter
    def getArmor(self,input):
        self.__armor = input

    @getArmor.deleter
    def getArmor(self):
        print("Armor didelete")
        self.__armor = None


miya = Heroes("Miya",120,30)
wukong = Heroes("Wukong",100,20)
may = Heroes("May",150,5)

print("Merubah Info")
print(wukong.getInfo)
wukong.name = "Asep"
print(wukong.getInfo)

print("Getter Dan Setter Untuk Armor")
print(wukong.getArmor)
print(wukong.__dict__)
wukong.getArmor = 50
print(wukong.getArmor)

print("Delete Armor")
del wukong.getArmor
print(wukong.__dict__)