from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.trending_country import TrendingCountry
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days"] = days

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reddit/stocks/v1/trending/countries",
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
    | list[TrendingCountry]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TrendingCountry.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
    | list[TrendingCountry]
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
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingCountry]
]:
    """Get trending countries

     Returns countries with highest aggregated buzz on Reddit, ranked by buzz score.

    **Aggregation**: Combines all stock mentions per country from ticker_reference.

    **Buzz score** combines:
    - Total mention volume across all tickers from country
    - Weighted average sentiment
    - Total engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per country by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingCountry]]
    """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        offset=offset,
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
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingCountry]
    | None
):
    """Get trending countries

     Returns countries with highest aggregated buzz on Reddit, ranked by buzz score.

    **Aggregation**: Combines all stock mentions per country from ticker_reference.

    **Buzz score** combines:
    - Total mention volume across all tickers from country
    - Weighted average sentiment
    - Total engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per country by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingCountry]
    """

    return sync_detailed(
        client=client,
        days=days,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingCountry]
]:
    """Get trending countries

     Returns countries with highest aggregated buzz on Reddit, ranked by buzz score.

    **Aggregation**: Combines all stock mentions per country from ticker_reference.

    **Buzz score** combines:
    - Total mention volume across all tickers from country
    - Weighted average sentiment
    - Total engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per country by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingCountry]]
    """

    kwargs = _get_kwargs(
        days=days,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingCountry]
    | None
):
    """Get trending countries

     Returns countries with highest aggregated buzz on Reddit, ranked by buzz score.

    **Aggregation**: Combines all stock mentions per country from ticker_reference.

    **Buzz score** combines:
    - Total mention volume across all tickers from country
    - Weighted average sentiment
    - Total engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per country by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingCountry]
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
            limit=limit,
            offset=offset,
        )
    ).parsed
