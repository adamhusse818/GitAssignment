import unittest
import assignment

class MyTestCase(unittest.TestCase):
	def test_add(self):
		self.assertEqual(assignment.add(2, 3), 5)

if __name__ == '__main__':
	unittest.main()