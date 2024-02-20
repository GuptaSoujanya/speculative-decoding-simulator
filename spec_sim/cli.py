import argparse
from .simulator import SpeculativeSimulator

def main():
    parser = argparse.ArgumentParser(
        prog="spec-sim",
        description="speculative-decoding-simulator: Benchmark speculative decoding acceleration."
    )
    parser.add_argument("--alpha", type=float, default=0.75, help="Draft model acceptance rate (0.0 to 1.0)")
    parser.add_argument("--cost-ratio", type=float, default=0.12, help="Draft-to-target latency cost ratio")
    parser.add_argument("--gamma", type=int, default=4, help="Speculative window draft length")
    parser.add_argument("--sweep", action="store_true", help="Sweep gamma from 1 to 8")

    args = parser.parse_args()

    sim = SpeculativeSimulator(alpha=args.alpha, cost_ratio=args.cost_ratio)

    print("\n" + "="*56)
    print("      SPECULATIVE DECODING SPEEDUP ANALYSIS")
    print("="*56)
    print(f" Acceptance Rate (alpha) : {args.alpha * 100:.1f}%")
    print(f" Cost Ratio (c)          : {args.cost_ratio:.3f} (Draft vs Target)")
    print("-" * 56)

    if args.sweep:
        results = sim.sweep_gamma(max_gamma=6)
        print("| Gamma (K) | E[Accepted] | Speedup Factor | Efficiency |")
        print("| :--- | :--- | :--- | :--- |")
        for r in results:
            eff = f"{r['speedup_factor']:.2f}x"
            print(f"| {r['gamma']:^9} | {r['theoretical_accepted_tokens']:^11.2f} | {eff:^14} | Optimal" if r['speedup_factor'] == max(x['speedup_factor'] for x in results) else f"| {r['gamma']:^9} | {r['theoretical_accepted_tokens']:^11.2f} | {eff:^14} |          |")
    else:
        res = sim.run_monte_carlo(gamma=args.gamma)
        print(f" Speculative Window (gamma) : {args.gamma}")
        print(f" Expected Accepted Tokens   : {res['theoretical_accepted_tokens']:.2f} tokens/step")
        print(f" Effective Speedup Factor   : {res['speedup_factor']:.2f}x faster than autoregressive")
    print("="*56 + "\n")

if __name__ == "__main__":
    main()
