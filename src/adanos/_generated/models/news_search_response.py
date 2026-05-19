from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.news_search_result_item import NewsSearchResultItem


T = TypeVar("T", bound="NewsSearchResponse")


@_attrs_define
class NewsSearchResponse:
    """Search response for news assets.

    Attributes:
        query (str): Original search query
        count (int): Total number of matching results before the limit is applied
        period_days (int): Lookback window used for each summary block
        results (list[NewsSearchResultItem]): Top matching stocks capped by the requested limit
    """

    query: str
    count: int
    period_days: int
    results: list[NewsSearchResultItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        query = self.query

        count = self.count

        period_days = self.period_days

        results = []
        for results_item_data in self.results:
            results_item = results_item_data.to_dict()
            results.append(results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "query": query,
                "count": count,
                "period_days": period_days,
                "results": results,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.news_search_result_item import NewsSearchResultItem

        d = dict(src_dict)
        query = d.pop("query")

        count = d.pop("count")

        period_days = d.pop("period_days")

        results = []
        _results = d.pop("results")
        for results_item_data in _results:
            results_item = NewsSearchResultItem.from_dict(results_item_data)

            results.append(results_item)

        news_search_response = cls(
            query=query,
            count=count,
            period_days=period_days,
            results=results,
        )

        news_search_response.additional_properties = d
        return news_search_response

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
