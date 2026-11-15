import unittest

from factorial import factorial

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        # Test basic cases
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

        # Test negative input raises ValueError
        with self.assertRaises(ValueError):
            factorial(-5)

if __name__ == "__main__":
    unittest.main()

