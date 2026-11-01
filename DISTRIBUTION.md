# Public distribution and private evidence

## Source and runtime

`distribution-files.json` is the exact reviewed public-source allowlist. The source ZIP includes documentation, runtime references, scripts, and **offline authored regression tests**, so contributors can inspect and reproduce the checks. These are not live conversation records.

Direct Hermes URL installation uses `SKILL.md` and its linked runtime references. Source-only test/build files do not need to be installed as teaching material.

## Build and verify

Use Python 3.10 or later, from the repository directory:

```sh
python -B -m unittest discover -s tests -v
python -B scripts/verification_probes.py --project .
python -B scripts/build_distribution.py --output-dir ../emirati-release-files
```

The output must be outside the repository. The builder rejects missing files, traversal/symlink members, recognized private filenames/content, and missing local documentation targets. It writes a deterministic ZIP with fixed member timestamps and an internal SHA-256 file manifest, then reads the ZIP back and checks its bytes and CRC. `SHA256SUMS` records the hash of the ZIP itself. Reproducibility assumes identical source bytes and compression implementation; a Git checkout with different line endings has different bytes.

Before distribution, extract the ZIP into a new disposable directory and run the same offline tests from the extracted `emirati-arabic` folder. Inspect every member and the public Git diff; automated patterns cannot detect every private statement or credential format.

## Single-file chat edition

For hosts without skill-folder support, generate a runtime-only companion outside the repository:

```sh
python -B scripts/build_chat_bundle.py --output-dir ../emirati-chat-files
```

The explicit runtime subset is assembled from the same validated public source allowlist. It includes the skill, conversation/regional guidance, source notes, authorized examples, and unchanged license/notices; it does not include test fixtures, model outputs, or private memory. The generated `emirati-arabic-chat.md` and `chat-manifest.json` are separate from the source ZIP. The manifest records source-byte hashes and the output hash, not a claim of model activation or compatibility. Rebuild after source edits instead of editing the assembled copy. See [usage guidance](USAGE.md) for attachment, paste, and context-size limits.

## Exclusions

Never allowlist chat transcripts, actual model outputs, session databases/identifiers, live-test JSONL/logs, private calibrations, credentials, local settings, internal review ZIPs, source books, or images. Keep those in a separate private review location outside this repository. Do not publish private logs in the PR description, comments, CI artifacts, or release assets.

Public release notes may summarize test methodology and limitations without including private conversations. The explicitly publication-authorized owner examples are distinct from private calibration and remain attributed and unchanged.

## Approval boundary

A source branch and Pull Request may be available for community review without merging `main` or creating a GitHub Release. Creating a tag, publishing a pre-release/final release, and submitting to a registry are separate actions requiring approval. Do not attach private evidence to any of them.

## Rights

Include `LICENSE` and `THIRD_PARTY_NOTICES.md` unchanged. Source citations and their scope statements must remain available. MIT covers original project material only, not the referenced third-party books or papers.
