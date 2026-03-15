from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_polymarket_trending_stocks_type_type_0 import (
    GetPolymarketTrendingStocksTypeType0,
)
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.polymarket_trending_stock import PolymarketTrendingStock
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    type_: GetPolymarketTrendingStocksTypeType0 | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days"] = days

    params["limit"] = limit

    params["offset"] = offset

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, GetPolymarketTrendingStocksTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/polymarket/stocks/v1/trending",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[PolymarketTrendingStock]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PolymarketTrendingStock.from_dict(
                response_200_item_data
            )

            response_200.append(response_200_item)

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
        response_429 = ErrorResponse.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[PolymarketTrendingStock]
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
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    type_: GetPolymarketTrendingStocksTypeType0 | None | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[PolymarketTrendingStock]
]:
    """Get trending stocks on Polymarket

     Get trending stocks based on Polymarket market activity.

    Args:
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 1.
        limit (int | Unset): Maximum stocks to return Default: 20.
        offset (int | Unset): Number of items to skip Default: 0.
        type_ (GetPolymarketTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or
            use 'all' for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | list[PolymarketTrendingStock]]
    """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        offset=offset,
        type_=type_,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    type_: GetPolymarketTrendingStocksTypeType0 | None | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[PolymarketTrendingStock]
    | None
):
    """Get trending stocks on Polymarket

     Get trending stocks based on Polymarket market activity.

    Args:
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 1.
        limit (int | Unset): Maximum stocks to return Default: 20.
        offset (int | Unset): Number of items to skip Default: 0.
        type_ (GetPolymarketTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or
            use 'all' for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | list[PolymarketTrendingStock]
    """

    return sync_detailed(
        client=client,
        days=days,
        limit=limit,
        offset=offset,
        type_=type_,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    type_: GetPolymarketTrendingStocksTypeType0 | None | Unset = UNSET,
) -> Response[
    ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[PolymarketTrendingStock]
]:
    """Get trending stocks on Polymarket

     Get trending stocks based on Polymarket market activity.

    Args:
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 1.
        limit (int | Unset): Maximum stocks to return Default: 20.
        offset (int | Unset): Number of items to skip Default: 0.
        type_ (GetPolymarketTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or
            use 'all' for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | list[PolymarketTrendingStock]]
    """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        offset=offset,
        type_=type_,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    type_: GetPolymarketTrendingStocksTypeType0 | None | Unset = UNSET,
) -> (
    ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[PolymarketTrendingStock]
    | None
):
    """Get trending stocks on Polymarket

     Get trending stocks based on Polymarket market activity.

    Args:
        days (int | Unset): Time period in days (1-30 free, 1-90 paid) Default: 1.
        limit (int | Unset): Maximum stocks to return Default: 20.
        offset (int | Unset): Number of items to skip Default: 0.
        type_ (GetPolymarketTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or
            use 'all' for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | list[PolymarketTrendingStock]
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            limit=limit,
            offset=offset,
            type_=type_,
        )
    ).parsed
