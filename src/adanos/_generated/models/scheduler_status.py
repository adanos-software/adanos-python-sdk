from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SchedulerStatus")


@_attrs_define
class SchedulerStatus:
    """Scheduler status information.

    Attributes:
        running (bool): Whether worker is alive (based on heartbeat freshness)
        last_scrape (None | str | Unset): ISO timestamp of last scrape (null if never run)
        scrape_count (int | Unset): Total number of scrapes performed Default: 0.
        error_count (int | Unset): Total number of scrape errors/failures Default: 0.
        success_rate (float | None | Unset): Scrape success rate (0.0-1.0)
        note (None | str | Unset): Additional info (e.g., worker heartbeat status)
    """

    running: bool
    last_scrape: None | str | Unset = UNSET
    scrape_count: int | Unset = 0
    error_count: int | Unset = 0
    success_rate: float | None | Unset = UNSET
    note: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        running = self.running

        last_scrape: None | str | Unset
        if isinstance(self.last_scrape, Unset):
            last_scrape = UNSET
        else:
            last_scrape = self.last_scrape

        scrape_count = self.scrape_count

        error_count = self.error_count

        success_rate: float | None | Unset
        if isinstance(self.success_rate, Unset):
            success_rate = UNSET
        else:
            success_rate = self.success_rate

        note: None | str | Unset
        if isinstance(self.note, Unset):
            note = UNSET
        else:
            note = self.note

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "running": running,
            }
        )
        if last_scrape is not UNSET:
            field_dict["last_scrape"] = last_scrape
        if scrape_count is not UNSET:
            field_dict["scrape_count"] = scrape_count
        if error_count is not UNSET:
            field_dict["error_count"] = error_count
        if success_rate is not UNSET:
            field_dict["success_rate"] = success_rate
        if note is not UNSET:
            field_dict["note"] = note

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        running = d.pop("running")

        def _parse_last_scrape(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        last_scrape = _parse_last_scrape(d.pop("last_scrape", UNSET))

        scrape_count = d.pop("scrape_count", UNSET)

        error_count = d.pop("error_count", UNSET)

        def _parse_success_rate(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        success_rate = _parse_success_rate(d.pop("success_rate", UNSET))

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        scheduler_status = cls(
            running=running,
            last_scrape=last_scrape,
            scrape_count=scrape_count,
            error_count=error_count,
            success_rate=success_rate,
            note=note,
        )

        scheduler_status.additional_properties = d
        return scheduler_status

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
