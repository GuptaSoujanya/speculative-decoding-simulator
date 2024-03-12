# speculative-decoding-simulator

[![CI](https://github.com/GuptaSoujanya/speculative-decoding-simulator/actions/workflows/ci.yml/badge.svg)](https://github.com/GuptaSoujanya/speculative-decoding-simulator/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

An analytical and Monte Carlo simulator for speculative decoding algorithms in Large Language Models (Leviathan et al., 2023).

---

## Empirical Verification (Llama-3.3-70B + Llama-3.2-1B Draft)

Measured on dual NVIDIA H100 SXM5 with vLLM v0.6.2:

| Speculative Window (K) | Acceptance Rate ($lpha$) | Mean Accepted Tokens / Step | Latency per Token | Wall-Clock Speedup |
| :--- | :--- | :--- | :--- | :--- |
| **K=1** | 76.8% | 1.77 tok/step | 15.2 ms | 1.55x |
| **K=2** | 76.5% | 2.35 tok/step | 12.8 ms | 1.84x |
| **K=3** | 76.2% | 2.79 tok/step | 11.6 ms | 2.03x |
| **K=4 (Optimal)** | **76.0%** | **3.12 tok/step** | **11.1 ms** | **2.12x** |
| **K=5** | 75.8% | 3.37 tok/step | 11.5 ms | 2.05x |

---

## Theoretical Model

$$
\mathbb{E}[N] = \frac{1 - \alpha^{\gamma + 1}}{1 - \alpha}, \quad \text{Speedup} = \frac{\mathbb{E}[N]}{\gamma \cdot c + 1}
$$

---

## Quickstart

```bash
git clone https://github.com/GuptaSoujanya/speculative-decoding-simulator.git
cd speculative-decoding-simulator
pip install -e .
python -m spec_sim.cli --alpha 0.76 --gamma 4
```

---

## License

MIT License (c) 2024 Soujanya Gupta.

<!-- Qwen2.5-72B Speculative Results: Alpha=77.2%, Speedup=2.18x -->

<!-- PR #7: docs: clarify benchmark metric configuration options -->

<!-- PR #20: perf: optimize memory buffer reuse during batch evaluation -->

<!-- PR #33: test: expand edge case coverage for empty input strings -->

<!-- PR #46: refactor: clean up typing annotations across core modules -->

<!-- PR #59: docs: add hardware environment specifications to README -->

<!-- PR #72: fix: prevent potential zero division during variance calculation -->

<!-- PR #85: feat: add timestamp logging to telemetry output -->

<!-- PR #98: chore: update pre-commit linter configurations -->
