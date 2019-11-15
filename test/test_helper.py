import unittest
from pacmanSimulator.components import Map, Game
from pacmanSimulator.helperFunctions import *

class TestHelper(unittest.TestCase):
	def setUp(self):
		self.game = Game()
		#error direction
		self.dir1 = ""
		self.dir2 = "HELLO"
		#correct direction
		self.dir3 = "NORTH"
		self.dir4 = "SOUTH"
		self.dir5 = "WEST"
		self.dir6 = "EAST"
		#correct degree
		self.deg1 = 0
		self.deg2 = 90
		self.deg3 = 180
		self.deg4 = 270
		#error degree
		self.deg5 = 360
		self.deg6 = -180
		self.deg7 = 1
		self.deg8 = -100
		#error place command
		self.place1 = "hello"
		self.place2 = ""
		self.place3 = "PLACE"
		self.place4 = "PLACE 1,1"
		self.place5 = "PLACE 1,NORTH,1"
		self.place6 = "PLACE NORTH,1,2"
		self.place7 = "PLACE 2,3,EMPTY"
		self.place8 = "PLACE 123,3,NORTH"
		#correct place command
		self.place9 = "PLACE 1,1,NORTH"
		self.place10 = "PLACE 2,3,SOUTH"
		self.place11 = "PLACE 4,4,WEST"
	def tearDown(self):
		pass

	def test_directionToDegree(self):
		self.assertEqual(directionToDegree(self.dir1),-1)
		self.assertEqual(directionToDegree(self.dir2),-1)
		self.assertEqual(directionToDegree(self.dir3),90)
		self.assertEqual(directionToDegree(self.dir4),270)
		self.assertEqual(directionToDegree(self.dir5),180)
		self.assertEqual(directionToDegree(self.dir6),0)

	def test_degreeToDirection(self):
		self.assertEqual(degreeToDirection(self.deg1),"EAST")
		self.assertEqual(degreeToDirection(self.deg2),"NORTH")
		self.assertEqual(degreeToDirection(self.deg3),"WEST")
		self.assertEqual(degreeToDirection(self.deg4),"SOUTH")
		self.assertEqual(degreeToDirection(self.deg5),"ERROR")
		self.assertEqual(degreeToDirection(self.deg6),"ERROR")
		self.assertEqual(degreeToDirection(self.deg7),"ERROR")
		self.assertEqual(degreeToDirection(self.deg8),"ERROR")

	def test_isPlaceValid(self):
		self.assertFalse(isPlaceValid(self.place1, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place2, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place3, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place4, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place5, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place6, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place7, self.game.gameMap))
		self.assertFalse(isPlaceValid(self.place8, self.game.gameMap))

		self.assertTrue(isPlaceValid(self.place9, self.game.gameMap))
		self.assertTrue(isPlaceValid(self.place10, self.game.gameMap))
		self.assertTrue(isPlaceValid(self.place11, self.game.gameMap))

if __name__ == '__main__':
	unittest.main()