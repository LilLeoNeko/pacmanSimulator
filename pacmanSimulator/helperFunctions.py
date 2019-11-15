from pacmanSimulator.components import Pacman, Map, Game

##########Helper functions START##########
def directionToDegree(direction):
	if direction == "NORTH":
		return 90
	if direction == "SOUTH":
		return 270
	if direction == "WEST":
		return 180
	if direction == "EAST":
		return 0
	return -1

def degreeToDirection(degree):
	if degree == 90:
		return "NORTH"
	if degree == 270:
		return "SOUTH"
	if degree == 180:
		return "WEST"
	if degree == 0:
		return "EAST"
	return "ERROR"

def isPlaceValid(tempString, gameMap):
	getInput = tempString.split()
	if len(getInput) ==0:
		return False
	if getInput[0]!="PLACE" or len(getInput)<=1 or len(getInput)>2:
		return False
	else:
		getInfo = getInput[1].split(',')
		if len(getInfo) != 3\
			or not getInfo[0].isdigit() or not getInfo[1].isdigit\
			or getInfo[2] not in ["NORTH","SOUTH","WEST","EAST"]:
			return False
		else:
			loc= (int(getInfo[0]),int(getInfo[1]))
			direction = directionToDegree(getInfo[2])
			if not gameMap.isValidPos(loc):
				return False
	return True

def handlePlace(string, game):
	inputContent = string.split()
	placeCommand = inputContent[0]
	placeDetail = inputContent[1].split(',')
	placeLoc = (int(placeDetail[0]),int(placeDetail[1]))
	placeDir = directionToDegree(placeDetail[2])

	game.place(placeLoc,placeDir)

##########Helper functions END##########