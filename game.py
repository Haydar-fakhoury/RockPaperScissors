class RockPaperScissors:
    def __init__(self, computer,user,score):
        self.computer = computer
        self.user = user
        self.score = 3
        print(self.user)
        print(self.computer)



    def ifs(self):
        if self.user == "ROCK" and self.computer == "SCISSORS" or self.user == "SCISSORS" and self.computer == "PAPER" or self.user == "PAPER" and self.computer == "ROCK":
            return "YOU WON!"
        elif self.user == self.computer:
            return "Draw"
        else:
            score = score-1
            return f"You lose and you have {score} tries left"
