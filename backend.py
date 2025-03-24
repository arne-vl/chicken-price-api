from typing import Optional
from custom_types import PriceData, PriceNotation
from datetime import datetime
import psycopg2
import os
import csv


class Backend:
    def write_abc(self, data: PriceNotation) -> bool:
        pass

    def write_deinze(self, data: PriceNotation) -> bool:
        pass

    def get_last_datapoint(self) -> Optional[PriceNotation]:
        pass

    def get_current_price(self) -> PriceData:
        pass


class LocalBackend(Backend):
    def __init__(self):
        self.abc_file = "./data/abc_prices.csv"
        self.deinze_file = "./data/deinze_prices.csv"
        os.makedirs(os.path.dirname(self.abc_file), exist_ok=True)
        os.makedirs(os.path.dirname(self.deinze_file), exist_ok=True)

        for file in [self.abc_file, self.deinze_file]:
            os.makedirs(os.path.dirname(file), exist_ok=True)
            if not os.path.exists(file):
                with open(file, mode="w", newline="") as f:
                    csv.writer(f).writerow(["week_start", "week_end", "price"])

    def write_abc(self, data: PriceNotation) -> bool:
        if data != self.get_last_datapoint(self.abc_file):
            with open(self.abc_file, mode="a", newline="") as f:
                csv.writer(f).writerow(
                    [data["date_start"], data["date_end"], data["price"]]
                )
            return True

        return False

    def write_deinze(self, data: PriceNotation) -> bool:
        if data != self.get_last_datapoint(self.deinze_file):
            with open(self.deinze_file, mode="a", newline="") as f:
                csv.writer(f).writerow(
                    [data["date_start"], data["date_end"], data["price"]]
                )
            return True

        return False

    def get_last_datapoint(self, file: str, depth=0) -> Optional[PriceNotation]:
        with open(file, mode="r") as f:
            reader = list(csv.reader(f))
            if len(reader) > depth + 1:
                last_row = reader[-(1 + depth)]
                if last_row == []:
                    return None
                return PriceNotation(
                    date_start=last_row[0],
                    date_end=last_row[1],
                    price=float(last_row[2]),
                )
        return None

    def get_current_price(self) -> PriceData:
        last_abc = self.get_last_datapoint(self.abc_file)
        last_deinze = self.get_last_datapoint(self.deinze_file)

        if datetime.now() < datetime.strptime(last_abc["date_start"], "%Y-%m-%d"):
            last_abc = self.get_last_datapoint(self.abc_file, 1)

        return PriceData(abc=last_abc["price"], deinze=last_deinze["price"])
