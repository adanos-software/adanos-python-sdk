# Changelog

All notable changes to the Adanos Python SDK will be documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [1.2.0] - 2026-03-27

### Added
- Added `market_sentiment()` and `market_sentiment_async()` across Reddit, News, X, Polymarket, and Reddit Crypto namespaces.

### Changed
- Renamed package metadata and docs from `Adanos Finance Sentiment API` to `Adanos Market Sentiment API`.

## [1.1.0] - 2026-03-19

### Added
- Search wrappers now accept `days` and `limit` across Reddit, News, X, Crypto, and Polymarket.
- Search models now expose the API `summary` payload for compact recent activity data.

### Changed
- Compare models now match the enriched `/compare` contract, including `trend`, `trend_history`, canonical `sentiment_score`, and platform-specific activity fields.
- Detail models now prefer canonical `mentions` and keep `total_mentions` only as a legacy alias where the API still exposes it.
- `daily_trend` models now expose canonical `sentiment_score` alongside the deprecated `sentiment` alias.

## [1.0.0] - 2026-03-15

### Added
- First public release of `adanos` as a standalone Python SDK package.
- Standalone GitHub Actions CI for tests, build, and isolated wheel smoke installation.
- Standalone Trusted Publishing workflow for PyPI from this repository.

### Changed
- Renamed the PyPI package from `social-stock-sentiment` to `adanos`.
- Renamed the Python import path from `stocksentiment` to `adanos`.
- Renamed the primary client class from `StockSentimentClient` to `AdanosClient`.
- Package metadata now points to the public repository, API docs, and the new PyPI project.
- CI and release smoke tests now validate the renamed distribution and import path.

### Migration
- Replace `pip install social-stock-sentiment` with `pip install adanos`.
- Replace `from stocksentiment import StockSentimentClient` with `from adanos import AdanosClient`.
- `StockSentimentClient` remains available as a compatibility alias.
