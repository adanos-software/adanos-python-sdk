from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoCompareTokenItem")


@_attrs_define
class CryptoCompareTokenItem:
    """Individual crypto token in a compare response.

    Attributes:
        symbol (str):
        buzz_score (float):
        mentions (int):
        upvotes (int):
        name (None | str | Unset):
        sentiment (float | None | Unset):
    """

    symbol: str
    buzz_score: float
    mentions: int
    upvotes: int
    name: None | str | Unset = UNSET
    sentiment: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        buzz_score = self.buzz_score

        mentions = self.mentions

        upvotes = self.upvotes

        name: None | str | Unset
        if isinstance(self.name, Unset):
            name = UNSET
        else:
            name = self.name

        sentiment: float | None | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "buzz_score": buzz_score,
                "mentions": mentions,
                "upvotes": upvotes,
            }
        )
        if name is not UNSET:
            field_dict["name"] = name
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        buzz_score = d.pop("buzz_score")

        mentions = d.pop("mentions")

        upvotes = d.pop("upvotes")

        def _parse_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        name = _parse_name(d.pop("name", UNSET))

        def _parse_sentiment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        crypto_compare_token_item = cls(
            symbol=symbol,
            buzz_score=buzz_score,
            mentions=mentions,
            upvotes=upvotes,
            name=name,
            sentiment=sentiment,
        )

        crypto_compare_token_item.additional_properties = d
        return crypto_compare_token_item

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
