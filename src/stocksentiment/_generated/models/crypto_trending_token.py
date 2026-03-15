from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.crypto_trending_token_trend import CryptoTrendingTokenTrend
from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoTrendingToken")


@_attrs_define
class CryptoTrendingToken:
    """Trending crypto token summary.

    Attributes:
        symbol (str): Token symbol
        buzz_score (float): Buzz score (0-100)
        trend (CryptoTrendingTokenTrend): 24h activity trend
        mentions (int): Explicit mention count
        unique_posts (int): Unique Reddit post count
        subreddit_count (int): Unique subreddit count
        sentiment_score (float): Average sentiment score
        bullish_pct (int): Bullish mention percentage
        bearish_pct (int): Bearish mention percentage
        total_upvotes (int): Total upvotes from explicit mentions
        name (None | str | Unset): Token name
        trend_history (list[float] | Unset): Daily buzz scores (oldest to newest), length max(days, 7).
    """

    symbol: str
    buzz_score: float
    trend: CryptoTrendingTokenTrend
    mentions: int
    unique_posts: int
    subreddit_count: int
    sentiment_score: float
    bullish_pct: int
    bearish_pct: int
    total_upvotes: int
    name: None | str | Unset = UNSET
    trend_history: list[float] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        buzz_score = self.buzz_score

        trend = self.trend.value

        mentions = self.mentions

        unique_posts = self.unique_posts

        subreddit_count = self.subreddit_count

        sentiment_score = self.sentiment_score

        bullish_pct = self.bullish_pct

        bearish_pct = self.bearish_pct

        total_upvotes = self.total_upvotes

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        trend_history: list[float] | Unset = UNSET
        if not isinstance(self.trend_history, Unset):
            trend_history = self.trend_history

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "buzz_score": buzz_score,
                "trend": trend,
                "mentions": mentions,
                "unique_posts": unique_posts,
                "subreddit_count": subreddit_count,
                "sentiment_score": sentiment_score,
                "bullish_pct": bullish_pct,
                "bearish_pct": bearish_pct,
                "total_upvotes": total_upvotes,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if trend_history is not UNSET:
            field_dict["trend_history"] = trend_history

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        buzz_score = d.pop("buzz_score")

        trend = CryptoTrendingTokenTrend(d.pop("trend"))

        mentions = d.pop("mentions")

        unique_posts = d.pop("unique_posts")

        subreddit_count = d.pop("subreddit_count")

        sentiment_score = d.pop("sentiment_score")

        bullish_pct = d.pop("bullish_pct")

        bearish_pct = d.pop("bearish_pct")

        total_upvotes = d.pop("total_upvotes")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        trend_history = cast(list[float], d.pop("trend_history", UNSET))

        crypto_trending_token = cls(
            symbol=symbol,
            buzz_score=buzz_score,
            trend=trend,
            mentions=mentions,
            unique_posts=unique_posts,
            subreddit_count=subreddit_count,
            sentiment_score=sentiment_score,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_upvotes=total_upvotes,
            name=name,
            trend_history=trend_history,
        )

        crypto_trending_token.additional_properties = d
        return crypto_trending_token

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
