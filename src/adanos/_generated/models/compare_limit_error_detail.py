from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CompareLimitErrorDetail")


@_attrs_define
class CompareLimitErrorDetail:
    """Structured error detail for compare item-count violations.

    Attributes:
        error (str): Machine-readable error code
        message (str): Human-readable error message
        max_items (int): Maximum accepted compare items
        item_name (str): Compared item type, such as ticker or symbol
    """

    error: str
    message: str
    max_items: int
    item_name: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        error = self.error

        message = self.message

        max_items = self.max_items

        item_name = self.item_name

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "error": error,
                "message": message,
                "max_items": max_items,
                "item_name": item_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        error = d.pop("error")

        message = d.pop("message")

        max_items = d.pop("max_items")

        item_name = d.pop("item_name")

        compare_limit_error_detail = cls(
            error=error,
            message=message,
            max_items=max_items,
            item_name=item_name,
        )

        compare_limit_error_detail.additional_properties = d
        return compare_limit_error_detail

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
