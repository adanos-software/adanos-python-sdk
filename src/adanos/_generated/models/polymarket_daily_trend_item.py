from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketDailyTrendItem")


@_attrs_define
class PolymarketDailyTrendItem:
    """Daily trend item for stock detail endpoint.

    Attributes:
        date (str): Date in YYYY-MM-DD format
        trade_count (int): Trade count on this date
        sentiment_score (float | None | Unset): Canonical implied sentiment on this date
        buzz_score (float | None | Unset): Buzz score on this date
        bullish_pct (int | None | Unset): Bullish market-direction percentage for this date
        bearish_pct (int | None | Unset): Bearish market-direction percentage for this date
    """

    date: str
    trade_count: int
    sentiment_score: float | None | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        trade_count = self.trade_count

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        buzz_score: float | None | Unset
        if isinstance(self.buzz_score, Unset):
            buzz_score = UNSET
        else:
            buzz_score = self.buzz_score

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "trade_count": trade_count,
            }
        )
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if buzz_score is not UNSET:
            field_dict["buzz_score"] = buzz_score
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        trade_count = d.pop("trade_count")

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_buzz_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        buzz_score = _parse_buzz_score(d.pop("buzz_score", UNSET))

        bullish_pct = cast(int | None | Unset, d.pop("bullish_pct", UNSET))

        bearish_pct = cast(int | None | Unset, d.pop("bearish_pct", UNSET))

        polymarket_daily_trend_item = cls(
            date=date,
            trade_count=trade_count,
            sentiment_score=sentiment_score,
            buzz_score=buzz_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
        )

        polymarket_daily_trend_item.additional_properties = d
        return polymarket_daily_trend_item

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
