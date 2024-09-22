class Heroes:   # Template

    def __init__(self, inputName, inputHealth, inputPower):
        # instance variable
        self.__name = inputName
        self.__health = inputHealth
        self.__power = inputPower
    
    # getter
    def getName(self):
        return self.__name
    
    def getHealth(self):
        return self.__health
    
    # setter
    def attack(self,powerAttack):
        self.__health -= powerAttack

    def setPowerAttack(self,newPowerAttack):
        self.__power = newPowerAttack



# awala dari game
miya = Heroes("Miya",120,30)
wukong = Heroes("Wukong",100,20)

# game berjalan
print(miya.getName())
print(miya.getHealth())
miya.attack(5)
print(miya.getHealth())

# tidak boleh
# miya.__name = "Natalia"
# print(miya.__dict__)