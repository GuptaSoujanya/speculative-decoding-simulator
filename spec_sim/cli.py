import argparse
from .math_model import compute_expected_accepted, compute_speedup

def main():
    parser = argparse.ArgumentParser(prog="spec-sim")
    parser.add_argument("--alpha", type=float, default=0.75)
    parser.add_argument("--cost-ratio", type=float, default=0.12)
    parser.add_argument("--gamma", type=int, default=4)
    args = parser.parse_args()

    e_n = compute_expected_accepted(args.gamma, args.alpha)
    speedup = compute_speedup(args.gamma, args.alpha, args.cost_ratio)

    print("\n" + "="*52)
    print("      SPECULATIVE DECODING SPEEDUP ANALYSIS")
    print("="*52)
    print(f" Draft Acceptance Rate (alpha): {args.alpha*100:.1f}%")
    print(f" Speculative Window (gamma)   : K={args.gamma}")
    print(f" Expected Accepted Tokens     : {e_n:.2f} tok/step")
    print(f" Effective Wall-Clock Speedup : {speedup:.2f}x faster")
    print("="*52 + "\n")

if __name__ == "__main__":
    main()
