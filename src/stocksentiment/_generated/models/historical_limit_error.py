from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.historical_limit_error_detail import HistoricalLimitErrorDetail


T = TypeVar("T", bound="HistoricalLimitError")


@_attrs_define
class HistoricalLimitError:
    """Error response for historical data limit exceeded (HTTP 403).

    Attributes:
        detail (HistoricalLimitErrorDetail): Structured error detail for historical data limit exceeded.
    """

    detail: HistoricalLimitErrorDetail
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
        from ..models.historical_limit_error_detail import HistoricalLimitErrorDetail

        d = dict(src_dict)
        detail = HistoricalLimitErrorDetail.from_dict(d.pop("detail"))

        historical_limit_error = cls(
            detail=detail,
        )

        historical_limit_error.additional_properties = d
        return historical_limit_error

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
