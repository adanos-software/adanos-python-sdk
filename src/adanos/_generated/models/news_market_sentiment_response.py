from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.news_market_sentiment_response_trend_type_0 import NewsMarketSentimentResponseTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.news_market_sentiment_driver import NewsMarketSentimentDriver


T = TypeVar("T", bound="NewsMarketSentimentResponse")


@_attrs_define
class NewsMarketSentimentResponse:
    """Service-level News market sentiment across all tracked stocks.

    Attributes:
        buzz_score (float): Service-wide News heat score relative to the service's trailing 90-day baseline. Around 50 =
            normal coverage heat, higher values = hotter-than-usual coverage.
        mentions (int): News mentions across the selected period
        unique_articles (int): Best-effort distinct article count across the selected period
        source_count (int): Distinct news sources contributing in the selected period
        active_tickers (int): Number of tickers with news activity in the selected period
        positive_count (int): Positive news mention count
        negative_count (int): Negative news mention count
        neutral_count (int): Neutral news mention count
        bullish_pct (int): Bullish news mention percentage
        bearish_pct (int): Bearish news mention percentage
        trend (NewsMarketSentimentResponseTrendType0 | None | Unset): Service-level News activity trend over current 3
            UTC days vs previous 3 UTC days using mentions/articles and source breadth
        sentiment_score (float | None | Unset): Service-wide average news sentiment score
        trend_history (list[float] | Unset): Daily service-wide buzz scores (oldest→newest) using the same relative
            baseline calibration. Length = max(effective_days, 7), where effective_days reflects any platform availability
            clamp.
        drivers (list[NewsMarketSentimentDriver] | Unset): Top assets by current buzz_score driving the service-level
            reading
    """

    buzz_score: float
    mentions: int
    unique_articles: int
    source_count: int
    active_tickers: int
    positive_count: int
    negative_count: int
    neutral_count: int
    bullish_pct: int
    bearish_pct: int
    trend: NewsMarketSentimentResponseTrendType0 | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    drivers: list[NewsMarketSentimentDriver] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        buzz_score = self.buzz_score

        mentions = self.mentions

        unique_articles = self.unique_articles

        source_count = self.source_count

        active_tickers = self.active_tickers

        positive_count = self.positive_count

        negative_count = self.negative_count

        neutral_count = self.neutral_count

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, NewsMarketSentimentResponseTrendType0):
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
                "unique_articles": unique_articles,
                "source_count": source_count,
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
        from ..models.news_market_sentiment_driver import NewsMarketSentimentDriver

        d = dict(src_dict)
        buzz_score = d.pop("buzz_score")

        mentions = d.pop("mentions")

        unique_articles = d.pop("unique_articles")

        source_count = d.pop("source_count")

        active_tickers = d.pop("active_tickers")

        positive_count = d.pop("positive_count")

        negative_count = d.pop("negative_count")

        neutral_count = d.pop("neutral_count")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        def _parse_trend(data: object) -> NewsMarketSentimentResponseTrendType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = NewsMarketSentimentResponseTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewsMarketSentimentResponseTrendType0 | None | Unset, data)

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
        drivers: list[NewsMarketSentimentDriver] | Unset = UNSET
        if _drivers is not UNSET:
            drivers = []
            for drivers_item_data in _drivers:
                drivers_item = NewsMarketSentimentDriver.from_dict(drivers_item_data)

                drivers.append(drivers_item)

        news_market_sentiment_response = cls(
            buzz_score=buzz_score,
            mentions=mentions,
            unique_articles=unique_articles,
            source_count=source_count,
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

        news_market_sentiment_response.additional_properties = d
        return news_market_sentiment_response

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
