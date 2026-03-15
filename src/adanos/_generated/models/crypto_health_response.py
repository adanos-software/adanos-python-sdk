from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.crypto_scheduler_status import CryptoSchedulerStatus


T = TypeVar("T", bound="CryptoHealthResponse")


@_attrs_define
class CryptoHealthResponse:
    """Health response for Reddit Crypto service.

    Attributes:
        status (str):
        service (None | str | Unset):
        version (None | str | Unset):
        total_mentions (int | Unset): Total rows in crypto_reddit_mentions Default: 0.
        tokens_tracked (int | Unset): Distinct symbols with mentions Default: 0.
        scheduler (CryptoSchedulerStatus | None | Unset):
        error (None | str | Unset):
    """

    status: str
    service: None | str | Unset = UNSET
    version: None | str | Unset = UNSET
    total_mentions: int | Unset = 0
    tokens_tracked: int | Unset = 0
    scheduler: CryptoSchedulerStatus | None | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.crypto_scheduler_status import CryptoSchedulerStatus

        status = self.status

        service: None | str | Unset
        if isinstance(self.service, Unset):
            service = UNSET
        else:
            service = self.service

        version: None | str | Unset
        if isinstance(self.version, Unset):
            version = UNSET
        else:
            version = self.version

        total_mentions = self.total_mentions

        tokens_tracked = self.tokens_tracked

        scheduler: dict[str, Any] | None | Unset
        if isinstance(self.scheduler, Unset):
            scheduler = UNSET
        elif isinstance(self.scheduler, CryptoSchedulerStatus):
            scheduler = self.scheduler.to_dict()
        else:
            scheduler = self.scheduler

        error: None | str | Unset
        if isinstance(self.error, Unset):
            error = UNSET
        else:
            error = self.error

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "status": status,
            }
        )
        if service is not UNSET:
            field_dict["service"] = service
        if version is not UNSET:
            field_dict["version"] = version
        if total_mentions is not UNSET:
            field_dict["total_mentions"] = total_mentions
        if tokens_tracked is not UNSET:
            field_dict["tokens_tracked"] = tokens_tracked
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.crypto_scheduler_status import CryptoSchedulerStatus

        d = dict(src_dict)
        status = d.pop("status")

        def _parse_service(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        service = _parse_service(d.pop("service", UNSET))

        def _parse_version(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        version = _parse_version(d.pop("version", UNSET))

        total_mentions = d.pop("total_mentions", UNSET)

        tokens_tracked = d.pop("tokens_tracked", UNSET)

        def _parse_scheduler(data: object) -> CryptoSchedulerStatus | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scheduler_type_0 = CryptoSchedulerStatus.from_dict(data)

                return scheduler_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(CryptoSchedulerStatus | None | Unset, data)

        scheduler = _parse_scheduler(d.pop("scheduler", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        crypto_health_response = cls(
            status=status,
            service=service,
            version=version,
            total_mentions=total_mentions,
            tokens_tracked=tokens_tracked,
            scheduler=scheduler,
            error=error,
        )

        crypto_health_response.additional_properties = d
        return crypto_health_response

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
