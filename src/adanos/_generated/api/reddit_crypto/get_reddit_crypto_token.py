from http import HTTPStatus
from typing import Any, cast
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.crypto_token_sentiment import CryptoTokenSentiment
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    symbol: str,
    *,
    days: int | Unset = 7,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reddit/crypto/v1/token/{symbol}".format(
            symbol=quote(str(symbol), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    Any
    | CryptoTokenSentiment
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | None
):
    if response.status_code == 200:
        response_200 = CryptoTokenSentiment.from_dict(response.json())

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
    | CryptoTokenSentiment
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
]:
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
) -> Response[
    Any
    | CryptoTokenSentiment
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
]:
    """Get Reddit sentiment for one crypto token

     Returns detailed sentiment, buzz score, and daily trend data for a single crypto symbol.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CryptoTokenSentiment | ErrorResponse | HTTPValidationError | HistoricalLimitError]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        days=days,
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
) -> (
    Any
    | CryptoTokenSentiment
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | None
):
    """Get Reddit sentiment for one crypto token

     Returns detailed sentiment, buzz score, and daily trend data for a single crypto symbol.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CryptoTokenSentiment | ErrorResponse | HTTPValidationError | HistoricalLimitError
    """

    return sync_detailed(
        symbol=symbol,
        client=client,
        days=days,
    ).parsed


async def asyncio_detailed(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
) -> Response[
    Any
    | CryptoTokenSentiment
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
]:
    """Get Reddit sentiment for one crypto token

     Returns detailed sentiment, buzz score, and daily trend data for a single crypto symbol.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | CryptoTokenSentiment | ErrorResponse | HTTPValidationError | HistoricalLimitError]
    """

    kwargs = _get_kwargs(
        symbol=symbol,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    symbol: str,
    *,
    client: AuthenticatedClient,
    days: int | Unset = 7,
) -> (
    Any
    | CryptoTokenSentiment
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | None
):
    """Get Reddit sentiment for one crypto token

     Returns detailed sentiment, buzz score, and daily trend data for a single crypto symbol.

    Args:
        symbol (str): Crypto symbol (e.g., BTC, $ETH, SOL)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | CryptoTokenSentiment | ErrorResponse | HTTPValidationError | HistoricalLimitError
    """

    return (
        await asyncio_detailed(
            symbol=symbol,
            client=client,
            days=days,
        )
    ).parsed
