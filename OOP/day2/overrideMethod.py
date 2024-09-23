class Heroes:   # Template

    def __init__(self, inputName, inputHealth):
        # instance variable
        self.name = inputName
        self.health = inputHealth

    def showInfo(self):
        print("{} \n\tHealth : {}".format(
            self.name,
            self.health
            )
        )

class Heroes_intelligent(Heroes):
    def __init__(self, inputName):
        super().__init__(inputName, 100)

    def showInfo(self):
        print("Show Info Hero Intelligent")
        print("{} \n\tTipe : Intelligent \n\tHealth : {}".format(
            self.name,
            self.health
            )
        )

class Heroes_strength(Heroes):
    def __init__(self, inputName):
        super().__init__(inputName, 200)
    def showInfo(self):
        print("Show Info Hero Strength")
        print("{} \n\tTipe : Strength \n\tHealth : {}".format(
            self.name,
            self.health
            )
        )



sniper = Heroes_intelligent("Sniper")
wukong = Heroes_strength("Wukong")

sniper.showInfo()
wukong.showInfo()
