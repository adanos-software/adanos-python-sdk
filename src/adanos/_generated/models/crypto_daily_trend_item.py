from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoDailyTrendItem")


@_attrs_define
class CryptoDailyTrendItem:
    """Daily trend datapoint for a crypto symbol.

    Attributes:
        date (datetime.date): Date in YYYY-MM-DD format
        mentions (int): Explicit mention count for the day
        sentiment_score (float | None | Unset): Average sentiment score for the day
        buzz_score (float | None | Unset): Daily buzz score
    """

    date: datetime.date
    mentions: int
    sentiment_score: float | None | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date.isoformat()

        mentions = self.mentions

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

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "date": date,
                "mentions": mentions,
            }
        )
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if buzz_score is not UNSET:
            field_dict["buzz_score"] = buzz_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = isoparse(d.pop("date")).date()

        mentions = d.pop("mentions")

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

        crypto_daily_trend_item = cls(
            date=date,
            mentions=mentions,
            sentiment_score=sentiment_score,
            buzz_score=buzz_score,
        )

        crypto_daily_trend_item.additional_properties = d
        return crypto_daily_trend_item

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
