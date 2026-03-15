from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="XSchedulerStatus")


@_attrs_define
class XSchedulerStatus:
    """X Worker scheduler/scraper status (from worker_heartbeat table).

    Attributes:
        running (bool): Whether worker is alive (heartbeat < 90 min old)
        last_scrape (None | str | Unset): ISO timestamp of last completed scrape cycle
        scrape_count (int | Unset): Total completed scrape cycles since worker start Default: 0.
        error_count (int | Unset): Total failed scrape cycles Default: 0.
        success_rate (float | Unset): Success rate (success_count / scrape_count) Default: 0.0.
        note (None | str | Unset): Additional status info (e.g., worker crash warning)
    """

    running: bool
    last_scrape: None | str | Unset = UNSET
    scrape_count: int | Unset = 0
    error_count: int | Unset = 0
    success_rate: float | Unset = 0.0
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

        success_rate = d.pop("success_rate", UNSET)

        def _parse_note(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        note = _parse_note(d.pop("note", UNSET))

        x_scheduler_status = cls(
            running=running,
            last_scrape=last_scrape,
            scrape_count=scrape_count,
            error_count=error_count,
            success_rate=success_rate,
            note=note,
        )

        x_scheduler_status.additional_properties = d
        return x_scheduler_status

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
