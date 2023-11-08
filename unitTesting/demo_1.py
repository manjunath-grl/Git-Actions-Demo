import unittest
import sys

sys.path.append('..')

from samplePythonfiles.demo_1 import squ, divide, cube


class TestMathFunctions(unittest.TestCase):

    def test_square(self):
        result = squ(4)
        self.assertEqual(16, result)
        result = squ(0)
        self.assertEqual(0, result)
        result = squ(-4)
        self.assertEqual(16, result)

    def test_cube(self):
        self.assertEqual(cube(2), 8)
        self.assertNotEqual(cube(4), 63)

    def test_divide(self):
        with self.assertRaises(ZeroDivisionError):
            divide(42, 0)
        self.assertEqual(divide(1,2), 0.5)


if __name__ == '__main__':
    unittest.main()
