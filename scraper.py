import httpx
from selectolax.parser import HTMLParser
from datetime import datetime

from util import write_to_csv

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
}

def save_price_deinze() -> float:
    url = "https://www.pluimveeslachthuizen.be/nl/node/246"

    response = httpx.get(url=url, headers=HEADERS)

    html = HTMLParser(response.text)

    most_recent_row = html.css("tr")[2]
    
    columns = most_recent_row.css("td")

    notation_date = datetime.strptime(columns[0].text(), "%d/%m/%y").date()
    price_broilers = float(columns[4].text()[2:].replace(",", "."))
    
    write_to_csv("data/deinze.csv", notation_date, price_broilers)

save_price_deinze()