from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.polymarket_compare_response import PolymarketCompareResponse
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    tickers: str,
    days: int | Unset = 7,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["tickers"] = tickers

    params["days"] = days

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/polymarket/stocks/v1/compare",
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
    | PolymarketCompareResponse
    | None
):
    if response.status_code == 200:
        response_200 = PolymarketCompareResponse.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400

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
    | PolymarketCompareResponse
]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    tickers: str,
    days: int | Unset = 7,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | PolymarketCompareResponse
]:
    """Compare multiple stocks on Polymarket

     Compare up to 10 stocks side-by-side.

    Args:
        tickers (str): Comma-separated ticker list (max 10)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | PolymarketCompareResponse]
    """

    kwargs = _get_kwargs(
        tickers=tickers,
        days=days,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    tickers: str,
    days: int | Unset = 7,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | PolymarketCompareResponse
    | None
):
    """Compare multiple stocks on Polymarket

     Compare up to 10 stocks side-by-side.

    Args:
        tickers (str): Comma-separated ticker list (max 10)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | PolymarketCompareResponse
    """

    return sync_detailed(
        client=client,
        tickers=tickers,
        days=days,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    tickers: str,
    days: int | Unset = 7,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | PolymarketCompareResponse
]:
    """Compare multiple stocks on Polymarket

     Compare up to 10 stocks side-by-side.

    Args:
        tickers (str): Comma-separated ticker list (max 10)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | PolymarketCompareResponse]
    """

    kwargs = _get_kwargs(
        tickers=tickers,
        days=days,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    tickers: str,
    days: int | Unset = 7,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | PolymarketCompareResponse
    | None
):
    """Compare multiple stocks on Polymarket

     Compare up to 10 stocks side-by-side.

    Args:
        tickers (str): Comma-separated ticker list (max 10)
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 7.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | PolymarketCompareResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            tickers=tickers,
            days=days,
        )
    ).parsed
