# adanos

[![PyPI version](https://img.shields.io/pypi/v/adanos.svg)](https://pypi.org/project/adanos/)

`adanos` is the public Python SDK for the [Adanos Market Sentiment API](https://api.adanos.org/docs).

It gives you typed access to:
- Reddit stock sentiment
- News sentiment and source-filtered rankings
- X/Twitter stock sentiment
- Polymarket stock activity and market attention
- Reddit crypto sentiment

Links:
- Source: https://github.com/adanos-software/adanos-python-sdk
- PyPI: https://pypi.org/project/adanos/
- API docs: https://api.adanos.org/docs
- Homepage: https://adanos.org

Package and import:
- PyPI package: `adanos`
- Python import: `adanos`

## Install

```bash
python3 -m pip install adanos
```

## Quick Start

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

trending = client.reddit.trending(limit=10)
tsla = client.reddit.stock("TSLA")
explanation = client.reddit.explain("TSLA")

print(trending[0].ticker)
print(tsla.buzz_score)
print(explanation.explanation)
```

## What You Can Do

- Rank trending stocks across Reddit, News, X, and Polymarket
- Pull service-level market sentiment snapshots across every public namespace
- Pull detailed ticker reports for a fixed lookback window
- Search and compare tickers across datasets
- Generate AI-written explanations for Reddit and News stock trends
- Track Reddit crypto tokens via the same client
- Use sync or async methods without changing the namespace structure

## Namespaces

- `client.reddit.*` for Reddit Stocks
- `client.news.*` for News Stocks
- `client.x.*` for X/Twitter Stocks
- `client.polymarket.*` for Polymarket Stocks
- `client.crypto.*` for Reddit Crypto
- `client.reddit_crypto.*` is an alias for `client.crypto.*`
- `client.health()` for root API health aggregated across services

## Examples

### Reddit Stocks

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

root_health = client.health()
trending = client.reddit.trending(limit=10)
sectors = client.reddit.trending_sectors(limit=10)
countries = client.reddit.trending_countries(limit=10)
tsla = client.reddit.stock("TSLA")
explanation = client.reddit.explain("TSLA")
results = client.reddit.search("Tesla", limit=10)
comparison = client.reddit.compare(["TSLA", "AAPL", "MSFT"])
market = client.reddit.market_sentiment()
```

### News

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

news_trending = client.news.trending(source="reuters")
sectors = client.news.trending_sectors(source="reuters")
countries = client.news.trending_countries(source="reuters")
nvda = client.news.stock("NVDA")
explanation = client.news.explain("NVDA")
results = client.news.search("Nvidia", limit=10)
comparison = client.news.compare(["NVDA", "AAPL"])
market = client.news.market_sentiment()
stats = client.news.stats()
health = client.news.health()
```

### X/Twitter

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

x_trending = client.x.trending(limit=20)
sectors = client.x.trending_sectors(limit=10)
countries = client.x.trending_countries(limit=10)
nvda = client.x.stock("NVDA")
explanation = client.x.explain("NVDA")
results = client.x.search("Nvidia", limit=10)
comparison = client.x.compare(["NVDA", "AMD"])
market = client.x.market_sentiment()
stats = client.x.stats()
health = client.x.health()
```

### Polymarket

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

pm_trending = client.polymarket.trending(limit=20, type="stock")
sectors = client.polymarket.trending_sectors(limit=10)
countries = client.polymarket.trending_countries(limit=10)
aapl = client.polymarket.stock("AAPL")
results = client.polymarket.search("Apple", limit=10)
comparison = client.polymarket.compare(["AAPL", "TSLA"])
market = client.polymarket.market_sentiment()
stats = client.polymarket.stats()
health = client.polymarket.health()
```

Polymarket semantics:
- `buzz_score` is activity-first and optimized for current market attention
- `total_liquidity` is a windowed signal over the selected period
- `current_market_count` is the live-only active-market breadth; `market_count` remains the selected-window breadth
- `top_mentions` on `stock()` are relevance-sorted by trading activity first

### Reddit Crypto

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

trending = client.crypto.trending(limit=20)
btc = client.crypto.token("BTC")
mentions = client.crypto.mentions("BTC", from_="2026-05-01", to="2026-05-07", limit=10, offset=10)
results = client.crypto.search("bitcoin", limit=10)
comparison = client.crypto.compare(["BTC", "ETH"])
market = client.crypto.market_sentiment()
stats = client.crypto.stats()
health = client.crypto.health()
```

## Available Methods

### `client.*`

| Method | Description |
|--------|-------------|
| `health()` | Root API health aggregated across services |

### `client.reddit.*`

| Method | Description |
|--------|-------------|
| `trending(from_, to, days, limit, offset, type)` | Trending stocks by buzz score |
| `trending_sectors(from_, to, days, limit, offset)` | Trending sectors |
| `trending_countries(from_, to, days, limit, offset)` | Trending countries |
| `stock(ticker, from_, to, days)` | Detailed sentiment for a ticker |
| `mentions(ticker, from_, to, days, limit, offset, include_inherited)` | Raw Reddit mention rows |
| `explain(ticker)` | AI-generated trend explanation |
| `search(query, limit)` | Search stocks by name or ticker with an API-managed recent summary block |
| `compare(tickers, from_, to, days)` | Compare up to 10 stocks |
| `market_sentiment(from_, to, days)` | Service-level Reddit market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

Period options: use `from_` and `to` as `YYYY-MM-DD` inclusive UTC dates for reproducible windows. The SDK serializes `from_` as query parameter `from`. `days` remains available as a legacy v1-compatible shorthand. The API returns `422` if `from`, `to`, and `days` are all sent together. Responses keep `period_days`; retain requested dates client-side if you need them later. Search endpoints are the exception: they accept only `limit` and use the API-managed recent summary window.

### `client.news.*`

| Method | Description |
|--------|-------------|
| `trending(from_, to, days, limit, offset, type, source)` | Trending stocks from news |
| `trending_sectors(from_, to, days, limit, offset, source)` | Trending sectors from news |
| `trending_countries(from_, to, days, limit, offset, source)` | Trending countries from news |
| `stock(ticker, from_, to, days)` | Detailed news sentiment for a ticker |
| `mentions(ticker, from_, to, days, limit, offset)` | Raw news mention rows |
| `explain(ticker)` | AI-generated explanation from news context |
| `search(query, limit)` | Search stocks in the news dataset with an API-managed recent summary block |
| `compare(tickers, from_, to, days)` | Compare up to 10 stocks in news |
| `market_sentiment(from_, to, days)` | Service-level News market sentiment snapshot |
| `stats()` | News dataset statistics |
| `health()` | Public news service health |

### `client.x.*`

| Method | Description |
|--------|-------------|
| `trending(from_, to, days, limit, offset, type)` | Trending stocks on X/Twitter |
| `trending_sectors(from_, to, days, limit, offset)` | Trending sectors |
| `trending_countries(from_, to, days, limit, offset)` | Trending countries |
| `stock(ticker, from_, to, days)` | Detailed X/Twitter sentiment |
| `mentions(ticker, from_, to, days, limit, offset)` | Raw X/Twitter mention rows |
| `explain(ticker)` | AI-generated explanation from X/Twitter context |
| `search(query, limit)` | Search stocks with an API-managed recent summary block |
| `compare(tickers, from_, to, days)` | Compare stocks |
| `market_sentiment(from_, to, days)` | Service-level X/Twitter market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

### `client.polymarket.*`

| Method | Description |
|--------|-------------|
| `trending(from_, to, days, limit, offset, type)` | Trending stocks on Polymarket with activity-first buzz and windowed liquidity |
| `trending_sectors(from_, to, days, limit, offset)` | Trending sectors |
| `trending_countries(from_, to, days, limit, offset)` | Trending countries |
| `stock(ticker, from_, to, days)` | Detailed Polymarket activity, sentiment, and relevance-sorted market questions |
| `mentions(ticker, from_, to, days, limit, offset)` | Raw Polymarket market snapshots |
| `search(query, limit)` | Search stocks with an API-managed recent summary block |
| `compare(tickers, from_, to, days)` | Compare stocks with windowed Polymarket activity signals |
| `market_sentiment(from_, to, days)` | Service-level Polymarket market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

### `client.crypto.*`

| Method | Description |
|--------|-------------|
| `trending(from_, to, days, limit, offset)` | Trending Reddit crypto tokens |
| `token(symbol, from_, to, days)` | Detailed token sentiment and buzz |
| `mentions(symbol, from_, to, days, limit, offset, include_inherited)` | Raw Reddit crypto mention rows |
| `search(query, limit)` | Search tokens by symbol or name with an API-managed recent summary block |
| `compare(symbols, from_, to, days)` | Compare multiple tokens |
| `market_sentiment(from_, to, days)` | Service-level Reddit Crypto market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

## Async Usage

Every namespace method also has an `_async` variant.

```python
import asyncio

from adanos import AdanosClient


async def main() -> None:
    async with AdanosClient(api_key="sk_live_...") as client:
        trending = await client.reddit.trending_async(limit=10)
        tsla = await client.reddit.stock_async("TSLA")
        explanation = await client.news.explain_async("NVDA")
        print(trending[0].ticker)
        print(tsla.trend)
        print(explanation.explanation)


asyncio.run(main())
```

## Authentication and Configuration

Get an API key at https://api.adanos.org/docs

```python
from adanos import AdanosClient

client = AdanosClient(
    api_key="sk_live_...",
    base_url="https://api.adanos.org",
    timeout=60.0,
)
```

Notes:
- `api_key` is required for protected endpoints
- `base_url` lets you target another deployment or staging environment
- `timeout` is passed through to the underlying `httpx` client
- the SDK does not auto-load local CLI profiles or env-specific config files

Context management:

```python
from adanos import AdanosClient

with AdanosClient(api_key="sk_live_...") as client:
    print(client.reddit.health())
```

## Errors and Responses

- Most SDK methods return typed models from the generated OpenAPI client
- `market_sentiment()` methods return the live JSON payload directly so the new endpoint family is available before the next full generated refresh
- Documented API errors are returned as typed error models
- Undocumented statuses raise `UnexpectedStatus`
- For long-lived processes, use `with`, `async with`, `close()`, or `aclose()` to release HTTP resources

## Rate Limits

Typical platform limits:

| Tier | Monthly Requests | Burst Limit |
|------|------------------|-------------|
| Free | 250 | 100/min |
| Paid | Unlimited | 1000/min |

See the live API docs for the current contract and plan details.

## Migration from `social-stock-sentiment`

Version `1.0.0` starts the new `adanos` package line and renames both the PyPI package and the Python import path.

Old:

```bash
python3 -m pip install social-stock-sentiment
```

```python
from stocksentiment import StockSentimentClient
```

New:

```bash
python3 -m pip install adanos
```

```python
from adanos import AdanosClient
```

The client API and namespace layout stay the same. Most upgrades only need a dependency rename and an import rewrite.

`AdanosClient` is now the primary public client name. `StockSentimentClient` remains available as a compatibility alias.

If you adopted the pre-release `adanos-python-sdk` naming locally, switch that install/import pair too:

```bash
python3 -m pip uninstall adanos-python-sdk
python3 -m pip install adanos
```

```python
from adanos import AdanosClient
```

## Development

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest tests -q
python3 -m build
```

## License

MIT
