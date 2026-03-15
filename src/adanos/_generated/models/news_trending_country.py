from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.news_trending_country_trend import NewsTrendingCountryTrend

T = TypeVar("T", bound="NewsTrendingCountry")


@_attrs_define
class NewsTrendingCountry:
    """Trending country with aggregated buzz metrics from news.

    Attributes:
        buzz_score (float): Aggregated Buzz Score (0-100)
        trend (NewsTrendingCountryTrend): Multi-factor activity trend using rolling 24h windows. Activity score = 60%
            mentions_ratio + 25% baseline_ratio + 15% source_ratio (baseline_ratio is fixed at 1.0 because news has no
            upvote signal). rising: >1.10 (+10%), falling: <0.90 (-10%), stable: 0.90-1.10.
        mentions (int): Total mentions
        unique_tickers (int): Number of unique tickers mentioned
        source_count (int): Number of distinct news sources with mentions
        sentiment_score (float): Weighted average sentiment (-1 bearish to +1 bullish)
        bullish_pct (int): Percentage of bullish mentions
        bearish_pct (int): Percentage of bearish mentions
        top_tickers (list[str]): Top 5 tickers by mentions
        country (str): Country name
    """

    buzz_score: float
    trend: NewsTrendingCountryTrend
    mentions: int
    unique_tickers: int
    source_count: int
    sentiment_score: float
    bullish_pct: int
    bearish_pct: int
    top_tickers: list[str]
    country: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        trend = self.trend.value

        mentions = self.mentions

        unique_tickers = self.unique_tickers

        source_count = self.source_count

        sentiment_score = self.sentiment_score

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        top_tickers = self.top_tickers

        country = self.country

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buzz_score": buzz_score,
                "trend": trend,
                "mentions": mentions,
                "unique_tickers": unique_tickers,
                "source_count": source_count,
                "sentiment_score": sentiment_score,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
                "top_tickers": top_tickers,
                "country": country,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        trend = NewsTrendingCountryTrend(d.pop("trend"))

        mentions = d.pop("mentions")

        unique_tickers = d.pop("unique_tickers")

        source_count = d.pop("source_count")

        sentiment_score = d.pop("sentiment_score")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        top_tickers = cast(list[str], d.pop("top_tickers"))

        country = d.pop("country")

        news_trending_country = cls(
            buzz_score=buzz_score,
            trend=trend,
            mentions=mentions,
            unique_tickers=unique_tickers,
            source_count=source_count,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            top_tickers=top_tickers,
            country=country,
        )

        news_trending_country.additional_properties = d
        return news_trending_country

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
