from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymarket_trending_stock_trend import PolymarketTrendingStockTrend
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketTrendingStock")


@_attrs_define
class PolymarketTrendingStock:
    """Trending stock from Polymarket in Reddit/X-compatible shape.

    Attributes:
        ticker (str): Stock ticker symbol
        buzz_score (float): Buzz score (0-100)
        trend (PolymarketTrendingStockTrend): UTC-day activity trend vs previous UTC day
        trade_count (int): Trade count in selected period
        market_count (int): Number of active markets for ticker
        bullish_pct (int): Share of markets with YES > 0.5
        bearish_pct (int): Share of markets with YES < 0.5
        total_liquidity (float): Total liquidity (USD)
        company_name (None | str | Unset): Company name from ticker_reference
        unique_traders (int | None | Unset): Sum of per-market day unique trader counters (can overcount across markets)
        sentiment_score (float | None | Unset): Implied sentiment (-1 to +1)
        trend_history (list[float] | Unset): Daily buzz scores (oldest→newest), length max(days, 7)
    """

    ticker: str
    buzz_score: float
    trend: PolymarketTrendingStockTrend
    trade_count: int
    market_count: int
    bullish_pct: int
    bearish_pct: int
    total_liquidity: float
    company_name: None | str | Unset = UNSET
    unique_traders: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        buzz_score = self.buzz_score

        trend = self.trend.value

        trade_count = self.trade_count

        market_count = self.market_count

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        total_liquidity = self.total_liquidity

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        unique_traders: int | None | Unset
        if isinstance(self.unique_traders, Unset):
            unique_traders = UNSET
        else:
            unique_traders = self.unique_traders

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        trend_history: list[float] | Unset = UNSET
        if not isinstance(self.trend_history, Unset):
            trend_history = self.trend_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "buzz_score": buzz_score,
                "trend": trend,
                "trade_count": trade_count,
                "market_count": market_count,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
                "total_liquidity": total_liquidity,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if unique_traders is not UNSET:
            field_dict["unique_traders"] = unique_traders
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        buzz_score = d.pop("buzz_score")

        trend = PolymarketTrendingStockTrend(d.pop("trend"))

        trade_count = d.pop("trade_count")

        market_count = d.pop("market_count")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        total_liquidity = d.pop("total_liquidity")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_unique_traders(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_traders = _parse_unique_traders(d.pop("unique_traders", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        polymarket_trending_stock = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            trend=trend,
            trade_count=trade_count,
            market_count=market_count,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_liquidity=total_liquidity,
            company_name=company_name,
            unique_traders=unique_traders,
            sentiment_score=sentiment_score,
            trend_history=trend_history,
        )

        polymarket_trending_stock.additional_properties = d
        return polymarket_trending_stock

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
