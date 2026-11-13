# Scripts

Small, auditable helpers only. No hidden grading.

Planned:
- `check_registry.py` — check IDs unique, required fields present, BR- links exist, bilingual fields present
- `check_consistency.py` — flag P03/P17-style rating mismatches, missing counter-evidence, metaphor in conclusion
- `export_csv.py` — Excel -> CSV for diffable review

All scripts must be deterministic and print their checks. AI-generated scripts must be human-reviewed before use in a PR.
