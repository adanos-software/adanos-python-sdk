from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crypto_token_sentiment_trend_type_0 import CryptoTokenSentimentTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crypto_token_sentiment_daily_trend_type_0_item import (
        CryptoTokenSentimentDailyTrendType0Item,
    )
    from ..models.crypto_token_sentiment_top_mentions_type_0_item import (
        CryptoTokenSentimentTopMentionsType0Item,
    )
    from ..models.crypto_token_sentiment_top_subreddits_type_0_item import (
        CryptoTokenSentimentTopSubredditsType0Item,
    )


T = TypeVar("T", bound="CryptoTokenSentiment")


@_attrs_define
class CryptoTokenSentiment:
    """Detailed Reddit sentiment for a single crypto symbol.

    Attributes:
        symbol (str): Token symbol
        found (bool): Whether mentions were found
        name (None | str | Unset): Token name
        buzz_score (float | None | Unset): Buzz score
        mentions (int | None | Unset): Canonical explicit mentions in selected period
        sentiment_score (float | None | Unset): Average sentiment
        positive_count (int | None | Unset): Positive mention count
        negative_count (int | None | Unset): Negative mention count
        neutral_count (int | None | Unset): Neutral mention count
        total_upvotes (int | None | Unset): Total upvotes from explicit mentions
        unique_posts (int | None | Unset): Distinct post count
        subreddit_count (int | None | Unset): Distinct subreddit count
        trend (CryptoTokenSentimentTrendType0 | None | Unset): 24h activity trend
        bullish_pct (int | None | Unset): Bullish mention percentage
        bearish_pct (int | None | Unset): Bearish mention percentage
        period_days (int | None | Unset): Analysis period in days
        top_subreddits (list[CryptoTokenSentimentTopSubredditsType0Item] | None | Unset): Top subreddits by mentions
        daily_trend (list[CryptoTokenSentimentDailyTrendType0Item] | None | Unset): Daily trend data
        top_mentions (list[CryptoTokenSentimentTopMentionsType0Item] | None | Unset): Top mentions by engagement
    """

    symbol: str
    found: bool
    name: None | str | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    mentions: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    positive_count: int | None | Unset = UNSET
    negative_count: int | None | Unset = UNSET
    neutral_count: int | None | Unset = UNSET
    total_upvotes: int | None | Unset = UNSET
    unique_posts: int | None | Unset = UNSET
    subreddit_count: int | None | Unset = UNSET
    trend: CryptoTokenSentimentTrendType0 | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    period_days: int | None | Unset = UNSET
    top_subreddits: list[CryptoTokenSentimentTopSubredditsType0Item] | None | Unset = (
        UNSET
    )
    daily_trend: list[CryptoTokenSentimentDailyTrendType0Item] | None | Unset = UNSET
    top_mentions: list[CryptoTokenSentimentTopMentionsType0Item] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        found = self.found

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

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
        elif isinstance(self.trend, CryptoTokenSentimentTrendType0):
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
                "symbol": symbol,
                "found": found,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
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
        from ..models.crypto_token_sentiment_daily_trend_type_0_item import (
            CryptoTokenSentimentDailyTrendType0Item,
        )
        from ..models.crypto_token_sentiment_top_mentions_type_0_item import (
            CryptoTokenSentimentTopMentionsType0Item,
        )
        from ..models.crypto_token_sentiment_top_subreddits_type_0_item import (
            CryptoTokenSentimentTopSubredditsType0Item,
        )

        d = dict(src_dict)
        symbol = d.pop("symbol")

        found = d.pop("found")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

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

        def _parse_trend(data: object) -> CryptoTokenSentimentTrendType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = CryptoTokenSentimentTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CryptoTokenSentimentTrendType0 | None | Unset, data)

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
        ) -> list[CryptoTokenSentimentTopSubredditsType0Item] | None | Unset:
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
                        CryptoTokenSentimentTopSubredditsType0Item.from_dict(
                            top_subreddits_type_0_item_data
                        )
                    )

                    top_subreddits_type_0.append(top_subreddits_type_0_item)

                return top_subreddits_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CryptoTokenSentimentTopSubredditsType0Item] | None | Unset, data
            )

        top_subreddits = _parse_top_subreddits(d.pop("top_subreddits", UNSET))

        def _parse_daily_trend(
            data: object,
        ) -> list[CryptoTokenSentimentDailyTrendType0Item] | None | Unset:
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
                        CryptoTokenSentimentDailyTrendType0Item.from_dict(
                            daily_trend_type_0_item_data
                        )
                    )

                    daily_trend_type_0.append(daily_trend_type_0_item)

                return daily_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CryptoTokenSentimentDailyTrendType0Item] | None | Unset, data
            )

        daily_trend = _parse_daily_trend(d.pop("daily_trend", UNSET))

        def _parse_top_mentions(
            data: object,
        ) -> list[CryptoTokenSentimentTopMentionsType0Item] | None | Unset:
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
                        CryptoTokenSentimentTopMentionsType0Item.from_dict(
                            top_mentions_type_0_item_data
                        )
                    )

                    top_mentions_type_0.append(top_mentions_type_0_item)

                return top_mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(
                list[CryptoTokenSentimentTopMentionsType0Item] | None | Unset, data
            )

        top_mentions = _parse_top_mentions(d.pop("top_mentions", UNSET))

        crypto_token_sentiment = cls(
            symbol=symbol,
            found=found,
            name=name,
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

        crypto_token_sentiment.additional_properties = d
        return crypto_token_sentiment

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
