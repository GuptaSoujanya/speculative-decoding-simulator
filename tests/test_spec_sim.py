import unittest
from spec_sim.math_model import compute_expected_accepted_tokens, compute_theoretical_speedup
from spec_sim.simulator import SpeculativeSimulator

class TestSpecSim(unittest.TestCase):
    def test_expected_accepted(self):
        # If alpha = 0, only 1 token accepted
        self.assertAlmostEqual(compute_expected_accepted_tokens(4, 0.0), 1.0)
        # If alpha = 1, all gamma + 1 accepted
        self.assertAlmostEqual(compute_expected_accepted_tokens(4, 1.0), 5.0)

    def test_speedup_positive(self):
        speedup = compute_theoretical_speedup(gamma=4, alpha=0.8, cost_ratio=0.1)
        self.assertGreater(speedup, 1.5)

    def test_monte_carlo(self):
        sim = SpeculativeSimulator(alpha=0.75, cost_ratio=0.15)
        res = sim.run_monte_carlo(gamma=3, total_steps=100)
        self.assertAlmostEqual(res["empirical_accepted_tokens"], res["theoretical_accepted_tokens"], delta=0.5)

if __name__ == "__main__":
    unittest.main()
