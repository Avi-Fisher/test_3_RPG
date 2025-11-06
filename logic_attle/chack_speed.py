from random import randint

class Chack_speed():



    @staticmethod
    def chack(self,player,monster):

        player_speed = player.speed + randint(1, 6)
        monster_speed = monster.speed + randint(1, 6)

        print(f"your speed is {player_speed}")
        print((f"The monster speed is {monster_speed}"))

        if monster.speed < player.speed:

            turn = player
            not_turn = monster
            print(f"{turn.name} attack")


        elif monster.speed > player.speed:

            turn = monster
            not_turn = player
            print(f"{turn.name} attack")


        return  [turn,not_turn]







