from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.trending_stock_trend import TrendingStockTrend
from ..types import UNSET, Unset

T = TypeVar("T", bound="TrendingStock")


@_attrs_define
class TrendingStock:
    """Trending stock with buzz metrics from Reddit.

    Attributes:
        ticker (str): Stock ticker symbol
        buzz_score (float): Buzz Score (0-100). Asymptotic scaling above 50.
        trend (TrendingStockTrend): Multi-factor activity trend using rolling 24h windows. Activity score = 60%
            mentions_ratio + 25% upvotes_ratio + 15% subreddits_ratio. rising: >1.10 (+10%), falling: <0.90 (-10%), stable:
            0.90-1.10.
        mentions (int): Total number of mentions
        unique_posts (int): Number of unique posts
        subreddit_count (int): Number of subreddits with mentions
        sentiment_score (float): Average sentiment score (-1 bearish to +1 bullish)
        bullish_pct (int): Percentage of bullish mentions
        bearish_pct (int): Percentage of bearish mentions
        total_upvotes (int): Total upvotes across all mentions
        company_name (None | str | Unset): Company name from ticker_reference (null if not found)
        trend_history (list[float] | Unset): Daily buzz scores (oldest→newest). Length = max(days, 7). Values 0-100.
    """

    ticker: str
    buzz_score: float
    trend: TrendingStockTrend
    mentions: int
    unique_posts: int
    subreddit_count: int
    sentiment_score: float
    bullish_pct: int
    bearish_pct: int
    total_upvotes: int
    company_name: None | str | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        buzz_score = self.buzz_score

        trend = self.trend.value

        mentions = self.mentions

        unique_posts = self.unique_posts

        subreddit_count = self.subreddit_count

        sentiment_score = self.sentiment_score

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        total_upvotes = self.total_upvotes

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        trend_history: list[float] | Unset = UNSET
        if not isinstance(self.trend_history, Unset):
            trend_history = self.trend_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "buzz_score": buzz_score,
                "trend": trend,
                "mentions": mentions,
                "unique_posts": unique_posts,
                "subreddit_count": subreddit_count,
                "sentiment_score": sentiment_score,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
                "total_upvotes": total_upvotes,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        buzz_score = d.pop("buzz_score")

        trend = TrendingStockTrend(d.pop("trend"))

        mentions = d.pop("mentions")

        unique_posts = d.pop("unique_posts")

        subreddit_count = d.pop("subreddit_count")

        sentiment_score = d.pop("sentiment_score")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        total_upvotes = d.pop("total_upvotes")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        trending_stock = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            trend=trend,
            mentions=mentions,
            unique_posts=unique_posts,
            subreddit_count=subreddit_count,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_upvotes=total_upvotes,
            company_name=company_name,
            trend_history=trend_history,
        )

        trending_stock.additional_properties = d
        return trending_stock

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
