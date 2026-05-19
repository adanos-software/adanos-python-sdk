from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.rate_limit_error import RateLimitError
from ...models.x_market_sentiment_response import XMarketSentimentResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 1,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/x/stocks/v1/market-sentiment",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse | None:
    if response.status_code == 200:
        response_200 = XMarketSentimentResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HistoricalLimitError.from_dict(response.json())

        return response_403

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = RateLimitError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
) -> Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse]:
    """Market Sentiment

     Returns the service-level X/Twitter market sentiment snapshot across all tracked stocks.

    Use this endpoint when you want a single X-wide market state instead of per-ticker rankings.
    It includes service-wide buzz, sentiment split, activity trend, breadth metrics, and the top drivers
    by current `buzz_score`.

    `buzz_score` here means relative X/Twitter market heat, not pure bullishness.
    It measures how hot overall X stock discussion is versus X's own trailing 90-day baseline:
    - around `50` = normal X market activity
    - higher = hotter / more active than usual
    - lower = quieter than usual

    `trend` is service-level activity momentum over current 3 UTC days vs previous
    3 UTC days using mentions, likes, and author breadth. It is not price trend.

    Use `sentiment_score`, `bullish_pct`, and `bearish_pct` for direction.

    Args:
        days (int | Unset): UTC calendar days including the current UTC day so far (1-30 free,
            1-90 hobby, 1-365 professional) Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse | None:
    """Market Sentiment

     Returns the service-level X/Twitter market sentiment snapshot across all tracked stocks.

    Use this endpoint when you want a single X-wide market state instead of per-ticker rankings.
    It includes service-wide buzz, sentiment split, activity trend, breadth metrics, and the top drivers
    by current `buzz_score`.

    `buzz_score` here means relative X/Twitter market heat, not pure bullishness.
    It measures how hot overall X stock discussion is versus X's own trailing 90-day baseline:
    - around `50` = normal X market activity
    - higher = hotter / more active than usual
    - lower = quieter than usual

    `trend` is service-level activity momentum over current 3 UTC days vs previous
    3 UTC days using mentions, likes, and author breadth. It is not price trend.

    Use `sentiment_score`, `bullish_pct`, and `bearish_pct` for direction.

    Args:
        days (int | Unset): UTC calendar days including the current UTC day so far (1-30 free,
            1-90 hobby, 1-365 professional) Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse
    """

    return sync_detailed(
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
) -> Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse]:
    """Market Sentiment

     Returns the service-level X/Twitter market sentiment snapshot across all tracked stocks.

    Use this endpoint when you want a single X-wide market state instead of per-ticker rankings.
    It includes service-wide buzz, sentiment split, activity trend, breadth metrics, and the top drivers
    by current `buzz_score`.

    `buzz_score` here means relative X/Twitter market heat, not pure bullishness.
    It measures how hot overall X stock discussion is versus X's own trailing 90-day baseline:
    - around `50` = normal X market activity
    - higher = hotter / more active than usual
    - lower = quieter than usual

    `trend` is service-level activity momentum over current 3 UTC days vs previous
    3 UTC days using mentions, likes, and author breadth. It is not price trend.

    Use `sentiment_score`, `bullish_pct`, and `bearish_pct` for direction.

    Args:
        days (int | Unset): UTC calendar days including the current UTC day so far (1-30 free,
            1-90 hobby, 1-365 professional) Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse]
    """

    kwargs = _get_kwargs(
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse | None:
    """Market Sentiment

     Returns the service-level X/Twitter market sentiment snapshot across all tracked stocks.

    Use this endpoint when you want a single X-wide market state instead of per-ticker rankings.
    It includes service-wide buzz, sentiment split, activity trend, breadth metrics, and the top drivers
    by current `buzz_score`.

    `buzz_score` here means relative X/Twitter market heat, not pure bullishness.
    It measures how hot overall X stock discussion is versus X's own trailing 90-day baseline:
    - around `50` = normal X market activity
    - higher = hotter / more active than usual
    - lower = quieter than usual

    `trend` is service-level activity momentum over current 3 UTC days vs previous
    3 UTC days using mentions, likes, and author breadth. It is not price trend.

    Use `sentiment_score`, `bullish_pct`, and `bearish_pct` for direction.

    Args:
        days (int | Unset): UTC calendar days including the current UTC day so far (1-30 free,
            1-90 hobby, 1-365 professional) Default: 1.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | XMarketSentimentResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
        )
    ).parsed
