from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StatsResponse")


@_attrs_define
class StatsResponse:
    """Database statistics.

    Attributes:
        total_mentions (int): Total stock mentions in database
        unique_tickers (int): Number of unique tickers with mentions
        supported_tickers (int): Number of supported ticker patterns (from ticker_reference)
        mentions_today (int | Unset): Mention rows created since today's UTC midnight Default: 0.
        unique_tickers_today (int | Unset): Unique tickers with mention rows since today's UTC midnight Default: 0.
        tickers (list[str] | Unset): List of ticker symbols (first 50)
    """

    total_mentions: int
    unique_tickers: int
    supported_tickers: int
    mentions_today: int | Unset = 0
    unique_tickers_today: int | Unset = 0
    tickers: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_mentions = self.total_mentions

        unique_tickers = self.unique_tickers

        supported_tickers = self.supported_tickers

        mentions_today = self.mentions_today

        unique_tickers_today = self.unique_tickers_today

        tickers: list[str] | Unset = UNSET
        if not isinstance(self.tickers, Unset):
            tickers = self.tickers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_mentions": total_mentions,
                "unique_tickers": unique_tickers,
                "supported_tickers": supported_tickers,
            }
        )
        if mentions_today is not UNSET:
            field_dict["mentions_today"] = mentions_today
        if unique_tickers_today is not UNSET:
            field_dict["unique_tickers_today"] = unique_tickers_today
        if tickers is not UNSET:
            field_dict["tickers"] = tickers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_mentions = d.pop("total_mentions")

        unique_tickers = d.pop("unique_tickers")

        supported_tickers = d.pop("supported_tickers")

        mentions_today = d.pop("mentions_today", UNSET)

        unique_tickers_today = d.pop("unique_tickers_today", UNSET)

        tickers = cast(list[str], d.pop("tickers", UNSET))

        stats_response = cls(
            total_mentions=total_mentions,
            unique_tickers=unique_tickers,
            supported_tickers=supported_tickers,
            mentions_today=mentions_today,
            unique_tickers_today=unique_tickers_today,
            tickers=tickers,
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
