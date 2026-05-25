from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymarket_search_summary_trend_type_0 import PolymarketSearchSummaryTrendType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketSearchSummary")


@_attrs_define
class PolymarketSearchSummary:
    """Compact recent-period summary attached to Polymarket search results.

    Attributes:
        trade_count (int): Trade count in the selected period
        buzz_score (float): Buzz score in the selected period
        trend (None | PolymarketSearchSummaryTrendType0 | Unset): Polymarket flow trend over current 3 UTC days vs
            previous 3 UTC days using trades, volume, market breadth, traders, and liquidity
        sentiment_score (float | None | Unset): Implied sentiment in the selected period
    """

    trade_count: int
    buzz_score: float
    trend: None | PolymarketSearchSummaryTrendType0 | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        trade_count = self.trade_count

        buzz_score = self.buzz_score

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, PolymarketSearchSummaryTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "trade_count": trade_count,
                "buzz_score": buzz_score,
            }
        )
        if trend is not UNSET:
            field_dict["trend"] = trend
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        trade_count = d.pop("trade_count")

        buzz_score = d.pop("buzz_score")

        def _parse_trend(data: object) -> None | PolymarketSearchSummaryTrendType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = PolymarketSearchSummaryTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolymarketSearchSummaryTrendType0 | Unset, data)

        trend = _parse_trend(d.pop("trend", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        polymarket_search_summary = cls(
            trade_count=trade_count,
            buzz_score=buzz_score,
            trend=trend,
            sentiment_score=sentiment_score,
        )

        polymarket_search_summary.additional_properties = d
        return polymarket_search_summary

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
