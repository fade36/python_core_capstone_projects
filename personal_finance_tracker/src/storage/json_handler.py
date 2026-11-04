import json
from pathlib import Path
from src.services.finance_manager import FinanceManager
from src.models.category import Category
from src.models.transaction import Transaction
from uuid import UUID
from decimal import Decimal
from datetime import date


def save_data(finance_manager: FinanceManager):
    if len(finance_manager.transactions) == 0:
        print("There is nothing to save")
        return
    
    data_to_save = {}
    data_to_save["transactions"] = []
    data_to_save["categories"] = []

    for transaction in finance_manager.transactions:
        data_to_save["transactions"].append(
            {
                "id": str(transaction.id),
                "value": str(transaction.value),
                "category": transaction.category.category,
                "date": transaction.transaction_date.isoformat(),
                "description": transaction.description
            }
        )
    for category in finance_manager.categories:
        data_to_save["categories"].append(
            {
                "category": category.category,
                "category_type": category.category_type
            }
        )
    
    path = Path(__file__).resolve().parents[2] / "data" / "transactions.json"
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4, ensure_ascii=False)

    print("Data successfully saved")

def load_data(finance_manager: FinanceManager):
    path = Path(__file__).resolve().parents[2] / "data" / "transactions.json"

    if not path.exists():
        print("No saved data found.")
        return

    if path.stat().st_size == 0:
        print("The data file is empty.")
        return
    
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError:
        print("The data file contains invalid JSON.")
        return
    except OSError as error:
        print(f"Could not read data file: {error}")
        return

    if not isinstance(data, dict) or "categories" not in data or "transactions" not in data:
        print("Invalid data file structure.")
        return

    if not isinstance(data["categories"], list) or not isinstance(data["transactions"], list):
        print("Invalid data file structure.")
        return

    categories = {}
    for category_data in data["categories"]:
        category = Category(category_data["category"], category_data["category_type"])
        finance_manager.add_category(category=category)
        categories[category.category] = category

    for transaction_data in data["transactions"]:
         transaction = Transaction(
            transaction_id = UUID(transaction_data["id"]),
            value = Decimal(transaction_data["value"]),
            category = categories[transaction_data["category"]],
            transaction_date=date.fromisoformat(transaction_data["date"]),
            description=transaction_data["description"]
         )
         finance_manager.add_transaction(transaction=transaction)

    print(f"Successfully loaded {len(data['categories'])} categories and {len(data['transactions'])} transactions.")
