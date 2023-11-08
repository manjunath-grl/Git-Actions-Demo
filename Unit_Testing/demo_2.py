import unittest

from Sample_Python_files.demo_2 import check_Prime


class TestPrime(unittest.TestCase):
    def test_prime_not_prime(self):
        self.assertTrue(self.demo_2.check_Prime.is_prime(2))
        self.assertTrue(self.demo_2.check_Prime.is_prime(3))
        self.assertFalse(self.demo_2.check_Prime.is_prime(9))
        self.assertTrue(self.demo_2.check_Prime.is_prime(11))

if __name__=='__main__':
	unittest.main()