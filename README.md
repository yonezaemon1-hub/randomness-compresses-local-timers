# Randomness Compresses Local Timers

Preprint v1.0.0 by **Ryutaro Yonezu (Independent Researcher)**.

Full title:

**Randomness Compresses Local Timers: Exact State Complexity of Beacon-Triggered Broadcast in Anonymous Dynamic Networks**

## Main result

For known `n >= 2`, within the deterministic beacon-triggered locally timed active-interval (BTAI) class defined in the paper,

```text
S_det_BTAI(n) = n + 1
```

persistent states are necessary and sufficient. Hence the exact binary persistent-memory requirement is

```text
M_det_BTAI(n) = ceil(log2(n + 1)) bits.
```

Before the state-count argument, the paper proves a broader architecture-level fact: every correct deterministic beacon-triggered bounded, non-renewing active-interval protocol must support an active interval of at least

```text
L >= n - 1
```

rounds.

## Scope

The exact theorem is deliberately restricted to the locally timed beacon-triggered active-interval subclass. It does **not** prove an `Omega(log n)` lower bound for unrestricted deterministic non-idle-start stabilizing broadcast. Collective/distributed timers, activity renewal while active, message-driven timing, and additional external timing signals are outside the exact theorem.

## Relation to randomized broadcast

The result isolates the deterministic local-timer cost behind the active-interval architecture. Turau's SAND 2026 randomized construction uses Morris-style approximate counting to realize the same broad beacon/active-interval idea with `O(log log n)` local memory with high probability when `n` is known.

## Files

- `Yonezu_2026_Randomness_Compresses_Local_Timers.pdf` — authoritative v1.0.0 manuscript PDF.
- `paper.tex` — LaTeX manuscript source.
- `references.bib` — bibliography.
- `PROOF_AUDIT.md` — theorem-chain and off-by-one audit.
- `PRIOR_ART_AUDIT.md` — targeted novelty and claim-boundary audit.
- `CITATION.cff` — citation metadata; DOI can be backfilled after publication.
- `.zenodo.json` — source/software deposit metadata.
- `paper.publish.json` — paper-deposit metadata checklist.
- `LICENSE` — MIT license for source/package materials.
- `LICENSE_PAPER.txt` — CC BY 4.0 notice for the manuscript text/PDF.

## Reproduction

A standard LaTeX installation with BibTeX can compile the manuscript source:

```bash
pdflatex paper.tex
bibtex paper
pdflatex paper.tex
pdflatex paper.tex
```

The authoritative publication artifact is the PDF released with v1.0.0.

## Current status

**PREPRINT v1.0.0 / NOT PEER REVIEWED.**

The theorem has an analytic proof and a targeted prior-art audit. The exact characterization is claimed only for the explicitly defined BTAI subclass.

## Repository

GitHub: https://github.com/yonezaemon1-hub/randomness-compresses-local-timers

## DOI

Paper DOI: **pending Zenodo publication**  
Software/source-package DOI: **pending Zenodo publication**
