class Heroes:   # Template

    def __init__(self,inputName,inputHealth,inputPower,inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    def attack(self,attack):
        print(f"{self.name} Menyerang {attack.name}")
        attack.underAttack(self)

    def underAttack(self,attack):
        print(f"{self.name} Diserang {attack.name}")


sniper = Heroes("Sniper",100,25,4)
mirana = Heroes("Mirana",220,50,7)
asep = Heroes("Asep",550,30,9)
udin = Heroes("Udin",330,10,10)


sniper.attack(asep)