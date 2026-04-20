from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CompareStockItem")


@_attrs_define
class CompareStockItem:
    """Individual stock in comparison.

    Shared between Reddit and X compare endpoints.

    Attributes:
        ticker (str): Stock ticker symbol
        buzz_score (float): Buzz Score (0-100). Asymptotic scaling above 50.
        mentions (int): Total mentions in period
        trend_history (list[float]): Daily buzz history (minimum 7 values, oldest to newest)
        company_name (None | str | Unset): Company name from ticker_reference
        trend (None | str | Unset): Trend direction for the selected period
        unique_posts (int | None | Unset): Distinct Reddit post count
        subreddit_count (int | None | Unset): Distinct subreddit count
        unique_tweets (int | None | Unset): Distinct tweet count
        sentiment_score (float | None | Unset): Canonical sentiment field
        bullish_pct (int | None | Unset): Percentage of bullish mentions
        bearish_pct (int | None | Unset): Percentage of bearish mentions
        total_upvotes (int | None | Unset): Canonical aggregate upvote/like count
    """

    ticker: str
    buzz_score: float
    mentions: int
    trend_history: list[float]
    company_name: None | str | Unset = UNSET
    trend: None | str | Unset = UNSET
    unique_posts: int | None | Unset = UNSET
    subreddit_count: int | None | Unset = UNSET
    unique_tweets: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    total_upvotes: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker
        buzz_score = self.buzz_score
        mentions = self.mentions
        trend_history = self.trend_history

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        else:
            trend = self.trend

        unique_posts: int | None | Unset
        if isinstance(self.unique_posts, Unset):
            unique_posts = UNSET
        else:
            unique_posts = self.unique_posts

        subreddit_count: int | None | Unset
        if isinstance(self.subreddit_count, Unset):
            subreddit_count = UNSET
        else:
            subreddit_count = self.subreddit_count

        unique_tweets: int | None | Unset
        if isinstance(self.unique_tweets, Unset):
            unique_tweets = UNSET
        else:
            unique_tweets = self.unique_tweets

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
                "ticker": ticker,
                "buzz_score": buzz_score,
                "mentions": mentions,
                "trend_history": trend_history,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if trend is not UNSET:
            field_dict["trend"] = trend
        if unique_posts is not UNSET:
            field_dict["unique_posts"] = unique_posts
        if subreddit_count is not UNSET:
            field_dict["subreddit_count"] = subreddit_count
        if unique_tweets is not UNSET:
            field_dict["unique_tweets"] = unique_tweets
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
        ticker = d.pop("ticker")
        buzz_score = d.pop("buzz_score")
        mentions = d.pop("mentions")
        trend_history = cast(list[float], d.pop("trend_history"))

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_trend(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        trend = _parse_trend(d.pop("trend", UNSET))

        def _parse_int(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_posts = _parse_int(d.pop("unique_posts", UNSET))
        subreddit_count = _parse_int(d.pop("subreddit_count", UNSET))
        unique_tweets = _parse_int(d.pop("unique_tweets", UNSET))

        def _parse_float(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_float(d.pop("sentiment_score", UNSET))
        bullish_pct = _parse_int(d.pop("bullish_pct", UNSET))
        bearish_pct = _parse_int(d.pop("bearish_pct", UNSET))
        total_upvotes = _parse_int(d.pop("total_upvotes", UNSET))

        compare_stock_item = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            mentions=mentions,
            trend_history=trend_history,
            company_name=company_name,
            trend=trend,
            unique_posts=unique_posts,
            subreddit_count=subreddit_count,
            unique_tweets=unique_tweets,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_upvotes=total_upvotes,
        )

        compare_stock_item.additional_properties = d
        return compare_stock_item

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
