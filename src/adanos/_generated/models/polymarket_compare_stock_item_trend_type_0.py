from enum import Enum


class PolymarketCompareStockItemTrendType0(str, Enum):
    FALLING = "falling"
    RISING = "rising"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
