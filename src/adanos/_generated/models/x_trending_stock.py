from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XTrendingStock")


@_attrs_define
class XTrendingStock:
    """Trending stock on X/Twitter - unified format matching Reddit API structure.

    V5.4: Uses real tweet data from x_mentions (collected via twscrape).
    All metrics now available - sentiment, upvotes, author diversity.

        Attributes:
            ticker (str): Stock ticker symbol
            buzz_score (float): V5.4 buzz score from real tweet data. Components: mentions (20), sentiment (20), quality
                (10), author diversity (14, HHI-based), trend (-10 to +20). Asymptotic scaling caps at 100.
            trend (str): Multi-Factor Activity Score trend (24h vs previous 24h). 60% rank + 25% upvotes + 15% author
                diversity. rising: >10% improvement. falling: >10% decline. stable: ±10%.
            mentions (int): Number of tweet mentions from x_mentions table
            company_name (None | str | Unset): Company name from ticker_reference
            sentiment_score (float | None | Unset): Average sentiment score from tweet analysis (-1 to +1)
            bullish_pct (int | None | Unset): Percentage of bullish tweet mentions
            bearish_pct (int | None | Unset): Percentage of bearish tweet mentions
            total_upvotes (int | None | Unset): Total likes across all tweet mentions
            unique_tweets (int | None | Unset): Number of unique tweets mentioning this ticker (distinct tweet_id)
            is_validated (bool | Unset): Also trending on Reddit (cross-platform validation) Default: False.
            trend_history (list[float] | Unset): Daily buzz scores for the last 7 days (oldest to newest). Last element is
                yesterday's score. Today's live score is in buzz_score.
    """

    ticker: str
    buzz_score: float
    trend: str
    mentions: int
    company_name: None | str | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    total_upvotes: int | None | Unset = UNSET
    unique_tweets: int | None | Unset = UNSET
    is_validated: bool | Unset = False
    trend_history: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        buzz_score = self.buzz_score

        trend = self.trend

        mentions = self.mentions

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

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

        unique_tweets: int | None | Unset
        if isinstance(self.unique_tweets, Unset):
            unique_tweets = UNSET
        else:
            unique_tweets = self.unique_tweets

        is_validated = self.is_validated

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
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if total_upvotes is not UNSET:
            field_dict["total_upvotes"] = total_upvotes
        if unique_tweets is not UNSET:
            field_dict["unique_tweets"] = unique_tweets
        if is_validated is not UNSET:
            field_dict["is_validated"] = is_validated
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        buzz_score = d.pop("buzz_score")

        trend = d.pop("trend")

        mentions = d.pop("mentions")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

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

        def _parse_unique_tweets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_tweets = _parse_unique_tweets(d.pop("unique_tweets", UNSET))

        is_validated = d.pop("is_validated", UNSET)

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        x_trending_stock = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            trend=trend,
            mentions=mentions,
            company_name=company_name,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_upvotes=total_upvotes,
            unique_tweets=unique_tweets,
            is_validated=is_validated,
            trend_history=trend_history,
        )

        x_trending_stock.additional_properties = d
        return x_trending_stock

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
