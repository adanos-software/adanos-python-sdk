"""Tests for the AdanosClient wrapper."""

import sys
from pathlib import Path

import pytest
import httpx
import respx


SDK_SRC = Path(__file__).resolve().parents[1] / "src"
if str(SDK_SRC) not in sys.path:
    sys.path.insert(0, str(SDK_SRC))

from adanos import AdanosClient, StockSentimentClient  # noqa: E402
from adanos._generated.errors import UnexpectedStatus  # noqa: E402

BASE_URL = "https://api.adanos.org"
API_KEY = "sdk_test_key_1234567890abcdef1234567890"


def request_params(route) -> dict:
    """Extract query params from the last call on a respx route."""
    return dict(route.calls[0].request.url.params)


# --- Mock data matching generated model required fields ---

TRENDING_STOCK = {
    "ticker": "TSLA", "buzz_score": 85.0, "trend": "rising",
    "mentions": 120, "source_count": 5, "unique_posts": 80, "subreddit_count": 5,
    "sentiment_score": 0.6, "bullish_pct": 65, "bearish_pct": 15,
    "total_upvotes": 5000,
}

STOCK_SENTIMENT = {
    "ticker": "TSLA",
    "found": True,
    "mentions": 342,
    "total_mentions": 342,
    "sentiment_score": 0.271,
    "daily_trend": [
        {
            "date": "2026-03-18",
            "mentions": 61,
            "sentiment_score": 0.245,
            "sentiment": 0.245,
            "buzz_score": 71.2,
        }
    ],
}

SEARCH_RESPONSE = {
    "query": "Tesla",
    "count": 1,
    "period_days": 7,
    "results": [
        {
            "ticker": "TSLA",
            "name": "Tesla Inc",
            "summary": {
                "mentions": 342,
                "buzz_score": 87.5,
                "trend": "rising",
                "sentiment_score": 0.231,
                "bullish_pct": 58,
                "bearish_pct": 16,
                "unique_posts": 112,
                "subreddit_count": 7,
                "total_upvotes": 9042,
            },
        },
    ],
}

POLYMARKET_SEARCH_RESPONSE = {
    "query": "AAPL", "count": 1, "period_days": 7, "results": [
        {
            "ticker": "AAPL",
            "name": "Apple Inc.",
            "type": "Stock",
            "exchange": "NASDAQ",
            "sector": "Technology",
            "country": "United States",
            "aliases": ["Apple"],
            "summary": {
                "trade_count": 12,
                "market_count": 3,
                "unique_traders": 9,
                "total_liquidity": 45200.0,
                "buzz_score": 71.4,
                "trend": "stable",
                "sentiment_score": 0.118,
                "bullish_pct": 55,
                "bearish_pct": 45,
            },
        },
    ],
}

COMPARE_RESPONSE = {
    "period_days": 7,
    "stocks": [
        {
            "ticker": "TSLA",
            "company_name": "Tesla, Inc.",
            "buzz_score": 87.5,
            "trend": "rising",
            "mentions": 342,
            "unique_posts": 112,
            "subreddit_count": 7,
            "sentiment_score": 0.231,
            "sentiment": 0.231,
            "bullish_pct": 58,
            "bearish_pct": 16,
            "total_upvotes": 9042,
            "upvotes": 9042,
            "trend_history": [51.2, 58.4, 64.1, 70.2, 75.9, 81.4, 87.5],
        }
    ],
}

NEWS_COMPARE_RESPONSE = {
    "period_days": 7,
    "stocks": [
        {
            "ticker": "TSLA",
            "company_name": "Tesla, Inc.",
            "buzz_score": 61.2,
            "mentions": 42,
            "source_count": 7,
            "trend": "rising",
            "sentiment_score": 0.31,
            "sentiment": 0.31,
            "bullish_pct": 57,
            "bearish_pct": 18,
            "trend_history": [22.4, 24.9, 28.5, 33.2, 39.4, 47.0, 61.2],
        }
    ],
}

NEWS_TRENDING_SECTOR = {
    "sector": "Technology",
    "buzz_score": 63.5,
    "trend": "rising",
    "mentions": 180,
    "unique_tickers": 14,
    "source_count": 9,
    "sentiment_score": 0.28,
    "bullish_pct": 62,
    "bearish_pct": 14,
    "top_tickers": ["NVDA", "AAPL", "MSFT"],
}

NEWS_TRENDING_COUNTRY = {
    "country": "United States",
    "buzz_score": 68.1,
    "trend": "stable",
    "mentions": 260,
    "unique_tickers": 21,
    "source_count": 11,
    "sentiment_score": 0.22,
    "bullish_pct": 58,
    "bearish_pct": 16,
    "top_tickers": ["NVDA", "AMZN", "TSLA"],
}

