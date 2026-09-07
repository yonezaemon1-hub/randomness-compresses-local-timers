#!/usr/bin/env python3
"""Finite arithmetic audit for Randomness Compresses Local Timers.

Computational evidence only; the exact proof is in the manuscript.
"""

import csv
import math
from pathlib import Path

OUT = Path(__file__).resolve().parent


def bits_for_states(s: int) -> int:
    return math.ceil(math.log2(s))


def main() -> None:
    path = OUT / "local_timer_finite_table.csv"
    prev_states = 0
    prev_bits = 0
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["n", "required_active_interval_L", "exact_states", "persistent_bits"])
        for n in range(2, 129):
            L = n - 1
            states = n + 1
            bits = bits_for_states(states)
            assert states == L + 2
            assert states > prev_states
            assert bits >= prev_bits
            assert 2 ** bits >= states
            if bits > 0:
                assert 2 ** (bits - 1) < states
            w.writerow([n, L, states, bits])
            prev_states, prev_bits = states, bits
    print("PASS_LOCAL_TIMER_FINITE_AUDIT")
    print(path.name)


if __name__ == "__main__":
    main()
