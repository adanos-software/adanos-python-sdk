from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.x_stock_detail_response import XStockDetailResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticker: str,
    *,
    days: int | Unset = 7,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/x/stocks/v1/stock/{ticker}".format(
            ticker=quote(str(ticker), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | XStockDetailResponse
    | None
):
    if response.status_code == 200:
        response_200 = XStockDetailResponse.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HistoricalLimitError.from_dict(response.json())

        return response_403

    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404

    if response.status_code == 422:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422

    if response.status_code == 429:
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | XStockDetailResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    ticker: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | XStockDetailResponse
]:
    """Get X/Twitter data for a specific stock

     Returns detailed X/Twitter data for a specific ticker.

    **Response includes:**
    - `buzz_score`: V5.4 score from tweet data (mentions, sentiment, likes, diversity)
    - `mentions`: Canonical number of tweet mentions within period (`total_mentions` remains as a legacy alias)
    - `sentiment_score`: Average sentiment from tweet analysis (-1 to +1)
    - `positive_count`, `negative_count`, `neutral_count`: Sentiment breakdown
    - `total_upvotes`: Total likes across tweet mentions
    - `daily_trend`: Daily data with mentions, canonical `sentiment_score`, legacy `sentiment`, and avg_rank
    - `is_validated`: Also trending on Reddit (cross-platform validation)

    Returns 404 when ticker data is not available in the requested window.

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, $AAPL)
        days (int | Unset): Days of history to analyze (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | XStockDetailResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    ticker: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | XStockDetailResponse
    | None
):
    """Get X/Twitter data for a specific stock

     Returns detailed X/Twitter data for a specific ticker.

    **Response includes:**
    - `buzz_score`: V5.4 score from tweet data (mentions, sentiment, likes, diversity)
    - `mentions`: Canonical number of tweet mentions within period (`total_mentions` remains as a legacy alias)
    - `sentiment_score`: Average sentiment from tweet analysis (-1 to +1)
    - `positive_count`, `negative_count`, `neutral_count`: Sentiment breakdown
    - `total_upvotes`: Total likes across tweet mentions
    - `daily_trend`: Daily data with mentions, canonical `sentiment_score`, legacy `sentiment`, and avg_rank
    - `is_validated`: Also trending on Reddit (cross-platform validation)

    Returns 404 when ticker data is not available in the requested window.

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, $AAPL)
        days (int | Unset): Days of history to analyze (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | XStockDetailResponse
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | XStockDetailResponse
]:
    """Get X/Twitter data for a specific stock

     Returns detailed X/Twitter data for a specific ticker.

    **Response includes:**
    - `buzz_score`: V5.4 score from tweet data (mentions, sentiment, likes, diversity)
    - `mentions`: Canonical number of tweet mentions within period (`total_mentions` remains as a legacy alias)
    - `sentiment_score`: Average sentiment from tweet analysis (-1 to +1)
    - `positive_count`, `negative_count`, `neutral_count`: Sentiment breakdown
    - `total_upvotes`: Total likes across tweet mentions
    - `daily_trend`: Daily data with mentions, canonical `sentiment_score`, legacy `sentiment`, and avg_rank
    - `is_validated`: Also trending on Reddit (cross-platform validation)

    Returns 404 when ticker data is not available in the requested window.

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, $AAPL)
        days (int | Unset): Days of history to analyze (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | XStockDetailResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticker: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | XStockDetailResponse
    | None
):
    """Get X/Twitter data for a specific stock

     Returns detailed X/Twitter data for a specific ticker.

    **Response includes:**
    - `buzz_score`: V5.4 score from tweet data (mentions, sentiment, likes, diversity)
    - `mentions`: Canonical number of tweet mentions within period (`total_mentions` remains as a legacy alias)
    - `sentiment_score`: Average sentiment from tweet analysis (-1 to +1)
    - `positive_count`, `negative_count`, `neutral_count`: Sentiment breakdown
    - `total_upvotes`: Total likes across tweet mentions
    - `daily_trend`: Daily data with mentions, canonical `sentiment_score`, legacy `sentiment`, and avg_rank
    - `is_validated`: Also trending on Reddit (cross-platform validation)

    Returns 404 when ticker data is not available in the requested window.

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, $AAPL)
        days (int | Unset): Days of history to analyze (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | XStockDetailResponse
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
            days=days,
        )
    ).parsed
