from core.Basic_players import Basic_player
from random import randint


class Orc(Basic_player):

    def __init__(self, name = "orc"):
        super().__init__(name)
        self.hp = 50
        self.type = "orc"
        self.speed = randint(0, 5)
        self.power = randint(5, 10)
        self.armor_rating = randint(2,8)
        self.weapon = self.weapon()

    def weapon(self):
        type_weapon = ["knife", "sword","axe"]
        index = randint(0, 2)

        return type_weapon[index]

    def speak(self):
        print(f"This is {self.name} from {self.type} family speak")

    def attack(self):
        pass
