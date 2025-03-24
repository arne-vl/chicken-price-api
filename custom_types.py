from typing_extensions import TypedDict
from datetime import date


class PriceNotation(TypedDict):
    date_start: date
    date_end: date
    price: float


class PriceData(TypedDict):
    abc: float
    deinze: float
