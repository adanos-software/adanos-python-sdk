from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="StatsResponse")


@_attrs_define
class StatsResponse:
    """Database statistics.

    Attributes:
        total_mentions (int): Total stock mentions in database
        unique_tickers (int): Number of unique tickers with mentions
        tickers (list[str]): List of ticker symbols (first 50)
        supported_tickers (int): Number of supported ticker patterns (from ticker_reference)
    """

    total_mentions: int
    unique_tickers: int
    tickers: list[str]
    supported_tickers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_mentions = self.total_mentions

        unique_tickers = self.unique_tickers

        tickers = self.tickers

        supported_tickers = self.supported_tickers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_mentions": total_mentions,
                "unique_tickers": unique_tickers,
                "tickers": tickers,
                "supported_tickers": supported_tickers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_mentions = d.pop("total_mentions")

        unique_tickers = d.pop("unique_tickers")

        tickers = cast(list[str], d.pop("tickers"))

        supported_tickers = d.pop("supported_tickers")

        stats_response = cls(
            total_mentions=total_mentions,
            unique_tickers=unique_tickers,
            tickers=tickers,
            supported_tickers=supported_tickers,
        )

        stats_response.additional_properties = d
        return stats_response

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
