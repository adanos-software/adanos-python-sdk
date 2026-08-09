from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.compare_limit_error_detail import CompareLimitErrorDetail


T = TypeVar("T", bound="CompareLimitError")


@_attrs_define
class CompareLimitError:
    """Error response for compare item-count violations (HTTP 400).

    Attributes:
        detail (CompareLimitErrorDetail): Structured error detail for compare item-count violations.
    """

    detail: CompareLimitErrorDetail
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        detail = self.detail.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "detail": detail,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.compare_limit_error_detail import CompareLimitErrorDetail

        d = dict(src_dict)
        detail = CompareLimitErrorDetail.from_dict(d.pop("detail"))

        compare_limit_error = cls(
            detail=detail,
        )

        compare_limit_error.additional_properties = d
        return compare_limit_error

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