NEWS_STATS = {
    "total_mentions": 1855,
    "unique_tickers": 766,
    "tickers": ["NVDA", "AAPL", "MSFT"],
    "supported_tickers": 11800,
    "days_covered": 30,
    "last_updated": "2026-03-07T08:36:07Z",
}

EXPLAIN_RESPONSE = {
    "ticker": "TSLA", "explanation": "Tesla is trending due to...",
    "cached": False, "generated_at": "2026-02-16T10:00:00Z",
    "model": "llama3.1:8b",
}

X_TRENDING_STOCK = {
    "ticker": "NVDA", "buzz_score": 90.0, "trend": "rising", "mentions": 200,
}

X_STOCK_DETAIL = {
    "ticker": "NVDA",
    "mentions": 156,
    "total_mentions": 156,
    "sentiment_score": 0.276,
    "daily_trend": [
        {
            "date": "2026-03-18",
            "mentions": 48,
            "sentiment_score": 0.244,
            "sentiment": 0.244,
            "avg_rank": 5.2,
            "buzz_score": 74.1,
        }
    ],
}

POLYMARKET_TRENDING_STOCK = {
    "ticker": "AAPL",
    "buzz_score": 71.4,
    "trend": "rising",
    "trade_count": 8,
    "market_count": 4,
    "unique_traders": 6,
    "bullish_pct": 67,
    "bearish_pct": 33,
    "total_liquidity": 94750.0,
}

POLYMARKET_STOCK_DETAIL = {
    "ticker": "AAPL",
    "found": True,
    "daily_trend": [
        {
            "date": "2026-03-18",
            "trade_count": 8,
            "sentiment_score": 0.114,
            "sentiment": 0.114,
            "buzz_score": 71.4,
        }
    ],
}

POLYMARKET_COMPARE_RESPONSE = {
    "period_days": 7,
    "stocks": [{
        "ticker": "AAPL",
        "buzz_score": 71.4,
        "trade_count": 8,
        "market_count": 4,
        "unique_traders": 6,
        "trend": "rising",
        "sentiment_score": 0.265,
        "sentiment": 0.265,
        "bullish_pct": 67,
        "bearish_pct": 33,
        "total_liquidity": 94750.0,
        "trend_history": [45.2, 49.1, 53.7, 58.0, 63.4, 68.9, 71.4],
    }],
}

REDDIT_MARKET_SENTIMENT = {
    "buzz_score": 57.4,
    "trend": "stable",
    "mentions": 3992,
    "unique_posts": 418,
    "subreddit_count": 21,
    "total_upvotes": 15234,
    "active_tickers": 1000,
    "sentiment_score": 0.045,
    "positive_count": 1440,
    "negative_count": 998,
    "neutral_count": 1554,
    "bullish_pct": 36,
    "bearish_pct": 25,
    "trend_history": [49.8, 52.1, 50.7, 55.6, 58.3, 60.2, 57.4],
    "drivers": [{"ticker": "SPY", "mentions": 129, "buzz_score": 74.1, "sentiment_score": 0.009}],
}

NEWS_MARKET_SENTIMENT = {
    "buzz_score": 53.8,
    "trend": "stable",
    "mentions": 1298,
    "unique_articles": 911,
    "source_count": 44,
    "active_tickers": 233,
    "sentiment_score": 0.064,
    "positive_count": 512,
    "negative_count": 308,
    "neutral_count": 478,
    "bullish_pct": 39,
    "bearish_pct": 24,
    "trend_history": [49.1, 50.4, 48.7, 52.2, 55.1, 54.3, 53.8],
    "drivers": [{"ticker": "AAPL", "mentions": 87, "buzz_score": 69.7, "sentiment_score": 0.22}],
}

X_MARKET_SENTIMENT = {
    "buzz_score": 56.2,
    "trend": "rising",
    "mentions": 2847,
    "unique_tweets": 913,
    "unique_authors": 604,
    "total_upvotes": 28471,
    "active_tickers": 442,
    "sentiment_score": 0.081,
    "positive_count": 1198,
    "negative_count": 741,
    "neutral_count": 908,
    "bullish_pct": 42,
    "bearish_pct": 26,
    "trend_history": [48.9, 50.7, 52.6, 54.4, 57.1, 58.3, 56.2],
    "drivers": [{"ticker": "TSLA", "mentions": 156, "buzz_score": 72.5, "sentiment_score": 0.35}],
}

POLYMARKET_MARKET_SENTIMENT = {
    "buzz_score": 58.4,
    "trend": "rising",
    "trade_count": 512,
    "market_count": 93,
    "unique_traders": 281,
    "total_liquidity": 245000.0,
    "active_tickers": 31,
    "sentiment_score": 0.11,
    "positive_count": 41,
    "negative_count": 29,
    "neutral_count": 23,
    "bullish_pct": 44,
    "bearish_pct": 31,
    "trend_history": [52.1, 54.0, 56.8, 59.2, 61.0, 60.1, 58.4],
    "drivers": [{"ticker": "AAPL", "trade_count": 52, "buzz_score": 68.9, "sentiment_score": 0.28}],
}

