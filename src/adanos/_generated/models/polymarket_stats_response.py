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
        total_trades (int): Total Polymarket trade activity from daily aggregates
        total_markets (int): Distinct Polymarket condition_id count
        unique_tickers (int): Distinct tickers with Polymarket market rows in the database
        supported_tickers (int): Ticker count in ticker_reference
        open_markets_current (int | Unset): Currently open Polymarket markets where active=true, closed=false, and
            end_date has not passed Default: 0.
        open_tickers_current (int | Unset): Distinct tickers with at least one currently open Polymarket market
            Default: 0.
        traded_markets_today (int | Unset): Distinct Polymarket condition_id values with UTC-day trade activity
            Default: 0.
        traded_tickers_today (int | Unset): Distinct tickers with UTC-day Polymarket trade activity Default: 0.
        trades_today (int | Unset): Polymarket trade activity during today's UTC date Default: 0.
    """

    total_trades: int
    total_markets: int
    unique_tickers: int
    supported_tickers: int
    open_markets_current: int | Unset = 0
    open_tickers_current: int | Unset = 0
    traded_markets_today: int | Unset = 0
    traded_tickers_today: int | Unset = 0
    trades_today: int | Unset = 0
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        total_trades = self.total_trades

        total_markets = self.total_markets

        unique_tickers = self.unique_tickers

        supported_tickers = self.supported_tickers

        open_markets_current = self.open_markets_current

        open_tickers_current = self.open_tickers_current

        traded_markets_today = self.traded_markets_today

        traded_tickers_today = self.traded_tickers_today

        trades_today = self.trades_today

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
        if open_markets_current is not UNSET:
            field_dict["open_markets_current"] = open_markets_current
        if open_tickers_current is not UNSET:
            field_dict["open_tickers_current"] = open_tickers_current
        if traded_markets_today is not UNSET:
            field_dict["traded_markets_today"] = traded_markets_today
        if traded_tickers_today is not UNSET:
            field_dict["traded_tickers_today"] = traded_tickers_today
        if trades_today is not UNSET:
            field_dict["trades_today"] = trades_today

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        total_trades = d.pop("total_trades")

        total_markets = d.pop("total_markets")

        unique_tickers = d.pop("unique_tickers")

        supported_tickers = d.pop("supported_tickers")

        open_markets_current = d.pop("open_markets_current", UNSET)

        open_tickers_current = d.pop("open_tickers_current", UNSET)

        traded_markets_today = d.pop("traded_markets_today", UNSET)

        traded_tickers_today = d.pop("traded_tickers_today", UNSET)

        trades_today = d.pop("trades_today", UNSET)

        polymarket_stats_response = cls(
            total_trades=total_trades,
            total_markets=total_markets,
            unique_tickers=unique_tickers,
            supported_tickers=supported_tickers,
            open_markets_current=open_markets_current,
            open_tickers_current=open_tickers_current,
            traded_markets_today=traded_markets_today,
            traded_tickers_today=traded_tickers_today,
            trades_today=trades_today,
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
