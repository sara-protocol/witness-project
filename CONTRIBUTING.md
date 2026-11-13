# Contributing

## Principles

1. Evidence first, conclusion second.
2. One claim = one ID. Never edit a claim silently — open a PR with a revision note.
3. Support + counter-evidence are both required for important claims.
4. AI-assisted work must be labelled as AI-assisted.
5. No claim becomes "frozen" without human review + expert review where required.

## Ways to contribute

- **Claim review**: pick one P01-P27 claim, check wording, sources, rating.
- **Reference verification**: check one REF item against the original source (author, year, title, journal, DOI, accessible?, what it actually supports / does not support).
- **Evidence extraction**: add one EVD item with sample/system, result, limitation.
- **Concept clarification**: propose a definition, boundary, counterexample.
- **Translation / bilingual check**: Chinese <-> English claim strength must match.
- **Method**: propose E-M-T-L-I scale definitions, thresholds, examples.

## Workflow

1. Open / pick an Issue (e.g. `claim: P17`, `ref: REF-009`).
2. Fork -> branch `claim/P17` or `ref/REF-009`.
3. Edit `registry/` + add a row in `06_Revision` (in PR description if Excel is hard to diff — see below).
4. Open PR with: what changed / why / evidence / what it does NOT prove.
5. At least one human reviewer approves. AI review is allowed but does not count as human review.

## Registry format (important)

Excel is hard to diff. Long-term we migrate to CSV / YAML in `registry/`:

- `registry/concepts.csv`
- `registry/claims.csv`
- `registry/references.csv`
- `registry/evidence.csv`
- `registry/bridging.csv`
- `registry/revision.csv`

Until migration is complete, Excel v0.2 is the working file. In PRs, always describe changes in text — do not rely on Excel diff alone.

## Labels for AI contributions

- `ai-assisted`: AI drafted, human reviewed
- `ai-draft-unreviewed`: AI drafted, NOT yet human reviewed — must not be cited as conclusion
- `human-verified`: human checked against original source

## What we do NOT accept

- Claims without a source or with only a secondary / press source for a key conclusion
- Metaphors presented as mechanisms
- Cross-level inference without an independent BR- ID
- "Proved consciousness survives death" style conclusions without evidence meeting the manual
- Deleting revision history to make tables look tidy
