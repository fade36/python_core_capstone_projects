from models.transaction import Transaction
from models.category import Category
from decimal import Decimal
from datetime import date

class FinanceManager:
    def __init__(self, ):
        self.transactions: list[Transaction] = []
        self.categories: set[Category] = set()

    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            raise TypeError("Not a transaction object")
        if transaction.category not in self.categories:
            raise Exception("Sorry, first create category")
        self.transactions.append(transaction)

    def rm_transaction(self, tr_id):
        for transaction in self.transactions:
            if str(transaction.id).endswith(tr_id):         #fix
                self.transactions.remove(transaction)
                return True
        return False

    def add_category(self, category):
        if not isinstance(category, Category):
            raise TypeError("Not a category object")
        self.categories.add(category) 

    def rm_category(self, category_name):
        for category in self.categories:
            if category_name == category.category:
                for transaction in self.transactions:
                    if transaction.category == category:
                        return False
                self.categories.remove(category)
                return True
        return False

    def filter_transactions(
        self, 
        date_from=None, 
        date_to=None, 
        category_type=None, 
        category=None,
        min_value=None,
        max_value=None):
        
        if date_from is not None and type(date_from) is not date:
            raise TypeError("date_from must be a date object")

        if date_to is not None and type(date_to) is not date:
            raise TypeError("date_to must be a date object")

        if date_from is not None and date_to is not None:
            if date_from > date_to:
                raise ValueError("Start date cannot be later than end date")

        if category_type is not None:
            if category_type not in ("income", "expense"):
                raise ValueError("Category type must be either income or expense")

        if min_value is not None and not isinstance(min_value, (int, Decimal)):
            raise TypeError("Minimum value must be a number")

        if max_value is not None and not isinstance(max_value, (int, Decimal)):
            raise TypeError("Maximum value must be a number")

        if min_value is not None and max_value is not None:
            if min_value > max_value:
                raise ValueError("Minimum value cannot be greater than maximum value")
            
        filtered_transactions = []
        for transaction in self.transactions:
            if date_from is not None:
                if transaction.transaction_date < date_from:
                    continue
            if date_to is not None:
                if transaction.transaction_date > date_to:
                    continue
            if category is not None:
                if category != transaction.category.category:
                    continue
            if min_value is not None:
                if transaction.value < min_value:
                    continue
            if max_value is not None:
                if transaction.value > max_value:
                    continue
            if category_type is not None:
                if category_type != transaction.category.category_type:
                    continue
            filtered_transactions.append(transaction)
        return filtered_transactions

    def evaluate_income(self, date_from, date_to):
        if type(date_from) != date or type(date_to) != date:
            raise TypeError("Dates must be dates")
        if date_from > date_to:
            raise ValueError("Start date cannot be later than end date")
        
        transactions = self.filter_transactions(date_from=date_from, date_to=date_to, category_type="income")
        income = sum((t.value for t in transactions), Decimal("0"))
        return income

    def evaluate_expense(self, date_from, date_to):
        if type(date_from) != date or type(date_to) != date:
            raise TypeError("Dates must be dates")
        if date_from > date_to:
            raise ValueError("Start date cannot be later than end date")
        
        transactions = self.filter_transactions(date_from=date_from, date_to=date_to, category_type="expense")
        expense = sum((t.value for t in transactions), Decimal("0"))
        return expense

    def evaluate_balance(self, date_from, date_to):
        return self.evaluate_income(date_from, date_to) - self.evaluate_expense(date_from, date_to)

