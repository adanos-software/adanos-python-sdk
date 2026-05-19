from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..models.polymarket_raw_mention_item_sentiment_label_type_0 import PolymarketRawMentionItemSentimentLabelType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="PolymarketRawMentionItem")


@_attrs_define
class PolymarketRawMentionItem:
    """Raw Polymarket market snapshot row for one stock ticker.

    Attributes:
        condition_id (str): Polymarket condition ID
        event_id (str): Polymarket event ID
        question (str): Market question/title
        market_type (str): Derived market type (`up_down`, `close_above`, `hit_target`, `earnings`, or `other`)
        liquidity (float): Market liquidity in USD at snapshot time
        volume_24h (float): Rolling 24h market volume in USD at snapshot time
        trade_count (int): UTC-day trade count observed for this market snapshot
        buy_trades (int): UTC-day Polymarket BUY trades for this snapshot; activity counter, not bullishness
        sell_trades (int): UTC-day Polymarket SELL trades for this snapshot; activity counter, not bearishness
        unique_traders (int): UTC-day unique trader counter for this market snapshot
        active (bool): Whether the market is currently open; false for closed or ended markets
        fetched_at (datetime.datetime): Snapshot fetch timestamp
        market_slug (None | str | Unset): Polymarket market slug
        strike_price (float | None | Unset): Extracted strike price when available
        yes_price (float | None | Unset): YES price from this snapshot
        no_price (float | None | Unset): NO price from this snapshot
        reference_price (float | None | Unset): Stock reference price attached during scrape when needed for range-
            ladder classification
        reference_price_timestamp (datetime.datetime | None | Unset): Timestamp for `reference_price` when available
        sentiment_score (float | None | Unset): Outcome-aware market price sentiment for this snapshot; null when no
            trade activity or direction is unclassified
        sentiment_label (None | PolymarketRawMentionItemSentimentLabelType0 | Unset): Classification derived from
            `sentiment_score`: positive=bullish, negative=bearish, neutral=flat; null when `sentiment_score` is null
        end_date (datetime.datetime | None | Unset): Market end timestamp when available. Unlike summary `top_mentions`,
            raw rows preserve the full timestamp from the stored snapshot.
    """

    condition_id: str
    event_id: str
    question: str
    market_type: str
    liquidity: float
    volume_24h: float
    trade_count: int
    buy_trades: int
    sell_trades: int
    unique_traders: int
    active: bool
    fetched_at: datetime.datetime
    market_slug: None | str | Unset = UNSET
    strike_price: float | None | Unset = UNSET
    yes_price: float | None | Unset = UNSET
    no_price: float | None | Unset = UNSET
    reference_price: float | None | Unset = UNSET
    reference_price_timestamp: datetime.datetime | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    sentiment_label: None | PolymarketRawMentionItemSentimentLabelType0 | Unset = UNSET
    end_date: datetime.datetime | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        condition_id = self.condition_id

        event_id = self.event_id

        question = self.question

        market_type = self.market_type

        liquidity = self.liquidity

        volume_24h = self.volume_24h

        trade_count = self.trade_count

        buy_trades = self.buy_trades

        sell_trades = self.sell_trades

        unique_traders = self.unique_traders

        active = self.active

        fetched_at = self.fetched_at.isoformat()

        market_slug: None | str | Unset
        if isinstance(self.market_slug, Unset):
            market_slug = UNSET
        else:
            market_slug = self.market_slug

        strike_price: float | None | Unset
        if isinstance(self.strike_price, Unset):
            strike_price = UNSET
        else:
            strike_price = self.strike_price

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

        reference_price: float | None | Unset
        if isinstance(self.reference_price, Unset):
            reference_price = UNSET
        else:
            reference_price = self.reference_price

        reference_price_timestamp: None | str | Unset
        if isinstance(self.reference_price_timestamp, Unset):
            reference_price_timestamp = UNSET
        elif isinstance(self.reference_price_timestamp, datetime.datetime):
            reference_price_timestamp = self.reference_price_timestamp.isoformat()
        else:
            reference_price_timestamp = self.reference_price_timestamp

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        sentiment_label: None | str | Unset
        if isinstance(self.sentiment_label, Unset):
            sentiment_label = UNSET
        elif isinstance(self.sentiment_label, PolymarketRawMentionItemSentimentLabelType0):
            sentiment_label = self.sentiment_label.value
        else:
            sentiment_label = self.sentiment_label

        end_date: None | str | Unset
        if isinstance(self.end_date, Unset):
            end_date = UNSET
        elif isinstance(self.end_date, datetime.datetime):
            end_date = self.end_date.isoformat()
        else:
            end_date = self.end_date

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "condition_id": condition_id,
                "event_id": event_id,
                "question": question,
                "market_type": market_type,
                "liquidity": liquidity,
                "volume_24h": volume_24h,
                "trade_count": trade_count,
                "buy_trades": buy_trades,
                "sell_trades": sell_trades,
                "unique_traders": unique_traders,
                "active": active,
                "fetched_at": fetched_at,
            }
        )
        if market_slug is not UNSET:
            field_dict["market_slug"] = market_slug
        if strike_price is not UNSET:
            field_dict["strike_price"] = strike_price
        if yes_price is not UNSET:
            field_dict["yes_price"] = yes_price
        if no_price is not UNSET:
            field_dict["no_price"] = no_price
        if reference_price is not UNSET:
            field_dict["reference_price"] = reference_price
        if reference_price_timestamp is not UNSET:
            field_dict["reference_price_timestamp"] = reference_price_timestamp
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if sentiment_label is not UNSET:
            field_dict["sentiment_label"] = sentiment_label
        if end_date is not UNSET:
            field_dict["end_date"] = end_date

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        condition_id = d.pop("condition_id")

        event_id = d.pop("event_id")

        question = d.pop("question")

        market_type = d.pop("market_type")

        liquidity = d.pop("liquidity")

        volume_24h = d.pop("volume_24h")

        trade_count = d.pop("trade_count")

        buy_trades = d.pop("buy_trades")

        sell_trades = d.pop("sell_trades")

        unique_traders = d.pop("unique_traders")

        active = d.pop("active")

        fetched_at = isoparse(d.pop("fetched_at"))

        def _parse_market_slug(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        market_slug = _parse_market_slug(d.pop("market_slug", UNSET))

        def _parse_strike_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        strike_price = _parse_strike_price(d.pop("strike_price", UNSET))

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

        def _parse_reference_price(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        reference_price = _parse_reference_price(d.pop("reference_price", UNSET))

        def _parse_reference_price_timestamp(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                reference_price_timestamp_type_0 = isoparse(data)

                return reference_price_timestamp_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        reference_price_timestamp = _parse_reference_price_timestamp(d.pop("reference_price_timestamp", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_sentiment_label(data: object) -> None | PolymarketRawMentionItemSentimentLabelType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                sentiment_label_type_0 = PolymarketRawMentionItemSentimentLabelType0(data)

                return sentiment_label_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolymarketRawMentionItemSentimentLabelType0 | Unset, data)

        sentiment_label = _parse_sentiment_label(d.pop("sentiment_label", UNSET))

        def _parse_end_date(data: object) -> datetime.datetime | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                end_date_type_0 = isoparse(data)

                return end_date_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(datetime.datetime | None | Unset, data)

        end_date = _parse_end_date(d.pop("end_date", UNSET))

        polymarket_raw_mention_item = cls(
            condition_id=condition_id,
            event_id=event_id,
            question=question,
            market_type=market_type,
            liquidity=liquidity,
            volume_24h=volume_24h,
            trade_count=trade_count,
            buy_trades=buy_trades,
            sell_trades=sell_trades,
            unique_traders=unique_traders,
            active=active,
            fetched_at=fetched_at,
            market_slug=market_slug,
            strike_price=strike_price,
            yes_price=yes_price,
            no_price=no_price,
            reference_price=reference_price,
            reference_price_timestamp=reference_price_timestamp,
            sentiment_score=sentiment_score,
            sentiment_label=sentiment_label,
            end_date=end_date,
        )

        polymarket_raw_mention_item.additional_properties = d
        return polymarket_raw_mention_item

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
