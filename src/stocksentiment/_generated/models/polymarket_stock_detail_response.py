from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.polymarket_stock_detail_response_trend_type_0 import (
    PolymarketStockDetailResponseTrendType0,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.polymarket_daily_trend_item import PolymarketDailyTrendItem
    from ..models.polymarket_top_mention import PolymarketTopMention


T = TypeVar("T", bound="PolymarketStockDetailResponse")


@_attrs_define
class PolymarketStockDetailResponse:
    """Detailed Polymarket data for a single stock.

    Attributes:
        ticker (str): Stock ticker symbol
        found (bool): Whether data for ticker exists
        company_name (None | str | Unset): Company name from ticker_reference
        buzz_score (float | None | Unset): Buzz score (0-100)
        trend (None | PolymarketStockDetailResponseTrendType0 | Unset): UTC-day activity trend vs previous UTC day
        period_days (int | None | Unset): Analysis period in days
        trade_count (int | None | Unset): Trade count in period
        market_count (int | None | Unset): Number of active markets for ticker
        unique_traders (int | None | Unset): Sum of per-market day unique trader counters (can overcount across markets)
        sentiment_score (float | None | Unset): Implied sentiment
        positive_count (int | None | Unset): Markets with YES > 0.5
        negative_count (int | None | Unset): Markets with YES < 0.5
        neutral_count (int | None | Unset): Markets with YES ~= 0.5
        bullish_pct (int | None | Unset): Bullish market share
        bearish_pct (int | None | Unset): Bearish market share
        total_liquidity (float | None | Unset): Total liquidity (USD)
        daily_trend (list[PolymarketDailyTrendItem] | None | Unset): Daily trend data (completed days)
        top_mentions (list[PolymarketTopMention] | None | Unset): Top active markets by liquidity
    """

    ticker: str
    found: bool
    company_name: None | str | Unset = UNSET
    buzz_score: float | None | Unset = UNSET
    trend: None | PolymarketStockDetailResponseTrendType0 | Unset = UNSET
    period_days: int | None | Unset = UNSET
    trade_count: int | None | Unset = UNSET
    market_count: int | None | Unset = UNSET
    unique_traders: int | None | Unset = UNSET
    sentiment_score: float | None | Unset = UNSET
    positive_count: int | None | Unset = UNSET
    negative_count: int | None | Unset = UNSET
    neutral_count: int | None | Unset = UNSET
    bullish_pct: int | None | Unset = UNSET
    bearish_pct: int | None | Unset = UNSET
    total_liquidity: float | None | Unset = UNSET
    daily_trend: list[PolymarketDailyTrendItem] | None | Unset = UNSET
    top_mentions: list[PolymarketTopMention] | None | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        ticker = self.ticker

        found = self.found

        company_name: None | str | Unset
        if isinstance(self.company_name, Unset):
            company_name = UNSET
        else:
            company_name = self.company_name

        buzz_score: float | None | Unset
        if isinstance(self.buzz_score, Unset):
            buzz_score = UNSET
        else:
            buzz_score = self.buzz_score

        trend: None | str | Unset
        if isinstance(self.trend, Unset):
            trend = UNSET
        elif isinstance(self.trend, PolymarketStockDetailResponseTrendType0):
            trend = self.trend.value
        else:
            trend = self.trend

        period_days: int | None | Unset
        if isinstance(self.period_days, Unset):
            period_days = UNSET
        else:
            period_days = self.period_days

        trade_count: int | None | Unset
        if isinstance(self.trade_count, Unset):
            trade_count = UNSET
        else:
            trade_count = self.trade_count

        market_count: int | None | Unset
        if isinstance(self.market_count, Unset):
            market_count = UNSET
        else:
            market_count = self.market_count

        unique_traders: int | None | Unset
        if isinstance(self.unique_traders, Unset):
            unique_traders = UNSET
        else:
            unique_traders = self.unique_traders

        sentiment_score: float | None | Unset
        if isinstance(self.sentiment_score, Unset):
            sentiment_score = UNSET
        else:
            sentiment_score = self.sentiment_score

        positive_count: int | None | Unset
        if isinstance(self.positive_count, Unset):
            positive_count = UNSET
        else:
            positive_count = self.positive_count

        negative_count: int | None | Unset
        if isinstance(self.negative_count, Unset):
            negative_count = UNSET
        else:
            negative_count = self.negative_count

        neutral_count: int | None | Unset
        if isinstance(self.neutral_count, Unset):
            neutral_count = UNSET
        else:
            neutral_count = self.neutral_count

        bullish_pct: int | None | Unset
        if isinstance(self.bullish_pct, Unset):
            bullish_pct = UNSET
        else:
            bullish_pct = self.bullish_pct

        bearish_pct: int | None | Unset
        if isinstance(self.bearish_pct, Unset):
            bearish_pct = UNSET
        else:
            bearish_pct = self.bearish_pct

        total_liquidity: float | None | Unset
        if isinstance(self.total_liquidity, Unset):
            total_liquidity = UNSET
        else:
            total_liquidity = self.total_liquidity

        daily_trend: list[dict[str, Any]] | None | Unset
        if isinstance(self.daily_trend, Unset):
            daily_trend = UNSET
        elif isinstance(self.daily_trend, list):
            daily_trend = []
            for daily_trend_type_0_item_data in self.daily_trend:
                daily_trend_type_0_item = daily_trend_type_0_item_data.to_dict()
                daily_trend.append(daily_trend_type_0_item)

        else:
            daily_trend = self.daily_trend

        top_mentions: list[dict[str, Any]] | None | Unset
        if isinstance(self.top_mentions, Unset):
            top_mentions = UNSET
        elif isinstance(self.top_mentions, list):
            top_mentions = []
            for top_mentions_type_0_item_data in self.top_mentions:
                top_mentions_type_0_item = top_mentions_type_0_item_data.to_dict()
                top_mentions.append(top_mentions_type_0_item)

        else:
            top_mentions = self.top_mentions

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "ticker": ticker,
                "found": found,
            }
        )
        if company_name is not UNSET:
            field_dict["company_name"] = company_name
        if buzz_score is not UNSET:
            field_dict["buzz_score"] = buzz_score
        if trend is not UNSET:
            field_dict["trend"] = trend
        if period_days is not UNSET:
            field_dict["period_days"] = period_days
        if trade_count is not UNSET:
            field_dict["trade_count"] = trade_count
        if market_count is not UNSET:
            field_dict["market_count"] = market_count
        if unique_traders is not UNSET:
            field_dict["unique_traders"] = unique_traders
        if sentiment_score is not UNSET:
            field_dict["sentiment_score"] = sentiment_score
        if positive_count is not UNSET:
            field_dict["positive_count"] = positive_count
        if negative_count is not UNSET:
            field_dict["negative_count"] = negative_count
        if neutral_count is not UNSET:
            field_dict["neutral_count"] = neutral_count
        if bullish_pct is not UNSET:
            field_dict["bullish_pct"] = bullish_pct
        if bearish_pct is not UNSET:
            field_dict["bearish_pct"] = bearish_pct
        if total_liquidity is not UNSET:
            field_dict["total_liquidity"] = total_liquidity
        if daily_trend is not UNSET:
            field_dict["daily_trend"] = daily_trend
        if top_mentions is not UNSET:
            field_dict["top_mentions"] = top_mentions

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.polymarket_daily_trend_item import PolymarketDailyTrendItem
        from ..models.polymarket_top_mention import PolymarketTopMention

        d = dict(src_dict)
        ticker = d.pop("ticker")

        found = d.pop("found")

        def _parse_company_name(data: object) -> None | str | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(None | str | Unset, data)

        company_name = _parse_company_name(d.pop("company_name", UNSET))

        def _parse_buzz_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        buzz_score = _parse_buzz_score(d.pop("buzz_score", UNSET))

        def _parse_trend(
            data: object,
        ) -> None | PolymarketStockDetailResponseTrendType0 | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                trend_type_0 = PolymarketStockDetailResponseTrendType0(data)

                return trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(None | PolymarketStockDetailResponseTrendType0 | Unset, data)

        trend = _parse_trend(d.pop("trend", UNSET))

        def _parse_period_days(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        period_days = _parse_period_days(d.pop("period_days", UNSET))

        def _parse_trade_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        trade_count = _parse_trade_count(d.pop("trade_count", UNSET))

        def _parse_market_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        market_count = _parse_market_count(d.pop("market_count", UNSET))

        def _parse_unique_traders(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        unique_traders = _parse_unique_traders(d.pop("unique_traders", UNSET))

        def _parse_sentiment_score(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        sentiment_score = _parse_sentiment_score(d.pop("sentiment_score", UNSET))

        def _parse_positive_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        positive_count = _parse_positive_count(d.pop("positive_count", UNSET))

        def _parse_negative_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        negative_count = _parse_negative_count(d.pop("negative_count", UNSET))

        def _parse_neutral_count(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        neutral_count = _parse_neutral_count(d.pop("neutral_count", UNSET))

        def _parse_bullish_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bullish_pct = _parse_bullish_pct(d.pop("bullish_pct", UNSET))

        def _parse_bearish_pct(data: object) -> int | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(int | None | Unset, data)

        bearish_pct = _parse_bearish_pct(d.pop("bearish_pct", UNSET))

        def _parse_total_liquidity(data: object) -> float | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(float | None | Unset, data)

        total_liquidity = _parse_total_liquidity(d.pop("total_liquidity", UNSET))

        def _parse_daily_trend(
            data: object,
        ) -> list[PolymarketDailyTrendItem] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                daily_trend_type_0 = []
                _daily_trend_type_0 = data
                for daily_trend_type_0_item_data in _daily_trend_type_0:
                    daily_trend_type_0_item = PolymarketDailyTrendItem.from_dict(
                        daily_trend_type_0_item_data
                    )

                    daily_trend_type_0.append(daily_trend_type_0_item)

                return daily_trend_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolymarketDailyTrendItem] | None | Unset, data)

        daily_trend = _parse_daily_trend(d.pop("daily_trend", UNSET))

        def _parse_top_mentions(
            data: object,
        ) -> list[PolymarketTopMention] | None | Unset:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                top_mentions_type_0 = []
                _top_mentions_type_0 = data
                for top_mentions_type_0_item_data in _top_mentions_type_0:
                    top_mentions_type_0_item = PolymarketTopMention.from_dict(
                        top_mentions_type_0_item_data
                    )

                    top_mentions_type_0.append(top_mentions_type_0_item)

                return top_mentions_type_0
            except (TypeError, ValueError, AttributeError, KeyError):
                pass
            return cast(list[PolymarketTopMention] | None | Unset, data)

        top_mentions = _parse_top_mentions(d.pop("top_mentions", UNSET))

        polymarket_stock_detail_response = cls(
            ticker=ticker,
            found=found,
            company_name=company_name,
            buzz_score=buzz_score,
            trend=trend,
            period_days=period_days,
            trade_count=trade_count,
            market_count=market_count,
            unique_traders=unique_traders,
            sentiment_score=sentiment_score,
            positive_count=positive_count,
            negative_count=negative_count,
            neutral_count=neutral_count,
            bullish_pct=bullish_pct,
            bearish_pct=bearish_pct,
            total_liquidity=total_liquidity,
            daily_trend=daily_trend,
            top_mentions=top_mentions,
        )

        polymarket_stock_detail_response.additional_properties = d
        return polymarket_stock_detail_response

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
