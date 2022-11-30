# The class was created to take information about the user's score
# in the game and transfer it to a file.
class Stats:
    # In the main function, to begin with, we restart the score counter every game
    # to calculate the score of a particular game.
    def __init__(self):
        self.reset_stats()
        # While the game is in progress, the score is written to a file
        self.run_game = True
        with open('TheBestScore', 'r') as f:
            self.high_score = int(f.readline())

    # Function to reboot...
    def reset_stats(self):
        # ...gun lives
        self.guns_left = 3
        # ... and points in each new game
        self.score = 0
