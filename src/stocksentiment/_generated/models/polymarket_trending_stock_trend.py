from enum import Enum


class PolymarketTrendingStockTrend(str, Enum):
    FALLING = "falling"
    RISING = "rising"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
