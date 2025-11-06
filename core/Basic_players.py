import abc



class Basic_player():


    def __init__(self,name):

        self.name = name

    @abc.abstractmethod
    def speak(self):
        pass

    @abc.abstractmethod
    def attack(self):
        pass












