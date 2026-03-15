# adanos-python-sdk

`adanos-python-sdk` is the public source repository for the Python SDK for the [Adanos Finance Sentiment API](https://api.adanos.org/docs).

Links:
- Source: https://github.com/adanos-software/adanos-python-sdk
- PyPI: https://pypi.org/project/social-stock-sentiment/
- API docs: https://api.adanos.org/docs
- Homepage: https://adanos.org

The package name on PyPI remains `social-stock-sentiment`. The Python import is `stocksentiment`.

## Install

```bash
python3 -m pip install social-stock-sentiment
```

## Quick Start

```python
from stocksentiment import StockSentimentClient

client = StockSentimentClient(api_key="sk_live_...")

trending = client.reddit.trending(days=7, limit=10)
tsla = client.reddit.stock("TSLA", days=14)
explanation = client.reddit.explain("TSLA")

print(trending[0].ticker)
print(tsla.buzz_score)
print(explanation.explanation)
```

## News

```python
from stocksentiment import StockSentimentClient

client = StockSentimentClient(api_key="sk_live_...")

news_trending = client.news.trending(days=7, source="reuters")
nvda = client.news.stock("NVDA", days=7)
comparison = client.news.compare(["NVDA", "AAPL"], days=7)
```

## X

```python
from stocksentiment import StockSentimentClient

client = StockSentimentClient(api_key="sk_live_...")

x_trending = client.x.trending(days=1, limit=20)
nvda = client.x.stock("NVDA")
```

## Polymarket

```python
from stocksentiment import StockSentimentClient

client = StockSentimentClient(api_key="sk_live_...")

pm_trending = client.polymarket.trending(days=7, limit=20, type="stock")
aapl = client.polymarket.stock("AAPL")
```

Polymarket semantics:
- `buzz_score` is activity-first and optimized for current market attention
- `total_liquidity` is a windowed signal over the selected `days`
- `top_mentions` on `stock()` are relevance-sorted by trading activity first

## Async Usage

Every namespace method also has an `_async` variant.

```python
import asyncio
from stocksentiment import StockSentimentClient


async def main() -> None:
    async with StockSentimentClient(api_key="sk_live_...") as client:
        trending = await client.reddit.trending_async(days=7)
        tsla = await client.reddit.stock_async("TSLA")
        print(trending[0].ticker)
        print(tsla.trend)


asyncio.run(main())
```

## Namespaces

- `client.reddit.*` for Reddit Stocks
- `client.news.*` for News Stocks
- `client.x.*` for X/Twitter Stocks
- `client.polymarket.*` for Polymarket Stocks

## Authentication

Get an API key at https://api.adanos.org/docs

```python
from stocksentiment import StockSentimentClient

client = StockSentimentClient(
    api_key="sk_live_...",
    base_url="https://api.adanos.org",
    timeout=60.0,
)
```

Priority is explicit in your application code; the SDK does not auto-load local profiles.

## Development

```bash
python3 -m pip install -e ".[dev]"
python3 -m pytest tests -q
python3 -m build
```

## License

MIT
