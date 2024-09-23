class Heroes:   # Template

    def __init__(self, inputName, inputHealth):
        # instance variable
        self.name = inputName
        self.health = inputHealth

class Heroes_intelligent(Heroes):
    pass

class Heroes_strength(Heroes):
    pass


lina = Heroes("Lina", 100)
sniper = Heroes_intelligent("Sniper", 50)
wukong = Heroes_strength("Wukong", 200)

print(lina.__dict__)
print(lina.name)
print(sniper.__dict__)
print(sniper.health)
print(wukong.__dict__)
print(wukong.name)