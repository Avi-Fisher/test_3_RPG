from core.Basic_players import Basic_player
from random import randint

class Player(Basic_player):

    def __init__(self,name):

        super().__init__(name)
        self.hp = 50
        self.type = "player"
        self.speed = randint(5,10)
        self.power = randint(5,10)
        self.armor_rating = randint(5,15)
        self.profession = self.profession()


    def profession(self):
        pro = ["fiter","doctor"]
        index = randint(0,1)

        if index == 1:
            self.hp += 10
        elif index == 0:
            self.power += 2

        return pro[index]


    def speak(self):
        print(f"Hi {self.name} lets go kill the all monstur")


    def attack(self):
        pass
































