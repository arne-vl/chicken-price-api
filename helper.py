import csv
from scraping.scraper import save_price_abc, save_price_deinze

def update() -> tuple:
    abc = save_price_abc()
    deinze = save_price_deinze()
    return (abc, deinze)

def get() -> tuple:
    return (get_most_recent_abc(), get_most_recent_deinze())

def get_most_recent_abc() -> str:
    last_row = get_last_row("data/abc.csv")
    if last_row == []:
        return "null"
    return last_row[1]

def get_most_recent_deinze() -> str:
    last_row = get_last_row("data/deinze.csv")
    if last_row == []:
        return "null"
    return last_row[1]

def get_last_row(filename: str) -> list:
    try:
        with open(filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
        
            for row in csvreader:
                last_row = row
        return last_row
    except:
        return []