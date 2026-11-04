from src.services.finance_manager import FinanceManager
from src.models.transaction import Transaction
from src.models.category import Category
import src.storage.json_handler as json_handler
from time import sleep
from decimal import Decimal
from datetime import datetime

class Menu:
    def __init__(self, finance_manager: FinanceManager):
        self.finance_manager = finance_manager

    def run(self):
        while True:
            try:
                self.show_main_menu()
                external_userInput = input("Select option: ")
                match external_userInput:
                    case "1":
                        while True:
                            self.show_transactions_menu()
                            internal_userInput = input("Select option: ")
                            match internal_userInput:
                                case "1":
                                    self.transactions_add_menu()
                                case "2":
                                    self.transactions_rm_menu()
                                case "3":
                                    self.view_transactions()
                                case "4":
                                    filtered_tr = self.filter_transaction_menu()
                                    if filtered_tr is not None:
                                        self.view_transactions(filtered_tr)
                                case "5":
                                    break
                                case _:
                                    print("Invalid option")
                    case "2":
                        while True:
                            self.show_categories_menu()
                            internal_userInput = input("Select option: ")
                            match internal_userInput:
                                case "1":
                                    self.category_add_menu()
                                case "2":
                                    self.category_rm_menu()
                                case "3":
                                    self.view_categories()
                                case "4":
                                    break
                                case _:
                                    print("Invalid option")
                    case "3":
                        while True:
                            self.show_financial_overview_menu()
                            internal_userInput = input("Select option: ")
                            match internal_userInput:
                                case "1":
                                    income = self.eval_all("income")
                                    print(f"Your income for that period is {income}$")
                                case "2":
                                    expense = self.eval_all("expense")
                                    print(f"Your expense for that period is {expense}$")
                                case "3":
                                    balance = self.eval_all("balance")
                                    print(f"Your balance for that period is {balance}$")
                                case "4":
                                    self.financial_summary_menu()
                                case "5":
                                    break
                                case _:
                                    print("Invalid option")
                    case "4":
                        while True:
                            self.data_management_menu()
                            userInput = input("Select option: ")
                            match userInput:
                                case "1":
                                    json_handler.save_data(finance_manager=self.finance_manager)
                                    break
                                case "2":
                                    json_handler.load_data(finance_manager=self.finance_manager)
                                    break
                                case "3":
                                    break
                                case _:
                                    print("Invalid option")
                    case "5":
                        print("Exiting...")
                        sleep(1)
                        break
                    case _:
                        print("Invalid option.")
            except:
                print("Error")
                json_handler.save_data(finance_manager=self.finance_manager)

    def show_main_menu(self):
        print("=" * 60)
        print("Personal Finance Manager".center(60))
        print("Main menu".center(60))
        print("1. Transactions")
        print("2. Categories")
        print("3. Financial Overview")
        print("4. Data Management")
        print("5. Exit")

    def show_transactions_menu(self):
        print("=" * 100)
        print("Transactions".center(100))
        print("1. Add transaction")
        print("2. Remove transaction")
        print("3. View all transactions")
        print("4. Filter transactions")
        print("5. Back")

    def transactions_add_menu(self):
        value = Decimal(input("Type value: "))
        date_input = input("Type date (dd-mm-yyyy): ")
        date_ = datetime.strptime(date_input, "%d-%m-%Y").date()
        description = input("Type description: ")

        category_name = input("Type category name: ").lower()
        for category in self.finance_manager.categories:
            if category_name == category.category:
                self.finance_manager.add_transaction(Transaction(value, category, date_, description))
                break
        else:
            category_type = input("The category does not exist. Type income or expense to define: ").lower()
            category = Category(category_name, category_type)
            self.finance_manager.add_category(category)
            self.finance_manager.add_transaction(Transaction(value, category, date_, description))

    def transactions_rm_menu(self):
        page_size = 10 
        page = 0

        while True:
            transactions = self.finance_manager.transactions

            if not transactions:
                break

            max_page = (len(transactions) - 1) // page_size
            page = min(page, max_page)

            start = page * page_size
            end = start + page_size

            print("\n" + "=" * 80)
            print("ID\t\tCategory\tType\t\tValue\t\tDate")
            print("-" * 80)

            for transaction in transactions[start:end]:
                print(f"{str(transaction.id)[-6:]}\t\t{transaction.category.category}\t\t{transaction.category.category_type}\t\t{transaction.value}\t\t{transaction.transaction_date}")
            print("-" * 80)
            print(f"Showing {start + 1}-{min(end, len(transactions))} " f"of {len(transactions)} transactions")
            print(f"Page {page + 1}/{max_page + 1}")
            
            userInput = input("\nEnter - next | p - previous | r - remove | q - quit: ").strip().lower()

            if userInput == "":
                if page < max_page:
                    page+=1
                else:
                    print("There is no next page.")

            elif userInput == "p":
                if page > 0:
                    page -= 1
                else:
                    print("There is no previous page.")
            elif userInput == "r":
                id_input = input("Type transaction ID (last 6 characters): ").strip()

                if len(id_input) != 6:
                    print("ID must contain exactly 6 characters.")
                    continue

                success = self.finance_manager.rm_transaction(id_input)

                if success:
                    print("Transaction has been removed.")
                else:
                    print("Transaction was not found or ID is not unique.")

            elif userInput == "q":
                break

            else:
                print("Invalid option.")

    def view_transactions(self, specific_transactions=None):
        print("\n" + "=" * 100)
        print("ID\t\tCategory\t\t\t\tType\t\tValue\t\tDate")
        print("-" * 100)

        if specific_transactions is not None:
            transactions = specific_transactions
        else:
            transactions = self.finance_manager.transactions

        if not transactions:
            return

        for transaction in transactions:
            print(f"{str(transaction.id)[-6:]}\t\t{transaction.category.category}\t\t\t\t{transaction.category.category_type}\t\t{transaction.value}\t\t{transaction.transaction_date}")

    def filter_transaction_menu(self):
        date_from, date_to, category_name, category_type, min_val, max_val = (None, None, None, None, None, None)
        while True:
            print("=" * 60)
            print("Select Filters".center(60))
            print("1. Date From")
            print("2. Date To")
            print("3. Category name")
            print("4. Category type")
            print("5. Minimal value")
            print("6. Maximal value")
            print("7. Save filters")
            print("8. Cancel")
            userInput = input("Select option: ")

            match userInput:
                case "1":
                    date_input = input("Type date (dd-mm-yyyy): ")
                    date_from = datetime.strptime(date_input, "%d-%m-%Y").date()
                case "2":
                    date_input = input("Type date (dd-mm-yyyy): ")
                    date_to = datetime.strptime(date_input, "%d-%m-%Y").date()
                case "3":
                    category_name = input("Category name: ")
                case "4":
                    category_type = input("Category type: ")
                case "5":
                    min_val = Decimal(input("Minimal value: "))
                case "6":
                    max_val = Decimal(input("Maximal value: "))
                case "7":
                    print("Implementing filters...")
                    sleep(0.5)
                    break
                case "8":
                    return None
                case _:
                    print("Invalid option")
        try:
            return self.finance_manager.filter_transactions(
                date_from=date_from,
                date_to=date_to,
                category=category_name,
                category_type=category_type,
                min_value=min_val,
                max_value=max_val
            )
        except (TypeError, ValueError) as error:
            print(f"Error: {error}")
            return []
                
    def show_categories_menu(self):
        print("=" * 60)
        print("Categories".center(60))
        print("1. Add category")
        print("2. Remove category")
        print("3. View all categories")
        print("4. Back")

    def category_add_menu(self):
        category_name = input("Type category name: ")
        if category_name in self.finance_manager.categories:
            print("Category already exists")
            return
        category_type = input("Type category type (income / expense): ")
        if category_type.lower() not in ["income", "expense"]:
            print("Wrong category type")
            return
        category = Category(category=category_name, category_type=category_type)
        self.finance_manager.add_category(category=category)
        print("Category was successfully added")

    def category_rm_menu(self):
        while True:
            category_name = input("Type category name: ")
            success = self.finance_manager.rm_category(category_name=category_name)
            if(success):
                print("Category was successfully removed")
                break
            else:
                print("Categoty not found. Try again")

    def view_categories(self):
        print("\n" + "=" * 60)
        print("Category name\t\t Category type")
        print("-" * 60)

        categories = self.finance_manager.categories
        if not categories:
            return
        for category in categories:
            print(f"{category.category}\t\t\t{category.category_type}")

    def show_financial_overview_menu(self):
        print("=" * 60)
        print("Financial Overview".center(60))
        print("1. Evaluate income")
        print("2. Evaluate expenses")
        print("3. Evaluate balance")
        print("4. View financial summary")
        print("5. Back")

    def eval_all(self, parameter, date_from=None, date_to=None):

        if date_to is None and date_from is None:
            date_input = input("Type date from (dd-mm-yyyy): ")
            date_from = datetime.strptime(date_input, "%d-%m-%Y").date()
            date_input = input("Type date to (dd-mm-yyyy): ")
            date_to = datetime.strptime(date_input, "%d-%m-%Y").date()

        if parameter == "income":
            return self.finance_manager.evaluate_income(date_from=date_from,date_to=date_to) 
        elif parameter == "expense": 
            return self.finance_manager.evaluate_expense(date_from=date_from,date_to=date_to) 
        else:
            return self.finance_manager.evaluate_balance(date_from=date_from,date_to=date_to)
           
    def financial_summary_menu(self):
        date_input = input("Type date from (dd-mm-yyyy): ")
        date_from = datetime.strptime(date_input, "%d-%m-%Y").date()
        date_input = input("Type date to (dd-mm-yyyy): ")
        date_to = datetime.strptime(date_input, "%d-%m-%Y").date()

        print("="*60)
        print("Financial Summary".center(60))
        print("="*60)
        print(f"Period: {date_from} - {date_to}")
        print()
        print(f"Total income: ", end="") 
        print(f"{self.eval_all(parameter="income", date_from=date_from, date_to=date_to)}")
        print(f"Total expense: ", end="") 
        print(f"{self.eval_all(parameter="expense", date_from=date_from, date_to=date_to)}")
        print(f"Net balance: ", end="") 
        print(f"{self.eval_all(parameter="balance", date_from=date_from, date_to=date_to)}")
        print()
        print("="*60)
        print("Income by category: ")
        income_by_category = {}
        for transaction in self.finance_manager.transactions:
            if transaction.category.category_type == "income":
                category = transaction.category.category
                income_by_category[category] = income_by_category.get(category, Decimal("0")) + transaction.value

        for key, value in income_by_category.items():
            print(f"{key}\t\t\t\t{value}")
        print()
        print("Expense by category: ")
        expense_by_category = {}
        for transaction in self.finance_manager.transactions:
            if transaction.category.category_type == "expense":
                category = transaction.category.category
                expense_by_category[category] = expense_by_category.get(category, Decimal("0")) + transaction.value

        for key, value in expense_by_category.items():
            print(f"{key}\t\t\t\t{value}")

    def data_management_menu(self):
        print("Data Management")
        print()
        print("1. Save data")
        print("2. Load data")
        print("3. Back")
