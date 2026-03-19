"""Ergonomic wrapper around the generated OpenAPI client."""

from __future__ import annotations

from typing import Any, Optional

from ._generated.client import AuthenticatedClient
from ._generated.types import UNSET


def _resolve_reddit_type(type: Optional[str]) -> Any:
    if type is None:
        return UNSET
    from ._generated.models.get_trending_stocks_type_type_0 import GetTrendingStocksTypeType0
    return GetTrendingStocksTypeType0(type)


def _resolve_news_type(type: Optional[str]) -> Any:
    if type is None:
        return UNSET
    from ._generated.models.get_news_trending_stocks_type_type_0 import GetNewsTrendingStocksTypeType0
    return GetNewsTrendingStocksTypeType0(type)


def _resolve_x_type(type: Optional[str]) -> Any:
    if type is None:
        return UNSET
    from ._generated.models.get_x_trending_stocks_type_type_0 import GetXTrendingStocksTypeType0
    return GetXTrendingStocksTypeType0(type)


def _resolve_polymarket_type(type: Optional[str]) -> Any:
    if type is None:
        return UNSET
    from ._generated.models.get_polymarket_trending_stocks_type_type_0 import (
        GetPolymarketTrendingStocksTypeType0,
    )

    return GetPolymarketTrendingStocksTypeType0(type)