TRENDING_SECTOR = {
    "sector": "Technology", "buzz_score": 75.0, "trend": "rising",
    "mentions": 500, "unique_tickers": 20, "subreddit_count": 8,
    "sentiment_score": 0.5, "bullish_pct": 60, "bearish_pct": 20,
    "total_upvotes": 15000, "top_tickers": ["TSLA", "AAPL", "NVDA"],
}

TRENDING_COUNTRY = {
    "country": "United States", "buzz_score": 80.0, "trend": "stable",
    "mentions": 800, "unique_tickers": 30, "subreddit_count": 10,
    "sentiment_score": 0.4, "bullish_pct": 55, "bearish_pct": 25,
    "total_upvotes": 20000, "top_tickers": ["TSLA", "AAPL"],
}

# --- Fixtures ---

@pytest.fixture
def client():
    c = AdanosClient(api_key=API_KEY, base_url=BASE_URL)
    yield c
    c.close()


# --- Auth header ---

class TestAuth:
    @respx.mock
    def test_api_key_header_sent(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[])
        )
        client.reddit.trending()
        assert route.called
        request = route.calls[0].request
        assert request.headers["X-API-Key"] == API_KEY

    def test_custom_base_url(self):
        c = AdanosClient(api_key=API_KEY, base_url="https://custom.example.com")
        assert c._client._base_url == "https://custom.example.com"


# --- Reddit namespace ---

class TestRedditTrending:
    @respx.mock
    def test_trending_default_params(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[TRENDING_STOCK])
        )
        result = client.reddit.trending()
        assert route.called
        assert len(result) == 1
        assert result[0].ticker == "TSLA"
        assert result[0].buzz_score == 85.0

    @respx.mock
    def test_trending_with_params(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[])
        )
        client.reddit.trending(days=7, limit=5, offset=10, type="etf")
        request = route.calls[0].request
        assert request.url.params["days"] == "7"
        assert request.url.params["limit"] == "5"
        assert request.url.params["offset"] == "10"
        assert request.url.params["type"] == "etf"

    @respx.mock
    def test_trending_empty(self, client):
        respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[])
        )
        result = client.reddit.trending()
        assert result == []


class TestRedditStock:
    @respx.mock
    def test_stock_detail(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/stock/TSLA").mock(
            return_value=httpx.Response(200, json=STOCK_SENTIMENT)
        )
        result = client.reddit.stock("TSLA")
        assert route.called
        assert result.ticker == "TSLA"
        assert result.found is True
        assert result.mentions == 342
        assert result.total_mentions == 342
        assert result.daily_trend[0].sentiment_score == 0.245
        assert result.daily_trend[0].sentiment == 0.245

    @respx.mock
    def test_stock_with_days(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/stock/AAPL").mock(
            return_value=httpx.Response(200, json={**STOCK_SENTIMENT, "ticker": "AAPL"})
        )
        client.reddit.stock("AAPL", days=14)
        assert request_params(route)["days"] == "14"


class TestRedditExplain:
    @respx.mock
    def test_explain(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/stock/TSLA/explain").mock(
            return_value=httpx.Response(200, json=EXPLAIN_RESPONSE)
        )
        result = client.reddit.explain("TSLA")
        assert route.called
        assert result.explanation == "Tesla is trending due to..."


class TestRedditSearch:
    @respx.mock
    def test_search(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/search").mock(
            return_value=httpx.Response(200, json=SEARCH_RESPONSE)
        )
        result = client.reddit.search("Tesla", days=7, limit=5)
        assert route.called
        assert request_params(route)["q"] == "Tesla"
        assert request_params(route)["days"] == "7"
        assert request_params(route)["limit"] == "5"
        assert result.count == 1
        assert result.period_days == 7
        assert result.results[0].summary["mentions"] == 342


class TestRedditCompare:
    @respx.mock
    def test_compare(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/compare").mock(
            return_value=httpx.Response(200, json=COMPARE_RESPONSE)
        )
        result = client.reddit.compare(["TSLA", "AAPL"], days=7)
        assert route.called
        assert request_params(route)["tickers"] == "TSLA,AAPL"
        assert result.stocks[0].trend == "rising"
        assert result.stocks[0].trend_history[-1] == 87.5
        assert result.stocks[0].total_upvotes == 9042


class TestRedditMarketSentiment:
    @respx.mock
    def test_market_sentiment(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/market-sentiment").mock(
            return_value=httpx.Response(200, json=REDDIT_MARKET_SENTIMENT)
        )
        result = client.reddit.market_sentiment(days=7)
        assert route.called
        assert request_params(route)["days"] == "7"
        assert result["drivers"][0]["ticker"] == "SPY"


