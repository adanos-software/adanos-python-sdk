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
        field (None | str | Unset): Invalid query parameter name
        value (int | None | str | Unset): Invalid query parameter value
        today (datetime.date | None | Unset): Current UTC date used for validation
        period_from (datetime.date | None | Unset): Resolved inclusive UTC start date
        period_to (datetime.date | None | Unset): Resolved inclusive UTC end date
        available_since (datetime.date | None | Unset): Earliest public data date for the platform
        retention_from (datetime.date | None | Unset): Earliest date retained for the endpoint
        requested_days (int | None | Unset): Number of days requested
        max_days (int | None | Unset): Maximum days accepted by the endpoint
        platform (None | str | Unset): Platform identifier
    """

    error: str
    message: str
    field: None | str | Unset = UNSET
    value: int | None | str | Unset = UNSET
    today: datetime.date | None | Unset = UNSET
    period_from: datetime.date | None | Unset = UNSET
    period_to: datetime.date | None | Unset = UNSET
    available_since: datetime.date | None | Unset = UNSET
    retention_from: datetime.date | None | Unset = UNSET
    requested_days: int | None | Unset = UNSET
    max_days: int | None | Unset = UNSET
    platform: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        field: None | str | Unset
        if isinstance(self.field, Unset):
            field = UNSET
        else:
            field = self.field

        value: int | None | str | Unset
        if isinstance(self.value, Unset):
            value = UNSET
        else:
            value = self.value

        today: None | str | Unset
        if isinstance(self.today, Unset):
            today = UNSET
        elif isinstance(self.today, datetime.date):
            today = self.today.isoformat()
        else:
            today = self.today

        period_from: None | str | Unset
        if isinstance(self.period_from, Unset):
            period_from = UNSET
        elif isinstance(self.period_from, datetime.date):
            period_from = self.period_from.isoformat()
        else:
            period_from = self.period_from

        period_to: None | str | Unset
        if isinstance(self.period_to, Unset):
            period_to = UNSET
        elif isinstance(self.period_to, datetime.date):
            period_to = self.period_to.isoformat()
        else:
            period_to = self.period_to

        available_since: None | str | Unset
        if isinstance(self.available_since, Unset):
            available_since = UNSET
        elif isinstance(self.available_since, datetime.date):
            available_since = self.available_since.isoformat()
        else:
            available_since = self.available_since

        retention_from: None | str | Unset
        if isinstance(self.retention_from, Unset):
            retention_from = UNSET
        elif isinstance(self.retention_from, datetime.date):
            retention_from = self.retention_from.isoformat()
        else:
            retention_from = self.retention_from

        requested_days: int | None | Unset
        if isinstance(self.requested_days, Unset):
            requested_days = UNSET
        else:
            requested_days = self.requested_days

        max_days: int | None | Unset
        if isinstance(self.max_days, Unset):
            max_days = UNSET
        else:
            max_days = self.max_days

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
        if field is not UNSET:
            field_dict["field"] = field
        if value is not UNSET:
            field_dict["value"] = value
        if today is not UNSET:
            field_dict["today"] = today
        if period_from is not UNSET:
            field_dict["period_from"] = period_from
        if period_to is not UNSET:
            field_dict["period_to"] = period_to
        if available_since is not UNSET:
            field_dict["available_since"] = available_since
        if retention_from is not UNSET:
            field_dict["retention_from"] = retention_from
        if requested_days is not UNSET:
            field_dict["requested_days"] = requested_days
        if max_days is not UNSET:
            field_dict["max_days"] = max_days
        if platform is not UNSET:
            field_dict["platform"] = platform

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        def _parse_field(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        field = _parse_field(d.pop("field", UNSET))

        def _parse_value(data: object) -> int | None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | str | Unset, data)

        value = _parse_value(d.pop("value", UNSET))

        def _parse_today(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                today_type_0 = datetime.date.fromisoformat(data)

                return today_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        today = _parse_today(d.pop("today", UNSET))

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

        def _parse_period_to(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                period_to_type_0 = datetime.date.fromisoformat(data)

                return period_to_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        period_to = _parse_period_to(d.pop("period_to", UNSET))

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

        def _parse_retention_from(data: object) -> datetime.date | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                retention_from_type_0 = datetime.date.fromisoformat(data)

                return retention_from_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.date | None | Unset, data)

        retention_from = _parse_retention_from(d.pop("retention_from", UNSET))

        def _parse_requested_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        requested_days = _parse_requested_days(d.pop("requested_days", UNSET))

        def _parse_max_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        max_days = _parse_max_days(d.pop("max_days", UNSET))

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
            field=field,
            value=value,
            today=today,
            period_from=period_from,
            period_to=period_to,
            available_since=available_since,
            retention_from=retention_from,
            requested_days=requested_days,
            max_days=max_days,
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
