# class A:

#     def methodA(self):
#         print("Ini Adalah Method A")

# class B:

#     def methodB(self):
#         print("Ini Adalah Method B")


# class Sesuatu(A,B):
#     pass


# objek = Sesuatu()

# objek.methodB()


class Team:
    def setTeam(self, team):
        self.team = team

    def showTeam(self):
        print(f"Team = {self.team}")

class TipeHero:
    def setTipe(self, tipe):
        self.tipe = tipe

    def showTipe(self):
        print(f"Tipe = {self.tipe}")

class Heroes(Team, TipeHero):
    def __init__(self, name, health) -> None:
        self.name = name
        self.health = health

karina = Heroes("Karina", 150)

karina.setTeam("red")
karina.setTipe('Assasin')

karina.showTeam()
karina.showTipe()