import unittest
from pacmanSimulator.components import Map
class TestMap(unittest.TestCase):

	def test_map(self):
		gameMap1 = Map(5,5)
		gameMap2 = Map(10,7)
		gameMap3 = Map(150,897)

		self.assertEqual((gameMap1.width,gameMap1.height),(4,4))
		self.assertEqual((gameMap2.width,gameMap2.height),(9,6))
		self.assertEqual((gameMap3.width,gameMap3.height),(149,896))

	def test_isValidPos(self):
		map1 = Map(150,897)
		test1 = map1.isValidPos((123,564))
		test2 = map1.isValidPos((0,0))
		test3 = map1.isValidPos((-566,0))
		test4 = map1.isValidPos((-126,-987))
		test5 = map1.isValidPos((150,897))
		self.assertEqual(test1,True)
		self.assertEqual(test2,True)
		self.assertEqual(test3,False)
		self.assertEqual(test4,False)
		self.assertEqual(test5,False)

if __name__ == '__main__':
	unittest.main()