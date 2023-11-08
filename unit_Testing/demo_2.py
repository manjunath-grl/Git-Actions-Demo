import unittest
import sys

sys.path.append('..')

from sample_Python_files.demo_2 import *

class CheckPrime(unittest.TestCase):
    def test_prime(self):
        print("Running Unit test to check value 3 is Prime or not")
        self.assertTrue(is_prime(3))


if __name__ == '__main__':
      unittest.main()
