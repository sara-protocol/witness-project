# Upload Guide — 10-Minute Go-Live

Repo name: `witness-project`
Visibility: Public
License: CC BY-SA 4.0 (content) + MIT (code/scripts) — see LICENSE files

## Option A: GitHub Web (no command line, fastest)

1. Go to https://github.com/new
2. Repository name: `witness-project`
3. Description: `Witness Project — a public, co-built research project for humans and AI. Physical records, cognitive monitoring, and first-person awareness: what they are, what evidence exists, and which cross-level inferences hold.`
4. Public, check "Add a README file" OFF (we already have one), Create repository
5. On the repo page: Add file > Upload files > drag ALL files from this folder (including `registry/`, `.github/`, `docs/`)
6. Commit message: `v0.2 backfill: P01-P27, 15 references, W-phen split, revision history — NOT frozen`
7. Click Commit

## Option B: Command line (recommended for later)

```bash
# 1. Unzip this folder, cd into it
cd witness-project

# 2. Init
git init
git branch -M main

# 3. Add all (respects .gitignore)
git add .
git status

# 4. First commit — keep this exact message
git commit -m "v0.2 backfill: P01-P27, 15 references, W-phen split, revision history — NOT frozen"

# 5. Connect to GitHub (replace <YOUR-USERNAME>)
git remote add origin https://github.com/<YOUR-USERNAME>/witness-project.git
git push -u origin main
```

If GitHub asks for auth, use a Personal Access Token (Settings > Developer settings > Personal access tokens), not your password.

## After upload — 5 things to do on GitHub

1. Settings > General > Add topics: `consciousness`, `philosophy-of-mind`, `quantum-foundations`, `scoping-review`, `open-science`, `human-ai-collaboration`
2. Settings > General > Website: leave blank for now, or link to a future docs page
3. Issues > New Issue > use templates: open 5 starter issues:
   - `claim: P03 — eternalism does not imply postmortem experience`
   - `claim: P06a — Frauchiger-Renner`
   - `claim: P06b — Local Friendliness`
   - `claim: P17 — quantum information does not imply personal survival`
   - `concept: W-phen split C-005a/b/c`
4. Pin the README: it already states the mission + status. No extra announcement needed.
5. Add a tag for v0.2:
```bash
git tag v0.2-backfill
git push origin v0.2-backfill
```

## Next milestones (GitHub Milestones)

- `v1.0-method-manual` — E-M-T-L-I scales frozen
- `v1.0-registry` — P01-P27 + concepts frozen
- `v1.0-evidence-map` — evidence map
- `v1.0-paper-draft` — Track A draft

## What NOT to upload yet

- 91-page / 31-page Word docs as the source of truth — put them in `docs/archive/` only as historical reference, with a note "historical, not authoritative".
- Any claim marked `ai-draft-unreviewed` as if it were a conclusion.
- Private notes, personal data, unpublished expert emails.

## Troubleshooting

- Large Excel upload fails: upload CSVs first, then Excel separately.
- CSV looks garbled: open with UTF-8 (we saved as UTF-8 with BOM for Excel).
- Push rejected: `git pull --rebase origin main` then push again (only if you created README on GitHub).
