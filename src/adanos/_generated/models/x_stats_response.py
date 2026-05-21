from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XStatsResponse")


@_attrs_define
class XStatsResponse:
    """X/Twitter service statistics.

    Attributes:
        total_mentions (int | Unset): Total X mention rows in the database Default: 0.
        unique_tickers (int | Unset): Number of unique tickers with X mentions in the database Default: 0.
        mentions_today (int | Unset): X mention rows created since today's UTC midnight Default: 0.
        unique_tickers_today (int | Unset): Unique tickers with X mentions since today's UTC midnight Default: 0.
        supported_tickers (int | Unset): Total tickers in ticker_reference table Default: 0.
    """

    total_mentions: int | Unset = 0
    unique_tickers: int | Unset = 0
    mentions_today: int | Unset = 0
    unique_tickers_today: int | Unset = 0
    supported_tickers: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_mentions = self.total_mentions

        unique_tickers = self.unique_tickers

        mentions_today = self.mentions_today

        unique_tickers_today = self.unique_tickers_today

        supported_tickers = self.supported_tickers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_mentions is not UNSET:
            field_dict["total_mentions"] = total_mentions
        if unique_tickers is not UNSET:
            field_dict["unique_tickers"] = unique_tickers
        if mentions_today is not UNSET:
            field_dict["mentions_today"] = mentions_today
        if unique_tickers_today is not UNSET:
            field_dict["unique_tickers_today"] = unique_tickers_today
        if supported_tickers is not UNSET:
            field_dict["supported_tickers"] = supported_tickers

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_mentions = d.pop("total_mentions", UNSET)

        unique_tickers = d.pop("unique_tickers", UNSET)

        mentions_today = d.pop("mentions_today", UNSET)

        unique_tickers_today = d.pop("unique_tickers_today", UNSET)

        supported_tickers = d.pop("supported_tickers", UNSET)

        x_stats_response = cls(
            total_mentions=total_mentions,
            unique_tickers=unique_tickers,
            mentions_today=mentions_today,
            unique_tickers_today=unique_tickers_today,
            supported_tickers=supported_tickers,
        )

        x_stats_response.additional_properties = d
        return x_stats_response

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
