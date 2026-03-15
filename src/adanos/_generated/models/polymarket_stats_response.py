from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="PolymarketStatsResponse")


@_attrs_define
class PolymarketStatsResponse:
    """Polymarket service statistics.

    Attributes:
        total_trades (int): Total aggregated trade_count (all time)
        total_markets (int): Distinct Polymarket condition_id count (all time)
        unique_tickers (int): Distinct tickers in latest snapshot
        tickers (list[str]): Top 50 ticker symbols from latest snapshot
        supported_tickers (int): Ticker count in ticker_reference
    """

    total_trades: int
    total_markets: int
    unique_tickers: int
    tickers: list[str]
    supported_tickers: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_trades = self.total_trades

        total_markets = self.total_markets

        unique_tickers = self.unique_tickers

        tickers = self.tickers

        supported_tickers = self.supported_tickers

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_trades": total_trades,
                "total_markets": total_markets,
                "unique_tickers": unique_tickers,
                "tickers": tickers,
                "supported_tickers": supported_tickers,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_trades = d.pop("total_trades")

        total_markets = d.pop("total_markets")

        unique_tickers = d.pop("unique_tickers")

        tickers = cast(list[str], d.pop("tickers"))

        supported_tickers = d.pop("supported_tickers")

        polymarket_stats_response = cls(
            total_trades=total_trades,
            total_markets=total_markets,
            unique_tickers=unique_tickers,
            tickers=tickers,
            supported_tickers=supported_tickers,
        )

        polymarket_stats_response.additional_properties = d
        return polymarket_stats_response

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
