from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymarket_ticker_pulse_mood import PolymarketTickerPulseMood
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymarket_pulse_evidence import PolymarketPulseEvidence


T = TypeVar("T", bound="PolymarketTickerPulse")


@_attrs_define
class PolymarketTickerPulse:
    """Compact interpretation layer for current ticker-level Polymarket data.

    Attributes:
        mood (PolymarketTickerPulseMood): Current compact Polymarket interpretation for this ticker
        confidence (float): Interpretation confidence capped by coverage, trade breadth, spread, liquidity and recency
        thin_data (bool): True when current evidence is insufficient for a strong directional interpretation
        why (list[str]): Stable machine-readable reason codes explaining the pulse interpretation
        evidence (PolymarketPulseEvidence): Compact data-quality evidence for the ticker-level Polymarket pulse.
        warnings (list[str] | Unset): Stable machine-readable data quality, freshness and tradability warnings
    """

    mood: PolymarketTickerPulseMood
    confidence: float
    thin_data: bool
    why: list[str]
    evidence: PolymarketPulseEvidence
    warnings: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mood = self.mood.value

        confidence = self.confidence

        thin_data = self.thin_data

        why = self.why

        evidence = self.evidence.to_dict()

        warnings: list[str] | Unset = UNSET
        if not isinstance(self.warnings, Unset):
            warnings = self.warnings

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "mood": mood,
                "confidence": confidence,
                "thin_data": thin_data,
                "why": why,
                "evidence": evidence,
            }
        )
        if warnings is not UNSET:
            field_dict["warnings"] = warnings

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymarket_pulse_evidence import PolymarketPulseEvidence

        d = dict(src_dict)
        mood = PolymarketTickerPulseMood(d.pop("mood"))

        confidence = d.pop("confidence")

        thin_data = d.pop("thin_data")

        why = cast(list[str], d.pop("why"))

        evidence = PolymarketPulseEvidence.from_dict(d.pop("evidence"))

        warnings = cast(list[str], d.pop("warnings", UNSET))

        polymarket_ticker_pulse = cls(
            mood=mood,
            confidence=confidence,
            thin_data=thin_data,
            why=why,
            evidence=evidence,
            warnings=warnings,
        )

        polymarket_ticker_pulse.additional_properties = d
        return polymarket_ticker_pulse

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
