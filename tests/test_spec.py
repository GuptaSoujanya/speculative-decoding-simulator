import unittest
from spec_sim.math_model import compute_expected_accepted, compute_speedup

class TestSpec(unittest.TestCase):
    def test_zero_alpha(self):
        self.assertEqual(compute_expected_accepted(4, 0.0), 1.0)
    def test_speedup(self):
        self.assertGreater(compute_speedup(4, 0.8, 0.1), 1.5)

if __name__ == "__main__":
    unittest.main()
