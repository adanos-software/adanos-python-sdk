from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.error_response import ErrorResponse
from ...models.historical_limit_error import HistoricalLimitError
from ...models.http_validation_error import HTTPValidationError
from ...models.invalid_period_error import InvalidPeriodError
from ...models.news_search_response import NewsSearchResponse
from ...models.rate_limit_error import RateLimitError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    q: str,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["q"] = q


    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/news/stocks/v1/search",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError | None:
    if response.status_code == 200:
        response_200 = NewsSearchResponse.from_dict(response.json())

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
        response_429 = RateLimitError.from_dict(response.json())

        return response_429

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError]:
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
    limit: int | Unset = 20,
) -> Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError]:
    """Search stocks

     Search stocks by ticker, company name, or alias within the news platform universe.

    Results prioritize match relevance first (exact ticker matches, then prefixes, then name/alias
    matches)
    and include a compact API-managed recent `summary` block.

    Args:
        q (str): Search query (minimum 2 non-$ characters after trimming).
        limit (int | Unset): Maximum number of results to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError]
    """

    kwargs = _get_kwargs(
        q=q,
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
    limit: int | Unset = 20,
) -> ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError | None:
    """Search stocks

     Search stocks by ticker, company name, or alias within the news platform universe.

    Results prioritize match relevance first (exact ticker matches, then prefixes, then name/alias
    matches)
    and include a compact API-managed recent `summary` block.

    Args:
        q (str): Search query (minimum 2 non-$ characters after trimming).
        limit (int | Unset): Maximum number of results to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError
    """

    return sync_detailed(
        client=client,
        q=q,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    q: str,
    limit: int | Unset = 20,
) -> Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError]:
    """Search stocks

     Search stocks by ticker, company name, or alias within the news platform universe.

    Results prioritize match relevance first (exact ticker matches, then prefixes, then name/alias
    matches)
    and include a compact API-managed recent `summary` block.

    Args:
        q (str): Search query (minimum 2 non-$ characters after trimming).
        limit (int | Unset): Maximum number of results to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError]
    """

    kwargs = _get_kwargs(
        q=q,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    q: str,
    limit: int | Unset = 20,
) -> ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError | None:
    """Search stocks

     Search stocks by ticker, company name, or alias within the news platform universe.

    Results prioritize match relevance first (exact ticker matches, then prefixes, then name/alias
    matches)
    and include a compact API-managed recent `summary` block.

    Args:
        q (str): Search query (minimum 2 non-$ characters after trimming).
        limit (int | Unset): Maximum number of results to return Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ErrorResponse | HTTPValidationError | InvalidPeriodError | HistoricalLimitError | NewsSearchResponse | RateLimitError
    """

    return (
        await asyncio_detailed(
            client=client,
            q=q,
            limit=limit,
        )
    ).parsed
