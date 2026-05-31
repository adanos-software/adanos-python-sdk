from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="InvalidPeriodErrorDetail")


@_attrs_define
class InvalidPeriodErrorDetail:
    """Structured error detail for invalid period windows.

    Attributes:
        error (str): Error type identifier
        message (str): Human-readable error message
        period_from (datetime.date | None | Unset): Resolved inclusive UTC start date
        available_since (datetime.date | None | Unset): Earliest public data date for the platform
        platform (None | str | Unset): Platform identifier
    """

    error: str
    message: str
    period_from: datetime.date | None | Unset = UNSET
    available_since: datetime.date | None | Unset = UNSET
    platform: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        period_from: None | str | Unset
        if isinstance(self.period_from, Unset):
            period_from = UNSET
        elif isinstance(self.period_from, datetime.date):
            period_from = self.period_from.isoformat()
        else:
            period_from = self.period_from

        available_since: None | str | Unset
        if isinstance(self.available_since, Unset):
            available_since = UNSET
        elif isinstance(self.available_since, datetime.date):
            available_since = self.available_since.isoformat()
        else:
            available_since = self.available_since

        platform: None | str | Unset
        if isinstance(self.platform, Unset):
            platform = UNSET
        else:
            platform = self.platform

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
            }
        )
        if period_from is not UNSET:
            field_dict["period_from"] = period_from
        if available_since is not UNSET:
            field_dict["available_since"] = available_since
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        def _parse_period_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_from_type_0 = datetime.date.fromisoformat(data)

                return period_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_from = _parse_period_from(d.pop("period_from", UNSET))

        def _parse_available_since(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                available_since_type_0 = datetime.date.fromisoformat(data)

                return available_since_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        available_since = _parse_available_since(d.pop("available_since", UNSET))

        def _parse_platform(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        platform = _parse_platform(d.pop("platform", UNSET))

        invalid_period_error_detail = cls(
            error=error,
            message=message,
            period_from=period_from,
            available_since=available_since,
            platform=platform,
        )

        invalid_period_error_detail.additional_properties = d
        return invalid_period_error_detail

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
