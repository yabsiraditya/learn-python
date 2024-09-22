class Heroes:   # Template

    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
    
    def attack(self, attack):
        print(f"{self.name} Menyerang {attack.name}")
        attack.underAttack(self, self.power)

    def underAttack(self, attack, attackPowerEnemy):
        print(f"{self.name} Diserang {attack.name}")
        attackReceived = attackPowerEnemy/self.armor
        print(f"Serangan Diterima : {str(attackReceived)}")
        self.health -= attackReceived
        print(f"Darah {self.name} Tersisa {str(self.health)}")


sniper = Heroes("Sniper",120,10,5)
mirana = Heroes("Mirana",100,20,10)
asep = Heroes("Asep",550,30,9)
udin = Heroes("Udin",330,10,10)


sniper.attack(mirana)
print("\n")
mirana.attack(sniper)