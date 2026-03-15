from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.x_health_response import XHealthResponse
from ...types import Response


def _get_kwargs() -> dict[str, Any]:
    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/x/stocks/v1/health",
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> XHealthResponse | None:
    if response.status_code == 200:
        response_200 = XHealthResponse.from_dict(response.json())

        return response_200

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[XHealthResponse]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[XHealthResponse]:
    """X/Twitter service health check

     Returns X/Twitter API health status with comprehensive diagnostics.

    **Includes:**
    - Service version
    - Total mentions in database
    - Tickers tracked count
    - Worker/scheduler status (from worker_heartbeat table)
    - Last worker scrape timestamp and heartbeat note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[XHealthResponse]
    """

    kwargs = _get_kwargs()

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
) -> XHealthResponse | None:
    """X/Twitter service health check

     Returns X/Twitter API health status with comprehensive diagnostics.

    **Includes:**
    - Service version
    - Total mentions in database
    - Tickers tracked count
    - Worker/scheduler status (from worker_heartbeat table)
    - Last worker scrape timestamp and heartbeat note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        XHealthResponse
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
) -> Response[XHealthResponse]:
    """X/Twitter service health check

     Returns X/Twitter API health status with comprehensive diagnostics.

    **Includes:**
    - Service version
    - Total mentions in database
    - Tickers tracked count
    - Worker/scheduler status (from worker_heartbeat table)
    - Last worker scrape timestamp and heartbeat note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[XHealthResponse]
    """

    kwargs = _get_kwargs()

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
) -> XHealthResponse | None:
    """X/Twitter service health check

     Returns X/Twitter API health status with comprehensive diagnostics.

    **Includes:**
    - Service version
    - Total mentions in database
    - Tickers tracked count
    - Worker/scheduler status (from worker_heartbeat table)
    - Last worker scrape timestamp and heartbeat note

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        XHealthResponse
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
