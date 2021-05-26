import random
class Sweepstakes:
    def __init__(self,):
        self.contestants = ('John Doe', 'Jane Smith', 'John Smith', 'Jane Doe', 'Will Smith')

    def choosing_winner(self):
        self.winner = random.choice(self.contestants)
        print(self.winner)