class TestRedditTrendingSectors:
    @respx.mock
    def test_trending_sectors(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending/sectors").mock(
            return_value=httpx.Response(200, json=[TRENDING_SECTOR])
        )
        result = client.reddit.trending_sectors(days=7)
        assert route.called
        assert len(result) == 1
        assert result[0].sector == "Technology"

    @respx.mock
    def test_trending_sectors_params(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending/sectors").mock(
            return_value=httpx.Response(200, json=[])
        )
        client.reddit.trending_sectors(days=3, limit=5, offset=2)
        params = request_params(route)
        assert params["days"] == "3"
        assert params["limit"] == "5"
        assert params["offset"] == "2"


class TestRedditTrendingCountries:
    @respx.mock
    def test_trending_countries(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending/countries").mock(
            return_value=httpx.Response(200, json=[TRENDING_COUNTRY])
        )
        result = client.reddit.trending_countries()
        assert route.called
        assert result[0].country == "United States"


class TestNews:
    @respx.mock
    def test_news_trending_with_source(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[TRENDING_STOCK])
        )
        result = client.news.trending(days=7, source="reuters")
        assert route.called
        assert len(result) == 1
        params = request_params(route)
        assert params["days"] == "7"
        assert params["source"] == "reuters"

    @respx.mock
    def test_news_stock(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/stock/TSLA").mock(
            return_value=httpx.Response(200, json=STOCK_SENTIMENT)
        )
        result = client.news.stock("TSLA")
        assert route.called
        assert result.ticker == "TSLA"
        assert result.mentions == 342
        assert result.total_mentions == 342
        assert request_params(route) == {"days": "7"}

    @respx.mock
    def test_news_health(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/health").mock(
            return_value=httpx.Response(200, json={"status": "healthy", "total_mentions": 0, "tickers_tracked": 0})
        )
        result = client.news.health()
        assert route.called
        assert result.status == "healthy"

    @respx.mock
    def test_news_compare(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/compare").mock(
            return_value=httpx.Response(200, json=NEWS_COMPARE_RESPONSE)
        )
        result = client.news.compare(["TSLA", "NVDA"], days=7)
        assert route.called
        params = request_params(route)
        assert params["tickers"] == "TSLA,NVDA"
        assert "source" not in params
        assert result.stocks[0].source_count == 7

    @respx.mock
    def test_news_trending_sectors(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/trending/sectors").mock(
            return_value=httpx.Response(200, json=[NEWS_TRENDING_SECTOR])
        )
        result = client.news.trending_sectors(days=3, source="reuters")
        assert route.called
        params = request_params(route)
        assert params["days"] == "3"
        assert params["source"] == "reuters"
        assert result[0].source_count == 9

    @respx.mock
    def test_news_trending_countries(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/trending/countries").mock(
            return_value=httpx.Response(200, json=[NEWS_TRENDING_COUNTRY])
        )
        result = client.news.trending_countries(source="reuters")
        assert route.called
        assert request_params(route)["source"] == "reuters"
        assert result[0].country == "United States"

    @respx.mock
    def test_news_explain(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/stock/TSLA/explain").mock(
            return_value=httpx.Response(200, json=EXPLAIN_RESPONSE)
        )
        result = client.news.explain("TSLA")
        assert route.called
        assert request_params(route) == {}
        assert result.explanation == EXPLAIN_RESPONSE["explanation"]

    @respx.mock
    def test_news_search(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/search").mock(
            return_value=httpx.Response(200, json=SEARCH_RESPONSE)
        )
        result = client.news.search("Tesla", days=7, limit=5)
        assert route.called
        params = request_params(route)
        assert params["q"] == "Tesla"
        assert params["days"] == "7"
        assert params["limit"] == "5"
        assert "source" not in params
        assert result.count == 1
        assert result.period_days == 7
        assert result.results[0].summary["buzz_score"] == 87.5

    @respx.mock
    def test_news_stats(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/stats").mock(
            return_value=httpx.Response(200, json=NEWS_STATS)
        )
        result = client.news.stats()
        assert route.called
        assert request_params(route) == {}
        assert result.total_mentions == NEWS_STATS["total_mentions"]

    @respx.mock
    def test_news_market_sentiment(self, client):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/market-sentiment").mock(
            return_value=httpx.Response(200, json=NEWS_MARKET_SENTIMENT)
        )
        result = client.news.market_sentiment(days=3)
        assert route.called
        assert request_params(route)["days"] == "3"
        assert result["source_count"] == 44


# --- Async methods ---

