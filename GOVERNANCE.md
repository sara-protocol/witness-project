# Governance

## Goal

Build a research system that remains rigorous even when evidence does NOT support the original hypothesis.

## Roles

- **Maintainer(s)**: merge PRs, freeze versions, resolve disputes. Initially the project founder.
- **Reviewers**: domain reviewers (physics, neuroscience, phenomenology, traditions, methods). Reviewers are credited by name/handle.
- **Contributors**: anyone who opens an Issue / PR.
- **AI contributors**: AI systems contributing drafts / checks. Must be labelled. AI cannot be a maintainer, cannot be a sole reviewer, and cannot freeze a version.

## Decision rules

- **Claim wording / rating change**: PR + at least 1 human reviewer + revision record.
- **Method manual change**: PR + discussion in Issue + maintainer approval. After v1.0 freeze, changes are recorded as "deviation" with reason.
- **Freeze**: only when Sprint 1 quality gates pass (see README / Sprint plan). Freeze does not mean never change — new evidence / error / expert opinion triggers a new version.
- **Disputes**: if two reviewers disagree, keep BOTH views in the record with "contested" status. Do not silently pick one.

## Transparency

- All research decisions in public Issues / PRs.
- No private decision that changes a claim rating.
- AI prompts / outputs used for a PR should be summarised in the PR (what the AI did, what the human checked).

## Code of Conduct

See CODE_OF_CONDUCT.md. Respectful disagreement is expected. Personal attacks, harassment, and ideological campaigning are not.
