import unittest
from solve import solve

class TestSolveEquation(unittest.TestCase):
    
    def test_no_roots(self):
        self.assertEqual(solve(1, 0, 1), [])

    def test_two_roots(self):
        self.assertEqual(sorted(solve(1, 0, -1)), [-1, 1])

    def test_one_root_double_multiplicity(self):
        self.assertEqual(solve(1, 2, 1), [-1, -1])

    def test_a_zero(self):
        with self.assertRaises(ValueError):
            solve(0, 2, 1)

if __name__ == '__main__':
    unittest.main()

