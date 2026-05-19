from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="RootHealthSummary")


@_attrs_define
class RootHealthSummary:
    """Aggregated root health summary.

    Attributes:
        total (int): Number of platform health checks
        healthy (int): Number of checks that reported healthy
        unhealthy (int): Number of checks that reported unhealthy or timed out
        unhealthy_services (list[str]): Service identifiers that reported unhealthy or timed out
    """

    total: int
    healthy: int
    unhealthy: int
    unhealthy_services: list[str]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total = self.total

        healthy = self.healthy

        unhealthy = self.unhealthy

        unhealthy_services = self.unhealthy_services

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total": total,
                "healthy": healthy,
                "unhealthy": unhealthy,
                "unhealthy_services": unhealthy_services,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total = d.pop("total")

        healthy = d.pop("healthy")

        unhealthy = d.pop("unhealthy")

        unhealthy_services = cast(list[str], d.pop("unhealthy_services"))

        root_health_summary = cls(
            total=total,
            healthy=healthy,
            unhealthy=unhealthy,
            unhealthy_services=unhealthy_services,
        )

        root_health_summary.additional_properties = d
        return root_health_summary

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
