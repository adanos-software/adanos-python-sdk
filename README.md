# adanos

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

trending = client.reddit.trending(days=7, limit=10)
tsla = client.reddit.stock("TSLA", days=14)
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

## Examples

### Reddit Stocks

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

trending = client.reddit.trending(days=7, limit=10)
sectors = client.reddit.trending_sectors(days=7, limit=10)
countries = client.reddit.trending_countries(days=7, limit=10)
tsla = client.reddit.stock("TSLA", days=14)
explanation = client.reddit.explain("TSLA")
results = client.reddit.search("Tesla", days=7, limit=10)
comparison = client.reddit.compare(["TSLA", "AAPL", "MSFT"], days=7)
market = client.reddit.market_sentiment(days=7)
```

### News

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

news_trending = client.news.trending(days=7, source="reuters")
sectors = client.news.trending_sectors(days=7, source="reuters")
countries = client.news.trending_countries(days=7, source="reuters")
nvda = client.news.stock("NVDA", days=7)
explanation = client.news.explain("NVDA")
results = client.news.search("Nvidia", days=7, limit=10)
comparison = client.news.compare(["NVDA", "AAPL"], days=7)
market = client.news.market_sentiment(days=7)
stats = client.news.stats()
health = client.news.health()
```

### X/Twitter

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

x_trending = client.x.trending(days=1, limit=20)
sectors = client.x.trending_sectors(days=1, limit=10)
countries = client.x.trending_countries(days=1, limit=10)
nvda = client.x.stock("NVDA")
results = client.x.search("Nvidia", days=7, limit=10)
comparison = client.x.compare(["NVDA", "AMD"], days=7)
market = client.x.market_sentiment(days=7)
stats = client.x.stats()
health = client.x.health()
```

### Polymarket

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

pm_trending = client.polymarket.trending(days=7, limit=20, type="stock")
sectors = client.polymarket.trending_sectors(days=7, limit=10)
countries = client.polymarket.trending_countries(days=7, limit=10)
aapl = client.polymarket.stock("AAPL")
results = client.polymarket.search("Apple", days=7, limit=10)
comparison = client.polymarket.compare(["AAPL", "TSLA"], days=7)
market = client.polymarket.market_sentiment(days=7)
stats = client.polymarket.stats()
health = client.polymarket.health()
```

Polymarket semantics:
- `buzz_score` is activity-first and optimized for current market attention
- `total_liquidity` is a windowed signal over the selected `days`
- `top_mentions` on `stock()` are relevance-sorted by trading activity first

### Reddit Crypto

```python
from adanos import AdanosClient

client = AdanosClient(api_key="sk_live_...")

trending = client.crypto.trending(days=7, limit=20)
btc = client.crypto.token("BTC", days=14)
results = client.crypto.search("bitcoin", days=7, limit=10)
comparison = client.crypto.compare(["BTC", "ETH"], days=7)
market = client.crypto.market_sentiment(days=7)
stats = client.crypto.stats()
health = client.crypto.health()
```

## Available Methods

### `client.reddit.*`

| Method | Description |
|--------|-------------|
| `trending(days, limit, offset, type)` | Trending stocks by buzz score |
| `trending_sectors(days, limit, offset)` | Trending sectors |
| `trending_countries(days, limit, offset)` | Trending countries |
| `stock(ticker, days)` | Detailed sentiment for a ticker |
| `explain(ticker)` | AI-generated trend explanation |
| `search(query, days, limit)` | Search stocks by name or ticker with a summary block |
| `compare(tickers, days)` | Compare up to 10 stocks |
| `market_sentiment(days)` | Service-level Reddit market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

### `client.news.*`

| Method | Description |
|--------|-------------|
| `trending(days, limit, offset, type, source)` | Trending stocks from news |
| `trending_sectors(days, limit, offset, source)` | Trending sectors from news |
| `trending_countries(days, limit, offset, source)` | Trending countries from news |
| `stock(ticker, days)` | Detailed news sentiment for a ticker |
| `explain(ticker)` | AI-generated explanation from news context |
| `search(query, days, limit)` | Search stocks in the news dataset with a summary block |
| `compare(tickers, days)` | Compare up to 10 stocks in news |
| `market_sentiment(days)` | Service-level News market sentiment snapshot |
| `stats()` | News dataset statistics |
| `health()` | Public news service health |

### `client.x.*`

| Method | Description |
|--------|-------------|
| `trending(days, limit, offset, type)` | Trending stocks on X/Twitter |
| `trending_sectors(days, limit, offset)` | Trending sectors |
| `trending_countries(days, limit, offset)` | Trending countries |
| `stock(ticker, days)` | Detailed X/Twitter sentiment |
| `search(query, days, limit)` | Search stocks with a summary block |
| `compare(tickers, days)` | Compare stocks |
| `market_sentiment(days)` | Service-level X/Twitter market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

### `client.polymarket.*`

| Method | Description |
|--------|-------------|
| `trending(days, limit, offset, type)` | Trending stocks on Polymarket with activity-first buzz and windowed liquidity |
| `trending_sectors(days, limit, offset)` | Trending sectors |
| `trending_countries(days, limit, offset)` | Trending countries |
| `stock(ticker, days)` | Detailed Polymarket activity, sentiment, and relevance-sorted market questions |
| `search(query, days, limit)` | Search stocks with a summary block |
| `compare(tickers, days)` | Compare stocks with windowed Polymarket activity signals |
| `market_sentiment(days)` | Service-level Polymarket market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

### `client.crypto.*`

| Method | Description |
|--------|-------------|
| `trending(days, limit, offset)` | Trending Reddit crypto tokens |
| `token(symbol, days)` | Detailed token sentiment and buzz |
| `search(query, days, limit)` | Search tokens by symbol or name with a summary block |
| `compare(symbols, days)` | Compare multiple tokens |
| `market_sentiment(days)` | Service-level Reddit Crypto market sentiment snapshot |
| `stats()` | Dataset statistics |
| `health()` | Public service health |

## Async Usage

Every namespace method also has an `_async` variant.

```python
import asyncio

from adanos import AdanosClient


async def main() -> None:
    async with AdanosClient(api_key="sk_live_...") as client:
        trending = await client.reddit.trending_async(days=7)
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
