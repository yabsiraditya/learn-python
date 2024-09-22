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

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print(f"Namaku adalah : {self.name}")

    # method dengan argumen, tanpa return
    def heatlhUp(self,up):
        self.health += up

    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Heroes("Sniper",100,25,4)    # Object / instance (instansiate)
hero2 = Heroes("Mirana",220,50,7)    # Object / instance (instansiate)
hero3 = Heroes("Asep",550,30,9)    # Object / instance (instansiate)
hero4 = Heroes("Udin",330,10,10)    # Object / instance (instansiate)

print(hero1.__dict__)
print(hero2.__dict__)
print(hero3.__dict__)
print(hero4.__dict__)

hero1.siapa()

hero1.heatlhUp(200)
print(f"Health UP Hero {hero1.name} : {hero1.getHealth()}")