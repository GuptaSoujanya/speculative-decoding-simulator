import random
from typing import List, Dict, Any
from .math_model import compute_expected_accepted_tokens, compute_theoretical_speedup

class SpeculativeSimulator:
    """Monte Carlo simulation of draft-target speculative decoding loops."""

    def __init__(self, alpha: float = 0.72, cost_ratio: float = 0.15):
        self.alpha = alpha
        self.cost_ratio = cost_ratio

    def run_monte_carlo(self, gamma: int = 4, total_steps: int = 500) -> Dict[str, Any]:
        accepted_tokens_log = []
        for _ in range(total_steps):
            accepted = 0
            for k in range(gamma):
                if random.random() <= self.alpha:
                    accepted += 1
                else:
                    break
            # +1 for target model sample on reject or step boundary
            accepted_tokens_log.append(accepted + 1)

        empirical_mean = sum(accepted_tokens_log) / len(accepted_tokens_log)
        theoretical_mean = compute_expected_accepted_tokens(gamma, self.alpha)
        speedup = compute_theoretical_speedup(gamma, self.alpha, self.cost_ratio)

        return {
            "gamma": gamma,
            "acceptance_rate_alpha": self.alpha,
            "cost_ratio_c": self.cost_ratio,
            "empirical_accepted_tokens": round(empirical_mean, 3),
            "theoretical_accepted_tokens": round(theoretical_mean, 3),
            "speedup_factor": speedup
        }

    def sweep_gamma(self, max_gamma: int = 8) -> List[Dict[str, Any]]:
        return [self.run_monte_carlo(gamma=g) for g in range(1, max_gamma + 1)]
