# Prior-Art and Claim-Boundary Audit

Paper: **Randomness Compresses Local Timers: Exact State Complexity of Beacon-Triggered Broadcast in Anonymous Dynamic Networks**

Audit date: 2026-09-07.

## Direct literature

1. **Parzych and Daymude, DISC 2024 / Distributed Computing 2026** — establish deterministic memory lower bounds for anonymous dynamic broadcast. For idle-start stabilizing termination they prove a superconstant lower bound and give the `O(log n)`-memory Countdown algorithm. Their work leaves the deterministic non-idle-start stabilizing regime unresolved.

2. **Turau, SAND 2026** — gives a randomized non-idle-start stabilizing-broadcast algorithm for known `n` using Morris-style approximate counting, `O(log log n)` local memory with high probability, and constant-size messages. Its communication pattern motivates the beacon-triggered active-interval abstraction used here.

3. **Morris 1978; Nelson and Yu 2022** — approximate-counting results used to explain why randomized local timers can escape the deterministic state-repetition barrier. No novelty is claimed for approximate counting itself.

## Narrow novelty claim

The manuscript claims novelty only for the following characterization:

- every correct deterministic beacon-triggered bounded, non-renewing active-interval architecture must support an interval of at least `n-1` rounds; and
- in the locally timed deterministic subclass, where active-state transitions depend only on persistent local state, the exact number of persistent states is `n+1`.

A targeted literature search through September 2026 did not identify a prior exact `n+1` state-complexity theorem for this explicitly defined beacon-triggered local-timer subclass.

## Claims deliberately not made

The paper does **not** claim:

- an `Omega(log n)` lower bound for all deterministic non-idle-start stabilizing broadcast algorithms;
- novelty for finite-state pumping or state-repetition arguments in general;
- novelty for countdown timers, active intervals, Morris counters, or approximate counting in general;
- a lower bound for protocols that encode time collectively across nodes;
- a lower bound for protocols whose active intervals can be renewed while active;
- a lower bound for protocols using message-driven or external timing information.

## Verdict

The claim is intentionally subclass-specific. Within that scope, no direct prior exact characterization was located in the targeted audit. This is a preprint novelty audit, not a guarantee against undiscovered prior art or a substitute for peer review.
