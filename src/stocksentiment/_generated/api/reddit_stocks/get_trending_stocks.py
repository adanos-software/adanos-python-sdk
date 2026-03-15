from http import HTTPStatus
from typing import Any, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.get_trending_stocks_type_type_0 import GetTrendingStocksTypeType0
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.trending_stock import TrendingStock
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = 1,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
    type_: GetTrendingStocksTypeType0 | None | Unset = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days"] = days

    params["limit"] = limit

    params["offset"] = offset

    json_type_: None | str | Unset
    if isinstance(type_, Unset):
        json_type_ = UNSET
    elif isinstance(type_, GetTrendingStocksTypeType0):
        json_type_ = type_.value
    else:
        json_type_ = type_
    params["type"] = json_type_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/reddit/stocks/v1/trending",
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
    | list[TrendingStock]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TrendingStock.from_dict(response_200_item_data)

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
    | list[TrendingStock]
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
    type_: GetTrendingStocksTypeType0 | None | Unset = UNSET,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingStock]
]:
    """Get trending stocks

     Returns stocks with highest buzz on Reddit, ranked by buzz score.

    **Buzz score** combines:
    - Mention volume
    - Sentiment score
    - Engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Trend calculation** uses a multi-factor weighted activity score:
    - **60% Mentions**: Primary activity indicator
    - **25% Upvotes**: Engagement quality signal
    - **15% Subreddit spread**: Discussion breadth indicator

    Activity score > 1.10 = rising, < 0.90 = falling, else stable.

    **History**: Each stock includes `trend_history` - daily buzz scores (oldest→newest).
    Length matches `days` parameter (minimum 7). Missing days are filled with 0.0.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). The trend field
            uses rolling 24h windows: compares last 24h vs previous 24h. Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.
        type_ (GetTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or use 'all'
            for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingStock]]
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
    type_: GetTrendingStocksTypeType0 | None | Unset = UNSET,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingStock]
    | None
):
    """Get trending stocks

     Returns stocks with highest buzz on Reddit, ranked by buzz score.

    **Buzz score** combines:
    - Mention volume
    - Sentiment score
    - Engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Trend calculation** uses a multi-factor weighted activity score:
    - **60% Mentions**: Primary activity indicator
    - **25% Upvotes**: Engagement quality signal
    - **15% Subreddit spread**: Discussion breadth indicator

    Activity score > 1.10 = rising, < 0.90 = falling, else stable.

    **History**: Each stock includes `trend_history` - daily buzz scores (oldest→newest).
    Length matches `days` parameter (minimum 7). Missing days are filled with 0.0.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). The trend field
            uses rolling 24h windows: compares last 24h vs previous 24h. Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.
        type_ (GetTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or use 'all'
            for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingStock]
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
    type_: GetTrendingStocksTypeType0 | None | Unset = UNSET,
) -> Response[
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingStock]
]:
    """Get trending stocks

     Returns stocks with highest buzz on Reddit, ranked by buzz score.

    **Buzz score** combines:
    - Mention volume
    - Sentiment score
    - Engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Trend calculation** uses a multi-factor weighted activity score:
    - **60% Mentions**: Primary activity indicator
    - **25% Upvotes**: Engagement quality signal
    - **15% Subreddit spread**: Discussion breadth indicator

    Activity score > 1.10 = rising, < 0.90 = falling, else stable.

    **History**: Each stock includes `trend_history` - daily buzz scores (oldest→newest).
    Length matches `days` parameter (minimum 7). Missing days are filled with 0.0.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). The trend field
            uses rolling 24h windows: compares last 24h vs previous 24h. Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.
        type_ (GetTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or use 'all'
            for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingStock]]
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
    type_: GetTrendingStocksTypeType0 | None | Unset = UNSET,
) -> (
    Any
    | ErrorResponse
    | HTTPValidationError
    | HistoricalLimitError
    | list[TrendingStock]
    | None
):
    """Get trending stocks

     Returns stocks with highest buzz on Reddit, ranked by buzz score.

    **Buzz score** combines:
    - Mention volume
    - Sentiment score
    - Engagement (upvotes)
    - Trend direction (rising/falling/stable)

    **Trend calculation** uses a multi-factor weighted activity score:
    - **60% Mentions**: Primary activity indicator
    - **25% Upvotes**: Engagement quality signal
    - **15% Subreddit spread**: Discussion breadth indicator

    Activity score > 1.10 = rising, < 0.90 = falling, else stable.

    **History**: Each stock includes `trend_history` - daily buzz scores (oldest→newest).
    Length matches `days` parameter (minimum 7). Missing days are filled with 0.0.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). The trend field
            uses rolling 24h windows: compares last 24h vs previous 24h. Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.
        type_ (GetTrendingStocksTypeType0 | None | Unset): Filter by asset type. Omit or use 'all'
            for all assets.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Any | ErrorResponse | HTTPValidationError | HistoricalLimitError | list[TrendingStock]
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
