from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="XStatsResponse")


@_attrs_define
class XStatsResponse:
    """X/Twitter service statistics.

    Attributes:
        total_appearances (int | Unset): Total appearances across all X trending fetches (all time) Default: 0.
        unique_tickers (int | Unset): Number of unique tickers in latest fetch Default: 0.
        tickers (list[str] | Unset): List of trending ticker symbols (first 100)
        supported_tickers (int | Unset): Total tickers in ticker_reference table Default: 0.
        last_fetch (datetime.datetime | None | Unset): Timestamp of last Grok fetch
        validation_rate (float | Unset): Percentage of tickers also on Reddit Default: 0.0.
    """

    total_appearances: int | Unset = 0
    unique_tickers: int | Unset = 0
    tickers: list[str] | Unset = UNSET
    supported_tickers: int | Unset = 0
    last_fetch: datetime.datetime | None | Unset = UNSET
    validation_rate: float | Unset = 0.0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_appearances = self.total_appearances

        unique_tickers = self.unique_tickers

        tickers: list[str] | Unset = UNSET
        if not isinstance(self.tickers, Unset):
            tickers = self.tickers

        supported_tickers = self.supported_tickers

        last_fetch: None | str | Unset
        if isinstance(self.last_fetch, Unset):
            last_fetch = UNSET
        elif isinstance(self.last_fetch, datetime.datetime):
            last_fetch = self.last_fetch.isoformat()
        else:
            last_fetch = self.last_fetch

        validation_rate = self.validation_rate

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if total_appearances is not UNSET:
            field_dict["total_appearances"] = total_appearances
        if unique_tickers is not UNSET:
            field_dict["unique_tickers"] = unique_tickers
        if tickers is not UNSET:
            field_dict["tickers"] = tickers
        if supported_tickers is not UNSET:
            field_dict["supported_tickers"] = supported_tickers
        if last_fetch is not UNSET:
            field_dict["last_fetch"] = last_fetch
        if validation_rate is not UNSET:
            field_dict["validation_rate"] = validation_rate

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_appearances = d.pop("total_appearances", UNSET)

        unique_tickers = d.pop("unique_tickers", UNSET)

        tickers = cast(list[str], d.pop("tickers", UNSET))

        supported_tickers = d.pop("supported_tickers", UNSET)

        def _parse_last_fetch(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                last_fetch_type_0 = isoparse(data)

                return last_fetch_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        last_fetch = _parse_last_fetch(d.pop("last_fetch", UNSET))

        validation_rate = d.pop("validation_rate", UNSET)

        x_stats_response = cls(
            total_appearances=total_appearances,
            unique_tickers=unique_tickers,
            tickers=tickers,
            supported_tickers=supported_tickers,
            last_fetch=last_fetch,
            validation_rate=validation_rate,
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
