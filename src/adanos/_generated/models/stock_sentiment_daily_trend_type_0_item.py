from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockSentimentDailyTrendType0Item")


@_attrs_define
class StockSentimentDailyTrendType0Item:
    """Daily Reddit trend datapoint."""

    date: str
    mentions: int
    sentiment_score: float | None | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({"date": self.date, "mentions": self.mentions})
        if self.sentiment_score is not UNSET:
            field_dict["sentiment_score"] = self.sentiment_score
        if self.buzz_score is not UNSET:
            field_dict["buzz_score"] = self.buzz_score
        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_float(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        item = cls(
            date=d.pop("date"),
            mentions=d.pop("mentions"),
            sentiment_score=_parse_float(d.pop("sentiment_score", UNSET)),
            buzz_score=_parse_float(d.pop("buzz_score", UNSET)),
        )
        item.additional_properties = d
        return item

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
