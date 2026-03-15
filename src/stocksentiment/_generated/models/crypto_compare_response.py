from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.crypto_compare_token_item import CryptoCompareTokenItem


T = TypeVar("T", bound="CryptoCompareResponse")


@_attrs_define
class CryptoCompareResponse:
    """Comparison response for multiple crypto symbols.

    Attributes:
        period_days (int):
        tokens (list[CryptoCompareTokenItem]):
    """

    period_days: int
    tokens: list[CryptoCompareTokenItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_days = self.period_days

        tokens = []
        for tokens_item_data in self.tokens:
            tokens_item = tokens_item_data.to_dict()
            tokens.append(tokens_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period_days": period_days,
                "tokens": tokens,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crypto_compare_token_item import CryptoCompareTokenItem

        d = dict(src_dict)
        period_days = d.pop("period_days")

        tokens = []
        _tokens = d.pop("tokens")
        for tokens_item_data in _tokens:
            tokens_item = CryptoCompareTokenItem.from_dict(tokens_item_data)

            tokens.append(tokens_item)

        crypto_compare_response = cls(
            period_days=period_days,
            tokens=tokens,
        )

        crypto_compare_response.additional_properties = d
        return crypto_compare_response

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
