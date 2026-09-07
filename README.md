# Randomness Compresses Local Timers

Preprint v1.0.0 by **Ryutaro Yonezu (Independent Researcher)**.

## Main result

For known `n >= 2`, within the deterministic beacon-triggered locally timed active-interval (BTAI) class defined in the paper,

`S_det(n) = n + 1` persistent states,

so the exact binary persistent-memory requirement is

`ceil(log2(n + 1))` bits.

The paper first proves a broader architecture-level fact: any deterministic beacon-triggered bounded, non-renewing active-interval protocol must support an active interval of at least `n - 1` rounds. The exact state lower bound then follows only for the local-timer subclass.

## Scope

This result does **not** prove an Omega(log n) lower bound for all deterministic non-idle-start stabilizing broadcast algorithms. Collective/distributed timers, activity renewal, message-driven timing, and different communication architectures are outside the exact theorem.

## Files

- `Yonezu_2026_Randomness_Compresses_Local_Timers.pdf` - authoritative v1.0.0 manuscript PDF
- `paper.tex` - LaTeX source
- `references.bib` - bibliography
- `PROOF_AUDIT.md` - theorem and off-by-one audit
- `PRIOR_ART_AUDIT.md` - targeted novelty audit through 2026-09-06
- `sanity_check.py` - lower-bound schedule checks and exhaustive small-n upper-bound model check
- `CITATION.cff` - citation metadata
- `.zenodo.json` - source/software deposit metadata
- `paper.publish.json` - paper-deposit metadata checklist
- `MANIFEST_SHA256.txt` - integrity manifest

## Current status

**PREPRINT v1.0.0 / NOT PEER REVIEWED.**

The theorem has an analytic proof, targeted prior-art checking, deterministic timing sanity checks for `n=2..128`, and exhaustive adversarial snapshot checking of the matching upper-bound protocol for `n=2..5`. The computational checks are supplementary and are not substitutes for the proof.

## Repository

GitHub: https://github.com/yonezaemon1-hub/randomness-compresses-local-timers

## DOI

Paper DOI: **pending Zenodo publication**  
Software/source-package DOI: **pending Zenodo publication**
