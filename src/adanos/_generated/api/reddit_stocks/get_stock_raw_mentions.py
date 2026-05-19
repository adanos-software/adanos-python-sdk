from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.rate_limit_error import RateLimitError
from ...models.reddit_raw_mentions_response import RedditRawMentionsResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    ticker: str,
    *,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["days"] = days

    params["limit"] = limit

    params["offset"] = offset

    params["include_inherited"] = include_inherited

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reddit/stocks/v1/stock/{ticker}/mentions".format(
            ticker=quote(str(ticker), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse | None:
    if response.status_code == 200:
        response_200 = RedditRawMentionsResponse.from_dict(response.json())

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
) -> Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse]:
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse]:
    """Raw Mentions

     Returns raw mention rows for a specific stock ticker within the live raw-data retention window.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    **Use this endpoint when you need:**
    - post/comment-level snippets
    - original timestamps
    - inherited-context filtering

    **Notes:**
    - `days` uses a rolling lookback from request time, not UTC calendar-day windows
    - Analytics endpoints such as `/stock/{ticker}` and `/trending` use UTC calendar-day semantics
    instead
    - Results are ordered newest first and support deterministic `offset` + `limit` pagination
    - `include_inherited=false` by default
    - empty result sets return `200` with `results=[]`

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, aapl, BRK.A, $GME)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mention rows to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include thread-context inherited mentions in addition to
            direct ticker mentions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        days=days,
        limit=limit,
        offset=offset,
        include_inherited=include_inherited,
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
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse | None:
    """Raw Mentions

     Returns raw mention rows for a specific stock ticker within the live raw-data retention window.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    **Use this endpoint when you need:**
    - post/comment-level snippets
    - original timestamps
    - inherited-context filtering

    **Notes:**
    - `days` uses a rolling lookback from request time, not UTC calendar-day windows
    - Analytics endpoints such as `/stock/{ticker}` and `/trending` use UTC calendar-day semantics
    instead
    - Results are ordered newest first and support deterministic `offset` + `limit` pagination
    - `include_inherited=false` by default
    - empty result sets return `200` with `results=[]`

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, aapl, BRK.A, $GME)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mention rows to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include thread-context inherited mentions in addition to
            direct ticker mentions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse
    """

    return sync_detailed(
        ticker=ticker,
        client=client,
        days=days,
        limit=limit,
        offset=offset,
        include_inherited=include_inherited,
    ).parsed


async def asyncio_detailed(
    ticker: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse]:
    """Raw Mentions

     Returns raw mention rows for a specific stock ticker within the live raw-data retention window.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    **Use this endpoint when you need:**
    - post/comment-level snippets
    - original timestamps
    - inherited-context filtering

    **Notes:**
    - `days` uses a rolling lookback from request time, not UTC calendar-day windows
    - Analytics endpoints such as `/stock/{ticker}` and `/trending` use UTC calendar-day semantics
    instead
    - Results are ordered newest first and support deterministic `offset` + `limit` pagination
    - `include_inherited=false` by default
    - empty result sets return `200` with `results=[]`

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, aapl, BRK.A, $GME)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mention rows to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include thread-context inherited mentions in addition to
            direct ticker mentions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse]
    """

    kwargs = _get_kwargs(
        ticker=ticker,
        days=days,
        limit=limit,
        offset=offset,
        include_inherited=include_inherited,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    ticker: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse | None:
    """Raw Mentions

     Returns raw mention rows for a specific stock ticker within the live raw-data retention window.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    **Use this endpoint when you need:**
    - post/comment-level snippets
    - original timestamps
    - inherited-context filtering

    **Notes:**
    - `days` uses a rolling lookback from request time, not UTC calendar-day windows
    - Analytics endpoints such as `/stock/{ticker}` and `/trending` use UTC calendar-day semantics
    instead
    - Results are ordered newest first and support deterministic `offset` + `limit` pagination
    - `include_inherited=false` by default
    - empty result sets return `200` with `results=[]`

    Args:
        ticker (str): Stock ticker symbol (e.g., TSLA, aapl, BRK.A, $GME)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mention rows to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include thread-context inherited mentions in addition to
            direct ticker mentions Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | RedditRawMentionsResponse
    """

    return (
        await asyncio_detailed(
            ticker=ticker,
            client=client,
            days=days,
            limit=limit,
            offset=offset,
            include_inherited=include_inherited,
        )
    ).parsed
