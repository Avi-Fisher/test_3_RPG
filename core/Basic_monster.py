from abc import abstractmethod
from random import randint


class Basic_monster():

    def __init__(self,name):

        self.name = name
        self.hp = self.class_hp
        self.type = self.class_type
        self.speed = self.class_speed
        self.power = self.class_power
        self.armor_rating =self.class_armor_rating
        self.weapon = self.weapon()

    def weapon(self):

        weapons = [{"weapon":"knife","damage":0.5},{"weapon":"axe","damage":1.5},{"weapon":"sword","damage":1}]
        return weapons[randint(0,2)]

    @abstractmethod
    def speak(self):
        pass

    @abstractmethod
    def attack(self,player):
        pass



























