import httpx
from selectolax.parser import HTMLParser
from datetime import datetime

from scraping.util import write_to_csv_deinze, write_to_csv_abc

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

def save_price_deinze():
    url = "https://www.pluimveeslachthuizen.be/nl/node/246"

    response = httpx.get(url=url, headers=HEADERS)

    html = HTMLParser(response.text)

    most_recent_row = html.css("tr")[2]
    
    columns = most_recent_row.css("td")

    notation_date = columns[0].text()
    price_broilers = columns[4].text()
    
    return write_to_csv_deinze("data/deinze.csv", notation_date, price_broilers)

def save_price_abc() -> bool:
    url = "https://www.pluimveeslachthuizen.be/nl/node/247"

    response = httpx.get(url=url, headers=HEADERS)

    html = HTMLParser(response.text)

    most_recent_row = html.css("tr")[1]
    
    columns = most_recent_row.css("td")

    notation_week = columns[0].text()
    price_broilers = columns[1].text()

    week_number = datetime.now().isocalendar()[1]
    if(int(notation_week) == week_number):
        return write_to_csv_abc("data/abc.csv", notation_week, price_broilers)
    return False