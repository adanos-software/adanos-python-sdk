from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.x_compare_stock_item_trend_type_0 import XCompareStockItemTrendType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="XCompareStockItem")


@_attrs_define
class XCompareStockItem:
    """Individual stock in X/Twitter comparison.

    Attributes:
        ticker (str): Stock ticker symbol
        buzz_score (float): Aggregated Buzz Score (0-100) from X mentions
        mentions (int): Total tweet mentions
        unique_tweets (int): Number of unique tweets mentioning this ticker (distinct tweet_id)
        total_upvotes (int): Total likes across all tweet mentions
        company_name (None | str | Unset): Company name from ticker_reference
        trend (None | Unset | XCompareStockItemTrendType0): X activity/attention trend over current 3 UTC days vs
            previous 3 UTC days using mentions, likes, and author breadth. Null when no qualifying X data exists.
        sentiment_score (float | None | Unset): Average sentiment score from tweet analysis (-1 to +1)
        bullish_pct (int | None | Unset): Percentage of bullish tweet mentions
        bearish_pct (int | None | Unset): Percentage of bearish tweet mentions
        trend_history (list[float] | Unset): Daily buzz history (oldest to newest). Length = max(days, 7) when data
            exists. Earlier values represent completed UTC calendar days; the final value is today's current live
            buzz_score. Empty when no qualifying data exists.
    """

    ticker: str
    buzz_score: float
    mentions: int
    unique_tweets: int
    total_upvotes: int
    company_name: None | str | Unset = UNSET
    trend: None | Unset | XCompareStockItemTrendType0 = UNSET
    sentiment_score: float | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        buzz_score = self.buzz_score

        mentions = self.mentions

        unique_tweets = self.unique_tweets

        total_upvotes = self.total_upvotes

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, XCompareStockItemTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

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

        trend_history: list[float] | Unset = UNSET
        if not isinstance(self.trend_history, Unset):
            trend_history = self.trend_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "buzz_score": buzz_score,
                "mentions": mentions,
                "unique_tweets": unique_tweets,
                "total_upvotes": total_upvotes,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if trend is not UNSET:
            field_dict["trend"] = trend
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        buzz_score = d.pop("buzz_score")

        mentions = d.pop("mentions")

        unique_tweets = d.pop("unique_tweets")

        total_upvotes = d.pop("total_upvotes")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_trend(data: object) -> None | Unset | XCompareStockItemTrendType0:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = XCompareStockItemTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | Unset | XCompareStockItemTrendType0, data)

        trend = _parse_trend(d.pop("trend", UNSET))

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

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        x_compare_stock_item = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            mentions=mentions,
            unique_tweets=unique_tweets,
            total_upvotes=total_upvotes,
            company_name=company_name,
            trend=trend,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            trend_history=trend_history,
        )

        x_compare_stock_item.additional_properties = d
        return x_compare_stock_item

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
