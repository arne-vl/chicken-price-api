import csv
from datetime import date

def date_exists_in_csv(filename: str, date: date):
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row and row[0] == date.strftime('%d-%m-%y'):
                    return True
    except FileNotFoundError:
        pass
    return False

def write_to_csv(filename: str, date: date, value: float, max_length: int = 100):
    if date_exists_in_csv(filename, date):
        print("Date already exists in CSV file. Skipping...")
        return
    
    existing_data = []
    try:
        with open(filename, 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                existing_data.append(row)
    except FileNotFoundError:
        pass
    
    existing_data.append([date.strftime('%Y-%m-%d'), value])
    
    if len(existing_data) > max_length:
        existing_data = existing_data[-max_length:]
    
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(existing_data)