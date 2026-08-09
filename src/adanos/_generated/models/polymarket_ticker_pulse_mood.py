from enum import Enum


class PolymarketTickerPulseMood(str, Enum):
    BEARISH = "bearish"
    BULLISH = "bullish"
    EVENT_DRIVEN = "event_driven"
    ILLIQUID = "illiquid"
    MIXED = "mixed"
    UNCLEAR = "unclear"

    def __str__(self) -> str:
        return str(self.value)
