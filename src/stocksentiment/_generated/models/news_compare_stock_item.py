from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="NewsCompareStockItem")


@_attrs_define
class NewsCompareStockItem:
    """Individual stock in news comparison.

    Attributes:
        ticker (str): Stock ticker symbol
        buzz_score (float): Buzz Score (0-100). Asymptotic scaling above 50.
        mentions (int): Total mentions in period
        source_count (int): Number of distinct news sources with mentions in period
        company_name (None | str | Unset): Company name from ticker_reference
        sentiment (float | None | Unset): Average sentiment (-1 to +1, null if no mentions)
    """

    ticker: str
    buzz_score: float
    mentions: int
    source_count: int
    company_name: None | str | Unset = UNSET
    sentiment: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        buzz_score = self.buzz_score

        mentions = self.mentions

        source_count = self.source_count

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        sentiment: float | None | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "buzz_score": buzz_score,
                "mentions": mentions,
                "source_count": source_count,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        buzz_score = d.pop("buzz_score")

        mentions = d.pop("mentions")

        source_count = d.pop("source_count")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_sentiment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        news_compare_stock_item = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            mentions=mentions,
            source_count=source_count,
            company_name=company_name,
            sentiment=sentiment,
        )

        news_compare_stock_item.additional_properties = d
        return news_compare_stock_item

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
