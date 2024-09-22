class Heroes:   # Template
    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor

hero1 = Heroes("Sniper",100,25,4)    # Object / instance (instansiate)
hero2 = Heroes("Mirana",220,50,7)    # Object / instance (instansiate)
hero3 = Heroes("Asep",550,30,9)    # Object / instance (instansiate)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero1.name)
print(hero3.health)
print(hero2.name)
print(hero3.power)

# hero2 = Heroes()
# hero3 = Heroes()

# hero1.name = "Sniper"
# hero1.health = 100

# hero2.name = "Sven"
# hero2.health = 200

# hero3.name = "Asep"
# hero3.health = 550

# print(hero3)
# print(hero3.__dict__)
# print(hero1.name)