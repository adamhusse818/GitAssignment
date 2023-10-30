import unittest
import assignment

class MyTestCase(unittest.TestCase):
	def test_character(self):
		with self.assertRaises(TypeError):
			assignment.add("w", 4)


if __name__ == '__main__':
	unittest.main()
