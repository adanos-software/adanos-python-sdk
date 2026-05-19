from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XMarketSentimentDriver")


@_attrs_define
class XMarketSentimentDriver:
    """Top asset contributing to the service-level X market sentiment.

    Attributes:
        ticker (str): Stock ticker symbol
        mentions (int): Tweet mentions in the selected period
        buzz_score (float): Asset buzz score in the selected period
        sentiment_score (float | None | Unset): Average tweet sentiment score for this asset
    """

    ticker: str
    mentions: int
    buzz_score: float
    sentiment_score: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        mentions = self.mentions

        buzz_score = self.buzz_score

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "mentions": mentions,
                "buzz_score": buzz_score,
            }
        )
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        mentions = d.pop("mentions")

        buzz_score = d.pop("buzz_score")

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        x_market_sentiment_driver = cls(
            ticker=ticker,
            mentions=mentions,
            buzz_score=buzz_score,
            sentiment_score=sentiment_score,
        )

        x_market_sentiment_driver.additional_properties = d
        return x_market_sentiment_driver

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
