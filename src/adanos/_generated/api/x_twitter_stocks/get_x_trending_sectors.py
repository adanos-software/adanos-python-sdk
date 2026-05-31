from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.invalid_period_error import InvalidPeriodError
from ...models.x_trending_sector import XTrendingSector
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["days"] = days

    params["from"] = from_

    params["to"] = to

    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/x/stocks/v1/trending/sectors",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> (
    ErrorResponse
    | HTTPValidationError
    | InvalidPeriodError
    | HistoricalLimitError
    | list[XTrendingSector]
    | None
):
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = XTrendingSector.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 401:
        response_401 = ErrorResponse.from_dict(response.json())

        return response_401

    if response.status_code == 403:
        response_403 = HistoricalLimitError.from_dict(response.json())

        return response_403

    if response.status_code == 422:

        def _parse_response_422(data: object) -> HTTPValidationError | InvalidPeriodError:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                detail = data.get("detail")
                error = str(detail.get("error", "")).lower().replace(" ", "_") if isinstance(detail, dict) else ""
                if error != "invalid_period":
                    raise TypeError()
                response_422_type_0 = InvalidPeriodError.from_dict(data)

                return response_422_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            if not isinstance(data, dict):
                raise TypeError()
            response_422_type_1 = HTTPValidationError.from_dict(data)

            return response_422_type_1

        response_422 = _parse_response_422(response.json())

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
    ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]
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
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[
    ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]
]:
    """Get trending sectors on X/Twitter

     Returns sectors with highest aggregated buzz on X/Twitter, ranked by buzz score.

    **Aggregation**: Combines all tweet mentions per sector from ticker_reference.

    **Buzz score** (V5.4) combines:
    - Total mention volume across all tickers in sector
    - Weighted average sentiment
    - Total engagement (likes)
    - Author diversity
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per sector by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        from_ (str | Unset): Inclusive UTC start date (`YYYY-MM-DD`).
        to (str | Unset): Inclusive UTC end date (`YYYY-MM-DD`).
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]]
    """

    kwargs = _get_kwargs(
        days=days,
        from_=from_,
        to=to,
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
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> (
    ErrorResponse
    | HTTPValidationError
    | InvalidPeriodError
    | HistoricalLimitError
    | list[XTrendingSector]
    | None
):
    """Get trending sectors on X/Twitter

     Returns sectors with highest aggregated buzz on X/Twitter, ranked by buzz score.

    **Aggregation**: Combines all tweet mentions per sector from ticker_reference.

    **Buzz score** (V5.4) combines:
    - Total mention volume across all tickers in sector
    - Weighted average sentiment
    - Total engagement (likes)
    - Author diversity
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per sector by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        from_ (str | Unset): Inclusive UTC start date (`YYYY-MM-DD`).
        to (str | Unset): Inclusive UTC end date (`YYYY-MM-DD`).
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]
    """

    return sync_detailed(
        client=client,
        days=days,
        from_=from_,
        to=to,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> Response[
    ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]
]:
    """Get trending sectors on X/Twitter

     Returns sectors with highest aggregated buzz on X/Twitter, ranked by buzz score.

    **Aggregation**: Combines all tweet mentions per sector from ticker_reference.

    **Buzz score** (V5.4) combines:
    - Total mention volume across all tickers in sector
    - Weighted average sentiment
    - Total engagement (likes)
    - Author diversity
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per sector by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        from_ (str | Unset): Inclusive UTC start date (`YYYY-MM-DD`).
        to (str | Unset): Inclusive UTC end date (`YYYY-MM-DD`).
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]]
    """

    kwargs = _get_kwargs(
        days=days,
        from_=from_,
        to=to,
        limit=limit,
        offset=offset,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    days: int | Unset = UNSET,
    from_: str | Unset = UNSET,
    to: str | Unset = UNSET,
    limit: int | Unset = 20,
    offset: int | Unset = 0,
) -> (
    ErrorResponse
    | HTTPValidationError
    | InvalidPeriodError
    | HistoricalLimitError
    | list[XTrendingSector]
    | None
):
    """Get trending sectors on X/Twitter

     Returns sectors with highest aggregated buzz on X/Twitter, ranked by buzz score.

    **Aggregation**: Combines all tweet mentions per sector from ticker_reference.

    **Buzz score** (V5.4) combines:
    - Total mention volume across all tickers in sector
    - Weighted average sentiment
    - Total engagement (likes)
    - Author diversity
    - Trend direction (rising/falling/stable)

    **Includes top 5 tickers** per sector by mention count.

    **Pagination**: Use `offset` and `limit` to paginate through results.

    Args:
        from_ (str | Unset): Inclusive UTC start date (`YYYY-MM-DD`).
        to (str | Unset): Inclusive UTC end date (`YYYY-MM-DD`).
        days (int | Unset): Time period in days to analyze (1-30 free, 1-90 paid). Default: 1.
        limit (int | Unset): Maximum number of results Default: 20.
        offset (int | Unset): Number of items to skip for pagination Default: 0.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | list[XTrendingSector]
    """

    return (
        await asyncio_detailed(
            client=client,
            days=days,
        from_=from_,
        to=to,
            limit=limit,
            offset=offset,
        )
    ).parsed
