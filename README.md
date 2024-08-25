# speculative-decoding-simulator

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)

An analytical and Monte Carlo simulator for speculative decoding algorithms in Large Language Models (Leviathan et al., 2023).

---

## Theoretical Model

Expected number of tokens accepted per verification cycle:

$$
\mathbb{E}[N] = \frac{1 - \alpha^{\gamma + 1}}{1 - \alpha}
$$

Wall-clock inference speedup:

$$
\text{Speedup} = \frac{\mathbb{E}[N]}{\gamma \cdot c + 1}
$$

where $\alpha$ is draft acceptance probability, $\gamma$ is speculative window size, and $c = \frac{\text{cost}(\text{draft})}{\text{cost}(\text{target})}$.

---

## Quickstart

```bash
# Run optimal window sweep
python -m spec_sim.cli --alpha 0.75 --cost-ratio 0.12 --sweep
```

---

## License

MIT License (c) 2023 Soujanya Gupta.
