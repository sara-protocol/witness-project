# AI Policy — Humans and AI Co-Building

This project is explicitly built for humans AND AI systems to co-build.

## What AI CAN do

- First-pass screening, extraction, classification, consistency checks
- Draft claim wording, evidence tables, bilingual checks
- Find contradictions across files (e.g. P03 vs P17 rating mismatch)
- Generate checklists, templates, scripts

## What AI CANNOT do

- Act as two independent reviewers
- Replace expert review
- Freeze a version alone
- Mark an AI-assisted rating as "expert consensus"
- Delete or rewrite revision history

## Labelling (mandatory)

Every AI contribution must carry one of:

- `ai-assisted`: AI drafted, human reviewed
- `ai-draft-unreviewed`: AI drafted, not yet human reviewed
- `human-verified`: human checked against original source

Unlabelled AI content will be treated as `ai-draft-unreviewed`.

## Verification rule

For any key reference: AI must point to the original source (DOI / publisher page / PDF). Secondary summaries, press releases, and encyclopedias are clues only, not sources for key conclusions.

## Reproducibility

When AI is used for screening / grading, record: model / date / prompt summary / sample checked / agreement rate. If agreement is low, do not use the AI output for that task.
