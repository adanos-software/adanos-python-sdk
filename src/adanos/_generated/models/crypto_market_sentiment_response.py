from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crypto_market_sentiment_response_trend_type_0 import CryptoMarketSentimentResponseTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crypto_market_sentiment_driver import CryptoMarketSentimentDriver


T = TypeVar("T", bound="CryptoMarketSentimentResponse")


@_attrs_define
class CryptoMarketSentimentResponse:
    """Service-level Reddit Crypto market sentiment across all tracked assets.

    Attributes:
        buzz_score (float): Service-wide Reddit Crypto heat score relative to the trailing 90-day baseline for the
            selected period
        mentions (int): Total Reddit mentions across the selected period, including inherited thread-context mentions
        unique_posts (int): Best-effort unique Reddit post count across the selected period
        subreddit_count (int): Distinct subreddits contributing in the selected period
        total_upvotes (int): Total upvotes across explicit mentions in the selected period
        active_tickers (int): Number of crypto symbols with activity in the selected period
        positive_count (int): Positive mention count across the selected period
        negative_count (int): Negative mention count across the selected period
        neutral_count (int): Neutral mention count across the selected period
        bullish_pct (int): Bullish mention percentage
        bearish_pct (int): Bearish mention percentage
        trend (CryptoMarketSentimentResponseTrendType0 | None | Unset): Service-level activity trend over current 3 UTC
            days vs previous 3 UTC days using mentions, upvotes, and subreddit breadth
        sentiment_score (float | None | Unset): Service-wide average sentiment score across the selected period
        trend_history (list[float] | Unset): Daily service-wide Reddit Crypto heat scores (oldest→newest), each
            calibrated relative to the trailing 90-day baseline. Length = max(effective_days, 7), where effective_days
            reflects any platform availability clamp.
        drivers (list[CryptoMarketSentimentDriver] | Unset): Top assets by current buzz_score driving the service-level
            reading
    """

    buzz_score: float
    mentions: int
    unique_posts: int
    subreddit_count: int
    total_upvotes: int
    active_tickers: int
    positive_count: int
    negative_count: int
    neutral_count: int
    bullish_pct: int
    bearish_pct: int
    trend: CryptoMarketSentimentResponseTrendType0 | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    drivers: list[CryptoMarketSentimentDriver] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        mentions = self.mentions

        unique_posts = self.unique_posts

        subreddit_count = self.subreddit_count

        total_upvotes = self.total_upvotes

        active_tickers = self.active_tickers

        positive_count = self.positive_count

        negative_count = self.negative_count

        neutral_count = self.neutral_count

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, CryptoMarketSentimentResponseTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        trend_history: list[float] | Unset = UNSET
        if not isinstance(self.trend_history, Unset):
            trend_history = self.trend_history

        drivers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.drivers, Unset):
            drivers = []
            for drivers_item_data in self.drivers:
                drivers_item = drivers_item_data.to_dict()
                drivers.append(drivers_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "buzz_score": buzz_score,
                "mentions": mentions,
                "unique_posts": unique_posts,
                "subreddit_count": subreddit_count,
                "total_upvotes": total_upvotes,
                "active_tickers": active_tickers,
                "positive_count": positive_count,
                "negative_count": negative_count,
                "neutral_count": neutral_count,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
            }
        )
        if trend is not UNSET:
            field_dict["trend"] = trend
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history
        if drivers is not UNSET:
            field_dict["drivers"] = drivers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crypto_market_sentiment_driver import CryptoMarketSentimentDriver

        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        mentions = d.pop("mentions")

        unique_posts = d.pop("unique_posts")

        subreddit_count = d.pop("subreddit_count")

        total_upvotes = d.pop("total_upvotes")

        active_tickers = d.pop("active_tickers")

        positive_count = d.pop("positive_count")

        negative_count = d.pop("negative_count")

        neutral_count = d.pop("neutral_count")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        def _parse_trend(data: object) -> CryptoMarketSentimentResponseTrendType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = CryptoMarketSentimentResponseTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CryptoMarketSentimentResponseTrendType0 | None | Unset, data)

        trend = _parse_trend(d.pop("trend", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        _drivers = d.pop("drivers", UNSET)
        drivers: list[CryptoMarketSentimentDriver] | Unset = UNSET
        if _drivers is not UNSET:
            drivers = []
            for drivers_item_data in _drivers:
                drivers_item = CryptoMarketSentimentDriver.from_dict(drivers_item_data)

                drivers.append(drivers_item)

        crypto_market_sentiment_response = cls(
            buzz_score=buzz_score,
            mentions=mentions,
            unique_posts=unique_posts,
            subreddit_count=subreddit_count,
            total_upvotes=total_upvotes,
            active_tickers=active_tickers,
            positive_count=positive_count,
            negative_count=negative_count,
            neutral_count=neutral_count,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            trend=trend,
            sentiment_score=sentiment_score,
            trend_history=trend_history,
            drivers=drivers,
        )

        crypto_market_sentiment_response.additional_properties = d
        return crypto_market_sentiment_response

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
