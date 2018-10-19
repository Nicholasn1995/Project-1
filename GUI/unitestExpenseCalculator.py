import unittest
from allFunctions import checkIsInteger
from allFunctions import checkTitleNoInt
class Test_testFile(unittest.TestCase):

	def test_isInteger(self):
		self.assertTrue(checkIsInteger(25))

	def test_checkTitleNoInt(self):
		self.assertFalse(checkTitleNoInt("hell0w0r1d"))
		self.assertTrue(checkTitleNoInt("HelloWorld"))


if __name__ == '__main__':
    unittest.main()
