from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trending_sector_trend import TrendingSectorTrend

T = TypeVar("T", bound="TrendingSector")


@_attrs_define
class TrendingSector:
    """Trending sector with aggregated buzz metrics from Reddit.

    Attributes:
        buzz_score (float): Aggregated Buzz Score (0-100)
        trend (TrendingSectorTrend): Multi-factor activity trend using rolling 24h windows. Activity score = 60%
            mentions_ratio + 25% upvotes_ratio + 15% subreddits_ratio. rising: >1.10 (+10%), falling: <0.90 (-10%), stable:
            0.90-1.10.
        mentions (int): Total mentions
        unique_tickers (int): Number of unique tickers mentioned
        subreddit_count (int): Number of subreddits with mentions
        sentiment_score (float): Weighted average sentiment (-1 bearish to +1 bullish)
        bullish_pct (int): Percentage of bullish mentions
        bearish_pct (int): Percentage of bearish mentions
        total_upvotes (int): Total upvotes across all mentions
        top_tickers (list[str]): Top 5 tickers by mentions
        sector (str): Industry sector name
    """

    buzz_score: float
    trend: TrendingSectorTrend
    mentions: int
    unique_tickers: int
    subreddit_count: int
    sentiment_score: float
    bullish_pct: int
    bearish_pct: int
    total_upvotes: int
    top_tickers: list[str]
    sector: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        trend = self.trend.value

        mentions = self.mentions

        unique_tickers = self.unique_tickers

        subreddit_count = self.subreddit_count

        sentiment_score = self.sentiment_score

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        total_upvotes = self.total_upvotes

        top_tickers = self.top_tickers

        sector = self.sector

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buzz_score": buzz_score,
                "trend": trend,
                "mentions": mentions,
                "unique_tickers": unique_tickers,
                "subreddit_count": subreddit_count,
                "sentiment_score": sentiment_score,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
                "total_upvotes": total_upvotes,
                "top_tickers": top_tickers,
                "sector": sector,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        trend = TrendingSectorTrend(d.pop("trend"))

        mentions = d.pop("mentions")

        unique_tickers = d.pop("unique_tickers")

        subreddit_count = d.pop("subreddit_count")

        sentiment_score = d.pop("sentiment_score")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        total_upvotes = d.pop("total_upvotes")

        top_tickers = cast(list[str], d.pop("top_tickers"))

        sector = d.pop("sector")

        trending_sector = cls(
            buzz_score=buzz_score,
            trend=trend,
            mentions=mentions,
            unique_tickers=unique_tickers,
            subreddit_count=subreddit_count,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_upvotes=total_upvotes,
            top_tickers=top_tickers,
            sector=sector,
        )

        trending_sector.additional_properties = d
        return trending_sector

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
