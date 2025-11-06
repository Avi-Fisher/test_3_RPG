from core.Basic_players import Basic_player
from random import randint


class Goblin(Basic_player):

    def __init__(self, name = "goblin"):
        super().__init__(name)
        self.hp = 20
        self.type = "goblin"
        self.speed = randint(5, 10)
        self.power = randint(5, 10)
        self.armor_rating = 1
        self.weapon = self.weapon()

    def weapon(self):
        type_weapon = ["knife", "sword","axe"]
        index = randint(0, 2)

        return type_weapon[index]

    def speak(self):
        print(f"This is {self.name} from {self.type} family speak")

    def attack(self):
        pass
