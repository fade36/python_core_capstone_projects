from pathlib import Path
import json

def json_load():
    path = Path(__file__).resolve().parents[2] / "data" / "hour.json"

    if not path.exists():
        print("File not found.")
        return None

    if path.stat().st_size == 0:
        print("The file is empty")
        return None

    try:
        with open(path, "r", encoding="utf-8") as file:
            dataset = json.load(file)
    except json.JSONDecodeError:
        print("Invalid JSON format")
        return None
    except OSError as error:
        print(f"File reading error: {error}")
        return None

    if not isinstance(dataset, list):
        print("Must contain list of records")
        return None
    
    if not dataset:
        print("Dataset is empty.")
        return None
    
    if not all(isinstance(row, dict) for row in dataset):
        print("Every record must be a dictionary")
        return None

    expected_cols = set(dataset[0].keys())

    if not expected_cols:
        print("Records contain no columns")
        return None

    result = []
    indices = []
    for i, row in enumerate(dataset):
        if set(row.keys()) != expected_cols:
            indices.append(i)
            continue
        result.append(row)

    for i in indices:
        print(f"Inconsistent columns in row #{i + 1}",end=" ")

    if not result:
        print("No valid records found.")
        return None

    return result

def json_save(dataset):
    if not dataset:
        print("Dataset is empty. Nothing to save.")
        return

    path = Path(__file__).resolve().parents[2] / "data" / "saved.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(dataset, file, indent=4, ensure_ascii=False)

    print("Data successfully saved")