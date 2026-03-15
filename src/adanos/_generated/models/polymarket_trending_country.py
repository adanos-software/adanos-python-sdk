from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymarket_trending_country_trend import PolymarketTrendingCountryTrend
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketTrendingCountry")


@_attrs_define
class PolymarketTrendingCountry:
    """Trending country on Polymarket.

    Attributes:
        buzz_score (float): Aggregated buzz score
        trend (PolymarketTrendingCountryTrend): Aggregated UTC-day trend vs previous UTC day
        trade_count (int): Total trade count in period
        market_count (int): Total distinct active markets in dimension
        unique_tickers (int): Unique tickers in dimension
        bullish_pct (int): Bullish market share
        bearish_pct (int): Bearish market share
        total_liquidity (float): Total liquidity (USD)
        top_tickers (list[str]): Top 5 tickers by trade_count
        country (str): Country name
        unique_traders (int | None | Unset): Aggregated ticker-level unique_traders sums in this dimension (can
            overcount)
        sentiment_score (float | None | Unset): Weighted implied sentiment
    """

    buzz_score: float
    trend: PolymarketTrendingCountryTrend
    trade_count: int
    market_count: int
    unique_tickers: int
    bullish_pct: int
    bearish_pct: int
    total_liquidity: float
    top_tickers: list[str]
    country: str
    unique_traders: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        trend = self.trend.value

        trade_count = self.trade_count

        market_count = self.market_count

        unique_tickers = self.unique_tickers

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        total_liquidity = self.total_liquidity

        top_tickers = self.top_tickers

        country = self.country

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buzz_score": buzz_score,
                "trend": trend,
                "trade_count": trade_count,
                "market_count": market_count,
                "unique_tickers": unique_tickers,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
                "total_liquidity": total_liquidity,
                "top_tickers": top_tickers,
                "country": country,
            }
        )
        if unique_traders is not UNSET:
            field_dict["unique_traders"] = unique_traders
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        trend = PolymarketTrendingCountryTrend(d.pop("trend"))

        trade_count = d.pop("trade_count")

        market_count = d.pop("market_count")

        unique_tickers = d.pop("unique_tickers")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        total_liquidity = d.pop("total_liquidity")

        top_tickers = cast(list[str], d.pop("top_tickers"))

        country = d.pop("country")

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

        polymarket_trending_country = cls(
            buzz_score=buzz_score,
            trend=trend,
            trade_count=trade_count,
            market_count=market_count,
            unique_tickers=unique_tickers,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_liquidity=total_liquidity,
            top_tickers=top_tickers,
            country=country,
            unique_traders=unique_traders,
            sentiment_score=sentiment_score,
        )

        polymarket_trending_country.additional_properties = d
        return polymarket_trending_country

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
