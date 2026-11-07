from pathlib import Path
import csv
from datetime import datetime
from decimal import Decimal, InvalidOperation

def csv_load():
    path = Path(__file__).resolve().parents[2] / "data" / "hour.csv"    #const directory and file for learning circumstances

    if not path.exists():
        print("No saved data found.")
        return

    if path.stat().st_size == 0:
        print("The data file is empty.")
        return
    
    dataset = []

    with open(path, "r", newline="") as file:
        reader = csv.DictReader(file, delimiter=",")
        for line in reader:
            data_row = {}
            for key, value in line.items():
                if not value.strip():
                    data_row[key] = None
                    continue
                try:
                    data_row[key] = datetime.strptime(value, "%Y-%m-%d").date()
                    continue
                except ValueError:
                    pass
                if value.isdigit():
                    if key == "windspeed":
                        data_row[key] = Decimal(value)
                    else:
                        data_row[key] = int(value)
                    continue
                try:
                    data_row[key] = Decimal(value)
                    continue
                except InvalidOperation:
                    pass
                data_row[key] = value

            dataset.append(data_row)

    return dataset 

    
def csv_save(dataset):
    if not dataset:
        print("Dataset is empty. Nothing to save.")
        return
    
    path = Path(__file__).resolve().parents[2] / "data" / "saved.csv"
    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", newline="", encoding="utf-8") as file:
        columns = dataset[0].keys()
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(dataset)
    print("Successfully saved")