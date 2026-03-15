from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x_trending_sector_trend import XTrendingSectorTrend
from ..types import UNSET, Unset

T = TypeVar("T", bound="XTrendingSector")


@_attrs_define
class XTrendingSector:
    """Trending sector with aggregated buzz metrics from X/Twitter.

    Attributes:
        buzz_score (float): Aggregated Buzz Score (0-100) from X mentions
        trend (XTrendingSectorTrend): Multi-factor activity trend using rolling 24h windows. Activity score = 60%
            mentions_ratio + 25% upvotes_ratio + 15% authors_ratio. rising: >1.10 (+10%), falling: <0.90 (-10%), stable:
            0.90-1.10.
        mentions (int): Total tweet mentions
        unique_tickers (int): Number of unique tickers mentioned
        unique_authors (int): Number of unique authors (diversity metric)
        top_tickers (list[str]): Top 5 tickers by mention count in this dimension
        sector (str): Industry sector name
        sentiment_score (float | None | Unset): Weighted average sentiment (-1 bearish to +1 bullish)
        bullish_pct (int | None | Unset): Percentage of bullish mentions
        bearish_pct (int | None | Unset): Percentage of bearish mentions
        total_upvotes (int | None | Unset): Total likes across all mentions
    """

    buzz_score: float
    trend: XTrendingSectorTrend
    mentions: int
    unique_tickers: int
    unique_authors: int
    top_tickers: list[str]
    sector: str
    sentiment_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    total_upvotes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        trend = self.trend.value

        mentions = self.mentions

        unique_tickers = self.unique_tickers

        unique_authors = self.unique_authors

        top_tickers = self.top_tickers

        sector = self.sector

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

        total_upvotes: int | None | Unset
        if isinstance(self.total_upvotes, Unset):
            total_upvotes = UNSET
        else:
            total_upvotes = self.total_upvotes

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buzz_score": buzz_score,
                "trend": trend,
                "mentions": mentions,
                "unique_tickers": unique_tickers,
                "unique_authors": unique_authors,
                "top_tickers": top_tickers,
                "sector": sector,
            }
        )
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if total_upvotes is not UNSET:
            field_dict["total_upvotes"] = total_upvotes

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        trend = XTrendingSectorTrend(d.pop("trend"))

        mentions = d.pop("mentions")

        unique_tickers = d.pop("unique_tickers")

        unique_authors = d.pop("unique_authors")

        top_tickers = cast(list[str], d.pop("top_tickers"))

        sector = d.pop("sector")

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

        def _parse_total_upvotes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_upvotes = _parse_total_upvotes(d.pop("total_upvotes", UNSET))

        x_trending_sector = cls(
            buzz_score=buzz_score,
            trend=trend,
            mentions=mentions,
            unique_tickers=unique_tickers,
            unique_authors=unique_authors,
            top_tickers=top_tickers,
            sector=sector,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_upvotes=total_upvotes,
        )

        x_trending_sector.additional_properties = d
        return x_trending_sector

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
