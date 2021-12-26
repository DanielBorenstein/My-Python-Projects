import math
import random

class Player:
    #"__init__" is a reseved method in python classes. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.
    #init is basically constructor from java
    def __init__(self, letter):
        self.letter = letter
    


    def get_move(self,game):
        pass                    # after inheritance come back and check this

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)        #super is used with the ineritance, come back and check this
    
    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super(),__init__(letter)

    def get_move(self, game):
        pass

     
