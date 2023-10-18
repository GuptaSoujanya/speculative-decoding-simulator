import math
from typing import Dict, Any

def compute_expected_accepted_tokens(gamma: int, alpha: float) -> float:
    """
    Compute expected accepted tokens E[N] per speculative step (Leviathan et al., 2023).
    Formula: (1 - alpha^(gamma + 1)) / (1 - alpha)
    """
    if abs(alpha - 1.0) < 1e-6:
        return float(gamma + 1)
    if alpha <= 0.0:
        return 1.0 # Only target fallback token accepted
    return (1.0 - math.pow(alpha, gamma + 1)) / (1.0 - alpha)

def compute_theoretical_speedup(gamma: int, alpha: float, cost_ratio: float) -> float:
    """
    Theoretical wall-clock speedup factor S:
    S = E[N] / (gamma * cost_ratio + 1)
    where cost_ratio = time(draft) / time(target).
    """
    expected_n = compute_expected_accepted_tokens(gamma, alpha)
    step_cost = (gamma * cost_ratio) + 1.0
    return round(expected_n / step_cost, 3)
