from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.news_stock_sentiment_trend_type_0 import NewsStockSentimentTrendType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.daily_trend_item import DailyTrendItem
    from ..models.news_source_count import NewsSourceCount
    from ..models.news_top_mention import NewsTopMention


T = TypeVar("T", bound="NewsStockSentiment")


@_attrs_define
class NewsStockSentiment:
    """Detailed sentiment analysis for a specific stock ticker from news mentions.

    Attributes:
        ticker (str): Stock ticker symbol
        found (bool): Whether mentions were found for this ticker
        company_name (None | str | Unset): Company name from ticker_reference (null if not found)
        buzz_score (float | None | Unset): Buzz Score (0-100). Asymptotic scaling above 50.
        total_mentions (int | None | Unset): Total number of mentions
        sentiment_score (float | None | Unset): Average sentiment score (-1 bearish to +1 bullish)
        positive_count (int | None | Unset): Number of positive mentions
        negative_count (int | None | Unset): Number of negative mentions
        neutral_count (int | None | Unset): Number of neutral mentions
        source_count (int | None | Unset): Number of sources with mentions
        trend (NewsStockSentimentTrendType0 | None | Unset): Multi-factor activity trend using rolling 24h windows.
            Activity score = 60% mentions_ratio + 25% baseline_ratio + 15% source_ratio (baseline_ratio is fixed at 1.0
            because news has no upvote signal). rising: >1.10, falling: <0.90, stable: 0.90-1.10.
        bullish_pct (int | None | Unset): Percentage of bullish mentions
        bearish_pct (int | None | Unset): Percentage of bearish mentions
        period_days (int | None | Unset): Analysis period in days
        top_sources (list[NewsSourceCount] | None | Unset): Top sources by mention count
        daily_trend (list[DailyTrendItem] | None | Unset): Mentions per day with sentiment and buzz_score
        top_mentions (list[NewsTopMention] | None | Unset): Top mentions by recency
    """

    ticker: str
    found: bool
    company_name: None | str | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    total_mentions: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    positive_count: int | None | Unset = UNSET
    negative_count: int | None | Unset = UNSET
    neutral_count: int | None | Unset = UNSET
    source_count: int | None | Unset = UNSET
    trend: NewsStockSentimentTrendType0 | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    period_days: int | None | Unset = UNSET
    top_sources: list[NewsSourceCount] | None | Unset = UNSET
    daily_trend: list[DailyTrendItem] | None | Unset = UNSET
    top_mentions: list[NewsTopMention] | None | Unset = UNSET
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

        source_count: int | None | Unset
        if isinstance(self.source_count, Unset):
            source_count = UNSET
        else:
            source_count = self.source_count

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, NewsStockSentimentTrendType0):
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

        top_sources: list[dict[str, Any]] | None | Unset
        if isinstance(self.top_sources, Unset):
            top_sources = UNSET
        elif isinstance(self.top_sources, list):
            top_sources = []
            for top_sources_type_0_item_data in self.top_sources:
                top_sources_type_0_item = top_sources_type_0_item_data.to_dict()
                top_sources.append(top_sources_type_0_item)

        else:
            top_sources = self.top_sources

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
        if source_count is not UNSET:
            field_dict["source_count"] = source_count
        if trend is not UNSET:
            field_dict["trend"] = trend
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if period_days is not UNSET:
            field_dict["period_days"] = period_days
        if top_sources is not UNSET:
            field_dict["top_sources"] = top_sources
        if daily_trend is not UNSET:
            field_dict["daily_trend"] = daily_trend
        if top_mentions is not UNSET:
            field_dict["top_mentions"] = top_mentions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.daily_trend_item import DailyTrendItem
        from ..models.news_source_count import NewsSourceCount
        from ..models.news_top_mention import NewsTopMention

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

        def _parse_total_mentions(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        total_mentions = _parse_total_mentions(d.pop("total_mentions", UNSET))

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

        def _parse_source_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        source_count = _parse_source_count(d.pop("source_count", UNSET))

        def _parse_trend(data: object) -> NewsStockSentimentTrendType0 | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = NewsStockSentimentTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(NewsStockSentimentTrendType0 | None | Unset, data)

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

        def _parse_top_sources(data: object) -> list[NewsSourceCount] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                top_sources_type_0 = []
                _top_sources_type_0 = data
                for top_sources_type_0_item_data in _top_sources_type_0:
                    top_sources_type_0_item = NewsSourceCount.from_dict(
                        top_sources_type_0_item_data
                    )

                    top_sources_type_0.append(top_sources_type_0_item)

                return top_sources_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewsSourceCount] | None | Unset, data)

        top_sources = _parse_top_sources(d.pop("top_sources", UNSET))

        def _parse_daily_trend(data: object) -> list[DailyTrendItem] | None | Unset:
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
                    daily_trend_type_0_item = DailyTrendItem.from_dict(
                        daily_trend_type_0_item_data
                    )

                    daily_trend_type_0.append(daily_trend_type_0_item)

                return daily_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[DailyTrendItem] | None | Unset, data)

        daily_trend = _parse_daily_trend(d.pop("daily_trend", UNSET))

        def _parse_top_mentions(data: object) -> list[NewsTopMention] | None | Unset:
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
                    top_mentions_type_0_item = NewsTopMention.from_dict(
                        top_mentions_type_0_item_data
                    )

                    top_mentions_type_0.append(top_mentions_type_0_item)

                return top_mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[NewsTopMention] | None | Unset, data)

        top_mentions = _parse_top_mentions(d.pop("top_mentions", UNSET))

        news_stock_sentiment = cls(
            ticker=ticker,
            found=found,
            company_name=company_name,
            buzz_score=buzz_score,
            total_mentions=total_mentions,
            sentiment_score=sentiment_score,
            positive_count=positive_count,
            negative_count=negative_count,
            neutral_count=neutral_count,
            source_count=source_count,
            trend=trend,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            period_days=period_days,
            top_sources=top_sources,
            daily_trend=daily_trend,
            top_mentions=top_mentions,
        )

        news_stock_sentiment.additional_properties = d
        return news_stock_sentiment

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
