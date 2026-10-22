# Changelog

## 0.2.0 — GitHub source update (no registry or GitHub Release)

### Owner-authorized examples on top of r3

- Preserve the owner's explicitly authorized example spellings and alternatives in separate readable/structured references, with context and attribution to Binablan rather than historical sources or all Abu Dhabi speakers.
- Guide notification direction, conditional updates, relative days, arrival/waiting context, and possible mild reproach; do not impose a universal negative-particle substitution.
- Add separate context-evaluation fixtures with multiple accepted phrasings, rejection probes, and mandatory human review. Existing r3 cases and historical model outputs are not replaced.
- Publish skill files, tests, and documentation only; exclude conversations, private calibration, archives, and historical logs. Verification outcomes and limitations are recorded in `references/evaluation.md`.
- Verified locally: 40/40 tests, including a fresh ZIP extraction; the prior r3 baseline remains 32/32. New owner-context fixtures contain 18 cases with 41 positive and 42 negative authored probes. These are checker tests, not evidence of model improvement or independent dialect certification.

### Review revision r3 (not a release)

- Reject the tomorrow modifiers `عقب باجر` and `ورا باجر`, including multiple spaces, tabs, line breaks, and non-breaking spaces, without changing the existing future-tense and negation guards.
- Preserve r1/r2 archives, outputs, and reports unchanged; record temporal false acceptances before the fix and rejection after it separately. This is a validator correction, not model improvement.

### Review revision r2 (not a release)

- Accept the requested tomorrow synonym in the future case while guarding future tense and polarity; preserve the original generated outputs and old result separately from re-evaluation.
- Reject decimal/numeric continuations in protected quantities, including `2.5` versus `2`.
- Bring the review probes into `scripts/verification_probes.py`, force UTF-8 output, and reproduce cp1252 behavior in a subprocess regression.
- Simplify provisional conversation examples without claiming local-speaker approval.

- Preserve the general Emirati profile, original source notes, examples, and license.
- Add an explicit opt-in Abu Dhabi profile with a small page-attested lexicon; distinguish regional attestation, shared forms, written spelling, and pronunciation.
- Add source/temporal limits, restrained conversation guidance, original MSA rewrite examples, and anti-caricature rules.
- Add offline regression cases and a fail-closed response checker with a separate human-review rubric.
- No claim of independent native-speaker validation or exhaustive Abu Dhabi coverage. Repository publication is separate from registry publication and GitHub Releases.

## 0.1.0

Initial source-grounded Emirati starter rules, original examples, source attribution, packaging/privacy checks, and corrected direct installation instructions.
