from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x_search_summary_trend_type_0 import XSearchSummaryTrendType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="XSearchSummary")


@_attrs_define
class XSearchSummary:
    """Compact recent-period summary attached to X search results.

    Attributes:
        mentions (int): Tweet mentions in the selected period
        buzz_score (float): Buzz score in the selected period
        unique_tweets (int): Distinct tweet count in the selected period
        total_upvotes (int): Total likes in the selected period
        trend (None | Unset | XSearchSummaryTrendType0): X activity/attention trend over current 3 UTC days vs previous
            3 UTC days using mentions, likes, and author breadth; not price trend
        sentiment_score (float | None | Unset): Average sentiment score in the selected period
        bullish_pct (int | None | Unset): Bullish tweet percentage
        bearish_pct (int | None | Unset): Bearish tweet percentage
    """

    mentions: int
    buzz_score: float
    unique_tweets: int
    total_upvotes: int
    trend: None | Unset | XSearchSummaryTrendType0 = UNSET
    sentiment_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mentions = self.mentions

        buzz_score = self.buzz_score

        unique_tweets = self.unique_tweets

        total_upvotes = self.total_upvotes

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, XSearchSummaryTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        bullish_pct: int | None | Unset
        if isinstance(self.bullish_pct, Unset):
            bullish_pct = UNSET
        else:
            bullish_pct = self.bullish_pct

        bearish_pct: int | None | Unset
        if isinstance(self.bearish_pct, Unset):
            bearish_pct = UNSET
        else:
            bearish_pct = self.bearish_pct

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mentions": mentions,
                "buzz_score": buzz_score,
                "unique_tweets": unique_tweets,
                "total_upvotes": total_upvotes,
            }
        )
        if trend is not UNSET:
            field_dict["trend"] = trend
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        mentions = d.pop("mentions")

        buzz_score = d.pop("buzz_score")

        unique_tweets = d.pop("unique_tweets")

        total_upvotes = d.pop("total_upvotes")

        def _parse_trend(data: object) -> None | Unset | XSearchSummaryTrendType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = XSearchSummaryTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | XSearchSummaryTrendType0, data)

        trend = _parse_trend(d.pop("trend", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_bullish_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bullish_pct = _parse_bullish_pct(d.pop("bullish_pct", UNSET))

        def _parse_bearish_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bearish_pct = _parse_bearish_pct(d.pop("bearish_pct", UNSET))

        x_search_summary = cls(
            mentions=mentions,
            buzz_score=buzz_score,
            unique_tweets=unique_tweets,
            total_upvotes=total_upvotes,
            trend=trend,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
        )

        x_search_summary.additional_properties = d
        return x_search_summary

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
