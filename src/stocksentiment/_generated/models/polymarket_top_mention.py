from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketTopMention")


@_attrs_define
class PolymarketTopMention:
    """Top Polymarket market for a ticker (latest snapshot per condition).

    Attributes:
        condition_id (str): Polymarket condition ID
        question (str): Market question/title
        market_type (str): Derived market type
        liquidity (float): Market liquidity in USD
        volume_24h (float): 24h volume in USD
        active (bool): Whether market is active
        trade_count (int | None | Unset): Current UTC-day trade count for this market from latest persisted snapshot
        sentiment_score (float | None | Unset): Market-level sentiment signal (price + optional buy/sell flow)
        yes_price (float | None | Unset): Latest YES price
        no_price (float | None | Unset): Latest NO price
        end_date (None | str | Unset): Market end date (ISO)
    """

    condition_id: str
    question: str
    market_type: str
    liquidity: float
    volume_24h: float
    active: bool
    trade_count: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    yes_price: float | None | Unset = UNSET
    no_price: float | None | Unset = UNSET
    end_date: None | str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_id = self.condition_id

        question = self.question

        market_type = self.market_type

        liquidity = self.liquidity

        volume_24h = self.volume_24h

        active = self.active

        trade_count: int | None | Unset
        if isinstance(self.trade_count, Unset):
            trade_count = UNSET
        else:
            trade_count = self.trade_count

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        yes_price: float | None | Unset
        if isinstance(self.yes_price, Unset):
            yes_price = UNSET
        else:
            yes_price = self.yes_price

        no_price: float | None | Unset
        if isinstance(self.no_price, Unset):
            no_price = UNSET
        else:
            no_price = self.no_price

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_id": condition_id,
                "question": question,
                "market_type": market_type,
                "liquidity": liquidity,
                "volume_24h": volume_24h,
                "active": active,
            }
        )
        if trade_count is not UNSET:
            field_dict["trade_count"] = trade_count
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_id = d.pop("condition_id")

        question = d.pop("question")

        market_type = d.pop("market_type")

        liquidity = d.pop("liquidity")

        volume_24h = d.pop("volume_24h")

        active = d.pop("active")

        def _parse_trade_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        trade_count = _parse_trade_count(d.pop("trade_count", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_yes_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        yes_price = _parse_yes_price(d.pop("yes_price", UNSET))

        def _parse_no_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        no_price = _parse_no_price(d.pop("no_price", UNSET))

        def _parse_end_date(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        polymarket_top_mention = cls(
            condition_id=condition_id,
            question=question,
            market_type=market_type,
            liquidity=liquidity,
            volume_24h=volume_24h,
            active=active,
            trade_count=trade_count,
            sentiment_score=sentiment_score,
            yes_price=yes_price,
            no_price=no_price,
            end_date=end_date,
        )

        polymarket_top_mention.additional_properties = d
        return polymarket_top_mention

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
