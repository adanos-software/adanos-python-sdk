from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsCompareStockItem")


@_attrs_define
class NewsCompareStockItem:
    """Individual stock in news comparison."""

    ticker: str
    buzz_score: float
    mentions: int
    source_count: int
    trend_history: list[float]
    company_name: None | str | Unset = UNSET
    trend: None | str | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": self.ticker,
                "buzz_score": self.buzz_score,
                "mentions": self.mentions,
                "source_count": self.source_count,
                "trend_history": self.trend_history,
            }
        )
        if self.company_name is not UNSET:
            field_dict["company_name"] = self.company_name
        if self.trend is not UNSET:
            field_dict["trend"] = self.trend
        if self.sentiment_score is not UNSET:
            field_dict["sentiment_score"] = self.sentiment_score
        if self.bullish_pct is not UNSET:
            field_dict["bullish_pct"] = self.bullish_pct
        if self.bearish_pct is not UNSET:
            field_dict["bearish_pct"] = self.bearish_pct
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        def _parse_string(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        def _parse_float(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        def _parse_int(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        news_compare_stock_item = cls(
            ticker=d.pop("ticker"),
            buzz_score=d.pop("buzz_score"),
            mentions=d.pop("mentions"),
            source_count=d.pop("source_count"),
            trend_history=cast(list[float], d.pop("trend_history")),
            company_name=_parse_company_name(d.pop("company_name", UNSET)),
            trend=_parse_string(d.pop("trend", UNSET)),
            sentiment_score=_parse_float(d.pop("sentiment_score", UNSET)),
            bullish_pct=_parse_int(d.pop("bullish_pct", UNSET)),
            bearish_pct=_parse_int(d.pop("bearish_pct", UNSET)),
        )

        news_compare_stock_item.additional_properties = d
        return news_compare_stock_item

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
