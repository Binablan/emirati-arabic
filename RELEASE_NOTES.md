# 1.0.0 — Stable

## Local contextual update

The unpublished source now identifies its behavior revision as `contextual-usage-1`. It adds [contextual meanings and source boundaries](references/contextual-usage.md), including edited owner-confirmed meanings and selected readings from three video texts. No private conversation transcript or full video transcript is included. Unresolved words remain in a clearly separated review queue, not in the established-definition table. Neither listening to audio nor precise word timestamps are claimed. Keep previous local artifacts intact and build this revision into a new output directory; previous response scores do not evaluate this new text. Remote publication remains a separate approval step.

## Purpose

Emirati conversation, contextual understanding, writing, and revision, with an explicit opt-in Abu Dhabi specialization. General Emirati remains the default. The lexicon supports the task; it does not turn ordinary conversation into vocabulary explanations.

This is a stable, versioned foundation for continued maintenance, not a prerelease label or a claim that development has ended. Stable does not mean 100% accuracy, exhaustive dialect coverage or native-speaker certification. Remote publication, tags, registry submission and synchronization into installed profiles each requires separate approval; a local build does not prove any of these occurred.

## Included improvements

- Incorporate the previously reviewed conversation-first instruction contract and its examples/tests: direct task completion, preserved facts, restrained self-directed humor, grounded practical drafts, conversation-scoped language changes, and local user corrections.
- Clarify actors, actions, and referents in spoken scripts when pronouns or ambiguous kinship/body-part spellings obscure what happened. Do not replace one event with a different mishap; do not prohibit a regional word globally.
- Preserve all prior source rules, historical/source boundaries, owner-authorized example spellings, lexicon entries, and offline conversion fixtures.
- Add an allowlisted source ZIP builder with SHA-256 manifest, defensive distribution tests, and separate handling of private evidence.
- Include portable activation and a generated single-file edition from the same source, plus eight selected heritage entries with source locators and evidence limits. The book and bulk extraction are not included.
- Carry source scope across follow-up turns: an earlier assistant explanation is not new evidence. Prefer a brief source qualifier over unnecessary bibliography; keep practical drafts direct.
- Distinguish traditional craft from the age, maker or family ownership of a pictured object. Do not invent provenance for a warmer caption.
- Update stable-version identity and installation guidance without assuming the remote copy has already been updated.

## Limits and evidence

Offline Python tests check the instruction contract, package integrity, references, metadata, privacy patterns, and scoped conversion constraints. They are not a fluency benchmark. The extended 96-response comparison evaluated the preceding heritage revision, not this exact 1.0.0 text. A focused post-change response check must be recorded separately with its artifact hash; earlier scores must not be relabeled as new measurements.

No independent native-speaker certification is claimed. Naturalness, regional coverage, and contextual interpretation remain open to human review. Minor wording issues can remain even when all offline checks pass. Rule changes alone do not prove every future model response is fixed.

Raw conversation outputs, live-test logs, session identifiers, local paths, private calibration, credentials, internal archives, copyrighted PDFs, and page images are not release assets. Owner-contributed examples explicitly authorized for publication remain in their attributed references.

## Files

The builders create `emirati-arabic-1.0.0.zip`, `SHA256SUMS`, `emirati-arabic-chat.md` and `chat-manifest.json` outside the repository. The ZIP contains only the files in `distribution-files.json` plus a generated `MANIFEST.json`, under `emirati-arabic/`. Verify the extracted archive and rebuild the chat edition from it. See [distribution policy](DISTRIBUTION.md). No remote tag or release asset is assumed to exist merely because these filenames are documented.

## Future updates

Keep this stable version reproducible. Deliver corrections and additive references as new versioned updates after review; do not silently replace archived artifacts or erase historical evaluation evidence. A breaking change to the documented usage contract requires an explicitly described version change.

## License

Original project material remains MIT, credited to Binablan. Third-party references retain their own rights; their books and media are not bundled. See [LICENSE](LICENSE) and [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).
