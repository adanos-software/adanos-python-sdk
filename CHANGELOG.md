# Changelog

All notable changes to the Adanos Python SDK will be documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [1.20.0] - 2026-03-15

### Added
- First public standalone Python SDK repository under `adanos-software/adanos-python-sdk`.
- Public README focused on installation, namespace usage, and async examples.
- Standalone GitHub Actions CI for tests, build, and isolated wheel smoke installation.
- Standalone Trusted Publishing workflow for PyPI from this repository.

### Changed
- Packaging now builds from the repository-local `src/` layout instead of monorepo-specific paths.
- Package metadata now points to the public repository, API docs, and PyPI project.
