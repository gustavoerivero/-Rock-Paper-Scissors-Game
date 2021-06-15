class Player():
    'Player Class.'

    def __init__(self, score, choice):
        'Player class constructor.'
        self.score = score
        self.choice = choice
    
    def setChoice(self, choice):
        'Set player choice.'
        self.choice = choice

    def getChoice(self):
        'Get player choice.'
        return self.choice

    def setScore(self, score):
        'Set player score.'
        self.score = score
    
    def getScore(self):
        'Get player score'
        return self.score
    
    def updateScore(self):
        """Updates the player's score when a game is won."""
        self.score+=1