class TestAsync:
    @respx.mock
    @pytest.mark.asyncio
    async def test_reddit_trending_async(self):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[TRENDING_STOCK])
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.reddit.trending_async(days=7)
        assert route.called
        assert len(result) == 1
        assert result[0].ticker == "TSLA"

    @respx.mock
    @pytest.mark.asyncio
    async def test_reddit_stock_async(self):
        respx.get(f"{BASE_URL}/reddit/stocks/v1/stock/TSLA").mock(
            return_value=httpx.Response(200, json=STOCK_SENTIMENT)
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.reddit.stock_async("TSLA")
        assert result.ticker == "TSLA"

    @respx.mock
    @pytest.mark.asyncio
    async def test_x_trending_async(self):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[X_TRENDING_STOCK])
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.x.trending_async()
        assert route.called
        assert result[0].ticker == "NVDA"

    @respx.mock
    @pytest.mark.asyncio
    async def test_x_explain_async(self):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/stock/NVDA/explain").mock(
            return_value=httpx.Response(200, json=EXPLAIN_RESPONSE)
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.x.explain_async("NVDA")
        assert route.called
        assert result.explanation == EXPLAIN_RESPONSE["explanation"]

    @respx.mock
    @pytest.mark.asyncio
    async def test_reddit_search_async(self):
        respx.get(f"{BASE_URL}/reddit/stocks/v1/search").mock(
            return_value=httpx.Response(200, json=SEARCH_RESPONSE)
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.reddit.search_async("Tesla", days=7, limit=5)
        assert result.count == 1
        assert result.period_days == 7

    @respx.mock
    @pytest.mark.asyncio
    async def test_polymarket_trending_async(self):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[POLYMARKET_TRENDING_STOCK])
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.polymarket.trending_async(days=7)
        assert route.called
        assert len(result) == 1
        assert result[0].ticker == "AAPL"

    @respx.mock
    @pytest.mark.asyncio
    async def test_reddit_compare_async(self):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/compare").mock(
            return_value=httpx.Response(200, json=COMPARE_RESPONSE)
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            await client.reddit.compare_async(["TSLA", "AAPL"])
        assert request_params(route)["tickers"] == "TSLA,AAPL"

    @respx.mock
    @pytest.mark.asyncio
    async def test_news_trending_async(self):
        route = respx.get(f"{BASE_URL}/news/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[TRENDING_STOCK])
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.news.trending_async(days=7, source="reuters")
        assert route.called
        assert request_params(route)["source"] == "reuters"
        assert len(result) == 1

    @respx.mock
    @pytest.mark.asyncio
    async def test_reddit_market_sentiment_async(self):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/market-sentiment").mock(
            return_value=httpx.Response(200, json=REDDIT_MARKET_SENTIMENT)
        )
        async with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            result = await client.reddit.market_sentiment_async(days=5)
        assert route.called
        assert request_params(route)["days"] == "5"
        assert result["buzz_score"] == 57.4


# --- X namespace ---

class TestXTrending:
    @respx.mock
    def test_trending(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[X_TRENDING_STOCK])
        )
        result = client.x.trending()
        assert route.called
        assert len(result) == 1
        assert result[0].ticker == "NVDA"

    @respx.mock
    def test_trending_with_type(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[])
        )
        client.x.trending(type="stock")
        assert request_params(route)["type"] == "stock"


class TestXStock:
    @respx.mock
    def test_stock(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/stock/NVDA").mock(
            return_value=httpx.Response(200, json=X_STOCK_DETAIL)
        )
        result = client.x.stock("NVDA")
        assert route.called
        assert result.ticker == "NVDA"
        assert result.mentions == 156
        assert result.total_mentions == 156
        assert result.daily_trend[0].sentiment_score == 0.244


class TestXExplain:
    @respx.mock
    def test_explain(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/stock/NVDA/explain").mock(
            return_value=httpx.Response(200, json=EXPLAIN_RESPONSE)
        )
        result = client.x.explain("NVDA")
        assert route.called
        assert request_params(route) == {}
        assert result.explanation == EXPLAIN_RESPONSE["explanation"]

    @respx.mock
    def test_explain_encodes_ticker_path(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/stock/%24GME/explain").mock(
            return_value=httpx.Response(200, json={**EXPLAIN_RESPONSE, "ticker": "GME"})
        )
        result = client.x.explain("$GME")
        assert route.called
        assert result.ticker == "GME"

    @respx.mock
    def test_explain_accepts_empty_503_response(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/stock/NVDA/explain").mock(
            return_value=httpx.Response(503)
        )
        result = client.x.explain("NVDA")
        assert route.called
        assert result is None


class TestXSearch:
    @respx.mock
    def test_search(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/search").mock(
            return_value=httpx.Response(200, json={**SEARCH_RESPONSE, "query": "NVDA"})
        )
        result = client.x.search("NVDA", days=7, limit=5)
        assert route.called
        assert request_params(route)["days"] == "7"
        assert request_params(route)["limit"] == "5"
        assert result.period_days == 7


