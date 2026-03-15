from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CryptoStatsResponse")


@_attrs_define
class CryptoStatsResponse:
    """High-level crypto dataset statistics.

    Attributes:
        total_mentions (int):
        unique_tokens (int):
        tokens (list[str]): List of symbols (first 50)
        supported_tokens (int):
    """

    total_mentions: int
    unique_tokens: int
    tokens: list[str]
    supported_tokens: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_mentions = self.total_mentions

        unique_tokens = self.unique_tokens

        tokens = self.tokens

        supported_tokens = self.supported_tokens

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_mentions": total_mentions,
                "unique_tokens": unique_tokens,
                "tokens": tokens,
                "supported_tokens": supported_tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_mentions = d.pop("total_mentions")

        unique_tokens = d.pop("unique_tokens")

        tokens = cast(list[str], d.pop("tokens"))

        supported_tokens = d.pop("supported_tokens")

        crypto_stats_response = cls(
            total_mentions=total_mentions,
            unique_tokens=unique_tokens,
            tokens=tokens,
            supported_tokens=supported_tokens,
        )

        crypto_stats_response.additional_properties = d
        return crypto_stats_response

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
