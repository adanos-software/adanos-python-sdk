from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.crypto_raw_mention_item import CryptoRawMentionItem


T = TypeVar("T", bound="CryptoRawMentionsResponse")


@_attrs_define
class CryptoRawMentionsResponse:
    """Paginated raw Reddit crypto mentions for a single symbol.

    Attributes:
        symbol (str): Crypto symbol
        period_days (int): Lookback window used for the query
        count (int): Total number of matching results before limit and offset are applied; only the requested page is
            returned
        results (list[CryptoRawMentionItem]): Raw mention rows ordered by newest first
    """

    symbol: str
    period_days: int
    count: int
    results: list[CryptoRawMentionItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        period_days = self.period_days

        count = self.count

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "period_days": period_days,
                "count": count,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crypto_raw_mention_item import CryptoRawMentionItem

        d = dict(src_dict)
        symbol = d.pop("symbol")

        period_days = d.pop("period_days")

        count = d.pop("count")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = CryptoRawMentionItem.from_dict(results_item_data)

            results.append(results_item)

        crypto_raw_mentions_response = cls(
            symbol=symbol,
            period_days=period_days,
            count=count,
            results=results,
        )

        crypto_raw_mentions_response.additional_properties = d
        return crypto_raw_mentions_response

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
