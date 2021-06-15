from computer import *
import os, sys

def cleaning():
    'Method that allows to clean the console, independent of the OS being used.'
    if sys.platform.startswith('win'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')

def game():
    'Method that establishes the guidelines for the "Rock, Paper, Scissors" game.'

    answer = "YES"
    played_games = 0
    tied_games = 0
    
    player = Player(0, 0)
    pc = Computer(0, 0)

    game_options = ["ROCK", "PAPER", "SCISSORS"]
    play_options = ["YES", "NO"]
    rules = {"ROCK": "SCISSORS", "PAPER": "ROCK", "SCISSORS": "PAPER"}

    while(answer == "YES"):

        print("\nLet's play 'ROCK, PAPER or SCISSORS'")

        choice = ""

        while(choice not in game_options):
            choice = input("\nWhat is your choice?\n-> ROCK\n-> PAPER\n-> SCISSORS\nEnter your choice: ").upper()
            if(choice not in game_options):
                cleaning()
                print("\nYou have entered an invalid option. Please re-enter your choice.")

        player.setChoice(choice)
        pc.choiceAnalysis()

        if(rules[player.getChoice()] == pc.getChoice()):
            print(f"\nYou won! The PC has chosen '{pc.getChoice()}' and you chose '{player.getChoice()}'.")
            player.updateScore()
            pc.lose()
        elif(rules[pc.getChoice()] == player.getChoice()):
            print(f"\nYou lose! The PC has chosen '{pc.getChoice()}' and you chose '{player.getChoice()}'.")
            pc.win()
        else:
            print(f"\nTie! You and the PC have chosen '{choice}'.")
            pc.tie()
            tied_games+=1

        played_games+=1

        print(f"\n- PC Score: {pc.getScore()} - Your Score: {player.getScore()} - Played games: {played_games} - Tied games: {tied_games} -")

        answer = ""

        while(answer not in play_options):
            answer = input("\nDo you want to continue playing? \n-> Yes\n-> No\nEnter your choice: ").upper()
            if(answer not in play_options):
                cleaning()
                print("\nYou have entered an invalid option. Please re-enter your choice.")
            else:
                cleaning()
