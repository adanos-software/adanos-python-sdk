from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.root_health_response_status import RootHealthResponseStatus
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.root_health_response_services import RootHealthResponseServices
    from ..models.root_health_summary import RootHealthSummary


T = TypeVar("T", bound="RootHealthResponse")


@_attrs_define
class RootHealthResponse:
    """Root API health status aggregated across platforms.

    Attributes:
        status (RootHealthResponseStatus): Aggregated root health status
        version (str): Service version
        summary (RootHealthSummary): Aggregated root health summary.
        services (RootHealthResponseServices): Per-platform health payloads keyed by service identifier
        service (str | Unset): Root service identifier Default: 'adanos-api'.
    """

    status: RootHealthResponseStatus
    version: str
    summary: RootHealthSummary
    services: RootHealthResponseServices
    service: str | Unset = "adanos-api"
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        status = self.status.value

        version = self.version

        summary = self.summary.to_dict()

        services = self.services.to_dict()

        service = self.service

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
                "version": version,
                "summary": summary,
                "services": services,
            }
        )
        if service is not UNSET:
            field_dict["service"] = service

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.root_health_response_services import RootHealthResponseServices
        from ..models.root_health_summary import RootHealthSummary

        d = dict(src_dict)
        status = RootHealthResponseStatus(d.pop("status"))

        version = d.pop("version")

        summary = RootHealthSummary.from_dict(d.pop("summary"))

        services = RootHealthResponseServices.from_dict(d.pop("services"))

        service = d.pop("service", UNSET)

        root_health_response = cls(
            status=status,
            version=version,
            summary=summary,
            services=services,
            service=service,
        )

        root_health_response.additional_properties = d
        return root_health_response

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
