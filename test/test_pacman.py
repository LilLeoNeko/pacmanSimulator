import unittest
from pacmanSimulator.components import Pacman

class TestPacman(unittest.TestCase):

	def test_location(self):
		pac_1 = Pacman((1,1),90)
		pac_2 = Pacman((2,3),180)

		self.assertEqual(pac_1.location,(1,1))
		self.assertEqual(pac_2.location,(2,3))
	def test_setLocation(self):
		pac_1 = Pacman((1,1),90)
		pac_2 = Pacman((2,3),180)

		pac_1.updateLocation((2,3))
		pac_2.updateLocation((1,1))

		self.assertEqual(pac_1.location,(2,3))
		self.assertEqual(pac_2.location,(1,1))

	def test_direction(self):
		pac_1 = Pacman((1,1),90)
		pac_2 = Pacman((2,3),180)

		self.assertEqual(pac_1.direction,90)
		self.assertEqual(pac_2.direction,180)

	def test_setDirection(self):
		pac_1 = Pacman((1,1),90)
		pac_2 = Pacman((2,3),180)

		pac_1.updateDirection(180)
		pac_2.updateDirection(90)

		self.assertEqual(pac_1.direction,180)
		self.assertEqual(pac_2.direction,90)

if __name__ == '__main__':
	unittest.main()