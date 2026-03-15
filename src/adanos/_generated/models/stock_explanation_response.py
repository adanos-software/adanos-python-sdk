from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="StockExplanationResponse")


@_attrs_define
class StockExplanationResponse:
    """AI-generated trend explanation for a stock.

    Attributes:
        ticker (str): Stock ticker symbol
        explanation (str): AI-generated explanation of why this stock is trending
        cached (bool): Whether the explanation was served from cache
        generated_at (str): ISO timestamp when explanation was generated
        company_name (None | str | Unset): Company name from ticker_reference
        model (None | str | Unset): LLM model used for generation
    """

    ticker: str
    explanation: str
    cached: bool
    generated_at: str
    company_name: None | str | Unset = UNSET
    model: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        explanation = self.explanation

        cached = self.cached

        generated_at = self.generated_at

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        model: None | str | Unset
        if isinstance(self.model, Unset):
            model = UNSET
        else:
            model = self.model

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "explanation": explanation,
                "cached": cached,
                "generated_at": generated_at,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if model is not UNSET:
            field_dict["model"] = model

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        ticker = d.pop("ticker")

        explanation = d.pop("explanation")

        cached = d.pop("cached")

        generated_at = d.pop("generated_at")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_model(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        model = _parse_model(d.pop("model", UNSET))

        stock_explanation_response = cls(
            ticker=ticker,
            explanation=explanation,
            cached=cached,
            generated_at=generated_at,
            company_name=company_name,
            model=model,
        )

        stock_explanation_response.additional_properties = d
        return stock_explanation_response

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
