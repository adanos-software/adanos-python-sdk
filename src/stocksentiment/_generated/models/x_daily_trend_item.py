from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XDailyTrendItem")


@_attrs_define
class XDailyTrendItem:
    """Daily trend data point for X/Twitter.

    Attributes:
        date (str): Date in YYYY-MM-DD format
        mentions (int): Number of tweet mentions on this date
        sentiment (float | None | Unset): Average sentiment score for the day
        avg_rank (float | None | Unset): Average X rank on this date (X-specific)
        buzz_score (float | None | Unset): Buzz score for this date (0-100)
    """

    date: str
    mentions: int
    sentiment: float | None | Unset = UNSET
    avg_rank: float | None | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        date = self.date

        mentions = self.mentions

        sentiment: float | None | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        avg_rank: float | None | Unset
        if isinstance(self.avg_rank, Unset):
            avg_rank = UNSET
        else:
            avg_rank = self.avg_rank

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
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment
        if avg_rank is not UNSET:
            field_dict["avg_rank"] = avg_rank
        if buzz_score is not UNSET:
            field_dict["buzz_score"] = buzz_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        date = d.pop("date")

        mentions = d.pop("mentions")

        def _parse_sentiment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        def _parse_avg_rank(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_rank = _parse_avg_rank(d.pop("avg_rank", UNSET))

        def _parse_buzz_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        buzz_score = _parse_buzz_score(d.pop("buzz_score", UNSET))

        x_daily_trend_item = cls(
            date=date,
            mentions=mentions,
            sentiment=sentiment,
            avg_rank=avg_rank,
            buzz_score=buzz_score,
        )

        x_daily_trend_item.additional_properties = d
        return x_daily_trend_item

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
