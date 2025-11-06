from game import Game
from core.player import Player


if __name__ == "__main__":

    game = Game()
    game.start()


    while True:
        if game.show_menu():

            if game.battle():

                print("goodbye")
                break

            continue

        print("loserrr!!!!!")
        break