class TestXCompare:
    @respx.mock
    def test_compare(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/compare").mock(
            return_value=httpx.Response(200, json=COMPARE_RESPONSE)
        )
        result = client.x.compare(["NVDA", "AMD"])
        assert route.called
        assert request_params(route)["tickers"] == "NVDA,AMD"
        assert result.stocks[0].trend_history[-1] == 87.5


class TestXMarketSentiment:
    @respx.mock
    def test_market_sentiment(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/market-sentiment").mock(
            return_value=httpx.Response(200, json=X_MARKET_SENTIMENT)
        )
        result = client.x.market_sentiment()
        assert route.called
        assert request_params(route)["days"] == "1"
        assert result["unique_authors"] == 604


# --- Polymarket namespace ---

class TestPolymarketTrending:
    @respx.mock
    def test_trending(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[POLYMARKET_TRENDING_STOCK])
        )
        result = client.polymarket.trending()
        assert route.called
        assert len(result) == 1
        assert result[0].ticker == "AAPL"
        assert result[0].trade_count == 8
        assert result[0].market_count == 4
        assert result[0].unique_traders == 6

    @respx.mock
    def test_trending_with_type(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[])
        )
        client.polymarket.trending(type="etf")
        assert request_params(route)["type"] == "etf"


class TestPolymarketStock:
    @respx.mock
    def test_stock(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/stock/AAPL").mock(
            return_value=httpx.Response(200, json=POLYMARKET_STOCK_DETAIL)
        )
        result = client.polymarket.stock("AAPL")
        assert route.called
        assert result.ticker == "AAPL"
        assert result.found is True
        assert result.daily_trend[0].sentiment_score == 0.114
        assert result.daily_trend[0].sentiment == 0.114


class TestPolymarketSearch:
    @respx.mock
    def test_search(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/search").mock(
            return_value=httpx.Response(200, json=POLYMARKET_SEARCH_RESPONSE)
        )
        result = client.polymarket.search("AAPL", days=7, limit=5)
        assert route.called
        assert request_params(route)["q"] == "AAPL"
        assert request_params(route)["days"] == "7"
        assert request_params(route)["limit"] == "5"
        assert result.query == "AAPL"
        assert result.count == 1
        assert result.period_days == 7
        assert result.results[0].summary["trade_count"] == 12


class TestPolymarketCompare:
    @respx.mock
    def test_compare(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/compare").mock(
            return_value=httpx.Response(200, json=POLYMARKET_COMPARE_RESPONSE)
        )
        result = client.polymarket.compare(["AAPL", "TSLA"])
        assert route.called
        assert request_params(route)["tickers"] == "AAPL,TSLA"
        assert result.stocks[0].trade_count == 8
        assert result.stocks[0].market_count == 4
        assert result.stocks[0].trend_history[-1] == 71.4


class TestPolymarketMarketSentiment:
    @respx.mock
    def test_market_sentiment(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/market-sentiment").mock(
            return_value=httpx.Response(200, json=POLYMARKET_MARKET_SENTIMENT)
        )
        result = client.polymarket.market_sentiment(days=2)
        assert route.called
        assert request_params(route)["days"] == "2"
        assert result["drivers"][0]["trade_count"] == 52


# --- Context manager ---

class TestContextManager:
    @respx.mock
    def test_sync_context_manager(self):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(200, json=[])
        )
        with AdanosClient(api_key=API_KEY, base_url=BASE_URL) as client:
            client.reddit.trending()
        assert route.called


def test_legacy_client_alias() -> None:
    assert StockSentimentClient is AdanosClient


# --- Error handling ---

class TestErrors:
    @respx.mock
    def test_undocumented_status_raises(self, client):
        """raise_on_unexpected_status=True should raise for undocumented codes."""
        respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(500, content=b"Internal Server Error")
        )
        with pytest.raises(UnexpectedStatus):
            client.reddit.trending()

    @respx.mock
    def test_401_returns_error_response(self, client):
        """401 is a documented status — returns ErrorResponse, not exception."""
        respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(401, json={"detail": "Invalid API key"})
        )
        result = client.reddit.trending()
        assert result.detail == "Invalid API key"

    @respx.mock
    def test_429_returns_error_response(self, client):
        """429 is a documented status — returns ErrorResponse."""
        respx.get(f"{BASE_URL}/reddit/stocks/v1/trending").mock(
            return_value=httpx.Response(429, json={"detail": "Rate limit exceeded"})
        )
        result = client.reddit.trending()
        assert result.detail == "Rate limit exceeded"


# --- Extended coverage: crypto + stats + health ---

