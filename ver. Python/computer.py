from player import *
from random import randint

class Computer(Player):
    'Computer Class. It inherits the Player Class.'

    def __init__(self, score, choice):
        'Computer class constructor.'
        super().__init__(score, choice)
        self.rock = 0
        self.paper = 0
        self.scissor = 0
    
    def win(self):
        'Computer analysis in case it has won.'
        if(self.choice == "ROCK"):
            'Analysis of the computer when winning with rock.'
            self.rock+=3
            self.scissor+=1
            self.paper-=1
        elif(self.choice == "PAPER"):
            'Analysis of the computer when winning with paper.'
            self.paper+=3
            self.scissor+=1
            self.rock-=1
        else:
            'Analysis of the computer when winning with scissor.'
            self.scissor+=3
            self.paper+=1
            self.rock-=1
        self.updateScore()
    
    def tie(self):
        'Computer analysis in case it has tie.'
        if(self.choice == "ROCK"):
            'Computer analysis when tying with rock.'
            self.paper+=1
        elif(self.choice == "PAPER"):
            'Computer analysis when tying with paper.'
            self.scissor+=1
        else:
            'Computer analysis when tying with scissor.'
            self.rock+=1

    def lose(self):
        'Computer analysis in case it has lose.'
        if(self.choice == "ROCK"):
            'Computer analysis when losing to rock.'
            self.scissor+=3
            self.paper+=1
            self.rock-=3
        elif(self.choice == "PAPER"):
            'Computer analysis when losing to paper.'
            self.rock+=3
            self.scissor+=1
            self.paper-=3
        else:
            'Computer analysis when losing to scissor'
            self.paper+=3
            self.rock+=1
            self.scissor-=3

    def choiceAnalysis(self):
        """
         " Full Computer Analysis.
         "
         " If it is being played for the first time or, 
         " all choice probabilities are at '0', the 
         " computer will choose a random choice.
         " 
         " Otherwise, the computer will perform a small 
         " calculation based on the choices in previous 
         " games and thus, decide which choice to make 
         " for the game.
         """
        options = ["ROCK", "PAPER", "SCISSORS"]
        if(self.rock == 0 or self.paper != 0 or self.scissor != 0):
            self.setChoice(options[randint(0,2)])
        else:
            size = self.rock + self.paper + self.scissor
            pcChoices = []
            index = 0

            while(index < size):
                for times in self.rock:
                    pcChoices[index] = 0
                    index+=1
                for times in self.paper:
                    pcChoices[index] = 1
                    index+=1
                for times in self.scissor:
                    pcChoices[index] = 2
                    index+=1
            
            self.setChoice(options[pcChoices[randint(0, size)]])
