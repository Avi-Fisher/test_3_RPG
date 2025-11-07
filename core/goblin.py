from random import randint
from .Basic_monster import Basic_monster


class Goblin(Basic_monster):

    class_hp = 20
    class_type = "goblin"
    class_speed = randint(5,10)
    class_power = randint(5, 10)
    class_armor_rating = 1



    def __init__(self,name="Bob"):

        super().__init__(name)


    def speak(self):
        print(f"This is {self.name} speak")


    def attack(self,player):

        if self.speed + randint(1,20) > player.armor_rating:  #chack if speed + 1-6 big in armor

            player.hp -= (self.power + randint(1,6)) * self.weapon["damage"]