class _RedditNamespace:
    """Access Reddit sentiment endpoints via ``client.reddit.*``."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def trending(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
    ) -> Any:
        """Get trending stocks on Reddit.

        Args:
            days: Time period (1-90). Free tier limited to 30.
            limit: Max results (1-100).
            offset: Pagination offset.
            type: Filter by ``"stock"``, ``"etf"``, or ``None`` for all.
        """
        from ._generated.api.reddit_stocks import get_trending_stocks
        return get_trending_stocks.sync(
            client=self._client, days=days, limit=limit, offset=offset, type_=_resolve_reddit_type(type),
        )

    async def trending_async(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
    ) -> Any:
        """Async variant of :meth:`trending`."""
        from ._generated.api.reddit_stocks import get_trending_stocks
        return await get_trending_stocks.asyncio(
            client=self._client, days=days, limit=limit, offset=offset, type_=_resolve_reddit_type(type),
        )

    def trending_sectors(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending sectors on Reddit."""
        from ._generated.api.reddit_stocks import get_trending_sectors
        return get_trending_sectors.sync(client=self._client, days=days, limit=limit, offset=offset)

    async def trending_sectors_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending_sectors`."""
        from ._generated.api.reddit_stocks import get_trending_sectors
        return await get_trending_sectors.asyncio(client=self._client, days=days, limit=limit, offset=offset)

    def trending_countries(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending countries on Reddit."""
        from ._generated.api.reddit_stocks import get_trending_countries
        return get_trending_countries.sync(client=self._client, days=days, limit=limit, offset=offset)

    async def trending_countries_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending_countries`."""
        from ._generated.api.reddit_stocks import get_trending_countries
        return await get_trending_countries.asyncio(client=self._client, days=days, limit=limit, offset=offset)

    def stock(self, ticker: str, *, days: int = 7) -> Any:
        """Get sentiment for a specific stock ticker.

        Args:
            ticker: Stock symbol (e.g. ``"TSLA"``).
            days: Time period (1-90). Free tier limited to 30.
        """
        from ._generated.api.reddit_stocks import get_stock_sentiment
        return get_stock_sentiment.sync(ticker, client=self._client, days=days)

    async def stock_async(self, ticker: str, *, days: int = 7) -> Any:
        """Async variant of :meth:`stock`."""
        from ._generated.api.reddit_stocks import get_stock_sentiment
        return await get_stock_sentiment.asyncio(ticker, client=self._client, days=days)

    def explain(self, ticker: str) -> Any:
        """Get AI-generated explanation for a stock's trend.

        Args:
            ticker: Stock symbol (e.g. ``"TSLA"``).
        """
        from ._generated.api.reddit_stocks import get_stock_explanation
        return get_stock_explanation.sync(ticker, client=self._client)

    async def explain_async(self, ticker: str) -> Any:
        """Async variant of :meth:`explain`."""
        from ._generated.api.reddit_stocks import get_stock_explanation
        return await get_stock_explanation.asyncio(ticker, client=self._client)

    def search(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Search for stocks by name or ticker.

        Args:
            query: Search term (e.g. ``"Tesla"`` or ``"TSLA"``).
            days: Lookback window for the attached summary block.
            limit: Maximum number of results to return.
        """
        from ._generated.api.reddit_stocks import search_stocks
        return search_stocks.sync(client=self._client, q=query, days=days, limit=limit)

    async def search_async(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Async variant of :meth:`search`."""
        from ._generated.api.reddit_stocks import search_stocks
        return await search_stocks.asyncio(client=self._client, q=query, days=days, limit=limit)

    def compare(self, tickers: list[str], *, days: int = 7) -> Any:
        """Compare multiple stocks side-by-side.

        Args:
            tickers: List of ticker symbols (max 10).
            days: Time period (1-90).
        """
        from ._generated.api.reddit_stocks import compare_stocks
        return compare_stocks.sync(client=self._client, tickers=",".join(tickers), days=days)

    async def compare_async(self, tickers: list[str], *, days: int = 7) -> Any:
        """Async variant of :meth:`compare`."""
        from ._generated.api.reddit_stocks import compare_stocks
        return await compare_stocks.asyncio(client=self._client, tickers=",".join(tickers), days=days)

    def stats(self) -> Any:
        """Get Reddit stock dataset statistics."""
        from ._generated.api.reddit_stocks import get_stats
        return get_stats.sync(client=self._client)

    async def stats_async(self) -> Any:
        """Async variant of :meth:`stats`."""
        from ._generated.api.reddit_stocks import get_stats
        return await get_stats.asyncio(client=self._client)

    def health(self) -> Any:
        """Get public Reddit stock service health."""
        from ._generated.api.status import get_health
        return get_health.sync(client=self._client)

    async def health_async(self) -> Any:
        """Async variant of :meth:`health`."""
        from ._generated.api.status import get_health
        return await get_health.asyncio(client=self._client)


class _NewsNamespace:
    """Access News sentiment endpoints via ``client.news.*``."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def trending(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
        source: Optional[str] = None,
    ) -> Any:
        """Get trending stocks in news."""
        from ._generated.api.news_stocks import get_news_trending_stocks
        return get_news_trending_stocks.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            type_=_resolve_news_type(type),
            source=source if source is not None else UNSET,
        )

    async def trending_async(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
        source: Optional[str] = None,
    ) -> Any:
        """Async variant of :meth:`trending`."""
        from ._generated.api.news_stocks import get_news_trending_stocks
        return await get_news_trending_stocks.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            type_=_resolve_news_type(type),
            source=source if source is not None else UNSET,
        )

    def trending_sectors(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        source: Optional[str] = None,
    ) -> Any:
        """Get trending sectors in news."""
        from ._generated.api.news_stocks import get_news_trending_sectors
        return get_news_trending_sectors.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            source=source if source is not None else UNSET,
        )

    async def trending_sectors_async(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        source: Optional[str] = None,
    ) -> Any:
        """Async variant of :meth:`trending_sectors`."""
        from ._generated.api.news_stocks import get_news_trending_sectors
        return await get_news_trending_sectors.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            source=source if source is not None else UNSET,
        )

    def trending_countries(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        source: Optional[str] = None,
    ) -> Any:
        """Get trending countries in news."""
        from ._generated.api.news_stocks import get_news_trending_countries
        return get_news_trending_countries.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            source=source if source is not None else UNSET,
        )

    async def trending_countries_async(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        source: Optional[str] = None,
    ) -> Any:
        """Async variant of :meth:`trending_countries`."""
        from ._generated.api.news_stocks import get_news_trending_countries
        return await get_news_trending_countries.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            source=source if source is not None else UNSET,
        )

    def stock(self, ticker: str, *, days: int = 7) -> Any:
        """Get sentiment for a specific stock ticker from news."""
        from ._generated.api.news_stocks import get_news_stock_sentiment
        return get_news_stock_sentiment.sync(
            ticker=ticker,
            client=self._client,
            days=days,
        )

    async def stock_async(self, ticker: str, *, days: int = 7) -> Any:
        """Async variant of :meth:`stock`."""
        from ._generated.api.news_stocks import get_news_stock_sentiment
        return await get_news_stock_sentiment.asyncio(
            ticker=ticker,
            client=self._client,
            days=days,
        )

    def explain(self, ticker: str) -> Any:
        """Get AI explanation for a stock trend in news."""
        from ._generated.api.news_stocks import get_news_stock_explanation
        return get_news_stock_explanation.sync(
            ticker=ticker,
            client=self._client,
        )

    async def explain_async(self, ticker: str) -> Any:
        """Async variant of :meth:`explain`."""
        from ._generated.api.news_stocks import get_news_stock_explanation
        return await get_news_stock_explanation.asyncio(
            ticker=ticker,
            client=self._client,
        )

    def search(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Search stocks by name/ticker in news."""
        from ._generated.api.news_stocks import search_news_stocks
        return search_news_stocks.sync(
            client=self._client,
            q=query,
            days=days,
            limit=limit,
        )

    async def search_async(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Async variant of :meth:`search`."""
        from ._generated.api.news_stocks import search_news_stocks
        return await search_news_stocks.asyncio(
            client=self._client,
            q=query,
            days=days,
            limit=limit,
        )

    def compare(self, tickers: list[str], *, days: int = 7) -> Any:
        """Compare multiple stocks in news sentiment."""
        from ._generated.api.news_stocks import compare_news_stocks
        return compare_news_stocks.sync(
            client=self._client,
            tickers=",".join(tickers),
            days=days,
        )

    async def compare_async(self, tickers: list[str], *, days: int = 7) -> Any:
        """Async variant of :meth:`compare`."""
        from ._generated.api.news_stocks import compare_news_stocks
        return await compare_news_stocks.asyncio(
            client=self._client,
            tickers=",".join(tickers),
            days=days,
        )

    def stats(self) -> Any:
        """Get News stock dataset statistics."""
        from ._generated.api.news_stocks import get_news_stats
        return get_news_stats.sync(client=self._client)

    async def stats_async(self) -> Any:
        """Async variant of :meth:`stats`."""
        from ._generated.api.news_stocks import get_news_stats
        return await get_news_stats.asyncio(client=self._client)

    def health(self) -> Any:
        """Get public News stock service health."""
        from ._generated.api.status import get_news_health
        return get_news_health.sync(client=self._client)

    async def health_async(self) -> Any:
        """Async variant of :meth:`health`."""
        from ._generated.api.status import get_news_health
        return await get_news_health.asyncio(client=self._client)


class _XNamespace:
    """Access X/Twitter sentiment endpoints via ``client.x.*``."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def trending(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
    ) -> Any:
        """Get trending stocks on X/Twitter.

        Args:
            days: Time period (1-90). Free tier limited to 30.
            limit: Max results (1-100).
            offset: Pagination offset.
            type: Filter by ``"stock"``, ``"etf"``, or ``None`` for all.
        """
        from ._generated.api.x_twitter_stocks import get_x_trending_stocks
        return get_x_trending_stocks.sync(
            client=self._client, days=days, limit=limit, offset=offset, type_=_resolve_x_type(type),
        )

    async def trending_async(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
    ) -> Any:
        """Async variant of :meth:`trending`."""
        from ._generated.api.x_twitter_stocks import get_x_trending_stocks
        return await get_x_trending_stocks.asyncio(
            client=self._client, days=days, limit=limit, offset=offset, type_=_resolve_x_type(type),
        )

    def trending_sectors(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending sectors on X/Twitter."""
        from ._generated.api.x_twitter_stocks import get_x_trending_sectors
        return get_x_trending_sectors.sync(client=self._client, days=days, limit=limit, offset=offset)

    async def trending_sectors_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending_sectors`."""
        from ._generated.api.x_twitter_stocks import get_x_trending_sectors
        return await get_x_trending_sectors.asyncio(client=self._client, days=days, limit=limit, offset=offset)

    def trending_countries(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending countries on X/Twitter."""
        from ._generated.api.x_twitter_stocks import get_x_trending_countries
        return get_x_trending_countries.sync(client=self._client, days=days, limit=limit, offset=offset)

    async def trending_countries_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending_countries`."""
        from ._generated.api.x_twitter_stocks import get_x_trending_countries
        return await get_x_trending_countries.asyncio(client=self._client, days=days, limit=limit, offset=offset)

    def stock(self, ticker: str, *, days: int = 7) -> Any:
        """Get X/Twitter sentiment for a specific stock ticker.

        Args:
            ticker: Stock symbol (e.g. ``"TSLA"``).
            days: Time period (1-90). Free tier limited to 30.
        """
        from ._generated.api.x_twitter_stocks import get_x_stock_sentiment
        return get_x_stock_sentiment.sync(ticker, client=self._client, days=days)

    async def stock_async(self, ticker: str, *, days: int = 7) -> Any:
        """Async variant of :meth:`stock`."""
        from ._generated.api.x_twitter_stocks import get_x_stock_sentiment
        return await get_x_stock_sentiment.asyncio(ticker, client=self._client, days=days)

    def search(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Search for stocks by name or ticker on X/Twitter.

        Args:
            query: Search term (e.g. ``"Tesla"`` or ``"TSLA"``).
        """
        from ._generated.api.x_twitter_stocks import search_x_stocks
        return search_x_stocks.sync(client=self._client, q=query, days=days, limit=limit)

    async def search_async(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Async variant of :meth:`search`."""
        from ._generated.api.x_twitter_stocks import search_x_stocks
        return await search_x_stocks.asyncio(client=self._client, q=query, days=days, limit=limit)

    def compare(self, tickers: list[str], *, days: int = 7) -> Any:
        """Compare multiple stocks side-by-side on X/Twitter.

        Args:
            tickers: List of ticker symbols (max 10).
            days: Time period (1-90).
        """
        from ._generated.api.x_twitter_stocks import compare_x_stocks
        return compare_x_stocks.sync(client=self._client, tickers=",".join(tickers), days=days)

    async def compare_async(self, tickers: list[str], *, days: int = 7) -> Any:
        """Async variant of :meth:`compare`."""
        from ._generated.api.x_twitter_stocks import compare_x_stocks
        return await compare_x_stocks.asyncio(client=self._client, tickers=",".join(tickers), days=days)

    def stats(self) -> Any:
        """Get X/Twitter dataset statistics."""
        from ._generated.api.x_twitter_stocks import get_x_stats
        return get_x_stats.sync(client=self._client)

    async def stats_async(self) -> Any:
        """Async variant of :meth:`stats`."""
        from ._generated.api.x_twitter_stocks import get_x_stats
        return await get_x_stats.asyncio(client=self._client)

    def health(self) -> Any:
        """Get public X/Twitter service health."""
        from ._generated.api.status import get_x_health
        return get_x_health.sync(client=self._client)

    async def health_async(self) -> Any:
        """Async variant of :meth:`health`."""
        from ._generated.api.status import get_x_health
        return await get_x_health.asyncio(client=self._client)


class _PolymarketNamespace:
    """Access Polymarket sentiment endpoints via ``client.polymarket.*``."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def trending(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
    ) -> Any:
        """Get trending stocks on Polymarket.

        Args:
            days: Time period (1-90). Free tier limited to 30.
            limit: Max results (1-100).
            offset: Pagination offset.
            type: Filter by ``"stock"``, ``"etf"``, ``"all"``, or ``None``.
        """
        from ._generated.api.polymarket_stocks import get_polymarket_trending_stocks

        return get_polymarket_trending_stocks.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            type_=_resolve_polymarket_type(type),
        )

    async def trending_async(
        self,
        *,
        days: int = 1,
        limit: int = 20,
        offset: int = 0,
        type: Optional[str] = None,
    ) -> Any:
        """Async variant of :meth:`trending`."""
        from ._generated.api.polymarket_stocks import get_polymarket_trending_stocks

        return await get_polymarket_trending_stocks.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
            type_=_resolve_polymarket_type(type),
        )

    def trending_sectors(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending sectors on Polymarket."""
        from ._generated.api.polymarket_stocks import get_polymarket_trending_sectors

        return get_polymarket_trending_sectors.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
        )

    async def trending_sectors_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending_sectors`."""
        from ._generated.api.polymarket_stocks import get_polymarket_trending_sectors

        return await get_polymarket_trending_sectors.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
        )

    def trending_countries(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending countries on Polymarket."""
        from ._generated.api.polymarket_stocks import get_polymarket_trending_countries

        return get_polymarket_trending_countries.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
        )

    async def trending_countries_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending_countries`."""
        from ._generated.api.polymarket_stocks import get_polymarket_trending_countries

        return await get_polymarket_trending_countries.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
        )

    def stock(self, ticker: str, *, days: int = 7) -> Any:
        """Get Polymarket sentiment for a specific stock ticker.

        Args:
            ticker: Stock symbol (e.g. ``"TSLA"``).
            days: Time period (1-90). Free tier limited to 30.
        """
        from ._generated.api.polymarket_stocks import get_polymarket_stock

        return get_polymarket_stock.sync(ticker, client=self._client, days=days)

    async def stock_async(self, ticker: str, *, days: int = 7) -> Any:
        """Async variant of :meth:`stock`."""
        from ._generated.api.polymarket_stocks import get_polymarket_stock

        return await get_polymarket_stock.asyncio(ticker, client=self._client, days=days)

    def search(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Search for stocks by name or ticker on Polymarket.

        Args:
            query: Search term (e.g. ``"Tesla"`` or ``"TSLA"``).
        """
        from ._generated.api.polymarket_stocks import search_polymarket_stocks

        return search_polymarket_stocks.sync(client=self._client, q=query, days=days, limit=limit)

    async def search_async(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Async variant of :meth:`search`."""
        from ._generated.api.polymarket_stocks import search_polymarket_stocks

        return await search_polymarket_stocks.asyncio(client=self._client, q=query, days=days, limit=limit)

    def compare(self, tickers: list[str], *, days: int = 7) -> Any:
        """Compare multiple stocks side-by-side on Polymarket.

        Args:
            tickers: List of ticker symbols (max 10).
            days: Time period (1-90).
        """
        from ._generated.api.polymarket_stocks import compare_polymarket_stocks

        return compare_polymarket_stocks.sync(client=self._client, tickers=",".join(tickers), days=days)

    async def compare_async(self, tickers: list[str], *, days: int = 7) -> Any:
        """Async variant of :meth:`compare`."""
        from ._generated.api.polymarket_stocks import compare_polymarket_stocks

        return await compare_polymarket_stocks.asyncio(
            client=self._client,
            tickers=",".join(tickers),
            days=days,
        )

    def stats(self) -> Any:
        """Get Polymarket dataset statistics."""
        from ._generated.api.polymarket_stocks import get_polymarket_stats
        return get_polymarket_stats.sync(client=self._client)

    async def stats_async(self) -> Any:
        """Async variant of :meth:`stats`."""
        from ._generated.api.polymarket_stocks import get_polymarket_stats
        return await get_polymarket_stats.asyncio(client=self._client)

    def health(self) -> Any:
        """Get public Polymarket service health."""
        from ._generated.api.status import get_polymarket_health
        return get_polymarket_health.sync(client=self._client)

    async def health_async(self) -> Any:
        """Async variant of :meth:`health`."""
        from ._generated.api.status import get_polymarket_health
        return await get_polymarket_health.asyncio(client=self._client)


class _RedditCryptoNamespace:
    """Access Reddit crypto endpoints via ``client.crypto.*``."""

    def __init__(self, client: AuthenticatedClient) -> None:
        self._client = client

    def trending(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Get trending crypto tokens on Reddit."""
        from ._generated.api.reddit_crypto import get_reddit_crypto_trending
        return get_reddit_crypto_trending.sync(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
        )

    async def trending_async(self, *, days: int = 1, limit: int = 20, offset: int = 0) -> Any:
        """Async variant of :meth:`trending`."""
        from ._generated.api.reddit_crypto import get_reddit_crypto_trending
        return await get_reddit_crypto_trending.asyncio(
            client=self._client,
            days=days,
            limit=limit,
            offset=offset,
        )

    def token(self, symbol: str, *, days: int = 7) -> Any:
        """Get Reddit sentiment for a specific crypto token."""
        from ._generated.api.reddit_crypto import get_reddit_crypto_token
        return get_reddit_crypto_token.sync(
            symbol=symbol,
            client=self._client,
            days=days,
        )

    async def token_async(self, symbol: str, *, days: int = 7) -> Any:
        """Async variant of :meth:`token`."""
        from ._generated.api.reddit_crypto import get_reddit_crypto_token
        return await get_reddit_crypto_token.asyncio(
            symbol=symbol,
            client=self._client,
            days=days,
        )

    def search(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Search crypto symbols by symbol/name/alias."""
        from ._generated.api.reddit_crypto import search_reddit_crypto
        return search_reddit_crypto.sync(client=self._client, q=query, days=days, limit=limit)

    async def search_async(self, query: str, *, days: int = 7, limit: int = 20) -> Any:
        """Async variant of :meth:`search`."""
        from ._generated.api.reddit_crypto import search_reddit_crypto
        return await search_reddit_crypto.asyncio(client=self._client, q=query, days=days, limit=limit)

    def compare(self, symbols: list[str], *, days: int = 7) -> Any:
        """Compare up to 10 crypto tokens side-by-side."""
        from ._generated.api.reddit_crypto import compare_reddit_crypto_tokens
        symbols_csv = ",".join(symbols)
        try:
            return compare_reddit_crypto_tokens.sync(
                client=self._client,
                symbols=symbols_csv,
                days=days,
            )
        except KeyError as exc:
            # Compare schema has changed over time (e.g. `found` vs `mentions`/`upvotes`).
            # Fall back to raw JSON when generated parsing fails on known drift keys.
            if str(exc).strip("'") not in {"found", "mentions", "upvotes"}:
                raise
            response = self._client.get_httpx_client().request(
                "get",
                "/reddit/crypto/v1/compare",
                params={"symbols": symbols_csv, "days": days},
            )
            response.raise_for_status()
            return response.json()

    async def compare_async(self, symbols: list[str], *, days: int = 7) -> Any:
        """Async variant of :meth:`compare`."""
        from ._generated.api.reddit_crypto import compare_reddit_crypto_tokens
        symbols_csv = ",".join(symbols)
        try:
            return await compare_reddit_crypto_tokens.asyncio(
                client=self._client,
                symbols=symbols_csv,
                days=days,
            )
        except KeyError as exc:
            if str(exc).strip("'") not in {"found", "mentions", "upvotes"}:
                raise
            response = await self._client.get_async_httpx_client().request(
                "get",
                "/reddit/crypto/v1/compare",
                params={"symbols": symbols_csv, "days": days},
            )
            response.raise_for_status()
            return response.json()

    def stats(self) -> Any:
        """Get Reddit crypto dataset statistics."""
        from ._generated.api.reddit_crypto import get_reddit_crypto_stats
        return get_reddit_crypto_stats.sync(client=self._client)

    async def stats_async(self) -> Any:
        """Async variant of :meth:`stats`."""
        from ._generated.api.reddit_crypto import get_reddit_crypto_stats
        return await get_reddit_crypto_stats.asyncio(client=self._client)

    def health(self) -> Any:
        """Get public Reddit crypto service health."""
        from ._generated.api.status import get_reddit_crypto_health
        return get_reddit_crypto_health.sync(client=self._client)

    async def health_async(self) -> Any:
        """Async variant of :meth:`health`."""
        from ._generated.api.status import get_reddit_crypto_health
        return await get_reddit_crypto_health.asyncio(client=self._client)


class AdanosClient:
    """Client for the Finance Sentiment API.

    Args:
        api_key: Your API key (``sk_live_...``).
        base_url: API base URL. Defaults to ``https://api.adanos.org``.
        timeout: Request timeout in seconds. Defaults to 30.

    Example::

        from adanos import AdanosClient

        client = AdanosClient(api_key="sk_live_...")
        trending = client.reddit.trending(days=7, limit=10)
    """

    def __init__(
        self,
        api_key: str,
        base_url: str = "https://api.adanos.org",
        timeout: float = 30.0,
    ) -> None:
        import httpx

        self._client = AuthenticatedClient(
            base_url=base_url,
            token=api_key,
            prefix="",
            auth_header_name="X-API-Key",
            timeout=httpx.Timeout(timeout),
            raise_on_unexpected_status=True,
        )
        self.news = _NewsNamespace(self._client)
        self.reddit = _RedditNamespace(self._client)
        self.crypto = _RedditCryptoNamespace(self._client)
        self.reddit_crypto = self.crypto
        self.x = _XNamespace(self._client)
        self.polymarket = _PolymarketNamespace(self._client)

    def close(self) -> None:
        """Close underlying HTTP connections."""
        self._client.__exit__(None, None, None)

    async def aclose(self) -> None:
        """Close underlying async HTTP connections."""
        await self._client.__aexit__(None, None, None)

    def __enter__(self) -> "AdanosClient":
        self._client.__enter__()
        return self

    def __exit__(self, *args: Any) -> None:
        self._client.__exit__(*args)

    async def __aenter__(self) -> "AdanosClient":
        await self._client.__aenter__()
        return self

    async def __aexit__(self, *args: Any) -> None:
        await self._client.__aexit__(*args)


# Backwards-compatible alias for earlier SDK naming.
StockSentimentClient = AdanosClient
