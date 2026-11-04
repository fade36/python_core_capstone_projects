from src.services.finance_manager import FinanceManager
from src.cli.menu import Menu


def main():
    finance_manager = FinanceManager()
    menu = Menu(finance_manager=finance_manager)
    menu.run()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user.")