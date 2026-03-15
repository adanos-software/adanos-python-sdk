from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketCompareStockItem")


@_attrs_define
class PolymarketCompareStockItem:
    """Single stock item for Polymarket compare endpoint.

    Attributes:
        ticker (str): Stock ticker symbol
        buzz_score (float): Buzz score (0-100)
        trade_count (int): Trade count in selected period
        market_count (int): Number of active markets for ticker
        total_liquidity (float): Total liquidity (USD)
        company_name (None | str | Unset): Company name from ticker_reference
        unique_traders (int | None | Unset): Sum of per-market day unique trader counters (can overcount across markets)
        sentiment (float | None | Unset): Implied sentiment
    """

    ticker: str
    buzz_score: float
    trade_count: int
    market_count: int
    total_liquidity: float
    company_name: None | str | Unset = UNSET
    unique_traders: int | None | Unset = UNSET
    sentiment: float | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        buzz_score = self.buzz_score

        trade_count = self.trade_count

        market_count = self.market_count

        total_liquidity = self.total_liquidity

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        unique_traders: int | None | Unset
        if isinstance(self.unique_traders, Unset):
            unique_traders = UNSET
        else:
            unique_traders = self.unique_traders

        sentiment: float | None | Unset
        if isinstance(self.sentiment, Unset):
            sentiment = UNSET
        else:
            sentiment = self.sentiment

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "buzz_score": buzz_score,
                "trade_count": trade_count,
                "market_count": market_count,
                "total_liquidity": total_liquidity,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if unique_traders is not UNSET:
            field_dict["unique_traders"] = unique_traders
        if sentiment is not UNSET:
            field_dict["sentiment"] = sentiment

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        buzz_score = d.pop("buzz_score")

        trade_count = d.pop("trade_count")

        market_count = d.pop("market_count")

        total_liquidity = d.pop("total_liquidity")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_unique_traders(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_traders = _parse_unique_traders(d.pop("unique_traders", UNSET))

        def _parse_sentiment(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment = _parse_sentiment(d.pop("sentiment", UNSET))

        polymarket_compare_stock_item = cls(
            ticker=ticker,
            buzz_score=buzz_score,
            trade_count=trade_count,
            market_count=market_count,
            total_liquidity=total_liquidity,
            company_name=company_name,
            unique_traders=unique_traders,
            sentiment=sentiment,
        )

        polymarket_compare_stock_item.additional_properties = d
        return polymarket_compare_stock_item

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
