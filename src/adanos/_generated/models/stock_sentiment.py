from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.stock_sentiment_trend_type_0 import StockSentimentTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.stock_sentiment_daily_trend_type_0_item import (
        StockSentimentDailyTrendType0Item,
    )
    from ..models.stock_sentiment_top_mentions_type_0_item import (
        StockSentimentTopMentionsType0Item,
    )
    from ..models.stock_sentiment_top_subreddits_type_0_item import (
        StockSentimentTopSubredditsType0Item,
    )


T = TypeVar("T", bound="StockSentiment")


@_attrs_define
class StockSentiment:
    """Detailed sentiment analysis for a specific stock ticker.

    Attributes:
        ticker (str): Stock ticker symbol
        found (bool): Whether mentions were found for this ticker
        company_name (None | str | Unset): Company name from ticker_reference (null if not found)
        buzz_score (float | None | Unset): Buzz Score (0-100). Asymptotic scaling above 50.
        mentions (int | None | Unset): Canonical total number of mentions
        sentiment_score (float | None | Unset): Average sentiment score (-1 bearish to +1 bullish)
        positive_count (int | None | Unset): Number of positive mentions
        negative_count (int | None | Unset): Number of negative mentions
        neutral_count (int | None | Unset): Number of neutral mentions
        total_upvotes (int | None | Unset): Total upvotes across all mentions
        unique_posts (int | None | Unset): Number of unique posts
        subreddit_count (int | None | Unset): Number of subreddits with mentions
        trend (None | StockSentimentTrendType0 | Unset): Multi-factor activity trend using rolling 24h windows. Activity
            score = 60% mentions_ratio + 25% upvotes_ratio + 15% subreddits_ratio. rising: >1.10, falling: <0.90, stable:
            0.90-1.10.
        bullish_pct (int | None | Unset): Percentage of bullish mentions
        bearish_pct (int | None | Unset): Percentage of bearish mentions
        period_days (int | None | Unset): Analysis period in days
        top_subreddits (list[StockSentimentTopSubredditsType0Item] | None | Unset): Top subreddits by mention count
        daily_trend (list[StockSentimentDailyTrendType0Item] | None | Unset): Mentions per day with sentiment and
            buzz_score
        top_mentions (list[StockSentimentTopMentionsType0Item] | None | Unset): Top mentions by upvotes
    """

    ticker: str
    found: bool
    company_name: None | str | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    mentions: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    positive_count: int | None | Unset = UNSET
    negative_count: int | None | Unset = UNSET
    neutral_count: int | None | Unset = UNSET
    total_upvotes: int | None | Unset = UNSET
    unique_posts: int | None | Unset = UNSET
    subreddit_count: int | None | Unset = UNSET
    trend: None | StockSentimentTrendType0 | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    period_days: int | None | Unset = UNSET
    top_subreddits: list[StockSentimentTopSubredditsType0Item] | None | Unset = UNSET
    daily_trend: list[StockSentimentDailyTrendType0Item] | None | Unset = UNSET
    top_mentions: list[StockSentimentTopMentionsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        found = self.found

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        buzz_score: float | None | Unset
        if isinstance(self.buzz_score, Unset):
            buzz_score = UNSET
        else:
            buzz_score = self.buzz_score

        mentions: int | None | Unset
        if isinstance(self.mentions, Unset):
            mentions = UNSET
        else:
            mentions = self.mentions

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        positive_count: int | None | Unset
        if isinstance(self.positive_count, Unset):
            positive_count = UNSET
        else:
            positive_count = self.positive_count

        negative_count: int | None | Unset
        if isinstance(self.negative_count, Unset):
            negative_count = UNSET
        else:
            negative_count = self.negative_count

        neutral_count: int | None | Unset
        if isinstance(self.neutral_count, Unset):
            neutral_count = UNSET
        else:
            neutral_count = self.neutral_count

        total_upvotes: int | None | Unset
        if isinstance(self.total_upvotes, Unset):
            total_upvotes = UNSET
        else:
            total_upvotes = self.total_upvotes

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

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, StockSentimentTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

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

        period_days: int | None | Unset
        if isinstance(self.period_days, Unset):
            period_days = UNSET
        else:
            period_days = self.period_days

        top_subreddits: list[dict[str, Any]] | None | Unset
        if isinstance(self.top_subreddits, Unset):
            top_subreddits = UNSET
        elif isinstance(self.top_subreddits, list):
            top_subreddits = []
            for top_subreddits_type_0_item_data in self.top_subreddits:
                top_subreddits_type_0_item = top_subreddits_type_0_item_data.to_dict()
                top_subreddits.append(top_subreddits_type_0_item)

        else:
            top_subreddits = self.top_subreddits

        daily_trend: list[dict[str, Any]] | None | Unset
        if isinstance(self.daily_trend, Unset):
            daily_trend = UNSET
        elif isinstance(self.daily_trend, list):
            daily_trend = []
            for daily_trend_type_0_item_data in self.daily_trend:
                daily_trend_type_0_item = daily_trend_type_0_item_data.to_dict()
                daily_trend.append(daily_trend_type_0_item)

        else:
            daily_trend = self.daily_trend

        top_mentions: list[dict[str, Any]] | None | Unset
        if isinstance(self.top_mentions, Unset):
            top_mentions = UNSET
        elif isinstance(self.top_mentions, list):
            top_mentions = []
            for top_mentions_type_0_item_data in self.top_mentions:
                top_mentions_type_0_item = top_mentions_type_0_item_data.to_dict()
                top_mentions.append(top_mentions_type_0_item)

        else:
            top_mentions = self.top_mentions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "found": found,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if buzz_score is not UNSET:
            field_dict["buzz_score"] = buzz_score
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if positive_count is not UNSET:
            field_dict["positive_count"] = positive_count
        if negative_count is not UNSET:
            field_dict["negative_count"] = negative_count
        if neutral_count is not UNSET:
            field_dict["neutral_count"] = neutral_count
        if total_upvotes is not UNSET:
            field_dict["total_upvotes"] = total_upvotes
        if unique_posts is not UNSET:
            field_dict["unique_posts"] = unique_posts
        if subreddit_count is not UNSET:
            field_dict["subreddit_count"] = subreddit_count
        if trend is not UNSET:
            field_dict["trend"] = trend
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if period_days is not UNSET:
            field_dict["period_days"] = period_days
        if top_subreddits is not UNSET:
            field_dict["top_subreddits"] = top_subreddits
        if daily_trend is not UNSET:
            field_dict["daily_trend"] = daily_trend
        if top_mentions is not UNSET:
            field_dict["top_mentions"] = top_mentions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.stock_sentiment_daily_trend_type_0_item import (
            StockSentimentDailyTrendType0Item,
        )
        from ..models.stock_sentiment_top_mentions_type_0_item import (
            StockSentimentTopMentionsType0Item,
        )
        from ..models.stock_sentiment_top_subreddits_type_0_item import (
            StockSentimentTopSubredditsType0Item,
        )

        d = dict(src_dict)
        ticker = d.pop("ticker")

        found = d.pop("found")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_buzz_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        buzz_score = _parse_buzz_score(d.pop("buzz_score", UNSET))

        def _parse_mentions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mentions = _parse_mentions(d.pop("mentions", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_positive_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        positive_count = _parse_positive_count(d.pop("positive_count", UNSET))

        def _parse_negative_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        negative_count = _parse_negative_count(d.pop("negative_count", UNSET))

        def _parse_neutral_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        neutral_count = _parse_neutral_count(d.pop("neutral_count", UNSET))

        def _parse_total_upvotes(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_upvotes = _parse_total_upvotes(d.pop("total_upvotes", UNSET))

        def _parse_unique_posts(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_posts = _parse_unique_posts(d.pop("unique_posts", UNSET))

        def _parse_subreddit_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        subreddit_count = _parse_subreddit_count(d.pop("subreddit_count", UNSET))

        def _parse_trend(data: object) -> None | StockSentimentTrendType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = StockSentimentTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | StockSentimentTrendType0 | Unset, data)

        trend = _parse_trend(d.pop("trend", UNSET))

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

        def _parse_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_days = _parse_period_days(d.pop("period_days", UNSET))

        def _parse_top_subreddits(
            data: object,
        ) -> list[StockSentimentTopSubredditsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                top_subreddits_type_0 = []
                _top_subreddits_type_0 = data
                for top_subreddits_type_0_item_data in _top_subreddits_type_0:
                    top_subreddits_type_0_item = (
                        StockSentimentTopSubredditsType0Item.from_dict(
                            top_subreddits_type_0_item_data
                        )
                    )

                    top_subreddits_type_0.append(top_subreddits_type_0_item)

                return top_subreddits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StockSentimentTopSubredditsType0Item] | None | Unset, data)

        top_subreddits = _parse_top_subreddits(d.pop("top_subreddits", UNSET))

        def _parse_daily_trend(
            data: object,
        ) -> list[StockSentimentDailyTrendType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                daily_trend_type_0 = []
                _daily_trend_type_0 = data
                for daily_trend_type_0_item_data in _daily_trend_type_0:
                    daily_trend_type_0_item = (
                        StockSentimentDailyTrendType0Item.from_dict(
                            daily_trend_type_0_item_data
                        )
                    )

                    daily_trend_type_0.append(daily_trend_type_0_item)

                return daily_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StockSentimentDailyTrendType0Item] | None | Unset, data)

        daily_trend = _parse_daily_trend(d.pop("daily_trend", UNSET))

        def _parse_top_mentions(
            data: object,
        ) -> list[StockSentimentTopMentionsType0Item] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                top_mentions_type_0 = []
                _top_mentions_type_0 = data
                for top_mentions_type_0_item_data in _top_mentions_type_0:
                    top_mentions_type_0_item = (
                        StockSentimentTopMentionsType0Item.from_dict(
                            top_mentions_type_0_item_data
                        )
                    )

                    top_mentions_type_0.append(top_mentions_type_0_item)

                return top_mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[StockSentimentTopMentionsType0Item] | None | Unset, data)

        top_mentions = _parse_top_mentions(d.pop("top_mentions", UNSET))

        stock_sentiment = cls(
            ticker=ticker,
            found=found,
            company_name=company_name,
            buzz_score=buzz_score,
            mentions=mentions,
            sentiment_score=sentiment_score,
            positive_count=positive_count,
            negative_count=negative_count,
            neutral_count=neutral_count,
            total_upvotes=total_upvotes,
            unique_posts=unique_posts,
            subreddit_count=subreddit_count,
            trend=trend,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            period_days=period_days,
            top_subreddits=top_subreddits,
            daily_trend=daily_trend,
            top_mentions=top_mentions,
        )

        stock_sentiment.additional_properties = d
        return stock_sentiment

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
