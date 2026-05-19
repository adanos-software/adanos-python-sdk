from enum import Enum


class XCompareStockItemTrendType0(str, Enum):
    FALLING = "falling"
    RISING = "rising"
    STABLE = "stable"

    def __str__(self) -> str:
        return str(self.value)
