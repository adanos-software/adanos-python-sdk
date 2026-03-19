from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.search_response import SearchResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    q: str,
    days: int | Any = UNSET,
    limit: int | Any = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    params["q"] = q
    params["days"] = days
    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/x/stocks/v1/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse | None:
    if response.status_code == 200:
        response_200 = SearchResponse.from_dict(response.json())

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
    ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse
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
    q: str,
    days: int | Any = UNSET,
    limit: int | Any = UNSET,
) -> Response[
    ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse
]:
    """Search for stocks

     Search for stocks by ticker symbol or company name. Results include a platform-specific `summary`
    block for the selected lookback window and are ranked by match relevance before recent activity.

    Args:
        q (str): Search query (ticker or company name)
        days (int | Any): Lookback window for the summary block.
        limit (int | Any): Maximum number of search results to return.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        days=days,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    q: str,
    days: int | Any = UNSET,
    limit: int | Any = UNSET,
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse | None:
    """Search for stocks

     Search for stocks by ticker symbol or company name. Results include a platform-specific `summary`
    block for the selected lookback window and are ranked by match relevance before recent activity.

    Args:
        q (str): Search query (ticker or company name)
        days (int | Any): Lookback window for the summary block.
        limit (int | Any): Maximum number of search results to return.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse
    """

    return sync_detailed(
        client=client,
        q=q,
        days=days,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    days: int | Any = UNSET,
    limit: int | Any = UNSET,
) -> Response[
    ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse
]:
    """Search for stocks

     Search for stocks by ticker symbol or company name. Results include a platform-specific `summary`
    block for the selected lookback window and are ranked by match relevance before recent activity.

    Args:
        q (str): Search query (ticker or company name)
        days (int | Any): Lookback window for the summary block.
        limit (int | Any): Maximum number of search results to return.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse]
    """

    kwargs = _get_kwargs(
        q=q,
        days=days,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    days: int | Any = UNSET,
    limit: int | Any = UNSET,
) -> ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse | None:
    """Search for stocks

     Search for stocks by ticker symbol or company name. Results include a platform-specific `summary`
    block for the selected lookback window and are ranked by match relevance before recent activity.

    Args:
        q (str): Search query (ticker or company name)
        days (int | Any): Lookback window for the summary block.
        limit (int | Any): Maximum number of search results to return.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | HistoricalLimitError | SearchResponse
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            days=days,
            limit=limit,
        )
    ).parsed