CRYPTO_TOKEN_DETAIL = {
    "symbol": "BTC",
    "found": True,
    "name": "Bitcoin",
    "buzz_score": 90.1,
    "mentions": 321,
    "total_mentions": 321,
    "sentiment_score": 0.42,
    "daily_trend": [
        {
            "date": "2026-03-18",
            "mentions": 54,
            "sentiment_score": 0.33,
            "sentiment": 0.33,
            "buzz_score": 75.1,
        }
    ],
}

CRYPTO_TRENDING = [
    {
        "symbol": "BTC",
        "name": "Bitcoin",
        "buzz_score": 90.1,
        "trend": "rising",
        "mentions": 321,
        "unique_posts": 120,
        "subreddit_count": 15,
        "sentiment_score": 0.42,
        "bullish_pct": 58,
        "bearish_pct": 14,
        "total_upvotes": 9900,
    }
]

CRYPTO_COMPARE = {
    "period_days": 7,
    "tokens": [
        {
            "symbol": "BTC",
            "name": "Bitcoin",
            "buzz_score": 90.1,
            "trend": "rising",
            "mentions": 321,
            "unique_posts": 120,
            "subreddit_count": 15,
            "sentiment_score": 0.42,
            "sentiment": 0.42,
            "bullish_pct": 58,
            "bearish_pct": 14,
            "total_upvotes": 9900,
            "upvotes": 9900,
            "trend_history": [60.1, 64.2, 70.4, 74.3, 81.8, 86.0, 90.1],
        },
        {
            "symbol": "ETH",
            "name": "Ethereum",
            "buzz_score": 75.3,
            "trend": "stable",
            "mentions": 210,
            "unique_posts": 88,
            "subreddit_count": 12,
            "sentiment_score": 0.31,
            "sentiment": 0.31,
            "bullish_pct": 49,
            "bearish_pct": 18,
            "total_upvotes": 6500,
            "upvotes": 6500,
            "trend_history": [51.3, 53.0, 58.6, 60.2, 66.9, 71.4, 75.3],
        },
    ],
}

CRYPTO_SEARCH = {
    "query": "btc",
    "count": 1,
    "period_days": 7,
    "results": [
        {
            "symbol": "BTC",
            "name": "Bitcoin",
            "summary": {
                "mentions": 321,
                "buzz_score": 90.1,
                "trend": "rising",
                "sentiment_score": 0.42,
                "bullish_pct": 58,
                "bearish_pct": 14,
                "unique_posts": 120,
                "subreddit_count": 15,
                "total_upvotes": 9900,
            },
        }
    ],
}

CRYPTO_STATS = {
    "total_mentions": 18352,
    "unique_tokens": 142,
    "tokens": ["BTC", "ETH", "SOL"],
    "supported_tokens": 500,
}

REDDIT_HEALTH = {"status": "healthy", "service": "reddit-stocks", "total_mentions": 100, "tickers_tracked": 20}
CRYPTO_HEALTH = {"status": "healthy", "service": "reddit-crypto", "total_mentions": 200, "tokens_tracked": 30}
X_HEALTH = {"status": "healthy", "service": "x-stocks", "version": "1.20.0", "total_mentions": 300, "tickers_tracked": 40}
POLYMARKET_HEALTH = {
    "status": "healthy",
    "service": "polymarket-stocks",
    "version": "1.20.0",
    "total_mentions": 400,
    "tickers_tracked": 50,
}
X_STATS = {"total_appearances": 935, "unique_tickers": 100, "tickers": ["TSLA"], "supported_tickers": 11800, "validation_rate": 37.5}
POLYMARKET_STATS = {"total_trades": 15420, "total_markets": 713, "unique_tickers": 119, "tickers": ["AAPL"], "supported_tickers": 11800}
REDDIT_STATS = {"total_mentions": 12833, "unique_tickers": 65, "tickers": ["AAPL"], "supported_tickers": 11800}
CRYPTO_MARKET_SENTIMENT = {
    "buzz_score": 52.4,
    "trend": "rising",
    "mentions": 5412,
    "unique_posts": 1184,
    "subreddit_count": 37,
    "total_upvotes": 41290,
    "active_tickers": 89,
    "sentiment_score": 0.117,
    "positive_count": 2101,
    "negative_count": 1318,
    "neutral_count": 1993,
    "bullish_pct": 39,
    "bearish_pct": 24,
    "trend_history": [47.1, 49.3, 50.4, 52.2, 51.8, 53.0, 52.4],
    "drivers": [{"symbol": "BTC", "mentions": 423, "buzz_score": 78.1, "sentiment_score": 0.31}],
}


