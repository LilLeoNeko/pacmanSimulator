import unittest
from pacmanSimulator.components import Game

class TestGame(unittest.TestCase):

	def setUp(self):
		self.testGame = Game()
		#test data 1
		self.loc1 = (0,0)
		self.dir1 = 90
		#test data 2
		self.loc2 = (4,4)
		self.dir2 = 250
		#test data 3
		self.loc3 = (2,3)
		self.dir3 = 410
		#test data 4
		self.loc4 = (10,-10)
		self.dir4 = 560
		#test data 5
		self.loc5 = (-1,-2)
		self.dir5 = -10

	def tearDown(self):
		pass

	def test_place(self):
		self.testGame.place(self.loc1,self.dir1)
		self.assertEqual(self.testGame.pacman.location,self.loc1)
		self.assertEqual(self.testGame.pacman.direction,self.dir1)

		self.testGame.place(self.loc2,self.dir2)
		self.assertEqual(self.testGame.pacman.location,self.loc2)
		self.assertEqual(self.testGame.pacman.direction,self.dir2)

		self.testGame.place(self.loc3,self.dir3)
		self.assertEqual(self.testGame.pacman.location,self.loc3)
		self.assertEqual(self.testGame.pacman.direction,self.dir3%360)

		self.testGame.place(self.loc4,self.dir4)
		self.assertEqual(self.testGame.pacman.location,(2,3))
		self.assertEqual(self.testGame.pacman.direction,self.dir3%360)

		self.testGame.place(self.loc5,self.dir5)
		self.assertEqual(self.testGame.pacman.location,(2,3))
		self.assertEqual(self.testGame.pacman.direction,self.dir3%360)

		self.testGame.place(self.loc2,self.dir2)
		self.assertEqual(self.testGame.pacman.location,self.loc2)
		self.assertEqual(self.testGame.pacman.direction,self.dir2)

	def test_move(self):
		self.testGame.place(self.loc1,self.dir1)
		for i in range(2):
			self.testGame.move()
		self.assertEqual(self.testGame.pacman.location,(0,2))
		self.assertEqual(self.testGame.pacman.direction,90)

		self.testGame.place(self.loc1,self.dir1)
		for i in range(5):
			self.testGame.move()
		self.assertEqual(self.testGame.pacman.location,(0,4))
		self.assertEqual(self.testGame.pacman.direction,90)

		self.testGame.place(self.loc2,self.dir2)
		for i in range(2):
			self.testGame.move()
		self.assertEqual(self.testGame.pacman.location,self.loc2)
		self.assertEqual(self.testGame.pacman.direction,self.dir2)

	#def test_left(self):

	#def test_right(self):

	#def test_report(self):

if __name__ == '__main__':
	unittest.main()