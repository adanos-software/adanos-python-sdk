from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x_stock_detail_response_trend_type_0 import XStockDetailResponseTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x_daily_trend_item import XDailyTrendItem
    from ..models.x_top_tweet import XTopTweet


T = TypeVar("T", bound="XStockDetailResponse")


@_attrs_define
class XStockDetailResponse:
    """Detailed X/Twitter data for a single stock - unified format matching Reddit API.

    V5.4: All metrics now available from real tweet data (x_mentions table).

        Attributes:
            ticker (str): Stock ticker symbol
            company_name (None | str | Unset): Company name from ticker_reference
            found (bool | Unset): Whether ticker was found in X trending Default: True.
            buzz_score (float | None | Unset): V5.4 buzz score from real tweet data (null if not found)
            mentions (int | None | Unset): Canonical total tweet mentions within period
            total_mentions (int | None | Unset): Deprecated alias for ``mentions``
            sentiment_score (float | None | Unset): Average sentiment score from tweet analysis (-1 to +1)
            positive_count (int | None | Unset): Bullish tweet mentions
            negative_count (int | None | Unset): Bearish tweet mentions
            neutral_count (int | None | Unset): Neutral tweet mentions
            total_upvotes (int | None | Unset): Total likes across all tweet mentions
            unique_tweets (int | None | Unset): Number of unique tweets (distinct tweet_id)
            trend (None | Unset | XStockDetailResponseTrendType0): Multi-factor activity trend using rolling 24h windows.
                Activity score = 60% rank_ratio + 25% upvotes_ratio + 15% authors_ratio. rising: >1.10, falling: <0.90, stable:
                0.90-1.10.
            bullish_pct (int | None | Unset): Percentage of bullish tweet mentions
            bearish_pct (int | None | Unset): Percentage of bearish tweet mentions
            period_days (int | None | Unset): Analysis period in days
            daily_trend (list[XDailyTrendItem] | None | Unset): Daily trend data with avg_rank (X-specific)
            top_tweets (list[XTopTweet] | None | Unset): Top 10 tweets by engagement (likes + retweets)
            is_validated (bool | Unset): Whether ticker is also trending on Reddit Default: False.
    """

    ticker: str
    company_name: None | str | Unset = UNSET
    found: bool | Unset = True
    buzz_score: float | None | Unset = UNSET
    mentions: int | None | Unset = UNSET
    total_mentions: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    positive_count: int | None | Unset = UNSET
    negative_count: int | None | Unset = UNSET
    neutral_count: int | None | Unset = UNSET
    total_upvotes: int | None | Unset = UNSET
    unique_tweets: int | None | Unset = UNSET
    trend: None | Unset | XStockDetailResponseTrendType0 = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    period_days: int | None | Unset = UNSET
    daily_trend: list[XDailyTrendItem] | None | Unset = UNSET
    top_tweets: list[XTopTweet] | None | Unset = UNSET
    is_validated: bool | Unset = False
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        found = self.found

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

        total_mentions: int | None | Unset
        if isinstance(self.total_mentions, Unset):
            total_mentions = UNSET
        else:
            total_mentions = self.total_mentions

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

        unique_tweets: int | None | Unset
        if isinstance(self.unique_tweets, Unset):
            unique_tweets = UNSET
        else:
            unique_tweets = self.unique_tweets

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, XStockDetailResponseTrendType0):
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

        top_tweets: list[dict[str, Any]] | None | Unset
        if isinstance(self.top_tweets, Unset):
            top_tweets = UNSET
        elif isinstance(self.top_tweets, list):
            top_tweets = []
            for top_tweets_type_0_item_data in self.top_tweets:
                top_tweets_type_0_item = top_tweets_type_0_item_data.to_dict()
                top_tweets.append(top_tweets_type_0_item)

        else:
            top_tweets = self.top_tweets

        is_validated = self.is_validated

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if found is not UNSET:
            field_dict["found"] = found
        if buzz_score is not UNSET:
            field_dict["buzz_score"] = buzz_score
        if mentions is not UNSET:
            field_dict["mentions"] = mentions
        if total_mentions is not UNSET:
            field_dict["total_mentions"] = total_mentions
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
        if unique_tweets is not UNSET:
            field_dict["unique_tweets"] = unique_tweets
        if trend is not UNSET:
            field_dict["trend"] = trend
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if period_days is not UNSET:
            field_dict["period_days"] = period_days
        if daily_trend is not UNSET:
            field_dict["daily_trend"] = daily_trend
        if top_tweets is not UNSET:
            field_dict["top_tweets"] = top_tweets
        if is_validated is not UNSET:
            field_dict["is_validated"] = is_validated

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.x_daily_trend_item import XDailyTrendItem
        from ..models.x_top_tweet import XTopTweet

        d = dict(src_dict)
        ticker = d.pop("ticker")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        found = d.pop("found", UNSET)

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

        def _parse_total_mentions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_mentions = _parse_total_mentions(d.pop("total_mentions", UNSET))
        if isinstance(mentions, Unset):
            mentions = total_mentions
        if isinstance(total_mentions, Unset):
            total_mentions = mentions

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

        def _parse_unique_tweets(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_tweets = _parse_unique_tweets(d.pop("unique_tweets", UNSET))

        def _parse_trend(data: object) -> None | Unset | XStockDetailResponseTrendType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = XStockDetailResponseTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | XStockDetailResponseTrendType0, data)

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

        def _parse_daily_trend(data: object) -> list[XDailyTrendItem] | None | Unset:
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
                    daily_trend_type_0_item = XDailyTrendItem.from_dict(
                        daily_trend_type_0_item_data
                    )

                    daily_trend_type_0.append(daily_trend_type_0_item)

                return daily_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[XDailyTrendItem] | None | Unset, data)

        daily_trend = _parse_daily_trend(d.pop("daily_trend", UNSET))

        def _parse_top_tweets(data: object) -> list[XTopTweet] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                top_tweets_type_0 = []
                _top_tweets_type_0 = data
                for top_tweets_type_0_item_data in _top_tweets_type_0:
                    top_tweets_type_0_item = XTopTweet.from_dict(
                        top_tweets_type_0_item_data
                    )

                    top_tweets_type_0.append(top_tweets_type_0_item)

                return top_tweets_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[XTopTweet] | None | Unset, data)

        top_tweets = _parse_top_tweets(d.pop("top_tweets", UNSET))

        is_validated = d.pop("is_validated", UNSET)

        x_stock_detail_response = cls(
            ticker=ticker,
            company_name=company_name,
            found=found,
            buzz_score=buzz_score,
            mentions=mentions,
            total_mentions=total_mentions,
            sentiment_score=sentiment_score,
            positive_count=positive_count,
            negative_count=negative_count,
            neutral_count=neutral_count,
            total_upvotes=total_upvotes,
            unique_tweets=unique_tweets,
            trend=trend,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            period_days=period_days,
            daily_trend=daily_trend,
            top_tweets=top_tweets,
            is_validated=is_validated,
        )

        x_stock_detail_response.additional_properties = d
        return x_stock_detail_response

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
