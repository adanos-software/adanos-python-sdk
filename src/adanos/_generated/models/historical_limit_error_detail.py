from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="HistoricalLimitErrorDetail")


@_attrs_define
class HistoricalLimitErrorDetail:
    """Structured error detail for historical data limit exceeded.

    Attributes:
        error (str): Error type identifier
        message (str): Human-readable error message
        requested_days (int): Number of days requested
        max_days (int): Maximum days allowed for account tier
        account_type (str): User's account type (free, hobby, professional, premium)
    """

    error: str
    message: str
    requested_days: int
    max_days: int
    account_type: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        requested_days = self.requested_days

        max_days = self.max_days

        account_type = self.account_type

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "requested_days": requested_days,
                "max_days": max_days,
                "account_type": account_type,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        requested_days = d.pop("requested_days")

        max_days = d.pop("max_days")

        account_type = d.pop("account_type")

        historical_limit_error_detail = cls(
            error=error,
            message=message,
            requested_days=requested_days,
            max_days=max_days,
            account_type=account_type,
        )

        historical_limit_error_detail.additional_properties = d
        return historical_limit_error_detail

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
