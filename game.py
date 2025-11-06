from random import randint
from core.orc import Orc
from core.goblin import Goblin
from core.player import Player

class Game():

    def __init__(self):

        self.menu = None
        self.player = None
        self.monster = None
        self.turn = None
        self.not_turn = None


    def start(self):
        print("Welcome to the monster game")
        name = input("Enter your name please")

        self.player = Player(name)
        print(f"{name} lets  kill a monster")



    def show_menu(self):

        while True:
            self.menu = input("""
            ==================
               W    A    R
              
              #1 GO to battle
              #2 Run like a coward
            
            """)
            if self.menu == "1":
                return True


            elif self.menu == "2":
                return False

            print("Dont do mistic monster kill you")



    def choose_random_monster(self):
        monster = []

        g1 = Goblin("Bob")
        o1 = Orc("Gil")

        monster.append(g1)
        monster.append(o1)

        return monster[randint(0,1)]



    def battle(self):
        player_speed = self.player.speed + randint(1,6)
        monster_speed = self.monster.speed + randint(1,6)

        print(f"your speed is {player_speed}")
        print((f"The monster speed is {monster_speed}"))


        if monster_speed < player_speed:

            self.turn = self.player
            self.not_turn = self.monster
            print(f"{self.turn.name} attack")


        elif monster_speed > player_speed:

            self.turn = self.monster
            self.not_turn = self.player
            print(f"{self.turn.name} attack")


        turn_speed = self.roll_dice() + self.turn.speed
        print(f"""
        
        ==========
        {self.turn.name} have {turn_speed}  speed!!!
        {self.not_turn.name} have {self.not_turn.armor_rating} armor!!!
        """)


        if turn_speed > self.not_turn.armor_rating:

            turn_power = self.turn.power + randint(1,6)


            if self.turn.type != "player":

                match self.turn.weapon:
                    case "knife":
                        turn_power *= 0.5
                    case "sword":
                        turn_power *= 1
                    case "axe":
                        turn_power *= 1.5

            print(f"{self.turn.name} have {turn_power}  power")

            self.not_turn.hp -= turn_power

        if self.not_turn.hp <= 0:
            print(f"{self.turn.name} winnnnn")
            return True

        print(f"{self.not_turn.name} have {self.not_turn.hp} life")

        self.turn, self.not_turn = self.not_turn, self.turn



    def roll_dice(self):
        return randint(6,20)














