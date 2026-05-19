from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymarket_market_sentiment_response_trend_type_0 import PolymarketMarketSentimentResponseTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymarket_market_sentiment_driver import PolymarketMarketSentimentDriver


T = TypeVar("T", bound="PolymarketMarketSentimentResponse")


@_attrs_define
class PolymarketMarketSentimentResponse:
    """Service-level Polymarket market sentiment across all tracked stocks.

    Attributes:
        buzz_score (float): Service-wide Polymarket heat score relative to the service's trailing 90-day baseline.
            Around 50 = normal activity, higher values = hotter-than-usual Polymarket activity.
        trade_count (int): Service-wide trade count in the selected period
        market_count (int): Best-effort sum of per-ticker distinct markets active in the selected period; not an exact
            global condition-id union, and longer windows use per-ticker daily-rollup breadth fallback
        current_market_count (int): Sum of ticker-level currently active markets in the latest UTC-day snapshot; use
            this for live-only market breadth
        unique_traders (int): Best-effort service-wide unique trader signal in the selected period
        total_liquidity (float): Windowed aggregated liquidity signal in USD over the selected period
        active_tickers (int): Number of tickers with market activity in the selected period
        positive_count (int): Outcome-aware bullish market count
        negative_count (int): Outcome-aware bearish market count
        neutral_count (int): Markets with neutral or unclassified outcome direction
        bullish_pct (int): Outcome-aware bullish market percentage
        bearish_pct (int): Outcome-aware bearish market percentage
        trend (None | PolymarketMarketSentimentResponseTrendType0 | Unset): Service-level Polymarket flow trend over
            current 3 UTC days vs previous 3 UTC days using trades, volume, market breadth, traders, and liquidity
        sentiment_score (float | None | Unset): Service-wide weighted implied sentiment score
        trend_history (list[float] | Unset): Daily service-wide buzz scores (oldest→newest) using the same relative
            baseline calibration. Length = max(effective_days, 7), where effective_days reflects any platform availability
            clamp.
        drivers (list[PolymarketMarketSentimentDriver] | Unset): Top assets by current buzz_score driving the service-
            level reading
    """

    buzz_score: float
    trade_count: int
    market_count: int
    current_market_count: int
    unique_traders: int
    total_liquidity: float
    active_tickers: int
    positive_count: int
    negative_count: int
    neutral_count: int
    bullish_pct: int
    bearish_pct: int
    trend: None | PolymarketMarketSentimentResponseTrendType0 | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    drivers: list[PolymarketMarketSentimentDriver] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        trade_count = self.trade_count

        market_count = self.market_count

        current_market_count = self.current_market_count

        unique_traders = self.unique_traders

        total_liquidity = self.total_liquidity

        active_tickers = self.active_tickers

        positive_count = self.positive_count

        negative_count = self.negative_count

        neutral_count = self.neutral_count

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, PolymarketMarketSentimentResponseTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        trend_history: list[float] | Unset = UNSET
        if not isinstance(self.trend_history, Unset):
            trend_history = self.trend_history

        drivers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drivers, Unset):
            drivers = []
            for drivers_item_data in self.drivers:
                drivers_item = drivers_item_data.to_dict()
                drivers.append(drivers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buzz_score": buzz_score,
                "trade_count": trade_count,
                "market_count": market_count,
                "current_market_count": current_market_count,
                "unique_traders": unique_traders,
                "total_liquidity": total_liquidity,
                "active_tickers": active_tickers,
                "positive_count": positive_count,
                "negative_count": negative_count,
                "neutral_count": neutral_count,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
            }
        )
        if trend is not UNSET:
            field_dict["trend"] = trend
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history
        if drivers is not UNSET:
            field_dict["drivers"] = drivers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymarket_market_sentiment_driver import PolymarketMarketSentimentDriver

        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        trade_count = d.pop("trade_count")

        market_count = d.pop("market_count")

        current_market_count = d.pop("current_market_count")

        unique_traders = d.pop("unique_traders")

        total_liquidity = d.pop("total_liquidity")

        active_tickers = d.pop("active_tickers")

        positive_count = d.pop("positive_count")

        negative_count = d.pop("negative_count")

        neutral_count = d.pop("neutral_count")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        def _parse_trend(data: object) -> None | PolymarketMarketSentimentResponseTrendType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = PolymarketMarketSentimentResponseTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolymarketMarketSentimentResponseTrendType0 | Unset, data)

        trend = _parse_trend(d.pop("trend", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        _drivers = d.pop("drivers", UNSET)
        drivers: list[PolymarketMarketSentimentDriver] | Unset = UNSET
        if _drivers is not UNSET:
            drivers = []
            for drivers_item_data in _drivers:
                drivers_item = PolymarketMarketSentimentDriver.from_dict(drivers_item_data)

                drivers.append(drivers_item)

        polymarket_market_sentiment_response = cls(
            buzz_score=buzz_score,
            trade_count=trade_count,
            market_count=market_count,
            current_market_count=current_market_count,
            unique_traders=unique_traders,
            total_liquidity=total_liquidity,
            active_tickers=active_tickers,
            positive_count=positive_count,
            negative_count=negative_count,
            neutral_count=neutral_count,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            trend=trend,
            sentiment_score=sentiment_score,
            trend_history=trend_history,
            drivers=drivers,
        )

        polymarket_market_sentiment_response.additional_properties = d
        return polymarket_market_sentiment_response

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
