from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketSearchResultItem")


@_attrs_define
class PolymarketSearchResultItem:
    """Individual Polymarket search result item.

    Attributes:
        ticker (str): Stock ticker symbol
        name (str): Company name
        trade_count (int): Current UTC-day trade count from latest active persisted snapshot
        type_ (None | str | Unset): Asset type (Stock, ETF, etc.)
        exchange (None | str | Unset): Stock exchange
        sector (None | str | Unset): Industry sector
        country (None | str | Unset): Country of headquarters
        aliases (list[str] | Unset): Alternative names/aliases
    """

    ticker: str
    name: str
    trade_count: int
    type_: None | str | Unset = UNSET
    exchange: None | str | Unset = UNSET
    sector: None | str | Unset = UNSET
    country: None | str | Unset = UNSET
    aliases: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        name = self.name

        trade_count = self.trade_count

        type_: None | str | Unset
        if isinstance(self.type_, Unset):
            type_ = UNSET
        else:
            type_ = self.type_

        exchange: None | str | Unset
        if isinstance(self.exchange, Unset):
            exchange = UNSET
        else:
            exchange = self.exchange

        sector: None | str | Unset
        if isinstance(self.sector, Unset):
            sector = UNSET
        else:
            sector = self.sector

        country: None | str | Unset
        if isinstance(self.country, Unset):
            country = UNSET
        else:
            country = self.country

        aliases: list[str] | Unset = UNSET
        if not isinstance(self.aliases, Unset):
            aliases = self.aliases

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "name": name,
                "trade_count": trade_count,
            }
        )
        if type_ is not UNSET:
            field_dict["type"] = type_
        if exchange is not UNSET:
            field_dict["exchange"] = exchange
        if sector is not UNSET:
            field_dict["sector"] = sector
        if country is not UNSET:
            field_dict["country"] = country
        if aliases is not UNSET:
            field_dict["aliases"] = aliases

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        name = d.pop("name")

        trade_count = d.pop("trade_count")

        def _parse_type_(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        type_ = _parse_type_(d.pop("type", UNSET))

        def _parse_exchange(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        exchange = _parse_exchange(d.pop("exchange", UNSET))

        def _parse_sector(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        sector = _parse_sector(d.pop("sector", UNSET))

        def _parse_country(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        country = _parse_country(d.pop("country", UNSET))

        aliases = cast(list[str], d.pop("aliases", UNSET))

        polymarket_search_result_item = cls(
            ticker=ticker,
            name=name,
            trade_count=trade_count,
            type_=type_,
            exchange=exchange,
            sector=sector,
            country=country,
            aliases=aliases,
        )

        polymarket_search_result_item.additional_properties = d
        return polymarket_search_result_item

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
