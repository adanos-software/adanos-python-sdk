from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketStatsResponse")


@_attrs_define
class PolymarketStatsResponse:
    """Polymarket service statistics.

    Attributes:
        total_trades (int): Total aggregated trade_count (all time)
        total_markets (int): Distinct Polymarket condition_id count (all time)
        unique_tickers (int): Distinct tickers with indexed market rows
        supported_tickers (int): Ticker count in ticker_reference
        trades_today (int | Unset): Polymarket trades observed since today's UTC midnight Default: 0.
        unique_tickers_today (int | Unset): Unique tickers in Polymarket snapshot rows fetched since today's UTC
            midnight Default: 0.
    """

    total_trades: int
    total_markets: int
    unique_tickers: int
    supported_tickers: int
    trades_today: int | Unset = 0
    unique_tickers_today: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_trades = self.total_trades

        total_markets = self.total_markets

        unique_tickers = self.unique_tickers

        supported_tickers = self.supported_tickers

        trades_today = self.trades_today

        unique_tickers_today = self.unique_tickers_today

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "total_trades": total_trades,
                "total_markets": total_markets,
                "unique_tickers": unique_tickers,
                "supported_tickers": supported_tickers,
            }
        )
        if trades_today is not UNSET:
            field_dict["trades_today"] = trades_today
        if unique_tickers_today is not UNSET:
            field_dict["unique_tickers_today"] = unique_tickers_today

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_trades = d.pop("total_trades")

        total_markets = d.pop("total_markets")

        unique_tickers = d.pop("unique_tickers")

        supported_tickers = d.pop("supported_tickers")

        trades_today = d.pop("trades_today", UNSET)

        unique_tickers_today = d.pop("unique_tickers_today", UNSET)

        polymarket_stats_response = cls(
            total_trades=total_trades,
            total_markets=total_markets,
            unique_tickers=unique_tickers,
            supported_tickers=supported_tickers,
            trades_today=trades_today,
            unique_tickers_today=unique_tickers_today,
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
