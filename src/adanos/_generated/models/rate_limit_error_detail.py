from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="RateLimitErrorDetail")


@_attrs_define
class RateLimitErrorDetail:
    """Structured rate-limit error detail.

    Attributes:
        error (str): Error type identifier
        message (str): Human-readable error message
        account_type (str): Resolved account type or fallback tier
        limit (int | None | Unset): Applied request limit for the window
        used (int | None | Unset): Requests used in the current window
    """

    error: str
    message: str
    account_type: str
    limit: int | None | Unset = UNSET
    used: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        account_type = self.account_type

        limit: int | None | Unset
        if isinstance(self.limit, Unset):
            limit = UNSET
        else:
            limit = self.limit

        used: int | None | Unset
        if isinstance(self.used, Unset):
            used = UNSET
        else:
            used = self.used

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "account_type": account_type,
            }
        )
        if limit is not UNSET:
            field_dict["limit"] = limit
        if used is not UNSET:
            field_dict["used"] = used

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        account_type = d.pop("account_type")

        def _parse_limit(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        limit = _parse_limit(d.pop("limit", UNSET))

        def _parse_used(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        used = _parse_used(d.pop("used", UNSET))

        rate_limit_error_detail = cls(
            error=error,
            message=message,
            account_type=account_type,
            limit=limit,
            used=used,
        )

        rate_limit_error_detail.additional_properties = d
        return rate_limit_error_detail

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
