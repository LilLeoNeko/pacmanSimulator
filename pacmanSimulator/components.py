##########Pacman Class Start##########
class Pacman():
	def __init__(self, location, direction):
		self.location = location
		self.direction = direction

	def updateLocation(self,location):
		self.location = location

	def getLocation(self):
		return self.location

	def updateDirection(self,direction):
		self.direction = direction%360

	def getDirection(self):
		return self.direction
##########Pacman Class END##########

##########Map Class Start##########
class Map:
	def __init__(self,width,height):
		self.width = width
		self.height = height

	def isValidPos(self,newLocation):
		x,y = newLocation
		if x > self.width or y > self.height:
			return False
		else:
			return True
##########Map Class END##########

##########Game Class Start##########
class Game():
	def __init__(self):
		self.gameMap = Map(5,5)
		self.pacman = Pacman((0,0), 90)

	def place(self, location, direction):
		if self.gameMap.isValidPos(location):
			self.pacman.updateLocation(location)
			self.pacman.updateDirection(direction)

	def move(self):
		x,y = self.pacman.getLocation()
		curDir = self.pacman.getDirection()

		if curDir == 90:
			y += 1
			newLoc = (x,y)
			if self.gameMap.isValidPos(newLoc):
				self.pacman.updateLocation(newLoc)
		if curDir == 270:
			y-=1
			newLoc = (x,y)
			if self.gameMap.isValidPos(newLoc):
				self.pacman.updateLocation(newLoc)
		if curDir == 180:
			x-=1
			newLoc = (x,y)
			if self.gameMap.isValidPos(newLoc):
				self.pacman.updateLocation(newLoc)
		if curDir == 0:
			x+=1
			newLoc = (x,y)
			if self.gameMap.isValidPos(newLoc):
				self.pacman.updateLocation(newLoc)

	def left(self):
		curDir = self.pacman.getDirection()
		self.pacman.updateDirection(curDir+90)
		
	def right(self):
		curDir = self.pacman.getDirection()
		self.pacman.updateDirection(curDir-90)

	def getGameMap(self):
		return self.gameMap

	def getPacman(self):
		return self.pacman

##########Game Class END##########