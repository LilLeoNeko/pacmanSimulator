import sys
from pacmanSimulator.components import Pacman, Map, Game
from pacmanSimulator.helperFunctions import *

##########Main function##########
def startGame():
	game = Game()
	#get place command first
	getInput = input()
	while not isPlaceValid(getInput, game.getGameMap()):
		print("invalid command, please PLACE pacman correctly\n")
		getInput = input()
	else:
		#start place the pacman
		handlePlace(getInput, game)
		print("Pacman placed correctly\n")

		#take other command
		getInput = input()
		while getInput != "REPORT":
			split = getInput.split()
			if len(split) == 1:
				if getInput == "MOVE":
					game.move()
				if getInput == "LEFT":
					game.left()
				if getInput == "RIGHT":
					game.right()
			else:
				if isPlaceValid(getInput, game.getGameMap()):
					handlePlace(getInput,game)
			print("\n")
			getInput = input()
		else:
			pacman = game.getPacman()
			print(pacman.getLocation())
			print(degreeToDirection(pacman.getDirection()) + "\n")

if __name__ == '__main__':
    startGame()