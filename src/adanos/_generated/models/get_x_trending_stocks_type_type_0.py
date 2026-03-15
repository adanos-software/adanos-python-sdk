from enum import Enum


class GetXTrendingStocksTypeType0(str, Enum):
    ALL = "all"
    ETF = "etf"
    STOCK = "stock"

    def __str__(self) -> str:
        return str(self.value)
