from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketPulseEvidence")


@_attrs_define
class PolymarketPulseEvidence:
    """Compact data-quality evidence for the ticker-level Polymarket pulse.

    Attributes:
        directional_coverage (float | None | Unset): Share of current open snapshot markets with outcome-aware
            directional evidence
        traded_market_pct (float | None | Unset): Share of current open snapshot markets with trades in the latest UTC
            day
        zero_trade_market_pct (float | None | Unset): Share of current open snapshot markets without trades in the
            latest UTC day
        avg_spread (float | None | Unset): Average YES-token spread across current open snapshot markets with bid/ask
            spread evidence
        snapshot_at (datetime.datetime | None | Unset): Latest stored snapshot timestamp used by the pulse read model
    """

    directional_coverage: float | None | Unset = UNSET
    traded_market_pct: float | None | Unset = UNSET
    zero_trade_market_pct: float | None | Unset = UNSET
    avg_spread: float | None | Unset = UNSET
    snapshot_at: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        directional_coverage: float | None | Unset
        if isinstance(self.directional_coverage, Unset):
            directional_coverage = UNSET
        else:
            directional_coverage = self.directional_coverage

        traded_market_pct: float | None | Unset
        if isinstance(self.traded_market_pct, Unset):
            traded_market_pct = UNSET
        else:
            traded_market_pct = self.traded_market_pct

        zero_trade_market_pct: float | None | Unset
        if isinstance(self.zero_trade_market_pct, Unset):
            zero_trade_market_pct = UNSET
        else:
            zero_trade_market_pct = self.zero_trade_market_pct

        avg_spread: float | None | Unset
        if isinstance(self.avg_spread, Unset):
            avg_spread = UNSET
        else:
            avg_spread = self.avg_spread

        snapshot_at: None | str | Unset
        if isinstance(self.snapshot_at, Unset):
            snapshot_at = UNSET
        elif isinstance(self.snapshot_at, datetime.datetime):
            snapshot_at = self.snapshot_at.isoformat()
        else:
            snapshot_at = self.snapshot_at

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if directional_coverage is not UNSET:
            field_dict["directional_coverage"] = directional_coverage
        if traded_market_pct is not UNSET:
            field_dict["traded_market_pct"] = traded_market_pct
        if zero_trade_market_pct is not UNSET:
            field_dict["zero_trade_market_pct"] = zero_trade_market_pct
        if avg_spread is not UNSET:
            field_dict["avg_spread"] = avg_spread
        if snapshot_at is not UNSET:
            field_dict["snapshot_at"] = snapshot_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)

        def _parse_directional_coverage(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        directional_coverage = _parse_directional_coverage(d.pop("directional_coverage", UNSET))

        def _parse_traded_market_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        traded_market_pct = _parse_traded_market_pct(d.pop("traded_market_pct", UNSET))

        def _parse_zero_trade_market_pct(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        zero_trade_market_pct = _parse_zero_trade_market_pct(d.pop("zero_trade_market_pct", UNSET))

        def _parse_avg_spread(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        avg_spread = _parse_avg_spread(d.pop("avg_spread", UNSET))

        def _parse_snapshot_at(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                snapshot_at_type_0 = datetime.datetime.fromisoformat(data)

                return snapshot_at_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        snapshot_at = _parse_snapshot_at(d.pop("snapshot_at", UNSET))

        polymarket_pulse_evidence = cls(
            directional_coverage=directional_coverage,
            traded_market_pct=traded_market_pct,
            zero_trade_market_pct=zero_trade_market_pct,
            avg_spread=avg_spread,
            snapshot_at=snapshot_at,
        )

        polymarket_pulse_evidence.additional_properties = d
        return polymarket_pulse_evidence

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
