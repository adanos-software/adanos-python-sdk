from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crypto_raw_mentions_response import CryptoRawMentionsResponse
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.rate_limit_error import RateLimitError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
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
        "url": "/reddit/crypto/v1/token/{symbol}/mentions".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | None:
    if response.status_code == 200:
        response_200 = CryptoRawMentionsResponse.from_dict(response.json())

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
) -> Response[CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> Response[CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError]:
    """Raw Mentions

     Return stored raw Reddit mention rows for one crypto symbol.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    Results are ordered by newest first and support deterministic `offset` + `limit` pagination.
    Inherited thread-context mentions are excluded by default and can be enabled
    with `include_inherited=true`.
    `days` uses a rolling lookback from request time, not UTC calendar-day windows.
    Analytics endpoints such as `/token/{symbol}`, `/compare`, and `/trending` use UTC calendar-day
    semantics instead.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mentions to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include inherited thread-context mentions in addition to
            direct symbol matches Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
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
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | None:
    """Raw Mentions

     Return stored raw Reddit mention rows for one crypto symbol.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    Results are ordered by newest first and support deterministic `offset` + `limit` pagination.
    Inherited thread-context mentions are excluded by default and can be enabled
    with `include_inherited=true`.
    `days` uses a rolling lookback from request time, not UTC calendar-day windows.
    Analytics endpoints such as `/token/{symbol}`, `/compare`, and `/trending` use UTC calendar-day
    semantics instead.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mentions to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include inherited thread-context mentions in addition to
            direct symbol matches Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        days=days,
        limit=limit,
        offset=offset,
        include_inherited=include_inherited,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> Response[CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError]:
    """Raw Mentions

     Return stored raw Reddit mention rows for one crypto symbol.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    Results are ordered by newest first and support deterministic `offset` + `limit` pagination.
    Inherited thread-context mentions are excluded by default and can be enabled
    with `include_inherited=true`.
    `days` uses a rolling lookback from request time, not UTC calendar-day windows.
    Analytics endpoints such as `/token/{symbol}`, `/compare`, and `/trending` use UTC calendar-day
    semantics instead.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mentions to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include inherited thread-context mentions in addition to
            direct symbol matches Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        days=days,
        limit=limit,
        offset=offset,
        include_inherited=include_inherited,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
    limit: int | Unset = 50,
    offset: int | Unset = 0,
    include_inherited: bool | Unset = False,
) -> CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError | None:
    """Raw Mentions

     Return stored raw Reddit mention rows for one crypto symbol.
    **Professional account required.** Free and Hobby accounts cannot use this endpoint.

    Results are ordered by newest first and support deterministic `offset` + `limit` pagination.
    Inherited thread-context mentions are excluded by default and can be enabled
    with `include_inherited=true`.
    `days` uses a rolling lookback from request time, not UTC calendar-day windows.
    Analytics endpoints such as `/token/{symbol}`, `/compare`, and `/trending` use UTC calendar-day
    semantics instead.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Raw mention lookback window in days within the live raw-data retention
            window. Uses a rolling lookback from request time, not UTC calendar-day windows.
            Professional-only endpoint; maximum 365 days. Default: 7.
        limit (int | Unset): Maximum number of raw mentions to return Default: 50.
        offset (int | Unset): Number of raw mention rows to skip for pagination Default: 0.
        include_inherited (bool | Unset): Include inherited thread-context mentions in addition to
            direct symbol matches Default: False.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        CryptoRawMentionsResponse | ErrorResponse | HTTPValidationError | HistoricalLimitError | RateLimitError
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            days=days,
            limit=limit,
            offset=offset,
            include_inherited=include_inherited,
        )
    ).parsed
