from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymarket_scheduler_status import PolymarketSchedulerStatus


T = TypeVar("T", bound="PolymarketHealthResponse")


@_attrs_define
class PolymarketHealthResponse:
    """Polymarket health response.

    Attributes:
        status (str): Current health status
        service (str): Service identifier
        version (str): API version
        total_mentions (int): Total rows in polymarket_mentions
        tickers_tracked (int): Distinct tracked tickers
        scheduler (None | PolymarketSchedulerStatus | Unset): Polymarket worker status
        error (None | str | Unset): Error message when unhealthy
    """

    status: str
    service: str
    version: str
    total_mentions: int
    tickers_tracked: int
    scheduler: None | PolymarketSchedulerStatus | Unset = UNSET
    error: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.polymarket_scheduler_status import PolymarketSchedulerStatus

        status = self.status

        service = self.service

        version = self.version

        total_mentions = self.total_mentions

        tickers_tracked = self.tickers_tracked

        scheduler: dict[str, Any] | None | Unset
        if isinstance(self.scheduler, Unset):
            scheduler = UNSET
        elif isinstance(self.scheduler, PolymarketSchedulerStatus):
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
                "service": service,
                "version": version,
                "total_mentions": total_mentions,
                "tickers_tracked": tickers_tracked,
            }
        )
        if scheduler is not UNSET:
            field_dict["scheduler"] = scheduler
        if error is not UNSET:
            field_dict["error"] = error

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymarket_scheduler_status import PolymarketSchedulerStatus

        d = dict(src_dict)
        status = d.pop("status")

        service = d.pop("service")

        version = d.pop("version")

        total_mentions = d.pop("total_mentions")

        tickers_tracked = d.pop("tickers_tracked")

        def _parse_scheduler(data: object) -> None | PolymarketSchedulerStatus | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                scheduler_type_0 = PolymarketSchedulerStatus.from_dict(data)

                return scheduler_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolymarketSchedulerStatus | Unset, data)

        scheduler = _parse_scheduler(d.pop("scheduler", UNSET))

        def _parse_error(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        error = _parse_error(d.pop("error", UNSET))

        polymarket_health_response = cls(
            status=status,
            service=service,
            version=version,
            total_mentions=total_mentions,
            tickers_tracked=tickers_tracked,
            scheduler=scheduler,
            error=error,
        )

        polymarket_health_response.additional_properties = d
        return polymarket_health_response

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
