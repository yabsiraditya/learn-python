class Heroes:   # Template

    def __init__(self, inputName):
        self.healthPool = [0,100,200,300,400,500]
        self.powerPool = [0,10,20,30,40,50]
        self.armorPool = [0,1,2,3,4,5]
        self.__name = inputName
        self.__exp = 0
        self.__level = 0

    def showInfo(self):
        print("{} \n\tLevel : {}\n\tHealth : {}\n\tPower : {}\n\tArmor : {}".format(
            self.__name,
            self.__level,
            self.__health,
            self.__power,
            self.__armor
            )
        )


    @property
    def healthPool(self):
        pass


    @property
    def powerPool(self):
        pass


    @property
    def armorPool(self):
        pass


    @property
    def levelUp(self):
        pass


    @property
    def gainExp(self):
        pass


    @healthPool.setter
    def healthPool(self, input):
        self.__healthPool = input


    @powerPool.setter
    def powerPool(self, input):
        self.__powerPool = input


    @armorPool.setter
    def armorPool(self, input):
        self.__armorPool = input


    @gainExp.setter
    def gainExp(self, input):
        self.__exp += input
        if(self.__exp >= 10):
            self.levelUp = self.__exp//100
            self.__exp %= 100


    @levelUp.setter
    def levelUp(self, input):
        print(self.__name, 'Level UP')
        self.__level += input
        self.__health = self.__healthPool[self.__level]
        self.__power = self.__powerPool[self.__level]
        self.__armor = self.__armorPool[self.__level]

    
class Heroes_intelligent(Heroes):
    def __init__(self, inputName):
        super().__init__(inputName)
        self.healthPool = [0,50,100,150,200,250]
        self.powerPool = [0,20,40,60,80,100]
        self.armorPool = [0,0.5,1,1.5,2,2.5]
        self.levelUp = 1


class Heroes_strength(Heroes):
    def __init__(self, inputName):
        super().__init__(inputName)
        self.healthPool = [0,200,300,400,500,600]
        self.powerPool = [0,20,40,60,80,100]
        self.armorPool = [0,2,4,6,8,10]
        self.levelUp = 1