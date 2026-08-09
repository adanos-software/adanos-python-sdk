# Changelog

All notable changes to the Adanos Python SDK will be documented in this file.

Format: [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
Versioning: [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [Unreleased]

### Added
- Synced generated model coverage with Adanos Market Sentiment API `1.49.0`, including Polymarket ticker `pulse`, daily bullish/bearish percentages, and structured compare/unsupported-asset errors.

### Changed
- Polymarket market-level `unique_traders` is nullable when retained wallet-level trades do not cover the requested window.
- X/Twitter trending `trend` now uses the documented `rising` / `falling` / `stable` enum.
- Documented stable per-UTC-day `trend_history` semantics from API `1.48.1`.

## [2.6.0] - 2026-06-23

### Added
- Added `client.sentiment.analyze()` and `analyze_async()` for `POST /sentiment/v1/analyze`.
- Added Polymarket `market_status` fields on stock detail `top_mentions[]` and raw mention rows.
- Added Polymarket `/stats` `open_markets_current`, `open_tickers_current`, `traded_markets_today`, and `traded_tickers_today`.

### Changed
- Synced generated client and wrapper coverage with Adanos Market Sentiment API `1.44.0`.
- Removed X/Twitter `daily_trend[].avg_rank` and Polymarket `/stats.unique_tickers_today` from public generated models.

## [2.5.0] - 2026-05-31

### Added
- Synced generated client and wrapper coverage with Adanos Market Sentiment API `1.40.0`.
- Added generated `InvalidPeriodError` models for structured 422 period-window errors.
- Added generated `XTopAuthor` and `XStockDetailResponse.top_authors` for X/Twitter contributor metrics.

## [2.4.0] - 2026-05-25

### Changed
- Synced generated client and wrapper coverage with Adanos Market Sentiment API `1.39.0`.
- Removed `from_`, `to`, and `days` from all public search wrappers and generated search endpoint functions; search endpoints now accept only `limit` and return API-managed recent summary windows.
- Removed compacted search summary fields that API `1.38.0` no longer returns.
- Removed `is_validated` from X/Twitter trending and stock detail models.

## [2.3.1] - 2026-05-21

### Fixed
- Handle API 422 validation envelopes where `detail` is a custom object instead of a Pydantic validation list.
- Preserve unexpected 422 detail payloads without raising parser errors.

## [2.3.0] - 2026-05-21

### Added
- Synced generated client and wrapper coverage with Adanos Market Sentiment API `1.37.0`.
- Added `from_` / `to` period options across Reddit Stocks, Reddit Crypto, X/Twitter Stocks, News Stocks, Polymarket Stocks, and raw mention helpers.

### Changed
- Updated `/stats` response models for API `1.36.0` compact standardized stats payloads.
- Documented `days` as a legacy v1-compatible shorthand while keeping it supported.

## [2.2.0] - 2026-05-19

### Added
- Synced generated client and wrapper coverage with Adanos Market Sentiment API `1.34.0`.
- Added root `health()` / `health_async()` helpers.
- Added generated market-sentiment, raw mention, X/Twitter explain, and root health endpoint modules.
- Added typed raw mention, market sentiment, platform-specific search/compare, rate-limit, validation detail, and Polymarket `current_market_count` models.
- Added raw mention `offset` support across Reddit Stocks, News Stocks, X/Twitter Stocks, Polymarket Stocks, and Reddit Crypto.

## [2.1.0] - 2026-04-29

### Added
- Added raw `mentions()` and `mentions_async()` helpers for Reddit Stocks, News Stocks, X/Twitter Stocks, Polymarket Stocks, and Reddit Crypto.
- Added test coverage for synchronous and asynchronous raw mention wrapper methods.

## [2.0.0] - 2026-04-20

### Breaking
- Removed typed model fields for API aliases removed in API `1.25.0`: `total_mentions` on detail responses, `sentiment` on daily trend and compare responses, and `upvotes` on compare responses. Use `mentions`, `sentiment_score`, and `total_upvotes`.

## [1.3.0] - 2026-04-12

### Added
- Added `client.x.explain()` and `client.x.explain_async()` for the X/Twitter stock explanation endpoint.

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
