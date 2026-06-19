# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

## [2.0.0] - 2026
### Changed
- Re-tagged ecosystem milestone release as v2.0.0 — the v1.0.0 tag in
  this repo's history predates the GenesisAeon ecosystem-wide milestone
  (a prior scaffold-template release) and was not available for reuse.
  v2.0.0 is the correct, free major version for this milestone and is
  functionally a continuation of the v1.0.0 release below.

## [1.0.0] - 2026
### Added
- Initial v1.0.0 release as part of the GenesisAeon ecosystem-wide 1.0.0
  milestone.
- `diamond` CLI: `scaffold`, `list-templates`, and `validate` commands.
- `minimal` and `genesis` project templates.
- Standardized release tooling: `.zenodo.json`, `RELEASE_GUIDE.md`,
  `CONTRIBUTING.md`, issue/PR templates.

### Changed
- Project metadata (`pyproject.toml`) normalized: description encoding
  fixed, license, authors, and `requires-python` confirmed present.
