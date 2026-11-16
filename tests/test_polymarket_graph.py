"""API 1.55 Polymarket contracts through the public sync and async clients."""

import pytest
import httpx
import respx

from adanos import AdanosClient
from adanos._generated.models import ErrorResponse, HTTPValidationError, UnsupportedAssetError


BASE_URL = "https://api.example.test"


@pytest.mark.parametrize("async_mode", [False, True])
@pytest.mark.parametrize("method", ["stock", "mentions"])
@pytest.mark.parametrize(
    ("ticker", "status", "payload", "model"),
    [
        ("BK", 404, {"detail": {"error_code": "unsupported_ticker", "message": "Unsupported ticker BK."}}, UnsupportedAssetError),
        ("AAPL", 503, {"detail": "Polymarket identity lookup unavailable"}, ErrorResponse),
        ("BRK.B", 422, {"detail": [{"loc": ["path", "ticker"], "msg": "Invalid Graph key", "type": "string_pattern_mismatch"}]}, HTTPValidationError),
        ("BRK-B", 422, {"detail": [{"loc": ["path", "ticker"], "msg": "Invalid Graph key", "type": "string_pattern_mismatch"}]}, HTTPValidationError),
        ("$AAPL", 422, {"detail": [{"loc": ["path", "ticker"], "msg": "Invalid Graph key", "type": "string_pattern_mismatch"}]}, HTTPValidationError),
    ],
)
@respx.mock
async def test_polymarket_graph_errors(async_mode, method, ticker, status, payload, model):
    suffix = "/mentions" if method == "mentions" else ""
    route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/stock/{ticker}{suffix}").mock(
        return_value=httpx.Response(status, json=payload)
    )
    async with AdanosClient(api_key="test-key", base_url=BASE_URL) as client:
        call = getattr(client.polymarket, method + ("_async" if async_mode else ""))
        result = await call(ticker) if async_mode else call(ticker)
        assert route.called
        assert isinstance(result, model)
        assert result.to_dict() == payload
        client.close()


@pytest.mark.parametrize("async_mode", [False, True])
@pytest.mark.parametrize("ticker", ["BRK", "EWG", "SAP.DE"])
@respx.mock
async def test_polymarket_graph_keys_reach_mentions_unchanged(async_mode, ticker):
    payload = {"ticker": ticker, "period_days": 7, "count": 0, "results": []}
    route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/stock/{ticker}/mentions").mock(
        return_value=httpx.Response(200, json=payload)
    )
    async with AdanosClient(api_key="test-key", base_url=BASE_URL) as client:
        result = await client.polymarket.mentions_async(ticker) if async_mode else client.polymarket.mentions(ticker)
        assert route.called
        assert result.to_dict() == payload
        client.close()


@pytest.mark.parametrize("async_mode", [False, True])
@pytest.mark.parametrize("buzz_score", [None, 0.0])
@respx.mock
async def test_polymarket_compare_accepts_nullable_score_and_missing_history(async_mode, buzz_score):
    row = {"ticker": "BK", "buzz_score": buzz_score, "trade_count": 0, "market_count": 0,
           "current_market_count": 0, "total_liquidity": 0.0}
    route = respx.get(f"{BASE_URL}/polymarket/stocks/v1/compare").mock(
        return_value=httpx.Response(200, json={"period_days": 7, "stocks": [row]})
    )
    async with AdanosClient(api_key="test-key", base_url=BASE_URL) as client:
        tickers = ["BNY", "SAP.DE", "BK"]
        result = await client.polymarket.compare_async(tickers) if async_mode else client.polymarket.compare(tickers)
        assert route.calls[0].request.url.params["tickers"] == "BNY,SAP.DE,BK"
        assert result.stocks[0].buzz_score == buzz_score
        assert result.stocks[0].trend_history == []
        assert "company_name" not in result.stocks[0].to_dict()
        assert result.to_dict()["stocks"][0]["buzz_score"] == buzz_score
        client.close()
