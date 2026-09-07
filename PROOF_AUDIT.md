# Proof Audit

Paper: **Randomness Compresses Local Timers: Exact State Complexity of Beacon-Triggered Broadcast in Anonymous Dynamic Networks**

Status: preprint v1.0.0 candidate / not peer reviewed.

## Audited claims

### Lemma 1 — moving-frontier lower bound

For every deterministic beacon-triggered bounded-interval (BTBI) protocol on known `n >= 2`, correctness on all 1-interval-connected dynamic networks forces

`L(A) >= n - 1`.

The adversary first informs `v1,...,v_{n-1}` along a path while keeping `v_n` uninformed. It then makes `v_n` adjacent to exactly one informed frontier node and rotates that frontier through the `n-1` informed nodes. If every non-renewing active interval has length at most `n-2`, each frontier node is quiet again before it is reused, so `v_n` never receives `INF` although every snapshot remains connected.

The timing/off-by-one point checked explicitly is that a frontier node is reused only after `n-1` rounds, strictly longer than the assumed interval bound `n-2`.

### Lemma 2 — no repeated active state

In the locally timed BTAI subclass, active-state evolution is a deterministic function `f : A -> A union Q` independent of received messages. If one active state repeats within an interval, determinism forces a cycle and the node can never reach `Q`. Hence an interval of length `ell` visits `ell` distinct active states.

Therefore `|A| >= L(A)`.

### Theorem 1 — exact state complexity

Combining the two lemmas gives `|A| >= n-1`. At least one uninformed state and one informed quiet state are additionally required, and these semantic roles are disjoint because they emit `IDLE`, `INF`, and silence respectively. Thus

`|Sigma| >= 1 + 1 + (n-1) = n+1`.

The matching construction uses states

`{U, Q, A_1, ..., A_{n-1}}`

with a deterministic countdown `A_i -> A_{i-1}`, `A_1 -> Q`, beacon-triggered restart from `Q`, and entry into `A_{n-1}` from `U` on receipt of `INF`.

During the initial `n-1` rounds every informed node remains active. If an uninformed node remains, 1-interval connectivity gives an informed/uninformed cut edge whose informed endpoint sends `INF`, so at least one new node is informed in that round. Therefore all nodes are informed by the start of round `n-1`. Once no uninformed node remains, no `IDLE` beacon is emitted, no new interval can be triggered, and every current interval expires within `n-1` rounds.

Hence

`S_det_BTAI(n) = n + 1`

and

`M_det_BTAI(n) = ceil(log2(n+1))` bits.

## Scope audit

The exact state theorem applies only to the explicitly defined locally timed BTAI subclass. It does not lower-bound unrestricted deterministic non-idle-start stabilizing broadcast. In particular, collective timers, active-state renewal, message-driven active timing, and additional external timing signals are outside the theorem.

## Verdict

No internal logical contradiction or off-by-one error was found in the theorem chain above. This audit is supplementary and is not peer review.
