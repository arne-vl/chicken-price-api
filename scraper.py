import httpx
from selectolax.parser import HTMLParser
from datetime import datetime, timedelta
from typing import TypedDict
from custom_types import PriceNotation


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}


def get_price_deinze() -> PriceNotation:
    url = "https://www.pluimveeslachthuizen.be/nl/node/246"

    response = httpx.get(url=url, headers=HEADERS)
    html = HTMLParser(response.text)

    most_recent_row = html.css("tr")[2]
    columns = most_recent_row.css("td")

    notation_date = datetime.strptime(columns[0].text(), "%d/%m/%y")
    notation_price = float(columns[4].text()[2:].replace(",", "."))

    notation_week = get_week_start_end(notation_date)

    return PriceNotation(
        date_start=notation_week[0], date_end=notation_week[1], price=notation_price
    )


def get_price_abc() -> PriceNotation:
    url = "https://www.pluimveeslachthuizen.be/nl/node/247"

    response = httpx.get(url=url, headers=HEADERS)
    html = HTMLParser(response.text)

    most_recent_row = html.css("tr")[1]
    columns = most_recent_row.css("td")

    notation_week_number = int(columns[0].text())
    notation_price = float(columns[1].text()[2:].replace(",", "."))

    notation_week = get_week_start_end_from_week(
        datetime.now().year, notation_week_number
    )

    return PriceNotation(
        date_start=notation_week[0], date_end=notation_week[1], price=notation_price
    )


def get_week_start_end(date: datetime):
    week_start = date - timedelta(days=date.weekday())
    week_end = week_start + timedelta(days=6)
    return week_start.strftime("%Y-%m-%d"), week_end.strftime("%Y-%m-%d")


def get_week_start_end_from_week(year: int, week: int):
    week_start = datetime.fromisocalendar(year, week, 1)
    week_end = week_start + timedelta(days=6)
    return week_start.strftime("%Y-%m-%d"), week_end.strftime("%Y-%m-%d")
