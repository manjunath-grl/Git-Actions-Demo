import unittest
import sys

print(sys.path)

from Sample_Python_files.demo_1 import Calculator

#sys.path.insert(0, '/home/grl/Desktop/Git-Actions-Demo/Sample_Python_files')


class Calculator(unittest.TestCase):
    def test_to_see_square_root_works_ok(self):
        result = self.Calculator.squ(4)
        self.assertEqual(16, result)
        result = self.Calculator.squ(0)
        self.assertEqual(0, result)
        result = self.Calculator.squ(-4)
        self.assertEqual(16, result)

if __name__=='__main__':
	unittest.main()