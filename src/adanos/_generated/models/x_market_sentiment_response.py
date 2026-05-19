from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x_market_sentiment_response_trend_type_0 import XMarketSentimentResponseTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.x_market_sentiment_driver import XMarketSentimentDriver


T = TypeVar("T", bound="XMarketSentimentResponse")


@_attrs_define
class XMarketSentimentResponse:
    """Service-level X/Twitter market sentiment across all tracked stocks.

    Attributes:
        buzz_score (float): Service-wide X/Twitter heat score relative to the service's trailing 90-day baseline. Around
            50 = normal activity, higher values = hotter-than-usual X activity.
        mentions (int): Tweet mentions across the selected period
        unique_tweets (int): Best-effort distinct tweet count across the selected period
        unique_authors (int): Best-effort distinct author breadth across the selected period; falls back to a
            conservative floor when hybrid historical rollups are incomplete
        total_upvotes (int): Total likes across the selected period
        active_tickers (int): Number of tickers with X activity in the selected period
        positive_count (int): Positive tweet count across the selected period
        negative_count (int): Negative tweet count across the selected period
        neutral_count (int): Neutral tweet count across the selected period
        bullish_pct (int): Bullish tweet percentage
        bearish_pct (int): Bearish tweet percentage
        trend (None | Unset | XMarketSentimentResponseTrendType0): Service-level X activity trend over current 3 UTC
            days vs previous 3 UTC days using mentions, likes, and author breadth
        sentiment_score (float | None | Unset): Service-wide average tweet sentiment score
        trend_history (list[float] | Unset): Daily service-wide buzz scores (oldest→newest) using the same relative
            baseline calibration. Length = max(effective_days, 7), where effective_days reflects any platform availability
            clamp.
        drivers (list[XMarketSentimentDriver] | Unset): Top assets by current buzz_score driving the service-level
            reading
    """

    buzz_score: float
    mentions: int
    unique_tweets: int
    unique_authors: int
    total_upvotes: int
    active_tickers: int
    positive_count: int
    negative_count: int
    neutral_count: int
    bullish_pct: int
    bearish_pct: int
    trend: None | Unset | XMarketSentimentResponseTrendType0 = UNSET
    sentiment_score: float | None | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    drivers: list[XMarketSentimentDriver] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        mentions = self.mentions

        unique_tweets = self.unique_tweets

        unique_authors = self.unique_authors

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
        elif isinstance(self.trend, XMarketSentimentResponseTrendType0):
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
                "unique_tweets": unique_tweets,
                "unique_authors": unique_authors,
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
        from ..models.x_market_sentiment_driver import XMarketSentimentDriver

        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        mentions = d.pop("mentions")

        unique_tweets = d.pop("unique_tweets")

        unique_authors = d.pop("unique_authors")

        total_upvotes = d.pop("total_upvotes")

        active_tickers = d.pop("active_tickers")

        positive_count = d.pop("positive_count")

        negative_count = d.pop("negative_count")

        neutral_count = d.pop("neutral_count")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        def _parse_trend(data: object) -> None | Unset | XMarketSentimentResponseTrendType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = XMarketSentimentResponseTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | XMarketSentimentResponseTrendType0, data)

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
        drivers: list[XMarketSentimentDriver] | Unset = UNSET
        if _drivers is not UNSET:
            drivers = []
            for drivers_item_data in _drivers:
                drivers_item = XMarketSentimentDriver.from_dict(drivers_item_data)

                drivers.append(drivers_item)

        x_market_sentiment_response = cls(
            buzz_score=buzz_score,
            mentions=mentions,
            unique_tweets=unique_tweets,
            unique_authors=unique_authors,
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

        x_market_sentiment_response.additional_properties = d
        return x_market_sentiment_response

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
