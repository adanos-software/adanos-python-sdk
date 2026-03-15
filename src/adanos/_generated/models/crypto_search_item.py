from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="CryptoSearchItem")


@_attrs_define
class CryptoSearchItem:
    """Single search result for crypto reference data.

    Attributes:
        symbol (str):
        name (str):
        market_cap_rank (int | None | Unset):
        market_cap_usd (float | None | Unset):
        aliases (list[str] | None | Unset):
        mention_count (int | None | Unset):
    """

    symbol: str
    name: str
    market_cap_rank: int | None | Unset = UNSET
    market_cap_usd: float | None | Unset = UNSET
    aliases: list[str] | None | Unset = UNSET
    mention_count: int | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        symbol = self.symbol

        name = self.name

        market_cap_rank: int | None | Unset
        if isinstance(self.market_cap_rank, Unset):
            market_cap_rank = UNSET
        else:
            market_cap_rank = self.market_cap_rank

        market_cap_usd: float | None | Unset
        if isinstance(self.market_cap_usd, Unset):
            market_cap_usd = UNSET
        else:
            market_cap_usd = self.market_cap_usd

        aliases: list[str] | None | Unset
        if isinstance(self.aliases, Unset):
            aliases = UNSET
        elif isinstance(self.aliases, list):
            aliases = self.aliases

        else:
            aliases = self.aliases

        mention_count: int | None | Unset
        if isinstance(self.mention_count, Unset):
            mention_count = UNSET
        else:
            mention_count = self.mention_count

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "symbol": symbol,
                "name": name,
            }
        )
        if market_cap_rank is not UNSET:
            field_dict["market_cap_rank"] = market_cap_rank
        if market_cap_usd is not UNSET:
            field_dict["market_cap_usd"] = market_cap_usd
        if aliases is not UNSET:
            field_dict["aliases"] = aliases
        if mention_count is not UNSET:
            field_dict["mention_count"] = mention_count

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        symbol = d.pop("symbol")

        name = d.pop("name")

        def _parse_market_cap_rank(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        market_cap_rank = _parse_market_cap_rank(d.pop("market_cap_rank", UNSET))

        def _parse_market_cap_usd(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        market_cap_usd = _parse_market_cap_usd(d.pop("market_cap_usd", UNSET))

        def _parse_aliases(data: object) -> list[str] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                aliases_type_0 = cast(list[str], data)

                return aliases_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[str] | None | Unset, data)

        aliases = _parse_aliases(d.pop("aliases", UNSET))

        def _parse_mention_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        mention_count = _parse_mention_count(d.pop("mention_count", UNSET))

        crypto_search_item = cls(
            symbol=symbol,
            name=name,
            market_cap_rank=market_cap_rank,
            market_cap_usd=market_cap_usd,
            aliases=aliases,
            mention_count=mention_count,
        )

        crypto_search_item.additional_properties = d
        return crypto_search_item

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
