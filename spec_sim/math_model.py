import math

def compute_expected_accepted(gamma: int, alpha: float) -> float:
    if abs(alpha - 1.0) < 1e-6: return float(gamma + 1)
    if alpha <= 0.0: return 1.0
    return (1.0 - math.pow(alpha, gamma + 1)) / (1.0 - alpha)

def compute_speedup(gamma: int, alpha: float, cost_ratio: float) -> float:
    e_n = compute_expected_accepted(gamma, alpha)
    denom = (gamma * cost_ratio) + 1.0
    return round(e_n / denom, 3)
