class Heroes:   # Template

    def __init__(self, inputName, inputHealth):
        # instance variable
        self.name = inputName
        self.health = inputHealth

    def showInfo(self):
        print("{} dengan Health : {}".format(self.name,self.health))

class Heroes_intelligent(Heroes):
    def __init__(self, inputName):
        # Heroes.__init__(self, inputName, 100)
        super().__init__(inputName, 100)
        super().showInfo()

class Heroes_strength(Heroes):
    def __init__(self, inputName):
        # Heroes.__init__(self, inputName, 200)
        super().__init__(inputName, 200)
        super().showInfo()



sniper = Heroes_intelligent("Sniper")
wukong = Heroes_strength("Wukong")

# print(f"{sniper.name} Heatlh = {sniper.health}")
# print(f"{wukong.name} Heatlh = {wukong.health}")