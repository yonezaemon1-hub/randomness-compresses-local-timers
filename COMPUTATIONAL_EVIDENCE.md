# Computational evidence backfill

Status: candidate for a future manuscript version; the current Zenodo PDF remains unchanged.

This is an exact state-complexity theorem paper. The appropriate computational evidence is therefore a finite arithmetic/state table rather than stochastic simulation.

## Added audit

Run:

```bash
python audit/computational_evidence.py
```

The script tabulates, for a finite range of network sizes, the deterministic active-interval requirement `L >= n-1`, the exact locally timed BTAI state count `S_det_BTAI(n) = n+1`, and the corresponding persistent-memory count `ceil(log2(n+1))` bits.

It also checks basic monotonicity and the exact conversion between state count and bit count on the audited range.

## Scope

The computation is a boundary/off-by-one audit of the theorem statement. It does not extend the lower bound to unrestricted deterministic non-idle-start broadcast, and it does not claim an exact randomized minimum.
