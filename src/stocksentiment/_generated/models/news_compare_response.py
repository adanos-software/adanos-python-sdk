from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_compare_stock_item import NewsCompareStockItem


T = TypeVar("T", bound="NewsCompareResponse")


@_attrs_define
class NewsCompareResponse:
    """Comparison of multiple stocks in news.

    Attributes:
        period_days (int): Analysis period in days
        stocks (list[NewsCompareStockItem]): Stocks sorted by buzz_score descending
    """

    period_days: int
    stocks: list[NewsCompareStockItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        period_days = self.period_days

        stocks = []
        for stocks_item_data in self.stocks:
            stocks_item = stocks_item_data.to_dict()
            stocks.append(stocks_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "period_days": period_days,
                "stocks": stocks,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.news_compare_stock_item import NewsCompareStockItem

        d = dict(src_dict)
        period_days = d.pop("period_days")

        stocks = []
        _stocks = d.pop("stocks")
        for stocks_item_data in _stocks:
            stocks_item = NewsCompareStockItem.from_dict(stocks_item_data)

            stocks.append(stocks_item)

        news_compare_response = cls(
            period_days=period_days,
            stocks=stocks,
        )

        news_compare_response.additional_properties = d
        return news_compare_response

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
