from game import RockPaperScissors
import random

choices = ["Rock","Paper","Scissors"]
def Computerplay(Computerchoice):
    Computerchoice = random.choice(choices)
    return Computerchoice.upper()




def userplay():
        UserChoice = input("Enter your choice of Rock,Paper or Scissors: ")
        return UserChoice.upper()
us = input("P to play R to stop").upper()
while us != "r":
    jack = RockPaperScissors(Computerplay(choices),userplay(),3)
    print(jack.ifs())