class TestCryptoNamespace:
    @respx.mock
    def test_crypto_token(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/token/BTC").mock(
            return_value=httpx.Response(200, json=CRYPTO_TOKEN_DETAIL)
        )
        result = client.crypto.token("BTC")
        assert route.called
        assert result.symbol == "BTC"
        assert result.found is True
        assert result.mentions == 321
        assert result.total_mentions == 321

    @respx.mock
    def test_crypto_market_sentiment(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/market-sentiment").mock(
            return_value=httpx.Response(200, json=CRYPTO_MARKET_SENTIMENT)
        )
        result = client.crypto.market_sentiment(days=4)
        assert route.called
        assert request_params(route)["days"] == "4"
        assert result["drivers"][0]["symbol"] == "BTC"

    @respx.mock
    def test_crypto_trending(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/trending").mock(
            return_value=httpx.Response(200, json=CRYPTO_TRENDING)
        )
        result = client.crypto.trending(days=7, limit=10, offset=0)
        assert route.called
        assert result[0].symbol == "BTC"

    @respx.mock
    def test_crypto_search(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/search").mock(
            return_value=httpx.Response(200, json=CRYPTO_SEARCH)
        )
        result = client.crypto.search("btc", days=7, limit=5)
        assert route.called
        assert request_params(route)["q"] == "btc"
        assert request_params(route)["days"] == "7"
        assert request_params(route)["limit"] == "5"
        assert result.count == 1
        assert result.period_days == 7
        assert result.results[0].summary["mentions"] == 321

    @respx.mock
    def test_crypto_compare(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/compare").mock(
            return_value=httpx.Response(200, json=CRYPTO_COMPARE)
        )
        result = client.crypto.compare(["BTC", "ETH"], days=7)
        assert route.called
        assert request_params(route)["symbols"] == "BTC,ETH"
        assert result.tokens[0].symbol == "BTC"
        assert result.tokens[0].mentions == 321
        assert result.tokens[0].trend_history[-1] == 90.1

    @respx.mock
    def test_crypto_compare_fallback_when_compare_shape_drifts(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/compare").mock(
            return_value=httpx.Response(
                200,
                json={
                    "period_days": 7,
                    "tokens": [
                        {"symbol": "BTC", "found": True, "buzz_score": 90.1, "total_mentions": 321, "sentiment_score": 0.42},
                        {"symbol": "ETH", "found": True, "buzz_score": 75.3, "total_mentions": 210, "sentiment_score": 0.31},
                    ],
                },
            )
        )
        result = client.crypto.compare(["BTC", "ETH"], days=7)
        assert route.called
        assert request_params(route)["symbols"] == "BTC,ETH"
        assert isinstance(result, dict)
        assert result["tokens"][0]["symbol"] == "BTC"

    @respx.mock
    def test_crypto_stats(self, client):
        route = respx.get(f"{BASE_URL}/reddit/crypto/v1/stats").mock(
            return_value=httpx.Response(200, json=CRYPTO_STATS)
        )
        result = client.crypto.stats()
        assert route.called
        assert result.unique_tokens == 142


class TestStatsAndHealth:
    @respx.mock
    def test_reddit_stats(self, client):
        route = respx.get(f"{BASE_URL}/reddit/stocks/v1/stats").mock(
            return_value=httpx.Response(200, json=REDDIT_STATS)
        )
        result = client.reddit.stats()
        assert route.called
        assert result.unique_tickers == 65

    @respx.mock
    def test_x_stats(self, client):
        route = respx.get(f"{BASE_URL}/x/stocks/v1/stats").mock(
            return_value=httpx.Response(200, json=X_STATS)
        )
        result = client.x.stats()
        assert route.called
        assert result.unique_tickers == 100

    @respx.mock
    def test_polymarket_stats(self, client):
        route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/stats").mock(
            return_value=httpx.Response(200, json=POLYMARKET_STATS)
        )
        result = client.polymarket.stats()
        assert route.called
        assert result.total_markets == 713

    @respx.mock
    def test_all_health_endpoints(self, client):
        reddit_route = respx.get(f"{BASE_URL}/reddit/stocks/v1/health").mock(
            return_value=httpx.Response(200, json=REDDIT_HEALTH)
        )
        crypto_route = respx.get(f"{BASE_URL}/reddit/crypto/v1/health").mock(
            return_value=httpx.Response(200, json=CRYPTO_HEALTH)
        )
        x_route = respx.get(f"{BASE_URL}/x/stocks/v1/health").mock(
            return_value=httpx.Response(200, json=X_HEALTH)
        )
        polymarket_route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/health").mock(
            return_value=httpx.Response(200, json=POLYMARKET_HEALTH)
        )

        assert client.reddit.health().status == "healthy"
        assert client.crypto.health().status == "healthy"
        assert client.x.health().status == "healthy"
        assert client.polymarket.health().status == "healthy"
        assert reddit_route.called
        assert crypto_route.called
        assert x_route.called
        assert polymarket_route.called
