class Heroes:   # Template
    # Private class variabel
    __jumlah = 0


    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variable
        self.__name = inputName
        self.__healthStandar = inputHealth
        self.__powerStandar = inputPower
        self.__armorStandar = inputArmor
        self.__level = 1
        self.__exp = 0

        self.__healthMax = self.__healthStandar * self.__level
        self.__powerMax = self.__powerStandar * self.__level
        self.__armorMax = self.__armorStandar * self.__level

        self.__health = self.__healthMax

        Heroes.__jumlah += 1

    @property
    def info(self):
        return "{} : \n\tHeatlh {}/{} \n\tAttack = {} \n\tArmor = {}".format(self.__name,self.__health,self.__healthMax,self.__powerMax,self.__armorMax)
    
    @property
    def gainExp(self):
        pass

    @gainExp.setter
    def gainExp(self, addExp):
        self.__exp += addExp
        if (self.__exp >= 100):
            print(self.__name, 'Level UP')
            self.__level += 1
            self.__exp -= 100

            self.__healthMax = self.__healthStandar * self.__level
            self.__powerMax = self.__powerStandar * self.__level
            self.__armorMax = self.__armorStandar * self.__level

    def attack(self,enemy):
        self.gainExp = 50


sniper = Heroes('Sniper', 100, 5, 10)
wodi = Heroes('Wodi', 120, 10, 5)

print(sniper.info)
sniper.attack(wodi)
sniper.attack(wodi)
sniper.attack(wodi)
print(sniper.info)